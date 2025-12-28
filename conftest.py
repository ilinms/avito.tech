import sys
from pathlib import Path


sys.path.insert(0, str(Path(__file__).parent))

import pytest
from playwright.sync_api import sync_playwright
