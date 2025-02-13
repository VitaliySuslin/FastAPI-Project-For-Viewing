import logging
from logging.config import dictConfig

# Define the logging configuration
dictConfig(
    {
        'version': 1,  # Version of the logging configuration schema
        'disable_existing_loggers': False,  # Keep existing loggers active
        'formatters': {
            'default': {
                'format': '%(pathname)s:%(lineno)d %(asctime)s [%(levelname)s] : %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S',  # Date format for timestamps
            },
            'access': {
                'format': '%(pathname)s:%(lineno)d %(asctime)s [%(levelname)s] : %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S',  # Date format for timestamps
            },
        },
        'handlers': {
            'console': {
                'formatter': 'default',  # Use the 'default' formatter
                'class': 'logging.StreamHandler',  # Output logs to the console
                'level': logging.INFO,  # Minimum log level for this handler
                'stream': 'ext://sys.stdout',  # Stream to standard output
            },
        },
        'root': {
            'level': logging.DEBUG,  # Minimum log level for the root logger
            'handlers': ['console'],  # Handlers to use for the root logger
        },
    }
)

# Create a logger for the application
logger: logging.Logger = logging.getLogger('src')

# Example usage of the logger
logger.debug("Debugging information")
logger.info("Informational message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical issue")