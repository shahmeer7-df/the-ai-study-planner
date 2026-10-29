# AI Study Planner
# A beginner-friendly Python project

def create_study_plan():
    print("=" * 40)
    print("       MY AI STUDY PLANNER")
    print("=" * 40)

    # Get student information
    name = input("Enter your name: ").strip()

    while name == "":
        name = input("Name cannot be empty. Enter your name: ").strip()

    goal = input("What is your AI learning goal? ").strip()

    while goal == "":
        goal = input("Please enter your AI learning goal: ").strip()

    # Get study days
    while True:
        try:
            days = int(input("Study days per week (1-7): "))
            if 1 <= days <= 7:
                break
            print("Please enter a number from 1 to 7.")
        except ValueError:
            print("Please enter a whole number.")

    # Get daily study hours
    while True:
        try:
            hours = float(input("Study hours per day (more than 0): "))
            if 0 < hours <= 24:
                break
            print("Enter hours greater than 0 and up to 24.")
        except ValueError:
            print("Please enter a valid number.")

    # Calculate weekly study hours
    weekly_hours = days * hours

    # Personalize topics based on the learning goal
    goal_lower = goal.lower()

    if "machine learning" in goal_lower:
        topics = [
            "Learn Python basics and practice coding.",
            "Study basic mathematics and data concepts.",
            "Understand supervised and unsupervised learning.",
            "Build a small machine learning project."
        ]
    elif "deep learning" in goal_lower:
        topics = [
            "Review Python and machine learning basics.",
            "Learn about neural networks.",
            "Study layers, activation functions, and training.",
            "Explore a small deep learning example."
        ]
    elif "data science" in goal_lower or "data analysis" in goal_lower:
        topics = [
            "Learn Python variables, lists, and dictionaries.",
            "Practice working with data and tables.",
            "Learn basic statistics and data visualization.",
            "Complete a small data analysis project."
        ]
    elif "generative ai" in goal_lower or "gen ai" in goal_lower:
        topics = [
            "Learn Python fundamentals.",
            "Understand AI, machine learning, and language models.",
            "Study prompts and how generative AI works.",
            "Create a small AI learning project using examples."
        ]
    elif "python" in goal_lower:
        topics = [
            "Learn variables, input, and output.",
            "Practice conditions and loops.",
            "Learn functions and file handling.",
            "Build a small Python project."
        ]
    else:
        topics = [
            "Learn the basic concepts related to your goal.",
            "Study important AI terms and concepts.",
            "Practice with simple examples and exercises.",
            "Review what you learned and complete a mini-project."
        ]

    # Build the personalized plan
    plan = []
    plan.append("=" * 40)
    plan.append("       YOUR PERSONALIZED STUDY PLAN")
    plan.append("=" * 40)
    plan.append(f"Student Name: {name}")
    plan.append(f"AI Learning Goal: {goal}")
    plan.append(f"Study Days per Week: {days}")
    plan.append(f"Daily Study Hours: {hours:g}")
    plan.append(f"Total Weekly Study Hours: {weekly_hours:g}")
    plan.append("")
    plan.append("YOUR WEEKLY SCHEDULE")
    plan.append("-" * 40)

    for day in range(1, days + 1):
        topic = topics[(day - 1) % len(topics)]
        plan.append(f"Study Day {day}: {topic}")
        plan.append(f"  Study time: {hours:g} hour(s)")

    plan.append("")
    plan.append("STUDY TIPS")
    plan.append("- Set a small goal for every study session.")
    plan.append("- Practice coding instead of only reading.")
    plan.append("- Take short breaks when needed.")
    plan.append("- Review your progress every week.")
    plan.append("- Adjust your plan as you improve.")
    plan.append("")
    plan.append("Good luck with your AI learning journey!")
    plan.append("=" * 40)

    # Display the plan
    study_plan = "\n".join(plan)
    print("\n" + study_plan)

    # Save the plan to a text file
    with open("study-plan.txt", "w", encoding="utf-8") as file:
        file.write(study_plan)

    print("\nYour study plan was saved to study-plan.txt")


# Run the program
create_study_plan()
