from openai import OpenAI
from application.services.ai_service import OpenAIService
from core.config import settings

def get_ai_service() -> OpenAIService:
    client = OpenAI(api_key = settings.OPENAI_API_KEY)
    return OpenAIService(settings.OPENAI_API_KEY)