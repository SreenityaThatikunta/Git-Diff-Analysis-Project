import os
import subprocess

output_folder = "git_diffs"
os.makedirs(output_folder, exist_ok=True)

commit_hashes = subprocess.check_output(["git", "log", "--pretty=format:%H"]).decode().splitlines()

count = 0
for commit in commit_hashes:
    diff_command = ["git", "diff", f"{commit}^", commit]
    diff_output = subprocess.check_output(diff_command).decode()
    
    file_path = os.path.join(output_folder, f"diff_{count}.txt")
    count += 1
    with open(file_path, "w") as file:
        file.write(diff_output)

    print(f"Saved diff for commit {commit} to {file_path}")