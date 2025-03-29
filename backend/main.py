from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from detector import extract_negative_treatments
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# Enable CORS (for React frontend later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict later to "http://localhost:3000"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CaseRequest(BaseModel):
    case_id: str

@app.post("/analyze-case")
def analyze_case(data: CaseRequest):
    try:
        result = extract_negative_treatments(data.case_id)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Only runs if you execute this file directly
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)