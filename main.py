import tkinter as tk
from tkinter import messagebox
import subprocess
import autopep8
import os
import pyflakes.api
import pyflakes.reporter
import tempfile
import shutil


def beautify_python(code):
    return autopep8.fix_code(code)


# Function to check for errors in Python code using pyflakes
def check_python_errors(code):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".py", mode="w") as temp_file:
        temp_file.write(code)
        temp_file_path = temp_file.name

    reporter = pyflakes.reporter.Reporter(open(os.devnull, 'w'), open(os.devnull, 'w'))
    errors = subprocess.run(["python", "-m", "pyflakes", temp_file_path], capture_output=True, text=True)

    os.remove(temp_file_path)

    if errors.stdout:
        # Displaying errors in a more readable format (e.g., line numbers)
        return f"Errors found:\n{errors.stdout}"
    else:
        return "No errors found."


# Function to check for errors in C/C++ using clang
def check_c_cpp_errors(code):
    temp_file = "temp.cpp"
    with open(temp_file, "w") as file:
        file.write(code)

    try:
        process = subprocess.run(['clang', '-fsyntax-only', temp_file], capture_output=True, text=True)
        errors = process.stderr if process.stderr else "No errors found."
    except FileNotFoundError:
        errors = "Error: Clang compiler not found. Please install Clang to use this feature."

    os.remove(temp_file)
    return errors


# Function to check for errors in Java using javac
def check_java_errors(code):
    temp_file = "TempProgram.java"
    with open(temp_file, "w") as file:
        file.write(code)

    try:
        process = subprocess.run(['javac', temp_file], capture_output=True, text=True)
        errors = process.stderr if process.stderr else "No errors found."
    except FileNotFoundError:
        errors = "Error: Java compiler (javac) not found. Ensure JDK is installed and added to PATH."

    os.remove(temp_file)
    return errors


# Function to beautify Java code using google-java-format
def beautify_java(code):
    temp_file = "temp.java"
    with open(temp_file, "w") as file:
        file.write(code)

    try:
        subprocess.run(['google-java-format', '-i', temp_file], check=True)
        with open(temp_file, "r") as file:
            beautified_code = file.read()
    except FileNotFoundError:
        beautified_code = "Error: google-java-format not found. Please install it before using beautification."
    except subprocess.CalledProcessError as e:
        beautified_code = f"Error during beautification: {e}"

    os.remove(temp_file)
    return beautified_code



def handle_debugging():
    code = code_text.get("1.0", tk.END).strip()
    language = language_var.get()

    if not code:
        messagebox.showerror("Error", "Code cannot be empty.")
        return

    if language == "Python":
        errors = check_python_errors(code)
        beautified_code = beautify_python(code)
    elif language == "C/C++":
        errors = check_c_cpp_errors(code)
        beautified_code = code
    elif language == "Java":
        errors = check_java_errors(code)
        beautified_code = beautify_java(code)
    else:
        messagebox.showerror("Error", "Please select a valid language.")
        return

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, f"Errors:\n{errors}\n\nBeautified Code:\n{beautified_code}")


root = tk.Tk()
root.title("Code Debugger and Beautifier")
root.geometry("700x600")
root.config(bg="#F0F0F0")

title_label = tk.Label(root, text="AI Code Debugger & Beautifier", font=("Arial", 18, "bold"), bg="#F0F0F0",
                       fg="#4B0082")
title_label.pack(pady=10)

language_frame = tk.Frame(root, bg="#F0F0F0")
language_frame.pack(pady=10)

language_label = tk.Label(language_frame, text="Select Language:", font=("Arial", 12), bg="#F0F0F0")
language_label.grid(row=0, column=0, padx=10)

language_var = tk.StringVar(value="Python")
language_menu = tk.OptionMenu(language_frame, language_var, "Python", "C/C++", "Java")
language_menu.grid(row=0, column=1)

code_label = tk.Label(root, text="Enter Your Code:", font=("Arial", 12), bg="#F0F0F0")
code_label.pack(pady=5)

code_text = tk.Text(root, height=12, width=70, font=("Courier", 10), bg="#FFFFFF", fg="#000000", wrap="word")
code_text.pack(pady=10)

debug_button = tk.Button(root, text="Debug & Beautify", font=("Arial", 12), bg="#4B0082", fg="#FFFFFF",
                         command=handle_debugging)
debug_button.pack(pady=10)

output_label = tk.Label(root, text="Output:", font=("Arial", 12), bg="#F0F0F0")
output_label.pack(pady=5)

output_text = tk.Text(root, height=12, width=70, font=("Courier", 10), bg="#F0F0F0", fg="#000000", wrap="word")
output_text.pack(pady=10)

root.mainloop()
