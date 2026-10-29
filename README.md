# My AI Study Planner

A beginner-friendly command-line study planner written in basic Python. It asks for your name, AI learning goal, study days per week, and study hours per day. It calculates your total weekly study hours, displays a personalized plan, and saves it to `study-plan.txt`.

## Features

- Asks for the learner's name and AI learning goal
- Accepts 1–7 study days per week
- Accepts daily study hours, including decimals such as `1.5`
- Calculates total weekly study hours
- Prints a simple weekly study plan
- Saves the plan as `study-plan.txt`
- Uses only Python's built-in features—no AI API, GUI, database, or external packages

## Requirements

- Python 3.8 or newer (Python 3 is recommended)
- No extra packages are required

## How to run

1. Download or clone this repository.
2. Open a terminal or command prompt in the project folder.
3. Run:

   ```bash
   python main.py
   ```

   On some systems, use `python3 main.py` instead.

4. Answer the questions.
5. Find your generated plan in `study-plan.txt` in the folder where you ran the program.

## Example

If you study 4 days per week for 1.5 hours each day:

`4 × 1.5 = 6 hours per week`

## Project files

- `main.py` — the Python program
- `README.md` — project instructions
- `study-plan.txt` — created automatically when you run the program

## Publish to GitHub

1. Sign in to [GitHub](https://github.com/) and create a new repository named `my-ai-study-planner`.
2. Keep the repository public if you want everyone to see it.
3. In your terminal, move into this project folder and run:

   ```bash
   git init
   git add main.py README.md .gitignore
   git commit -m "Add beginner-friendly AI study planner"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/my-ai-study-planner.git
   git push -u origin main
   ```

4. Replace `YOUR-USERNAME` with your GitHub username.

If Git asks you to sign in, follow GitHub's authentication prompts. If Git is not installed, install Git first or use GitHub's website to upload the files.

## License

You may add a license file if you want others to reuse or modify the project.
