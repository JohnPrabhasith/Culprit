import os
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
load_dotenv()

os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')

tool = SerperDevTool()