import logging
import httpx

logger = logging.getLogger(__name__)


def verify(url: str):

    logger.info("Starting verification for %s", url)

    try:
        response = httpx.get(url, timeout=30)

    except httpx.RequestError:
        logger.exception("Failed to connect to %s", url)
        return

    logger.info(
        "Received HTTP %d from %s",
        response.status_code,
        url,
    )

    match response.status_code:

        case 200:
            logger.info("Request completed successfully.")

        case 403:
            logger.warning("Access forbidden.")

        case 404:
            logger.warning("Resource not found.")

        case 429:
            logger.warning("Rate limit encountered.")

        case _:
            logger.warning(
                "Unexpected status code %d",
                response.status_code,
            )

    if "verify" in response.text.lower():
        logger.warning(
            "Verification challenge detected. Playwright may be required."
        )

    else:
        logger.info(
            "No verification challenge detected."
        )

    logger.info("Verification complete.")