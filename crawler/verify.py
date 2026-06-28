import httpx
import logging
from config.logging_config import setup_logging

# Logging system
setup_logging()
logger = logging.getLogger(__name__)

# HTTP Request 
response = httpx.get("https://www.reddit.com/r/learnprogramming/")

# Status code check
match response.status_code:
    case 200:
        _
    case 404:
        _
    case 403:
        _
    case 429:
        _


# Check for specific content in the response
if "verify" in response.text.lower():
    print("Switch to playwright")