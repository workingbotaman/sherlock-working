from presidio_analyzer import AnalyzerEngine, PatternRecognizer, Pattern
from presidio_anonymizer import AnonymizerEngine
from collections import defaultdict
from fastapi import FastAPI, HTTPException, UploadFile, File
import uvicorn
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import spacy
import urllib3
nlp = spacy.load('en_core_web_lg')

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)


@app.get("/")
def welcome():
  return{"message":"Hello"}

class text_input(BaseModel):
  text: str

@app.post('/text')
async def analyze_text(input_text : text_input):
  analyzer = AnalyzerEngine()
  analyzed_text = analyzer.analyze(input_text.text, language="en")
  for res in analyzed_text:
    print(res)

  return f"Running"