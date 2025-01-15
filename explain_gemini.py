import os
import google.generativeai as genai

api_key = "AIzaSyAj9rECNOl_zwQ0zgc4K8xAqucwYgEySQg"  
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

        prompt = f"I am doing a course on redux. The course is in JavaScript. I have files containing git diffs of each lesson, I need a detailed explanation of the code in a beginner friendly way. Give the output in markdown format. The following is a git diff:\n\n{git_diff_content}"

        try:
            model = genai.GenerativeModel(model_name="gemini-2.0-flash-exp", system_instruction="you are a redux tutor. redux is a javascript library for predictable and maintainable global state management. use UTF-8 encoding for the output text.")  
            response = model.generate_content(prompt)
            explanation = response.text

            explanation_file = os.path.join(explanation_folder, f"explanation_{diff_file}") 
            explanation_file = explanation_file.replace(".txt", ".md")

            with open(explanation_file, "w") as file:
                file.write(explanation)

            print(f"Saved explanation for {diff_file} to {explanation_file}\n")

        except Exception as e:
            print(f"Failed to process {diff_file}. Error: {e}")