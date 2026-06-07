# Contributing to General Knowledge Quiz

Thank you for your interest in contributing to the General Knowledge Quiz project! 🎉

## 📋 How to Contribute

We welcome contributions of all kinds. Here are some ways you can help:

### 1. **Report Bugs** 🐛

If you find a bug in the project:

- Check if the issue already exists in the [Issues](https://github.com/yourusername/general-knowledge-quiz/issues)
- If not, create a new issue with:
  - A clear and descriptive title
  - Detailed description of the problem
  - Steps to reproduce the issue
  - Your Python version and OS information

### 2. **Suggest Enhancements** 💡

Have an idea to improve the quiz?

- Open an issue titled "[FEATURE REQUEST]" with your suggestion
- Explain the motivation and use case
- Provide examples of how the feature would work

### 3. **Improve Documentation** 📚

Help us improve the README and code comments:

- Fix typos or unclear explanations
- Add examples or clarifications
- Improve formatting and readability

### 4. **Add New Questions** ❓

Help expand the quiz with new questions:

- Propose questions with correct answers
- Ensure questions are clear and unambiguous
- Questions should be educational and interesting

### 5. **Code Improvements** 🔧

Submit code improvements through pull requests:

- Refactor existing code
- Add new features (see suggested enhancements in README)
- Improve code quality and efficiency

## 🚀 Getting Started with Development

1. **Fork the repository**
   ```bash
   # Click the "Fork" button on GitHub
   ```

2. **Clone your fork**
   ```bash
   git clone https://github.com/yourusername/general-knowledge-quiz.git
   cd general-knowledge-quiz
   ```

3. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b bugfix/your-bug-fix
   ```

4. **Make your changes**
   - Follow the code style guidelines below
   - Add comments to explain your changes
   - Test your changes thoroughly

5. **Commit your changes**
   ```bash
   git add .
   git commit -m "Clear description of your changes"
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request**
   - Go to GitHub and create a Pull Request from your fork
   - Provide a clear description of your changes
   - Reference any related issues

## 📝 Code Style Guidelines

To maintain consistency in the codebase:

### Python Style

- Follow **PEP 8** standards
- Use meaningful variable and function names
- Add comments for complex logic
- Use f-strings for string formatting
- Keep lines under 100 characters where practical
- Include docstrings for functions

### Example

```python
# Good: Clear comment and f-string
score = 3
total = 5
percentage = (score / total) * 100
print(f"Your score: {score}/{total} ({percentage:.1f}%)")

# Avoid: Unclear variable names
s = 3
t = 5
print(s, "/", t, "=", (s/t)*100)
```

### Comments

- Use `#` for single-line comments
- Explain the "why", not the "what"
- Keep comments up-to-date with code

## 🧪 Testing Your Changes

Before submitting a pull request:

1. **Test the quiz thoroughly**
   ```bash
   python knowledgequiz.py
   ```

2. **Test edge cases**
   - Try different answer formats (uppercase, lowercase, mixed)
   - Test with extra spaces before/after answers
   - Verify all questions work correctly

3. **Check for errors**
   - Run the script multiple times
   - Look for any runtime errors or unexpected behavior

## 📋 Pull Request Guidelines

When submitting a pull request:

1. **Clear title**: Use descriptive titles like:
   - `Add feature: X`
   - `Fix bug: Y`
   - `Improve: Z`

2. **Clear description**: Include:
   - What changes were made
   - Why these changes are necessary
   - Any related issues (use `#issueNumber`)

3. **Keep it focused**: PR should address one main issue/feature

4. **Well-tested**: Ensure all changes are tested

5. **Updated documentation**: Update README or comments if needed

## ✅ Review Process

After you submit a pull request:

1. Maintainers will review your changes
2. You may be asked to make adjustments
3. Once approved, your PR will be merged
4. Your contribution will be credited! 🌟

## 🎯 Project Goals

Our project aims to:

- ✨ Provide an educational Python learning tool
- 📚 Demonstrate fundamental programming concepts
- 🤝 Foster a welcoming community
- 🚀 Continuously improve and expand

## 💬 Questions?

- Open an issue with the `[QUESTION]` tag
- Check existing issues for answers
- Refer to the README documentation

## 📜 Code of Conduct

We are committed to providing a welcoming and inclusive environment:

- Be respectful and constructive
- Avoid harassment or discriminatory language
- Focus on the code, not the person
- Help others learn and grow

## 🙏 Thank You

Thank you for contributing to the General Knowledge Quiz project! Your efforts help make this project better for everyone. Happy coding! 🎓
