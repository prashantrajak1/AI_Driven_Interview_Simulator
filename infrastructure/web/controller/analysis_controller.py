from flask import jsonify, request
import os
import tempfile

from application.use_cases.video_analysis import VideoAnalysisUseCase
from domain.entities import VideoAnalysisRequest

class AnalysisController:
    def __init__(self, analysis_use_case: VideoAnalysisUseCase):
        self.analysis_use_case = analysis_use_case

    def analyze(self):
        try:
            print("Recieved request...")
            if 'video' not in request.files:
                print("No video found")
                return jsonify({"error": "No video file uploaded"}), 400

            video_file = request.files['video']
            
            if not video_file or video_file.filename == '':
                print("empty file received")
                return jsonify({"error": "Empty file received"}), 400
            with tempfile.NamedTemporaryFile(delete=False, suffix='.webm') as temp_file:
                video_path = temp_file.name
                video_file.save(video_path)
                print("video saved")

            try:
                print("Calling use case...")
                result = self.analysis_use_case.execute(
                    VideoAnalysisRequest(video_path=video_path)
                )
                
                print("Result : ", result.analysis)
                
                if result is None:
                    print("No result came")
                
                print("Giving Response...")
                return jsonify(result.dict()), 200
                
            finally:
                if os.path.exists(video_path):
                    os.remove(video_path)

        except Exception as e:
            return jsonify({
                "error": "Analysis failed",
                "details": str(e)
            }), 500