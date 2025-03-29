import json
import os
from typing import Dict, Any
import openai
from dotenv import load_dotenv
from scholar import ScholarAPI
from prompts import create_analysis_prompt

# Load environment variables
load_dotenv()

# Initialize OpenAI client
openai.api_key = os.getenv("OPENAI_API_KEY")

FAKE_CASE_ID = "johnson-v-mta-2025"

def extract_negative_treatments(id: str) -> Dict[str, Any]:
    """
    Extracts negative treatments from a legal case using LLM analysis.
    
    Args:
        id: The Google Scholar case ID
        
    Returns:
        Dictionary containing negative treatments found in the case
    """
    
    # ✅ Fake Case Logic for Demo UI Testing
    if id == FAKE_CASE_ID:
        return {
            "negative_treatments": [
                {
                    "treated_case_citation": "Smith v. RapidBus Co., 512 U.S. 134 (1999)",
                    "treatment_type": "overruling",
                    "relevant_text": "The court explicitly overrules its prior decision in Smith v. RapidBus Co.",
                    "explanation": "The precedent in Smith is declared no longer valid, thus it is overruled."
                },
                {
                    "treated_case_citation": "Allen v. City Transport, 402 F.3d 221 (2007)",
                    "treatment_type": "limiting",
                    "relevant_text": "This court narrows the earlier interpretation from Allen.",
                    "explanation": "It limits the broad interpretation in Allen by excluding third-party contractors from municipal liability."
                }
            ]
        }

    # 🔍 Normal processing with OpenAI + Scholar scraping
    case_info = ScholarAPI.fetch_case(id)
    if not case_info:
        return {"error": "Failed to fetch case information"}
    
    prompt = create_analysis_prompt(case_info)
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a legal expert analyzing court cases for negative treatments."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.1,
        )
        result = json.loads(response.choices[0].message.content)
        return result
    
    except Exception as e:
        return {"error": f"Failed to analyze case: {str(e)}"}