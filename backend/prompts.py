from typing import Dict, Any

def create_analysis_prompt(case_text: str) -> str:
    """
    Creates a prompt for analyzing negative treatments in a legal case.

    Args:
        case_text (str): Full text of the legal case.

    Returns:
        str: Formatted prompt string for the LLM.
    """
    return f"""You are a legal expert analyzing a court case for negative treatments of other cases.
A negative treatment occurs when a court overrules, limits, or otherwise diminishes the holding of a prior case.

Please analyze the following case text and identify any negative treatments of other cases. For each negative treatment found, provide:
1. The citation of the treated case
2. The type of negative treatment (e.g., overruling, limiting, distinguishing)
3. The relevant text from the case that shows the negative treatment
4. A brief explanation of why this constitutes negative treatment

Case Text:
\"\"\"
{case_text}
\"\"\"

Please format your response as a JSON object with the following structure:
{{
  "negative_treatments": [
    {{
      "treated_case_citation": "citation",
      "treatment_type": "type",
      "relevant_text": "text",
      "explanation": "explanation"
    }}
  ]
}}

If no negative treatments are found, return:
{{
  "negative_treatments": []
}}"""
