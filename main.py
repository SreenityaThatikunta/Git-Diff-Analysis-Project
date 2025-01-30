from dotenv import load_dotenv
import os
import subprocess
from save_diff import save_diff
from explain_gemini import explain_gemini
from convert import combine_markdown_files

load_dotenv()
api_key = os.getenv('API_KEY')
output_file = "final.pdf"
markdown_file = "combined_explanations.md"

if __name__ == "__main__":
    try:
        save_diff()
        explain_gemini()
        combine_markdown_files()
        subprocess.run(["mdpdf", "-o", output_file, markdown_file], check=True)
        print("Workflow completed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")