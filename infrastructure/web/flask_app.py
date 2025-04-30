from flask import Flask, jsonify, render_template
from core.config import settings
from infrastructure.api.openai_client import get_ai_service
from application.services.video_service import VideoService
from application.use_cases.video_analysis import VideoAnalysisUseCase
from infrastructure.web.controller.analysis_controller import AnalysisController

def create_app():
    app = Flask(__name__)
    app.config['MAX_CONTENT_LENGTH'] = settings.MAX_CONTENT_LENGTH
    
    ai_service = get_ai_service()
    video_service = VideoService()
    use_case = VideoAnalysisUseCase(ai_service, video_service)
    controller = AnalysisController(use_case)
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/analyze', methods = ['POST'])
    def analyze():
        try:
            return controller.analyze()
        except Exception as e:
            return jsonify({'error': 'Unexpected Server Error'}), 500
    return app



