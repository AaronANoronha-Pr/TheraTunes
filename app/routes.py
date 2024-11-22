from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import Optional
from app.models import SessionLocal, UserSession, init_db
from langchain_ollama import OllamaLLM
import spotipy
from spotipy.oauth2 import SpotifyOAuth

router = APIRouter()

# Initialize Gemma LLM with Ollama
llm = OllamaLLM(model="gemma2:2b")

# Spotify API setup
SPOTIFY_CLIENT_ID = "your_spotify_client_id"
SPOTIFY_CLIENT_SECRET = "your_spotify_client_secret"
SPOTIFY_REDIRECT_URI = "your_redirect_uri"

spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="playlist-modify-private"
))

# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# On startup, initialize the database
@router.on_event("startup")
def on_startup():
    init_db()

# Function to analyze mood using Gemma
def analyze_mood(conversation: str):
    prompt = f"Analyze the mood of the following conversation and provide a single-word mood descriptor (e.g., 'relaxation', 'happiness', 'stress'): '{conversation}'"
    response = llm.generate(prompts=[prompt])
    mood = response["results"][0]["text"].strip().lower()
    return mood

# Function to create a Spotify playlist based on mood
def create_playlist(user_id: str, mood: str):
    playlist_name = f"Therapeutic Playlist for {mood.capitalize()}"
    description = "A personalized playlist based on your recent conversation and mood analysis."
    playlist = spotify.user_playlist_create(user=user_id, name=playlist_name, public=False, description=description)
    
    # Example tracks based on mood
    mood_tracks = {
        "relaxation": ["spotify:track:4uLU6hMCjMI75M1A2tKUQC"],  
        "happiness": ["spotify:track:2XU0oxnq2qxCpomAAuJY8K"],
        "stress": ["spotify:track:7ouMYWpwJ422jRcDASZB7P"], 
        "focus": ["spotify:track:5qnpQ80tJ3yHBLJps0zJFs"]
    }

    tracks = mood_tracks.get(mood, [])
    spotify.playlist_add_items(playlist_id=playlist["id"], items=tracks)
    return playlist

# Function to suggest a breathing exercise
def get_breathing_exercise():
    return {
        "exercise": "4-7-8 Breathing",
        "instructions": [
            "Inhale through your nose for 4 seconds.",
            "Hold your breath for 7 seconds.",
            "Exhale slowly through your mouth for 8 seconds.",
            "Repeat this cycle 4-6 times for a calming effect."
        ]
    }

# Function to provide journaling prompts
def get_journaling_prompts():
    return [
        "Write down three things you are grateful for today.",
        "Describe a moment today that made you smile.",
        "What would you tell your younger self if you could?"
    ]

# Function to return relaxation quotes
def get_relaxation_quotes():
    return [
        "Take rest; a field that has rested gives a bountiful crop. – Ovid",
        "Almost everything will work again if you unplug it for a few minutes, including you. – Anne Lamott",
        "Keep your face to the sunshine, and you cannot see a shadow. – Helen Keller"
    ]

# Endpoint to track conversation, analyze mood, create a playlist, and provide relaxing content
@router.post("/conversation")
def track_conversation(
    user_id: str,
    conversation: str,
    db: Session = Depends(get_db)
):
    try:
        # Save conversation to the database
        user_session = UserSession(user_id=user_id, conversation=conversation)
        db.add(user_session)
        db.commit()

        # Analyze mood using Gemma
        mood = analyze_mood(conversation)

        # Create Spotify playlist
        playlist = create_playlist(user_id, mood)

        # Get additional relaxation resources
        breathing_exercise = get_breathing_exercise()
        journaling_prompts = get_journaling_prompts()
        relaxation_quotes = get_relaxation_quotes()

        return {
            "message": "Conversation processed successfully.",
            "mood": mood,
            "playlist": {
                "name": playlist["name"],
                "url": playlist["external_urls"]["spotify"]
            },
            "breathing_exercise": breathing_exercise,
            "journaling_prompts": journaling_prompts,
            "relaxation_quotes": relaxation_quotes
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to process conversation: {str(e)}")
