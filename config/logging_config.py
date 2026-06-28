from pathlib import Path
import logging
from logging.handlers import RotatingFileHandler
from rich.logging import RichHandler

def setup_logging(level=logging.INFO):
    log_dir = Path("logs")
    log_dir.mkdir(parents=True, exist_ok=True)

    file_formatter = logging.Formatter(
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    console_handler = RichHandler(
        rich_tracebacks=True,
        show_path=False,
    )
    console_handler.setFormatter(
        logging.Formatter("%(message)s")
    )

    file_handler = RotatingFileHandler(
        log_dir / "gmideas.log",
        maxBytes=5 * 1024 * 1024,  # 5 MB
        backupCount=5,
        encoding="utf-8",
    )

    file_handler.setFormatter(file_formatter)

    root_logger = logging.getLogger()

                         
    # Prevent duplicate handlers if setup_logging() is called twice)
    if root_logger.handlers:
        return
    
    root_logger.setLevel(level)
    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)


