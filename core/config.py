# Title : Configuring the settings for the App
# Date : 09-04-2025
# Author : Himanshu Sharma


from pydantic_settings import BaseSettings # Used for defining settings configuration

class Settings(BaseSettings):
    OPENAI_API_KEY: str
    upload_folder:str = "uploads"
    MAX_CONTENT_LENGTH: int = 100 * 1024 * 1024 
    
    class Config:
        env_file = ".env"

settings = Settings()