import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
	PROJECT_NAME: str = "Containerized FastAPI App"
	DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./test.db")
settings = Settings()
