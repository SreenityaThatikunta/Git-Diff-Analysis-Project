import os
import google.generativeai as genai
from dotenv import load_dotenv

def explain_gemini():
    load_dotenv()
    api_key = os.getenv("api_key")
    genai.configure(api_key=api_key)

    diff_folder = "git_diffs"
    explanation_folder = "explanations"

    os.makedirs(explanation_folder, exist_ok=True)

    diff_files = [file for file in os.listdir(diff_folder) if file.endswith(".txt")]

    if not diff_files:
        print(f"No '.txt' files found in the folder {diff_folder}.")
    else:
        for diff_file in diff_files:
            file_path = os.path.join(diff_folder, diff_file)
            with open(file_path, "r") as file:
                git_diff_content = file.read()

            # make sure to edit this prompt based on the contents of the repo that you want to be explained
            prompt = f"I want to understand how password is generated. I have files containing git diffs of each lesson, I need a detailed explanation of the code in a beginner friendly way. Give the output in markdown format. The following is a git diff:\n\n{git_diff_content}"

            try:
                # edit the system instructions accordingly as well
                model = genai.GenerativeModel(model_name="gemini-2.0-flash-exp", system_instruction="use UTF-8 encoding for the output text.")  
                response = model.generate_content(prompt)
                explanation = response.text

                explanation_file = os.path.join(explanation_folder, f"explanation_{diff_file}") 
                explanation_file = explanation_file.replace(".txt", ".md")

                with open(explanation_file, "w") as file:
                    file.write(explanation)


            except Exception as e:
                print(f"Failed to process {diff_file}. Error: {e}")
        print(f"Saved explanations for {len(diff_files)}")