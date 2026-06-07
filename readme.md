# General Knowledge Quiz 🎯

A simple yet engaging interactive Python application that tests users on general knowledge questions. This project demonstrates fundamental Python programming concepts including variables, input/output, conditional statements, and f-strings.

## 📋 Overview

The **General Knowledge Quiz** is a console-based application that presents users with 5 thought-provoking general knowledge questions. The application tracks the user's score and provides performance feedback based on their answers.

### Features

- ✨ **5 Engaging Questions**: Covers diverse topics including geography, astronomy, wildlife, history, and nature
- 📊 **Score Tracking**: Maintains and displays the user's score throughout the quiz
- ✅ **Real-time Feedback**: Shows "Correct!" or "Wrong!" after each question with the correct answer when needed
- 📈 **Performance Analysis**: Displays total score, percentage, and a personalized performance message
- 🎯 **Case-Insensitive Input**: Automatically handles uppercase/lowercase differences
- 💬 **User-Friendly Interface**: Clean, formatted console output with clear prompts

## 🚀 Getting Started

### Prerequisites

- **Python 3.6+** installed on your system
- No external dependencies required

### Installation

1. **Clone or download the project**:
   ```bash
   git clone https://github.com/suhailapvak-ux/decodelab_project4.git
   cd decodelab_project4
   ```

### Running the Quiz

Simply execute the Python script:

```bash
python knowledgequiz.py
```

Or:

```bash
python3 knowledgequiz.py
```

## 📚 Quiz Questions

The quiz includes 5 questions covering various domains:

1. **Geography**: "What is the capital of France?" → `paris`
2. **Astronomy**: "Which planet is known as the Red Planet?" → `mars`
3. **Wildlife**: "What is the national animal of India?" → `tiger`
4. **History**: "Who is known as the Father of Computer?" → `charles babbage`
5. **Nature**: "What is the largest ocean on Earth?" → `pacific ocean`

## 🎲 Performance Levels

Your performance is evaluated based on the following scale:

| Score | Performance Level      |
|-------|------------------------|
| 5/5   | ⭐ Excellent           |
| 4/5   | 👍 Very Good           |
| 3/5   | 😊 Good                |
| <3/5  | 📚 Needs Improvement   |

## 💻 Code Structure

### Key Concepts Demonstrated

- **Variables**: `score` variable to track correct answers
- **Input Handling**: `input()` function to accept user responses
- **String Methods**: `.strip()` and `.lower()` for case-insensitive comparison
- **Conditional Logic**: `if-else` statements to validate answers
- **Score Calculation**: Arithmetic operations to update and calculate scores
- **String Formatting**: f-strings for dynamic output
- **Comments**: Comprehensive comments throughout the code

### File Structure

```
project_4_knowledgequiz/
│
├── knowledgequiz.py           # Main quiz application
├── README.md                   # Project documentation
├── QUICKSTART.md               # Quick start guide
├── CONTRIBUTING.md             # Contribution guidelines
├── CHANGELOG.md                # Version history
├── LICENSE                     # MIT License
├── requirement.txt             # Project dependencies
├── .gitignore                  # Git configuration
└── screenshot/                 # Screenshots directory (optional)
```

## 🎮 Example Run

```
============================================================
        Welcome to the General Knowledge Quiz!        
============================================================

Answer the following 5 questions. Good luck!

Question 1: What is the capital of France?
Your answer: paris
Correct!

Question 2: Which planet is known as the Red Planet?
Your answer: MARS
Correct!

Question 3: What is the national animal of India?
Your answer: lion
Wrong! The correct answer is: Tiger

Question 4: Who is known as the Father of Computer?
Your answer: charles babbage
Correct!

Question 5: What is the largest ocean on Earth?
Your answer: pacific ocean
Correct!

============================================================
                    Quiz Completed!                    
============================================================

Total Score: 4/5
Percentage: 80.0%
Performance: Very Good 👍
============================================================

Thank you for taking the quiz!
```

## 🔧 How to Use

1. **Start the Quiz**: Run the script with Python
2. **Answer Questions**: Type your answer and press Enter
3. **View Feedback**: The application immediately tells you if your answer is correct
4. **Get Results**: After completing all 5 questions, view your final score and performance rating

### Tips for Better Accuracy

- Answer format is case-insensitive (e.g., "PARIS", "Paris", "paris" are all accepted)
- Extra spaces before/after your answer are automatically removed
- Focus on the core answer (e.g., "paris" for France's capital)

## 📝 Learning Objectives

This project is designed to teach and reinforce:

- ✅ Variable declaration and assignment
- ✅ User input and output operations
- ✅ Conditional statements (if-else)
- ✅ String manipulation and methods
- ✅ Basic arithmetic and percentage calculations
- ✅ Code documentation with comments
- ✅ F-string formatting for dynamic output
- ✅ Program flow and logic

## 🚀 Future Enhancements

Possible improvements and extensions:

- 📂 Load questions from an external file or database
- 🔀 Randomize question order
- ⏱️ Add a timer to answer each question
- 🎨 Create a GUI version using tkinter
- 📱 Add difficulty levels (Easy, Medium, Hard)
- 🗄️ Store results in a database for progress tracking
- 🌐 Add multiple language support

## 📄 License

This project is open source and available under the MIT License. Feel free to use, modify, and distribute it.

## 🤝 Contributing

Contributions are welcome! If you'd like to:

- Add more questions
- Improve the code structure
- Enhance the user interface
- Fix any bugs

Please feel free to submit a pull request or open an issue. See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## 📬 Contact & Support

If you have any questions or face any issues:

- Open an issue on GitHub
- Contact the project maintainer
- Check the documentation in the code comments

## 📚 Additional Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [Python Input/Output Guide](https://docs.python.org/3/howto/pyos.html)
- [Python String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [F-string Formatting](https://docs.python.org/3/tutorial/inputoutput.html#tut-f-strings)

---

**Happy Learning!** 🎓
