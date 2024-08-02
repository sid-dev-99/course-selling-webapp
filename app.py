from flask import Flask
from routes.student import student_bp 

app = Flask(__name__)

app.register_blueprint(student_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)


