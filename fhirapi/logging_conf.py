import logging
from logging.config import dictConfig

from fhirapi.config import DevConfig, config


def obfuscated(email: str, obfuscation_length: int) -> str:
    """
    Obfuscate the email address by replacing the characters with asterisks.
    """
    characters = email[:obfuscation_length]
    first, last = email.split("@")
    return characters + ("*" * (len(first) - obfuscation_length)) + "@" + last


class EmailObfuscatorFilter(logging.Filter):
    """
    Filter to obfuscate the email address in the logging.
    """

    def __init__(self, name: str = "", obfuscation_length: int = 2) -> None:
        super().__init__(name)
        self.obfuscation_length = obfuscation_length

    def filter(self, record: logging.LogRecord) -> bool:
        if "email" in record.__dict__:
            record.email = obfuscated(record.email, self.obfuscation_length)
        return True


handlers = ["default", "rotating_file"]
if isinstance(config, DevConfig):
    handlers.append("logtail")


def configure_logging() -> None:
    dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "filters": {
                # asgi_correlation_id is a library that adds a correlation ID to the logging
                "correlation_id": {
                    "()": "asgi_correlation_id.CorrelationIdFilter",
                    "uuid_length": 8 if isinstance(config, DevConfig) else 32,
                    "default_value": "-",
                },
                "email_obfuscator": {
                    "()": EmailObfuscatorFilter,
                    "obfuscation_length": 2 if isinstance(config, DevConfig) else 0,
                },
            },
            "formatters": {
                "console": {
                    "class": "logging.Formatter",
                    "datefmt": "%Y-%m-%d %H:%M:%S",
                    "format": "(%(correlation_id)s) %(name)s:%(lineno)d - %(message)s",
                },
                "file": {
                    "class": "pythonjsonlogger.jsonlogger.JsonFormatter",
                    "datefmt": "%Y-%m-%d %H:%M:%S",
                    "format": "%(asctime)s %(msecs)03d %(levelname)-8s %(correlation_id)s %(name)s %(lineno)d %(message)s",
                },
            },
            "handlers": {
                "default": {
                    "class": "rich.logging.RichHandler",
                    "level": "DEBUG",
                    "formatter": "console",
                    "filters": ["correlation_id", "email_obfuscator"],
                },
                "rotating_file": {
                    "class": "logging.handlers.RotatingFileHandler",
                    "level": "DEBUG",
                    "formatter": "file",
                    "filename": "fhirapi.log",
                    "maxBytes": 1024 * 1024,  # 1MB
                    "backupCount": 5,
                    "encoding": "utf-8",
                    "filters": ["correlation_id", "email_obfuscator"],
                },
                "logtail": {
                    "class": "logtail.LogtailHandler",
                    "level": "DEBUG",
                    "formatter": "console",
                    "source_token": config.LOGTAIL_API_KEY,
                    "host": "https://s1595814.eu-nbg-2.betterstackdata.com",
                    "filters": ["correlation_id", "email_obfuscator"],
                },
            },
            "loggers": {
                "uvicorn": {"handlers": ["default", "rotating_file"], "level": "INFO"},
                "fhirapi": {  # root logger for the fhirapi package
                    "handlers": handlers,
                    "level": "DEBUG"
                    if isinstance(config, DevConfig)
                    else "INFO",  # Debug in development, INFO otherwise
                    "propagate": False,  # Prevent the logger from propagating messages to the parent logger
                },
                "databases": {"handlers": ["default"], "level": "WARNING"},
                "aiosqlite": {"handlers": ["default"], "level": "WARNING"},
            },
        }
    )
