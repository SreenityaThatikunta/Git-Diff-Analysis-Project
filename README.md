# Git-Diff-Analysis-Project

## Overview:

This project automates the process of compiling and explaining git diffs from a repository. It is designed for budding developers to comprehend the working of a repository.

## Files:

### 1. save_diff.py
- Extracts diffs for all Git commits in the current repository.
- Saves each diff to a separate `.txt` file in the `git_diffs` folder.

### 2. explain_gemini.py
- Uses Google's Gemini AI model to generate detailed, beginner-friendly explanations for Git diffs stored in the `git_diffs` folder.
- Outputs explanations in Markdown format, stored in the `explanations` folder.

### 3. convert.py
- Combines multiple Markdown files in the `explanations` folder into a single file called `combined_explanations.md`.

## Requirements
- Python 3.7+
- Required Python libraries:
  - `os`
  - `subprocess`
  - `google.generativeai`
- A terminal with Git installed.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/SreenityaThatikunta/Git-Diff-Analysis-Project.git
   
   cd Git-Diff-Analysis-Project
   ```
2. Install dependencies:
   ```bash
   pip install google-generativeai

   npm i mdpdf
   ```


## Workflow:

1. Clone the GitHub repository that you wish to be explained.

2. Create a .env file and add your Gemini API key and the cloned GitHub repository folder path.
   ```bash
      api_key = ""
      repo_path = ""
      ```

3. Add the suitable prompt and system instructions according the repo in the ```explain_gemini.py ``` file.

4. Run the main.py file.
   ```bash
   python3 main.py
   ```

5. A pdf named final.pdf is saved in your current directory.