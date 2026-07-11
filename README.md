# Java Comment Generator

## Overview

The Java Comment Generator is a Python-based academic project developed to automatically generate meaningful comments for Java source code. The project uses a Large Language Model (LLM) accessed through the Groq API and provides a simple web interface using Streamlit.

This project focuses on **AI-assisted software documentation** and is intended for learning and academic purposes.

---

## Problem Definition

In many software projects, source code lacks proper comments due to time constraints or oversight. Poorly documented code is difficult to understand, maintain, and extend. Writing comments manually is repetitive and time-consuming.

This project addresses the problem by using an AI model to automatically generate descriptive comments for Java programs.

---

## Project Objectives

* To design a tool that automatically generates comments for Java code
* To reduce manual effort in software documentation
* To improve code readability and maintainability
* To demonstrate the application of Large Language Models in software engineering

---

## Scope of the Project

* Accepts Java source code as input
* Generates meaningful comments for classes, methods, and logic blocks
* Displays the commented code through a web interface

This project does not aim to modify or optimize the original Java logic.

---

## Technologies Used

* **Programming Language:** Python 3
* **Web Framework:** Streamlit
* **AI Model:** LLaMA (via Groq API)
* **Environment Management:** python-dotenv
* **Operating System:** Windows

---

## Project Structure

```
java-comment-generator/
│
├── app.py
├── core/
│   └── comment_generator.py
├── .env
├── requirements.txt
└── README.md
```

---

## Development Methodology

1. Requirement analysis was carried out to identify the need for automated code documentation.
2. Python and Streamlit were selected for rapid development and ease of use.
3. The project was modularized into frontend (UI) and backend (comment generation logic).
4. The Groq API was integrated to access a Large Language Model for comment generation.
5. The application was tested with multiple Java source files to validate output accuracy.

---

## Installation and Execution

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Configure API Key

Create a `.env` file in the project root directory and add:

```
GROQ_API_KEY=your_api_key_here
```

### Step 3: Run the Application

```bash
streamlit run app.py
```

---

## Output

The system produces Java source code with clear and meaningful comments while preserving the original program structure and logic.

---

## Limitations

* Accuracy depends on the AI model response
* Requires active internet connection
* Performance may vary for large source files

---

## Future Enhancements

* Support for additional programming languages
* Offline model integration
* Export commented code as downloadable files
* Integration with IDEs

---

## Conclusion

This project demonstrates how AI-based language models can be effectively used to automate software documentation. The Java Comment Generator reduces manual effort and improves code understanding, making it useful for students and developers.

---

## requirements.txt

```
streamlit
python-dotenv
groq
```
