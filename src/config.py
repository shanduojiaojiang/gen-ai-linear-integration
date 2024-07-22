import os

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY') # You can overwrite this directly with your OpenAI API Key when testing
LINEAR_API_KEY = os.getenv('LINEAR_API_KEY') # You can overwrite this directly with your Linear API Key when testing
LINEAR_API_URL = 'https://api.linear.app/graphql'
HEADERS = {
    'Authorization': LINEAR_API_KEY,
    'Content-Type': 'application/json'
}

if not OPENAI_API_KEY:
    raise ValueError("The environment variable 'OPENAI_API_KEY' is not set.")
if not LINEAR_API_KEY:
    raise ValueError("The environment variable 'LINEAR_API_KEY' is not set.")