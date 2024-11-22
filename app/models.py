from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Define the database URL
DATABASE_URL = "sqlite:///./test.db"

# SQLAlchemy engine and session setup
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Document model for storing scraped or generated documents
class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)

# UserSession model for tracking user conversations
class UserSession(Base):
    __tablename__ = "user_sessions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)  # Identifier for the user
    conversation = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

# Function to initialize the database tables
def init_db():
    Base.metadata.create_all(bind=engine)
