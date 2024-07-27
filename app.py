from flask import Flask
from routes.student import student_bp  # Import the blueprint

app = Flask(__name__)

# Register the blueprint with the Flask application
app.register_blueprint(student_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
