# Final Project: Enhancing Python Applications with Defensive Programming

**BSCS 3A**

**Submitted by:**

- Eugene P. Aquilino
- Mary France B. San Andres

---

## 1. Project Overview

This project demonstrates how to enhance a basic Python application, specifically a Phone Number Tracker, with robust defensive programming techniques.

### 1.1 Original Project Description

The original project was a Phone Number Tracker application built using Python and Tkinter for the Graphical User Interface (GUI). Its core function was to accept a phone number as input and then determine the associated country.

### 1.2 Rationale for Project Choice

We selected this project to illustrate the practical application of:

*   **GUI Integration:** Combining front-end user interaction with backend logic.
*   **Data Processing:** Handling user input and processing it in real-time.
*   **External Libraries:** Utilizing external resources (like `pycountry` and `phone_iso3166`) for enhanced functionality.

### 1.3 Summary of Improvements and Enhancements

Our enhancements focused on improving the application's reliability, user-friendliness, and code quality:

*   **Robust Input Validation:** Implemented stricter checks to ensure valid phone number formats.
*   **Comprehensive Error Handling:** Added `try-except` blocks to gracefully handle potential errors and provide informative feedback to the user.
*   **Enhanced User Interface:** Refined the GUI layout and added a "Clear" button for better usability.
*   **Detailed Error Messages:** Improved the clarity of error messages to help users understand and resolve issues.

---

## 2. Installation and Setup Guide

Follow these steps to set up the development environment and run the enhanced application.

### 2.1 Setting Up the Development Environment

1.  **Clone the Repository:**
    ```bash
    git clone [repository_url] 
    ```
    (Replace `[repository_url]` with the actual URL of your project repository).

2.  **Navigate to the Project Directory:**
    ```bash
    cd [project_directory_name]
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### 2.2 Dependencies and Requirements

*   **Python 3.x**
*   **Tkinter:** (Usually comes bundled with Python)
*   **pycountry:** `pip install pycountry`
*   **phone_iso3166:** `pip install phone-iso3166`

---

## 3. User Manual

Learn how to use the enhanced Phone Number Tracker application.

### 3.1 How to Use the Application

1.  **Save the Code:** Save the Python code as a file named `app.py` (or any `.py` file).
2.  **Run the Application:** Execute the script from your terminal:
    ```bash
    python app.py
    ```
3.  **Enter a Phone Number:** Input a phone number into the entry field.
4.  **Track the Country:** Click the "Track Country" button.
5.  **View Results:** The application will display the country associated with the phone number. If the country cannot be determined, it will display "Country is Unknown."

### 3.2 New Features and Functionalities

*   **Clear Button:** A new "Clear" button resets the input field, making it easier to enter new numbers.
*   **Enhanced Error Handling:** The application is more resilient to invalid inputs and provides more informative error messages.

---

## 4. Technical Documentation

This section provides in-depth information about the technical aspects of the project.

### 4.1 Architectural Changes
-The overall architecture of the application changed the font size, color of a simple GUI application with a main window, entry field, button, and label.

### 4.2 New Classes, Methods, and Functions

*   **No New Classes:** The project's structure remains similar to the original.
*   **Enhanced Methods:** The `track_location` and `clear_fields` methods were improved for better functionality and error handling.

### 4.3 Defensive Programming Techniques Implemented

*   **Input Validation:** We implemented strict checks to ensure the entered phone number consists of valid digits only.
*   **Exception Handling:** `try-except` blocks are used to catch potential errors during country information retrieval, preventing crashes and providing user-friendly error messages.

---

## 5. Code Review and Refactoring

This section details the code improvements made during the project.

### 5.1 Major Code Changes

*   **Improved Input Validation:** The `track_location` method now includes more robust validation of the phone number input.
*   **Enhanced Error Messages:** Error messages are more descriptive and user-friendly.
*   **Clear Button Functionality:** Added the functionality for the "Clear" button to reset the input field.

### 5.2 Justification for Refactoring Decisions

Refactoring was essential to:

*   **Improve Code Readability:** Make the code easier to understand and maintain.
*   **Enhance Maintainability:** Simplify future modifications and debugging.
*   **Improve User Experience:** Provide a smoother and more intuitive interaction for the user.

---

## 6. Testing Documentation

This section outlines the testing strategy and results.

### 6.1 Overview of Testing Strategy

We employed manual testing to verify the application's functionality and the effectiveness of the enhancements.

### 6.2 Test Cases and Results

| Test Case                   | Input             | Expected Result                          | Actual Result         | Status |
| :-------------------------- | :---------------- | :--------------------------------------- | :-------------------- | :----- |
| Valid Phone Number          | +15551234567      | Country: United States                   | Country: United States | Pass   |
| Invalid Phone Number        | abc               | Error: Invalid phone number format      | Error: Invalid phone number format | Pass   |
| Clear Button                | (Any input)      | Input field is cleared                 | Input field is cleared | Pass   |
| Country not found          | +9999999999       | Country is Unknown                       | Country is Unknown    | Pass   |

---

## 7. Challenges and Solutions

Here, we discuss the challenges faced and how we overcame them.

### 7.1 Difficulties Encountered

*   **Handling Invalid Phone Number Inputs:** Ensuring the application gracefully handles various invalid input formats.
*   **Managing Exceptions:** Dealing with potential errors during country information retrieval from external libraries.

### 7.2 How Challenges Were Addressed

*   **Input Validation:** Implemented rigorous input validation using conditional statements to check for valid digits before processing.
*   **Exception Handling:** Added `try-except` blocks to catch exceptions, preventing the application from crashing and providing informative error messages to the user.

---

## 8. Future Improvements

We propose the following enhancements for future development:

*   **Support for International Formats:** Extend the application to handle a wider range of international phone number formats.
*   **Robust Testing Framework:** Implement automated unit and integration tests using a framework like `unittest` or `pytest`.
*   **GUI Enhancements:** Improve the user interface with:
    *   More advanced styling (e.g., using themed Tkinter widgets).
    *   Additional features (e.g., displaying the country flag, a map).

---

## 9. References and Resources

*   Original Project: 
*   Alternative Project: [https://github.com/Kalebu/Python-phonenumber-tracker-App.git](https://github.com/Kalebu/Python-phonenumber-tracker-App.git)

---
