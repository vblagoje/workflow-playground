import os
import json
import subprocess
import random

def get_committers(project_dir: str) -> set:
    try:
        result = subprocess.run(
            ["git", "log", "--pretty=%an", "--", project_dir],
            check=True,
            text=True,
            capture_output=True
        )
        return set(result.stdout.strip().split('\n'))
    except subprocess.CalledProcessError as e:
        print(f"Error while running git log: {e}")
        return set()

def main():
    project_dir = os.getenv('INPUT_PROJECT_DIR')
    names_handles_json = os.getenv('INPUT_NAMES_HANDLES')
    default_user = os.getenv('INPUT_DEFAULT_USER')

    if not names_handles_json:
        raise ValueError("names_handles_json is None")

    names_handles = json.loads(names_handles_json)
    committers = get_committers(project_dir)

    filtered_handles = [names_handles[name] for name in committers if name in names_handles]

    random_user = random.choice(filtered_handles) if filtered_handles else default_user
    print(f"Selected user: {random_user}")

    output_file = os.getenv('GITHUB_OUTPUT')
    with open(output_file, 'a') as fh:
        fh.write(f"user={random_user}\n")

if __name__ == "__main__":
    main()
