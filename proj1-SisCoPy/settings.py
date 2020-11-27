from dotenv import load_dotenv
from os import getenv
# from csv import 

load_dotenv()

settings = {
  "username": getenv('SIS_USERNAME'),
  "password": getenv('SIS_PASSWORD')
}
