from datetime import datetime
import os

os.makedirs("logs", exist_ok=True)

log_file = f"logs/hotfix_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

with open(log_file, "w") as f:
    f.write(f"{datetime.now()} | HOTFIX_CREATED\n")
    f.write(f"{datetime.now()} | CODE_COMMITTED\n")
    f.write(f"{datetime.now()} | PR_OPENED\n")
    f.write(f"{datetime.now()} | PR_MERGED\n")
    f.write(f"{datetime.now()} | RELEASE_CREATED\n")

print(f"Generated: {log_file}")