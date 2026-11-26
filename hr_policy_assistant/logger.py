"""Step 0: shared logger used by every other step.

Every module in this app asks this file for a logger instead of
setting up its own. That way all logs (from document loading to the
final answer) end up in one place, in one consistent format.
"""

import logging 
import os 
from datetime import datetime


LOGS_DIR = "logs"

# One folder per day (e.g. logs/26_November_2026/), and inside it
# one log file per run, named with the time the run started.
_now = datetime.now()
DAILY_LOGS_DIR = os.path.join(LOGS_DIR, _now.strftime("%d_%B_%Y"))
os.makedirs(DAILY_LOGS_DIR, exist_ok=True)

RUN_LOG_FILE = os.path.join(DAILY_LOGS_DIR, f"run_{_now.strftime('%H%M%S')}.log")


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler(RUN_LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(),
    ],
)

def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)