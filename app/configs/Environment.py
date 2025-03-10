from functools import lru_cache
import os
from pydantic_settings import BaseSettings  # type: ignore
from dotenv import load_dotenv

# Load .env file dynamically based on ENV variable
def get_env_filename():
    runtime_env = os.getenv("ENV")
    return f".env.{runtime_env}" if runtime_env else ".env"

# Load the correct .env file
load_dotenv(get_env_filename())

class EnvironmentSettings(BaseSettings):
    API_VERSION: str
    APP_NAME: str
    DATABASE_DIALECT: str
    DATABASE_HOSTNAME: str
    DATABASE_NAME: str
    DATABASE_PASSWORD: str
    DATABASE_PORT: int
    DATABASE_USERNAME: str
    DEBUG_MODE: bool
    

    class Config:
        env_file = ".env"  # Keep default, as dotenv is loading the dynamic file
        env_file_encoding = "utf-8"

# Do not use @lru_cache here, as settings might need to be reloaded dynamically
def get_environment_variables():
    return EnvironmentSettings()
