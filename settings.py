import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_DATABASE = os.getenv('DB_DATABASE')
DB_PORT = os.getenv('DB_PORT', 5432)
KAFKA_BOOTSTRAP_SERVER = os.getenv('KAFKA_BOOTSTRAP_SERVER')

# Port for web
WEB_PORT = os.getenv('WEB_PORT', 8000)
