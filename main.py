from infrastructure.web.flask_app import create_app
from flask_cors import CORS

app = create_app()


if __name__ == "__main__":
    app.run(debug = True)
    CORS(app)