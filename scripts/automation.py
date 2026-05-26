import subprocess
import time
import sys

# Replace with your actual commit id
COMMIT_ID = "dcc9f74"

print("\n=== HOTFIX WORKFLOW STARTED ===\n")

commands = [

    ["git", "checkout", "main"],

    ["git", "checkout", "-b", "hotfix/login-fix"],

    ["git", "cherry-pick", COMMIT_ID],

    ["git", "status"]
]

# ---------------------------------
# REAL CLI COMMAND EXECUTION
# ---------------------------------

for command in commands:

    print(f"\nRunning command: {' '.join(command)}")

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    print("STDOUT:")
    print(result.stdout)

    print("STDERR:")
    print(result.stderr)

    print("RETURN CODE:")
    print(result.returncode)

    # VALIDATION
    if result.returncode != 0:

        print(f"\nFAILED COMMAND: {' '.join(command)}")

        sys.exit(1)

# ---------------------------------
# MODIFY FILE
# ---------------------------------

with open("app.txt", "a") as file:
    file.write("\nHotfix deployed")

print("\nDeployment change added")

# ---------------------------------
# ADD + COMMIT
# ---------------------------------

extra_commands = [

    ["git", "add", "."],

    ["git", "commit", "-m", "deploy hotfix"]
]

for command in extra_commands:

    print(f"\nRunning command: {' '.join(command)}")

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    print(result.stdout)
    print(result.stderr)

    if result.returncode != 0:

        print(f"\nFAILED COMMAND: {' '.join(command)}")

        sys.exit(1)

# ---------------------------------
# ASYNC WORKFLOW SIMULATION
# ---------------------------------

print("\nCI/CD PIPELINE RUNNING...\n")

for i in range(5):

    print(f"Polling pipeline status... Attempt {i+1}")

    time.sleep(5)

print("\nPipeline SUCCESS")

# ---------------------------------
# FINAL VALIDATION
# ---------------------------------

validation = subprocess.run(
    ["git", "status"],
    capture_output=True,
    text=True
)

print(validation.stdout)

if validation.returncode != 0:

    print("Validation failed")

    sys.exit(1)

print("\n=== HOTFIX WORKFLOW SUCCESSFUL ===")

sys.exit(0)