"""
Configuration settings for AI Adaptive Shoe Design System
"""
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Base configuration"""
    DEBUG = False
    TESTING = False
    
    # Flask settings
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-change-in-production')
    
    # Upload settings
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'static/uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'tiff'}
    
    # Database
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        'sqlite:///shoe_design.db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # API settings
    API_TITLE = 'AI Adaptive Shoe Design System'
    API_VERSION = '1.0.0'
    JSON_SORT_KEYS = False
    
    # AI Model settings
    MODEL_PATH = os.path.join(os.path.dirname(__file__), 'models')
    IMAGE_SIZE = (224, 224)
    BATCH_SIZE = 32
    EPOCHS = 50
    
    # Material research
    OXMAN_RESEARCH_URL = 'https://www.oxman.com/work'
    MATERIALS_DB_PATH = os.path.join(os.path.dirname(__file__), 'data/materials_db.json')
    MANUFACTURING_SPECS_PATH = os.path.join(os.path.dirname(__file__), 'data/manufacturing_specs.json')
    
    # Durability settings
    TARGET_DURABILITY_MONTHS = 8
    DURABILITY_CONFIDENCE_THRESHOLD = 0.75
    
    # Learning engine
    FEEDBACK_BATCH_SIZE = 10
    RETRAINING_INTERVAL = 100  # Retrain after 100 feedback items
    
    # Logging
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False


class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False


# Configuration dictionary
config_by_name = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

def get_config(env=None):
    """Get configuration based on environment"""
    if env is None:
        env = os.getenv('FLASK_ENV', 'development')
    return config_by_name.get(env, config_by_name['default'])
