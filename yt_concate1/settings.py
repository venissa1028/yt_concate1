import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('API_KEY')

DOWNLOADS_DIR="downloads"
VIDEO_DIR=os.path.join(DOWNLOADS_DIR, 'vdieos')
CATION_DIR=os.path.join(DOWNLOADS_DIR,'captions')

#2ed way
#import os
#from pathlib import Path
#from dotenv import load_dotenv
#basepath = Path()
#basedir = str(basepath.cwd())
#envars = basepath.cwd() / '.env'
#load_dotenv(envars)
#API_KEY = os.getenv('API_KEY')
#print(API_KEY)