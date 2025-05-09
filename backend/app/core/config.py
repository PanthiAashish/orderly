from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# Load .env file
env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path=env_path)

class Settings(BaseSettings):
    OPENAI_API_KEY: str
    ROBINHOOD_USERNAME: str
    ROBINHOOD_PASSWORD: str

settings = Settings()

# This Settings class loads and validates environment variables using Pydantic.
# Compared to using os.environ directly, this approach:
# - Ensures required variables are present and raises clear errors if not
# - Automatically handles type conversion (e.g., str -> int, bool)
# - Keeps all config variables in one central, structured location
# - Makes it easy to import config across the project using `from app.core.config import settings`
# - Supports future features like defaults, nested configs, and environment-specific overrides
# For small scripts, os.environ may be sufficient, but for real applications, this provides better safety and maintainability.