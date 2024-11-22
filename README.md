# 🎵 Theratunes: AI-Powered Therapy and Personalized Playlists

Theratunes combines AI and music therapy to help users enhance their mood through personalized playlists, mood analysis, and relaxation techniques. By leveraging state-of-the-art language models and APIs, Theratunes offers a therapeutic conversational experience and curates music tailored to user emotions.

## 🛠️ Features

1)Mood Analysis: Conversational AI (powered by Google Gemma) analyzes user inputs to detect emotions and mental states.

2)Personalized Playlists: Creates Spotify playlists based on real-time mood analysis using the Spotify API.

3)Relaxation Techniques: Provides guided breathing exercises, positive affirmations, and other relaxation suggestions.

4)Conversation Tracking: Stores user conversations to enhance personalization and provide better context.

5)User-Friendly Design: Integrated database for storing user interactions and customizable sessions.

## 🔧 Installation
Clone the repository:
```
git clone https://github.com/yourusername/theratunes.git
```
Direct into Folder:
```
cd theratunes
```
Set up a Python virtual environment:
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
Install dependencies:
```
pip install -r requirements.txt
```
Configure environment variables: Create a .env file in the project root and add the following:
```
SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
DATABASE_URL=sqlite:///./test.db
```
Initialize the database:
```
python -c "from app.models import init_db; init_db()"
```
Run the application:
```
uvicorn app.main:app --reload
```
## 📚 Usage

### Have a Conversation
Use the /chat endpoint to analyze your mood and receive personalized suggestions.

### Generate a Playlist
Call /generate_playlist to get a curated Spotify playlist based on your mood.

### Relaxation Techniques
Access guided activities through the /relax endpoint.

## 💻 Technologies Used
Backend: FastAPI, SQLAlchemy, SQLite
AI Models: Google Gemma, Sentence Transformers
APIs: Spotify API

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1)Fork the repository.

2)Create a new branch for your feature:
```
git checkout -b feature-name
```
3)Commit your changes and push to your fork.

4)Open a pull request with details about your changes.
📄 License
This project is licensed under the MIT License. See the LICENSE file for details.


