import os
from unicodedata import name
from dotenv import load_dotenv
load_dotenv()

if (os.getenv("PROFILE") == "DEV"):
    from to_be_import1 import *
else:
    from to_be_import2 import *


print(name_import)