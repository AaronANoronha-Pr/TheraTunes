from fastapi import FastAPI, Depends, HTTPException
from app.routes import router
from app.models import SessionLocal, UserConversation, init_db
from sqlalchemy.orm import Session
from langchain_ollama import OllamaLLM
from sentence_transformers import SentenceTransformer
from pydantic import BaseModel
import requests

app = FastAPI()

# Initialize the Ollama model for conversation analysis (Gemma model)
llm = OllamaLLM(model="gemma2:2b")

# Sentence transformer model for emotion detection
model = SentenceTransformer("paraphrase-MiniLM-L6-v2")

# Include routes from the external router (e.g., handling playlist generation and relaxation)
app.include_router(router)

# Health check endpoint
@app.get("/health")
def health_check():
    return {"Status": "Active"}

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# User conversation model
class ConversationRequest(BaseModel):
    text: str

class ConversationResponse(BaseModel):
    response: str
    mood: str

# Endpoint for user conversations
@app.post("/chat", response_model=ConversationResponse)
def chat_with_therapist(conversation: ConversationRequest, db: Session = Depends(get_db)):
    try:
        # Send the user's input to the Ollama model (Gemma) for mood analysis and response generation
        prompt = f"User: {conversation.text}\nTherapist:"
        response = llm.generate(prompts=[prompt])[0]

        # Analyze the mood from the user's input using sentence transformers
        user_embedding = model.encode([conversation.text])[0]
        mood_score = sum(user_embedding) / len(user_embedding)  
        mood = "positive" if mood_score > 0 else "negative" 
        
        # Save the conversation in the database for future personalization
        db.add(UserConversation(text=conversation.text, response=response, mood=mood))
        db.commit()

        # Return the generated response and mood
        return ConversationResponse(response=response, mood=mood)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing conversation: {str(e)}")

# Main entry point to run the FastAPI app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
