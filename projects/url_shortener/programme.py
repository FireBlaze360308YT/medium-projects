from typing import Final, Dict, Optional
import requests
import logging

API_KEY: Final[str] = "#U need to sign up to this site https://cutt.ly/ and get the API key"
BASE_URL: Final[str] = "https://cutt.ly/api/api.php"


def shorten_link(full_link: str) -> Optional[str]:
    """Shorten a URL using the Cutt.ly API."""
    payload: Dict[str, str] = {"key": API_KEY, "short": full_link}
    try:
        response = requests.get(BASE_URL, params=payload)
        response.raise_for_status()  # Will raise an HTTPError for bad responses (4xx, 5xx)
        
        data: Dict = response.json()
        
        url_data = data.get("url")
        if not url_data:
            logging.error("No URL data returned from API.")
            return None
        
        if url_data["status"] == 7:
            return url_data["shortLink"]
        else:
            logging.error(f"API returned error status: {url_data['status']}")
            return None
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")
        return None
    except ValueError as e:
        logging.error(f"Failed to parse JSON response: {e}")
        return None


def main():
    input_link: str = input("Enter a link: ")
    short_link = shorten_link(input_link)
    
    if short_link:
        print("Shortened Link:", short_link)
    else:
        print("Failed to shorten the link.")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()
