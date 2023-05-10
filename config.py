import os
from dotenv import load_dotenv
load_dotenv()
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = False


# Connect to the database
class Config(object):
    TESTING = False


class TestingConfig(Config):
    DATABASE_URI = os.environ.get("TEST_DATABASE_URI")
    TESTING = True
