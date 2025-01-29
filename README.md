# AI Code Debugger & Beautifier

## Overview

AI Code Debugger & Beautifier is a graphical user interface (GUI) application developed using **Tkinter** that allows users to debug and beautify code in multiple programming languages: **Python**, **C/C++**, and **Java**. It provides users with:

- Code error detection
- Beautification of code (formatting) using tools like **autopep8** (for Python) and **google-java-format** (for Java)

This project is useful for developers who want to quickly check and beautify their code without using command-line interfaces or switching between different tools.

## Features

- **Code Debugging**: The app checks for errors in Python, C/C++, and Java code using appropriate tools and compilers.
- **Code Beautification**: The app beautifies Python code using `autopep8` and Java code using `google-java-format`.
- **GUI Interface**: Built with **Tkinter**, providing an intuitive interface for users.
- **Error Reporting**: Displays detailed error messages with line numbers and descriptions.
  
## Requirements

- Python 3.x
- Required Python libraries:
  - **Tkinter**: For GUI creation.
  - **autopep8**: For Python code beautification.
  - **pyflakes**: For Python code error checking.
  - **subprocess**: For calling external programs (like `clang`, `javac`, and `google-java-format`).
  - **shutil** and **tempfile**: For file operations.

For Java:
- **Java Development Kit (JDK)** with the `javac` compiler installed.
- **Clang** (for C/C++) should be installed.

To install the required Python libraries, run:

```
pip install requirements.txt

```

Run the Application:

```
python main.py

```

How to Use
Select the Programming Language: Choose from Python, C/C++, or Java.
Enter Your Code: Paste or write your code in the provided text box.
Click the "Debug & Beautify" Button: This will:
Check for errors in the code and display them.
Beautify the code according to the selected language (for Python and Java).
View Output: The results will be displayed in the output section, including any errors found and the beautified code.

Example:

For Python:

Select Python from the language dropdown.
Paste Python code with formatting issues or errors in the text box.
Click Debug & Beautify. Errors will be shown, and the code will be beautified using autopep8.

For Java:

Select Java from the language dropdown.
Paste Java code in the text box.
Click Debug & Beautify. The code will be formatted using google-java-format, and any errors will be shown.
