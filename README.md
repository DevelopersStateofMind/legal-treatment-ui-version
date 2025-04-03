# ⚖️ Legal Treatment Detector – UI Version

This is a full-stack implementation of the Legal Treatment Detector assignment with a React-based frontend and a FastAPI backend. Users can enter a Google Scholar case ID and view detected **negative legal treatments**, such as **overruling**, **limiting**, or **distinguishing** prior cases.

---

## 📌 Project Structure

legal-treatment-ui-version/
├── backend/
│ ├── main.py # FastAPI entrypoint
│ ├── detector.py # OpenAI logic & fake data fallback
│ ├── scholar.py # Google Scholar HTML parser
│ ├── prompts.py # Prompt template builder
│ ├── .env # OpenAI API key (excluded from version control)
│ └── requirements.txt # Backend dependencies
├── frontend/
│ ├── public/
│ ├── src/
│ │ ├── App.js # React UI
│ │ └── index.js
│ └── package.json # Frontend dependencies

---

## 🖥️ Live Demo / Output Example

Enter the case ID `johnson-v-mta-2025` to test the app without using OpenAI credits.


{
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

#🚀 How to Run the App Locally
✅ Prerequisites
Node.js v18+

Python 3.9 – 3.11 recommended (Python 3.13 may cause compatibility issues)


OpenAI API Key (add to .env)

📦 1. Clone the Repository
    git clone https://github.com/your-username/legal-treatment-ui-version.git
    cd legal-treatment-ui-version

⚙️ 2. Run the Backend
    cd backend
    python -m venv venv
    venv\Scripts\activate        # On Windows
    # or `source venv/bin/activate` on Mac/Linux

    pip install -r requirements.txt
    python -m uvicorn main:app --reload

Server will run on: http://127.0.0.1:8000

🖼️ 3. Run the Frontend

    cd ../frontend
    npm install
    npm start

App will be available at: http://localhost:3000

#🧪 API Docs (Backend)
Method	Endpoint	Description
POST	/analyze-case	Accepts a JSON body with case_id and returns detected negative treatments
Sample Request:

{
  "case_id": "johnson-v-mta-2025"
}

#🧪 Demo Case IDs to Try

Case Title	Case ID	Notes
🧪 Johnson v. MTA (Fake)	johnson-v-mta-2025	Returns fake example
Littlejohn v. State	8560467914430638671	Real case
Beattie v. Beattie	10195889690540364307	Real case
Travelers Indemnity v. Lake	8355294677874943981	Real case
Tilden v. State	4924998297704337602	Real case
Tynes v. Florida Dept. of Juvenile Justice	9445364666925364919	Real case


#✨ Features

🧠 Uses OpenAI GPT-3.5 to detect legal case treatments

⚡ Responsive frontend for user interaction

🔐 .env protected API key storage

🛠️ Fallback demo mode using johnson-v-mta-2025

🔄 JSON-based API output for easy integration

#🧠 Why This Project?
This project extends the original LLM take-home assignment by adding a full frontend and live API. It demonstrates:

Prompt engineering

API development with FastAPI

Integration of LLMs with real-world interfaces

UI/UX packaging and testing

👩‍💻 Created by
Teila A. Garraway
🔗 Portfolio
💼 LinkedIn
📦 GitHub

