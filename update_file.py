from datetime import datetime

with open("daily_update.txt", "w") as f:
    f.write(f"Updated on {datetime.utcnow().isoformat()} UTC\n")
