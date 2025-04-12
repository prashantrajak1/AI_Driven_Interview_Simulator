# Title : Defining shape of the data : what out app will recieve and return 
# Date : 09-04-2025
# Author : Himanshu Sharma

from pydantic import BaseModel

class VideoAnalysisRequest(BaseModel): # Data required to send to the api
    video_path: str
    
class VideoAnalysisResult(BaseModel): # Data returned by the api
    transcript: str
    analysis: str
    metrics: dict = None
    
