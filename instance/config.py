import os

# Flask configuration settings

class Config:
    """Base configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_default_secret_key')
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    DEBUG = FLASK_ENV == 'development'
    TESTING = False
    SERVER_NAME = os.getenv('SERVER_NAME', 'localhost:5000')
    
    # Optional: Configure other settings here
    # Example: DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///default.db')

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True

class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    DEBUG = True

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    TESTING = False
    # Example: DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///production.db')
