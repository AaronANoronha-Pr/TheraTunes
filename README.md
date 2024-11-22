#🎵 Theratunes: AI-Powered Therapy and Personalized Playlists
Theratunes combines AI and music therapy to help users enhance their mood through personalized playlists, mood analysis, and relaxation techniques. By leveraging state-of-the-art language models and APIs, Theratunes offers a therapeutic conversational experience and curates music tailored to user emotions.

##🛠️ Features
Mood Analysis

Conversational AI (powered by Ollama Gemma) analyzes user inputs to detect emotions and mental states.
Personalized Playlists

Creates Spotify playlists based on real-time mood analysis using the Spotify API.
Relaxation Techniques

Provides guided breathing exercises, positive affirmations, and other relaxation suggestions.
Conversation Tracking

Stores user conversations to enhance personalization and provide better context.
User-Friendly Design

Integrated database for storing user interactions and customizable sessions.
🔧 Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/theratunes.git
cd theratunes
Set up a Python virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Configure environment variables: Create a .env file in the project root and add the following:

makefile
Copy code
SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
DATABASE_URL=sqlite:///./test.db
Initialize the database:

bash
Copy code
python -c "from app.models import init_db; init_db()"
Run the application:

bash
Copy code
uvicorn app.main:app --reload
📚 Usage
Have a Conversation
Use the /chat endpoint to analyze your mood and receive personalized suggestions.

Generate a Playlist
Call /generate_playlist to get a curated Spotify playlist based on your mood.

Relaxation Techniques
Access guided activities through the /relax endpoint.

💻 Technologies Used
Backend: FastAPI, SQLAlchemy, SQLite
AI Models: Ollama Gemma, Sentence Transformers
APIs: Spotify API
Frontend: React (planned for future versions)
🚀 Roadmap
Add a user-friendly React-based interface.
Enhance relaxation features with audio and video content.
Support more advanced therapeutic tools and techniques.
🤝 Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.
Create a new branch for your feature:
bash
Copy code
git checkout -b feature-name
Commit your changes and push to your fork.
Open a pull request with details about your changes.
📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

🙌 Acknowledgements
LangChain Ollama for conversational AI.
Spotify Developers for the playlist generation API.
Sentence Transformers for mood analysis.
