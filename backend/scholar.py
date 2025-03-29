import requests
from bs4 import BeautifulSoup
from typing import Optional, Dict, Any

class ScholarAPI:
    """Handles interactions with Google Scholar's case API."""
    
    BASE_URL = "https://scholar.google.com/scholar_case"
    
    @classmethod
    def fetch_case(cls, case_id: str) -> Optional[Dict[str, Any]]:
        """
        Fetches case information from Google Scholar.
        
        Args:
            case_id: The unique identifier for the case
            
        Returns:
            Dictionary containing case information or None if not found
        """
        try:
            response = requests.get(f"{cls.BASE_URL}?case={case_id}")
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract case title
            title = soup.find('div', {'id': 'title'})
            case_title = title.text if title else "Unknown Title"
            
            # Extract case text
            case_text = soup.find('div', {'id': 'case_text'})
            text = case_text.text if case_text else ""
            
            return {
                "id": case_id,
                "title": case_title,
                "text": text
            }
            
        except requests.RequestException as e:
            print(f"Error fetching case {case_id}: {str(e)}")
            return None 