import os

def combine_markdown_files():
    combined_file = "combined_explanations.md"
    exp_folder = "explanations"
    markdown_files = [file for file in os.listdir(exp_folder) if file.endswith(".md")]
    markdown_files = sorted(markdown_files, key=lambda x: int(x.split("_")[-1].split(".")[0]))

    if not markdown_files:
        print(f"No '.md' files found in the folder {exp_folder}.")
    else:
        with open(combined_file, "w", encoding="utf-8") as combined:
            for markdown_file in markdown_files:
                file_path = os.path.join(exp_folder, markdown_file)
                with open(file_path, "r", encoding="utf-8") as file:
                    markdown_content = file.read()
                    combined.write(markdown_content)
                    combined.write("\n\n---\n\n")

        print(f"Combined all explanations to {combined_file}")