import requests as r
from dataclasses import dataclass
from typing import Optional
import logging

# Configure logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


@dataclass
class Quote:
    quote: str
    author: str


# Define custom exception for better error handling
class QuoteFetchError(Exception):
    pass


def get_quote(url_site: str) -> Optional[Quote]:
    try:
        # Send a GET request with a timeout to avoid hanging indefinitely
        response: r.Response = r.get(url=url_site, timeout=10)
        response.raise_for_status()  # Will raise an HTTPError for bad status codes

        # Validate if the response is JSON and contains necessary data
        try:
            data: dict = response.json()
        except ValueError:
            logging.error(f"Failed to parse JSON response from {url_site}")
            return None

        # Extract quote and author with fallback values
        quote: str = data.get("content", "...").strip()
        author: str = data.get("author", "...").strip()

        if not quote or not author:
            logging.warning(f"Incomplete data from API. Quote: {quote}, Author: {author}")

        return Quote(quote=quote, author=author)

    except r.exceptions.Timeout:
        logging.error(f"Request to {url_site} timed out.")
    except r.exceptions.RequestException as e:
        logging.error(f"Request to {url_site} failed with error: {e}")
    except QuoteFetchError as e:
        logging.error(f"Quote fetching failed: {e}")

    return None


def main():
    url: str = 'https://api.quotable.io/random'

    # Get the quote
    quote: Optional[Quote] = get_quote(url_site=url)

    if quote:
        # If we successfully got the quote, print it
        print(f"Quote: {quote.quote}")
        print(f"Author: {quote.author}")
    else:
        # If the quote couldn't be fetched, notify the user
        print("Failed to retrieve a quote.")


if __name__ == "__main__":
    main()
