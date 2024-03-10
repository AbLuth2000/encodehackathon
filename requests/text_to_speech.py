from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load variables from .env into environment
load_dotenv()

def output_to_mp3(text):
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    speech_file_path = Path(__file__).parent / "speech.mp3"
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text
    )

    response.stream_to_file(speech_file_path)