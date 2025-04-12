# Title: Setting up blueprint for how the AI service should behave; and then gives real implementation

from abc import ABC, abstractmethod

from domain.entities import VideoAnalysisResult

class AIServiceInterface(ABC): # setting up interface for any AI service to be used
    @abstractmethod
    def transcript_audio(self, audio_path:str) -> str:
        pass
    def analyse_transcript(self, transcript: str) -> str:
        pass
    
class OpenAIService(AIServiceInterface): # defining blueprint for OpenAI
    def __init__(self, api_key: str):
        import openai
        openai.api_key = api_key
        self.client = openai
        
    def transcript_audio(self, audio_path):
        try:
            with open(audio_path, "rb") as audio_file:
                transcript = self.client.audio.transcriptions.create(
                    model = "whisper-1",
                    file = audio_file
                )
            return transcript.text
        except Exception as e:
            print("Error occured while transcripting audio : ", str(e))
            pass
    
    def analyse_transcript(self, transcript: str) -> str:
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "Analyse this video resume and give feedback"},
                    {"role": "user", "content": transcript}
                ]
            )
            
            return response.choices[0].message.content

        except Exception as e:
            print("Error occured in analysing transcript : ", str(e))
            pass # Define error and logging
        