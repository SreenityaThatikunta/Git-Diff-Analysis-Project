import os
import subprocess
from dotenv import load_dotenv

def save_diff():
    load_dotenv()
    repo_path = os.getenv("repo_path")
    output_folder = "git_diffs"
    os.makedirs(output_folder, exist_ok=True)

    try:
        subprocess.run(["git", "-C", repo_path, "status"], check=True, stdout=subprocess.DEVNULL)

        commit_hashes = subprocess.check_output(
            ["git", "-C", repo_path, "log", "--pretty=format:%H"]
        ).decode().splitlines()

        count = 1
        for commit in commit_hashes:
            diff_command = ["git", "-C", repo_path, "diff", f"{commit}^", commit]
            diff_output = subprocess.check_output(diff_command).decode()
            file_path = os.path.join(output_folder, f"diff_{count}.txt")
            count += 1
            with open(file_path, "w") as file:
                file.write(diff_output)

        print(f"{count} diffs have been saved successfully.")

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
