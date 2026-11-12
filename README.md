# 🔐 Password Strength Checker (Headless Auth)

<p align="center">
  <b>Check Passwords. Improve Security. Build Safer Habits.</b>
  <br>
  A beginner-friendly Python project that evaluates password strength using regular expressions and basic security validation techniques.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Language-Python%203-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Concept-Regular%20Expressions-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Domain-Cybersecurity-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Project-Console%20Based-green?style=for-the-badge" />
</p>

---

## 📌 About the Project

**Password Strength Checker** is a Python-based application that evaluates the strength of a password using regular expressions and common password security practices.

The program analyzes different password characteristics, including length, uppercase and lowercase letters, numeric digits, and special characters.

Based on these checks, it classifies the password as **Weak, Medium, or Strong** and provides suggestions to help users improve password security.

This project demonstrates how Python regular expressions can be used for input validation and introduces fundamental concepts of cybersecurity and authentication systems.

---

## ✨ Features

- 🔐 Evaluates password strength based on predefined security conditions.
- 📏 Validates minimum password length.
- 🔠 Detects uppercase and lowercase characters.
- 🔢 Checks for numeric digits.
- 🔣 Identifies special characters.
- 📊 Classifies passwords as Weak, Medium, or Strong.
- 💡 Provides suggestions to improve password strength.
- ⚡ Uses Python's built-in regular expression module.
- 🖥️ Simple and beginner-friendly console interface.

---

## ⚙️ How It Works

1. **Password Input:** The user enters a password through the console.
2. **Length Validation:** The program checks whether the password satisfies the minimum length requirement.
3. **Character Validation:** Regular expressions identify uppercase letters, lowercase letters, numbers, and special characters.
4. **Strength Evaluation:** The program evaluates the results of the validation checks.
5. **Password Classification:** The password is categorized as Weak, Medium, or Strong based on the implemented conditions.
6. **Suggestions:** If the password is weak, the program displays suggestions for improvement.

---

## 🔍 Password Validation Criteria

| Validation | Description |
|---|---|
| Minimum Length | Checks whether the password meets the required length |
| Uppercase Letters | Detects characters from A to Z |
| Lowercase Letters | Detects characters from a to z |
| Numeric Digits | Checks for numbers from 0 to 9 |
| Special Characters | Identifies symbols such as @, #, $, and ! |

---

## 🔄 System Workflow

```text
          START
            |
            v
       Enter Password
            |
            v
      Check Password Length
            |
            v
     Analyze Character Patterns
            |
      +-----+-----+
      |           |
      v           v
 Uppercase     Lowercase
      |           |
      +-----+-----+
            |
            v
       Check Digits
            |
            v
   Check Special Characters
            |
            v
     Evaluate Conditions
            |
            v
    Classify Password
            |
      +-----+------+
      |      |     |
      v      v     v
    Weak   Medium Strong
      |      |     |
      v      v     v
  Display Suggestions
            |
            v
           END
```

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Core programming language |
| `re` | Regular expression-based pattern matching |
| Console | User input and output |

---

## 🧩 Python Concepts Used

- **Regular Expressions:** Used to identify specific character patterns in passwords.
- **Conditional Statements:** Used to evaluate password validation results.
- **String Handling:** Used to process and analyze password input.
- **Input/Output Operations:** Used to interact with the user.
- **Logical Operators:** Used to combine multiple validation conditions.

---

## 📂 Project Structure

```text
HeadlessAuth/
│
├── Password.py
│
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Any Python IDE or code editor (VS Code, PyCharm, etc.).

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/srxxr4man/HeadlessAuth.git
```

**2. Navigate to the project directory**

```bash
cd HeadlessAuth
```

**3. Run the Python program**

```bash
python Password.py
```

No external Python packages are required because the `re` module is included in the Python standard library.

---

## 🖥️ Sample Execution

**Input:**

```text
Enter Password: Hello123
```

**Output:**

```text
Password Strength: Weak

Suggestions:
- Add special characters.
- Increase password length.
```

*The sample output is illustrative; actual results depend on the validation conditions implemented in the program.*

---

## 🎯 Learning Outcomes

Through this project, I explored:

- Using Python regular expressions for pattern matching.
- Implementing password validation techniques.
- Understanding uppercase, lowercase, numeric, and special character checks.
- Applying conditional statements and logical operators.
- Understanding basic password security practices.
- Developing a simple console-based Python application.

---

## 🔮 Future Improvements

- 🔒 Add more advanced password validation rules.
- 📊 Introduce a numerical password strength score.
- 🚫 Detect commonly used and compromised passwords using an appropriate secure checking service.
- 🎨 Develop a graphical user interface.
- 🔑 Integrate password generation functionality.
- 🌐 Extend the project into a basic authentication application.

---

## ⚠️ Security Note

This project is an educational password-strength checker, not a complete authentication or password security system.

A password's strength cannot be determined reliably from character variety and length alone. Real authentication systems should also use secure password hashing, rate limiting, and other appropriate security controls.

---

## 👨‍💻 Author

**A Sreeram**

Artificial Intelligence and Data Science Student  
Muthoot Institute of Technology and Science (MITS)

Interested in Python, Cybersecurity, Software Development, and Artificial Intelligence.

---

<p align="center">
  ⭐ If you find this project useful, consider giving this repository a star!
  <br><br>
  <b>🔐 Small Projects. Stronger Security. Smarter Coding.</b>
</p>
