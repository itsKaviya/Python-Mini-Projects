# 🧮 Python Calculator

This is a simple interactive **command-line calculator** written in Python. It supports basic arithmetic operations: addition, subtraction, multiplication, and division. Users can chain calculations together or start over at any point.

---

## ✅ Features

* Perform **addition, subtraction, multiplication, and division**
* **Looping interface**: continue calculations with the result or start fresh
* Dynamic operation selection using Python functions
* ASCII logo support (optional)

---

## 🧠 How It Works

* The program defines functions for each arithmetic operation.
* These functions are mapped to symbols in a dictionary (`operations`).
* Users pick an operation and enter numbers to perform calculations.
* A loop lets users continue with the result or restart a new calculation.

## 📌 Notes

* Input is converted to `float` to support decimal operations.
* The calculator supports only basic operations. For scientific functions, you can extend the `operations` dictionary.
* Be cautious of division by zero – this is not currently handled with error catching.