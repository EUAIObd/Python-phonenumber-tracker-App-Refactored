Final Project: Enhancing Python Applications with Defensive Programming

				
1.	Project Overview
o	Description of the original project
-	The original project is a Phone Number Tracker application built using Python and Tkinter for the GUI. It allows users to input a phone number and retrieve the corresponding country information.

o	Rationale for choosing this project
-	This project was chosen to demonstrate the integration of GUI elements with backend logic for real-time data processing and display. It also showcases the use of external libraries for country information retrieval based on phone numbers.

o	Summary of improvements and enhancements
-	Improved input validation and error handling.
-	Enhanced user interface with better layout and design.
-	Added functionality to clear input fields.
-	Provided detailed error messages for better user experience.

2.	Installation and Setup Guide
o	Steps to set up the development environment
-	Clone the repository.
-	Navigate to the project directory.
-	Install the required dependencies using pip install -r requirements.txt.

o	Dependencies and requirements
-	 Python 3.x 
-	 Tkinter library 
-	 pycountry library 
-	phone_iso3166 library

3.	User Manual
o	Instructions on how to use the application
-	Save the code as a Python file (app.py).
-	Run the application.
-	Enter a phone number in the entry field.
-	Click the "Track Country" button.
-	The application will display the country associated with the phone number (or "Country is Unknown" if the country cannot be determined).

o	Description of new features and functionalities
-	Clear button to reset input fields.
-	Enhance error handling for invalid inputs and exceptions.

4.	Technical Documentation
o	Architectural changes (if any)
-	The overall architecture of the application changed the font size, color of a simple GUI application with a main window, entry field, button, and label.

o	Description of new classes, methods, and functions
-	No new classes were added. The existing methods track_location and clear_fields were enhanced for better functionality.

o	Explanation of defensive programming techniques implemented
-	Input validation to ensure the phone number is a valid digit.
-	Exception handling to manage errors during country information retrieval.


5.	Code Review and Refactoring
o	Discussion of major code changes
-	Improved input validation in the track_location method.
-	Enhanced error messages for better user feedback.
-	Added a clear button functionality to reset input fields.

o	Justification for refactoring decisions
-	Refactoring was done to improve code readability, maintainability, and user experience.

6.	Testing Documentation
o	Overview of testing strategy
-	Manual testing was performed to ensure the application works as expected.

o	Description of test cases and their results
-	Valid phone number input: Successfully retrieved country information.
-	Invalid phone number input: Displayed appropriate error message.
-	Clear button functionality: Successfully reset input fields.

7.	Challenges and Solutions
o	Discussion of difficulties encountered during the project
-	Handling invalid phone number inputs.
-	Managing exceptions during country information retrieval.

o	How these challenges were addressed
-	Implemented input validation to ensure only valid digits are accepted.
-	Added exception handling to manage errors gracefully.

8.	Future Improvements
o	Suggestions for further enhancements or features
-	Add support for international phone number formats.
-	Implement a more robust testing framework.
-	Enhance the user interface with additional styling and features.

9.	References and Resources
o	List of resources used during the project
-	https://github.com/miafrancembsa/Python-phonenumber-tracker-App
-	https://github.com/Kalebu/Python-phonenumber-tracker-App.git




Students submitted:

AQUILINO, Eugene P.
SAN ANDRES, Mary France B. 	
						
BSCS3A
