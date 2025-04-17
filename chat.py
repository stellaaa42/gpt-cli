from openai import OpenAI
import argparse
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

client = OpenAI(api_key=API_KEY)


parser = argparse.ArgumentParser(description="Ask a question to GPT")
parser.add_argument('-q', type=str, required=True, help='Question to ask GPT')
args = parser.parse_args()

response = client.responses.create(
    model="gpt-4.1",
    input=args.q

)

print(response.output_text)
