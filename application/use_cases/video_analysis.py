from abc import ABC, abstractmethod
from application.services import ai_service, video_service
from domain.entities import VideoAnalysisRequest, VideoAnalysisResult

class VideoAnalysisUseCase:
    
    def __init__(self, ai_service: ai_service, video_service: video_service):
        self.ai_service = ai_service
        self.video_service = video_service
        
    def execute(self, request: VideoAnalysisRequest) -> VideoAnalysisResult:
        print("Extracting audio...")
        print(f"Video path: {request.video_path}")
        audio_path = self.video_service.extract_audio(request.video_path)
        
        print("Transcripting audio...")
        transcript = self.ai_service.transcript_audio(audio_path)
        
        print("Analysing audio...")
        analysis = self.ai_service.analyse_transcript(transcript)

        print("Generating graph...")
        graph_url = self.ai_service.give_graph(transcript)
        
        return VideoAnalysisResult(
            transcript=transcript,
            analysis=analysis
        )