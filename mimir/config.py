import os
from pathlib import Path

# Norns
NORNS_URL = os.environ.get("NORNS_URL", "http://localhost:4001")
NORNS_API_KEY = os.environ.get("NORNS_API_KEY", "")
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")

# Discord
DISCORD_BOT_TOKEN = os.environ.get("DISCORD_BOT_TOKEN", "")

# GitHub
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
GITHUB_REPOS = [r.strip() for r in os.environ.get("GITHUB_REPOS", "").split(",") if r.strip()]

# Google Docs
GOOGLE_CREDENTIALS_PATH = os.environ.get("GOOGLE_CREDENTIALS_PATH", "")
GOOGLE_DOC_IDS = [d.strip() for d in os.environ.get("GOOGLE_DOC_IDS", "").split(",") if d.strip()]

# Memory
MEMORY_PATH = Path(os.environ.get("MEMORY_PATH", Path.home() / ".mimir" / "memory.json"))
