import os

# SET env variable
os.environ["PROFILE"] = "dev"

PROFILE = os.getenv('PROFILE')

print(PROFILE)