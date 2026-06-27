import httpx
import logging

response = httpx.get("https://www.reddit.com/r/learnprogramming/")

# Status code check
match response.status_code:
    case 200:

match response.status_code:
    case 404:

match response.status_code:
    case 403:

match response.status_code
    case 429:

# Check for specific content in the response
if "verify" in response.text.lower():
    return "Switch to playwright"