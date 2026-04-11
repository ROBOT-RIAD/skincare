
from google import genai


client = genai.Client(api_key='AIzaSyAQ46PzD0A4iemCkaeFjhvrr9JtC4USKBI')

for m in client.models.list():
    print(m)