import subprocess
import sys

commands = [
    ["git", "--version"],
    ["git", "status"],
]

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

    if result.returncode != 0:
        print("Command failed!")
        sys.exit(1)

print("\nAll commands executed successfully!")