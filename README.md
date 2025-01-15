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
   cd your-repo
   ```
2. Install dependencies:
   ```bash
   pip install google-generativeai
   ```
   ```bash
   npm i mdpdf
   ```


## Workflow:

1. **Save Diffs**:
   - Run `save_diff.py` to extract Git diffs from the repository.
   - The diffs will be saved in the `git_diffs` folder.

2. **Generate Explanations**:
   - Run `explain_gemini.py` to generate explanations for the diffs using the Gemini AI model.
   - The explanations will be saved in the `explanations` folder.

3. **Combine Explanations**:
   - Run `convert.py` to combine all Markdown explanations into a single file, `combined_explanations.md`.

4. **Export to PDF**:
   - Use `mdpdf` to convert `combined_explanations.md` into a PDF:
     ```bash
     mdpdf -o final.pdf combined_explanations.md
     ```
