# Title: Setting up blueprint for how the AI service should behave; and then gives real implementation

from abc import ABC, abstractmethod

from domain.entities import VideoAnalysisResult

class AIServiceInterface(ABC): # setting up interface for any AI service to be used
    @abstractmethod
    def transcript_audio(self, audio_path:str) -> str:
        pass
    def analyse_transcript(self, transcript: str) -> str:
        pass
    def give_graph(self, transcript: str) -> str:
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
        
    def give_graph(self, transcript: str) -> str:
        try:
            response = self.client.images.generate(
                model="dall-e-3",
                prompt=f"Create a bar graph that visually represents this candidate’s skill analysis from a video resume transcript. Highlight soft skills, technical skills, problem-solving, and teamwork based on the following input: {transcript}",
                n=1,
                size="1024x1024"
            )
            image_url = response.data[0].url
            return image_url
        except Exception as e:
            print("Error occurred while generating graph image:", str(e))
            return None
