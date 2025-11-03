from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

api_key = os.getenv("API_KEY")
database_url = os.getenv("DATABASE_URL")
debug_mode = os.getenv("DEBUG")

print(f"API Key: {api_key}")
print(f"Database URL: {database_url}")
print(f"Debug Mode: {debug_mode}")