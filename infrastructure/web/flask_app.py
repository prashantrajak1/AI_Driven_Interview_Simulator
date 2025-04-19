# from flask import Flask, jsonify, render_template
# from core.config import settings
# from infrastructure.api.openai_client import get_ai_service
# from application.services.video_service import VideoService
# from application.use_cases.video_analysis import VideoAnalysisUseCase
# from infrastructure.web.controller.analysis_controller import AnalysisController

# def create_app():
#     app = Flask(__name__)
#     app.config['MAX_CONTENT_LENGTH'] = settings.MAX_CONTENT_LENGTH
    
#     ai_service = get_ai_service()
#     video_service = VideoService()
#     use_case = VideoAnalysisUseCase(ai_service, video_service)
#     controller = AnalysisController(use_case)
    
#     @app.route('/')
#     def index():
#         return render_template('index.html')
    
#     @app.route('/analyze', methods = ['POST'])
#     def analyze():
#         try:
#             return controller.analyze()
#         except Exception as e:
#             return jsonify({'error': 'Unexpected Server Error'}), 500
#     return app


from flask import Flask, request, jsonify
from your_project_path.application.services import ai_service, video_service
from your_project_path.domain.entities import VideoAnalysisRequest

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze_video():
    try:
        # Parse the request data
        request_data = VideoAnalysisRequest.parse_obj(request.json)
        
        # Create use case and execute it
        use_case = VideoAnalysisUseCase(ai_service=ai_service, video_service=video_service)
        result = use_case.execute(request_data)
        
        # Return the result as JSON (including the graph URL)
        return jsonify(result.dict())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
