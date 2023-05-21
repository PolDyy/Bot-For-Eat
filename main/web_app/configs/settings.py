from flask import Flask
from pathlib import Path
from os import getenv
from dotenv import load_dotenv

env_path = Path(__file__).parents[1].joinpath('env')
load_dotenv(env_path)

app = Flask(__name__)
app.config["SESSION_KEY"] = getenv("SESSION_KEY")
