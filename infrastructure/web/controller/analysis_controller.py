# from flask import jsonify, request
# import os
# import tempfile

# from application.use_cases.video_analysis import VideoAnalysisUseCase
# from domain.entities import VideoAnalysisRequest
# from application.use_cases import video_analysis
# # from utils import get_transcript

# class AnalysisController:
#     def __init__(self, analysis_use_case: VideoAnalysisUseCase):
#         self.analysis_use_case = analysis_use_case
    
#     def get_transcript(video_id):
#         # TODO: Replace this with real logic to fetch the transcript
#         return "This is a sample transcript for video ID: " + video_id


#     @app.route('/api/analyze-video/<video_id>', methods=['GET'])

#     def analyze_video(video_id):       
#     # Assuming you already get transcript from somewhere:
#       transcript = get_transcript(video_id)

#     # Existing analysis
#       summary, soft_skills, technical_skills = video_analysis.analyze(transcript)

#     # NEW: Extract skill scores
#       skill_scores = video_analysis.extract_skills_from_transcript(transcript)

#       return jsonify({
#         "summary": summary,
#         "soft_skills": soft_skills,
#         "technical_skills": technical_skills,
#         "skill_scores": skill_scores  # 👈 this powers your graph

#         return "This is a sample transcript for video ID: " + video_id
#     })    

#     def analyze(self):
#         try:
#             print("Recieved request...")
#             if 'video' not in request.files:
#                 print("No video found")
#                 return jsonify({"error": "No video file uploaded"}), 400

#             video_file = request.files['video']
            
#             if not video_file or video_file.filename == '':
#                 print("empty file received")
#                 return jsonify({"error": "Empty file received"}), 400
#             with tempfile.NamedTemporaryFile(delete=False, suffix='.webm') as temp_file:
#                 video_path = temp_file.name
#                 video_file.save(video_path)
#                 print("video saved")

#             try:
#                 print("Calling use case...")
#                 result = self.analysis_use_case.execute(
#                     VideoAnalysisRequest(video_path=video_path)
#                 )
                
#                 print("Result : ", result.analysis)
                
#                 if result is None:
#                     print("No result came")
                
#                 print("Giving Response...")
#                 return jsonify(result.dict()), 200
                
#             finally:
#                 if os.path.exists(video_path):
#                     os.remove(video_path)

#         except Exception as e:
#             return jsonify({
#                 "error": "Analysis failed",
#                 "details": str(e)
#             }), 500
        
# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask, jsonify, request
import os
import tempfile

from application.use_cases.video_analysis import VideoAnalysisUseCase
from domain.entities import VideoAnalysisRequest
from application.use_cases import video_analysis

app = Flask(__name__)  # Initialize Flask app


# ✅ Dummy function for now
def get_transcript(video_id):
    # TODO: Replace this with real logic to fetch the transcript
    return "This is a sample transcript for video ID: " + video_id


# ✅ Flask route to analyze video using its video_id
@app.route('/api/analyze-video/<video_id>', methods=['GET'])
def analyze_video(video_id):
    print(f"Analyzing video: {video_id}")

    # Get transcript
    transcript = get_transcript(video_id)

    # Existing analysis
    summary, soft_skills, technical_skills = video_analysis.analyze(transcript)

    # NEW: Extract skill scores
    skill_scores = video_analysis.extract_skills_from_transcript(transcript)

    return jsonify({
        "summary": summary,
        "soft_skills": soft_skills,
        "technical_skills": technical_skills,
        "skill_scores": skill_scores  # 👈 this powers your graph
    })


# ✅ Class-based controller for upload endpoint
class AnalysisController:
    def __init__(self, analysis_use_case: VideoAnalysisUseCase):
        self.analysis_use_case = analysis_use_case

    def analyze(self):
        try:
            print("Received request...")

            if 'video' not in request.files:
                print("No video found")
                return jsonify({"error": "No video file uploaded"}), 400

            video_file = request.files['video']
            
            if not video_file or video_file.filename == '':
                print("Empty file received")
                return jsonify({"error": "Empty file received"}), 400

            with tempfile.NamedTemporaryFile(delete=False, suffix='.webm') as temp_file:
                video_path = temp_file.name
                video_file.save(video_path)
                print("Video saved")

            try:
                print("Calling use case...")
                result = self.analysis_use_case.execute(
                    VideoAnalysisRequest(video_path=video_path)
                )

                print("Result:", result.analysis)

                if result is None:
                    print("No result returned")

                print("Sending response...")
                return jsonify(result.dict()), 200

            finally:
                if os.path.exists(video_path):
                    os.remove(video_path)

        except Exception as e:
            return jsonify({
                "error": "Analysis failed",
                "details": str(e)
            }), 500


# Optional: Run the app if this is the main file
if __name__ == '__main__':
    app.run(debug=True)
