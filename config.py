import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "22432833"))
    API_HASH = os.environ.get("API_HASH", "897f1c440892cfc46c7e222dfb37d015")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION = os.environ.get("BOT_SESSION", "Kakashi_the_mini_copybot")
    OWNER_ID = os.environ.get("OWNER_ID", "")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://eno2223456:7Cdmqig5Ih2vrqW4@cluster0.ccpmee5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "copydata")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'data')
    SESSION = os.environ.get("SESSION", "")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1002498435630"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "Kakashi_the_mini_copybot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
