# Library imports
import logging


# Local imports
from config.logging_config import setup_logging
from crawler.verify import verify

# Logging
logger = logging.getLogger(__name__)

def main() -> None:
    setup_logging()
    logger.info("gmIdeas is running...")

    url = "https://www.reddit.com/r/learnprogramming/"
    
    verify(url)
    logger.info("gmIdeas finished successfully")


if __name__ == "__main__":
    main()