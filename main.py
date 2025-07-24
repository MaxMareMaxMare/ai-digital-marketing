from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import openai

# Load environment variables from .env file
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Set OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define request model
class PromptRequest(BaseModel):
    prompt: str
    max_tokens: int = 100

# Define POST endpoint to generate text using OpenAI
@app.post("/generate/")
async def generate_text(request: PromptRequest):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=request.prompt,
            max_tokens=request.max_tokens
        )
        return {"response": response.choices[0].text.strip()}
    except Exception as e:
        return {"error": str(e)}
