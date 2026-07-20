import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from flask import Flask
from routes.student_routes import student_bp


app = Flask(__name__)


# Register routes
app.register_blueprint(student_bp)


@app.route("/")
def home():
    return {
        "message": "Hello, Backend AI Internship!"
    }


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
