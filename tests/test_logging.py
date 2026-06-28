import logging
import sys
import pytest

from logging.handlers import RotatingFileHandler
from pathlib import Path
from rich.logging import RichHandler

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from config.logging_config import setup_logging


@pytest.fixture(autouse=True)
def clean_logging():
    root_logger = logging.getLogger()
    old_handlers = root_logger.handlers[:]
    old_level = root_logger.level
    root_logger.handlers.clear()

    yield

    for handler in root_logger.handlers:
        handler.close()
    root_logger.handlers[:] = old_handlers
    root_logger.setLevel(old_level)


def test_setup_logging_configures_handlers_and_file(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    logging.getLogger().handlers.clear()

    setup_logging(logging.DEBUG)
    logging.getLogger("test").info("logging works")

    root_logger = logging.getLogger()
    log_file = tmp_path / "logs" / "gmideas.log"

    assert root_logger.level == logging.DEBUG
    assert any(isinstance(handler, RichHandler) for handler in root_logger.handlers)
    assert any(isinstance(handler, RotatingFileHandler) for handler in root_logger.handlers)
    assert logging.getLogger("httpx").level == logging.WARNING
    assert logging.getLogger("httpcore").level == logging.WARNING
    assert "logging works" in log_file.read_text(encoding="utf-8")
