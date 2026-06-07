# ============================================================================
# General Knowledge Quiz Application
# ============================================================================
# This is a simple interactive quiz application that tests users on general
# knowledge questions. The application tracks scores and provides performance
# feedback based on the user's performance.
# ============================================================================

# Initialize score variable to track correct answers
score = 0

# Display welcome message
print("=" * 60)
print("        Welcome to the General Knowledge Quiz!        ".center(60))
print("=" * 60)
print("\nAnswer the following 5 questions. Good luck!\n")

# Question 1: Capital of France
print("Question 1: What is the capital of France?")
user_answer_1 = input("Your answer: ").strip().lower()

# Validate answer and update score
if user_answer_1 == "paris":
    print("Correct!\n")
    score = score + 1
else:
    print("Wrong! The correct answer is: Paris\n")

# Question 2: The Red Planet
print("Question 2: Which planet is known as the Red Planet?")
user_answer_2 = input("Your answer: ").strip().lower()

# Validate answer and update score
if user_answer_2 == "mars":
    print("Correct!\n")
    score = score + 1
else:
    print("Wrong! The correct answer is: Mars\n")

# Question 3: National animal of India
print("Question 3: What is the national animal of India?")
user_answer_3 = input("Your answer: ").strip().lower()

# Validate answer and update score
if user_answer_3 == "tiger":
    print("Correct!\n")
    score = score + 1
else:
    print("Wrong! The correct answer is: Tiger\n")

# Question 4: Father of Computer
print("Question 4: Who is known as the Father of Computer?")
user_answer_4 = input("Your answer: ").strip().lower()

# Validate answer and update score
if user_answer_4 == "charles babbage":
    print("Correct!\n")
    score = score + 1
else:
    print("Wrong! The correct answer is: Charles Babbage\n")

# Question 5: Largest ocean
print("Question 5: What is the largest ocean on Earth?")
user_answer_5 = input("Your answer: ").strip().lower()

# Validate answer and update score
if user_answer_5 == "pacific ocean":
    print("Correct!\n")
    score = score + 1
else:
    print("Wrong! The correct answer is: Pacific Ocean\n")

# ============================================================================
# Display Results and Performance Analysis
# ============================================================================

# Calculate percentage
total_questions = 5
percentage = (score / total_questions) * 100

# Display score summary
print("=" * 60)
print("                    Quiz Completed!                    ".center(60))
print("=" * 60)
print(f"\nTotal Score: {score}/{total_questions}")
print(f"Percentage: {percentage:.1f}%")

# Determine and display performance message based on score
if score == 5:
    performance_message = "Excellent"
    print(f"Performance: {performance_message} 🌟")
elif score == 4:
    performance_message = "Very Good"
    print(f"Performance: {performance_message} 👍")
elif score == 3:
    performance_message = "Good"
    print(f"Performance: {performance_message} 😊")
else:
    performance_message = "Needs Improvement"
    print(f"Performance: {performance_message} 📚")

print("=" * 60)
print("\nThank you for taking the quiz!\n")
