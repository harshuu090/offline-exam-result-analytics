from flask import Flask
from config import Config

# Import routes
from backend.routes import students, subjects, marks, results, analytics

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Register routes / blueprints
app.register_blueprint(students.bp)
app.register_blueprint(subjects.bp)
app.register_blueprint(marks.bp)
app.register_blueprint(results.bp)
app.register_blueprint(analytics.bp)

# Run the server
if __name__ == "__main__":
    app.run()
