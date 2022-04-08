from dotenv import load_dotenv
import os

load_dotenv()
PROFILE = os.getenv("PROFILE")
print(PROFILE) 