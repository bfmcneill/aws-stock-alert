import os
from dotenv import load_dotenv


ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_FILE_PATH = os.path.join(ROOT_DIR, ".env")

load_dotenv(dotenv_path=ENV_FILE_PATH)
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# print(ENV_FILE_PATH)
# print(os.path.exists(ENV_FILE_PATH))
