import os

# Flask configuration
class Config:
    DEBUG = True  # Development mode
    SECRET_KEY = os.urandom(24)  # For security / session
    DATABASE = os.path.join(os.getcwd(), "exam_results.db")  # Database path
    UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")  # Folder to store uploaded files
    ALLOWED_EXTENSIONS = {'csv', 'xlsx'}  # Allowed file extensions for upload