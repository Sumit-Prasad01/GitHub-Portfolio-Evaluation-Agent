import os
from pydantic_settings import BaseSettings
from functools import lru_cache
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    """
    Central configuration for the application.
    Loads values from environment variables or .env file.
    """

    # Application
    APP_NAME: str = "GitHub Portfolio Agent"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True

    # Database
    DATABASE_URL: str = "sqlite:///./portfolio.db"

    # GitHub API
    GITHUB_TOKEN: str | None = None
    GITHUB_API_URL: str = "https://api.github.com"

    # AI / LLM
    GROQ_API_KEY: str | None = os.getenv("GROQ_API_KEY")
    GROQ_MODEL: str = "llama-3.3-70b-versatile"

    # Logging
    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings():
    """
    Returns cached settings object.
    Prevents reloading .env multiple times.
    """
    return Settings()


settings = get_settings()