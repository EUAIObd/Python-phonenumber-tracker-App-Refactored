import json  # Importing necessary libraries
import pycountry  # Importing pycountry for country information
from tkinter import Tk, Label, Button, Entry, messagebox  # Importing tkinter for GUI
from phone_iso3166.country import phone_country  # Importing phone_country for phone number to country mapping

class Location_Tracker:
    def __init__(self, App):
        self.window = App  # Initializing the main window
        self.window.title("Phone Number Tracker")  # Setting window title
        self.window.geometry("550x400")  # Setting window size
        self.window.configure(bg="#2c3e50")  # Setting window background color
        self.window.resizable(False, False)  # Disabling window resizing

        # Application menu
        Label(App, text="Enter a phone number:", fg="white", font=("Helvetica", 15, "bold"), bg="#2c3e50", justify="right").place(x=150, y=50)  # Creating label
        self.phone_number = Entry(App, width=20, font=("Arial", 15), relief="flat", justify="center")  # Creating entry for phone number
        self.track_button = Button(App, text="Track Country", bg="#e74c3c", fg="white", font=("Helvetica", 13, "bold"), relief="raised", command=self.track_location)  # Creating button to track location
        self.clear_button = Button(App, text="Clear", bg="#3498db", fg="white", font=("Helvetica", 13, "bold"), relief="raised", command=self.clear_fields)  # Creating button to clear fields
        self.country_label = Label(App, fg="white", font=("Helvetica", 20, "bold"), bg="#2c3e50", justify="center")   # Creating label to display country

        # Place widgets on the window
        self.phone_number.place(x=150, y=120)  # Placing phone number entry
        self.track_button.place(x=180, y=200)  # Placing track button
        self.clear_button.place(x=320, y=200)  # Placing clear button
        self.country_label.place(x=100, y=280)  # Placing country label

    def track_location(self):
        phone_number = self.phone_number.get().strip()  # Getting and stripping phone number input
        
        # Input validation and sanitization
        if not phone_number.isdigit():  # Checking if input is a valid digit
            messagebox.showerror("Invalid Input", "Please enter a valid phone number.")  # Showing error message
            return  # Exiting function

        country = "Country is Unknown"  # Default country value
        try:
            # Error handling and exception management
            tracked = pycountry.countries.get(alpha_2=phone_country(phone_number))  # Getting country information
            if tracked:  # Checking if country information is found
                country = tracked.official_name if hasattr(tracked, "official_name") else tracked.name  # Setting country name
        except Exception as e:  # Catching exceptions
            messagebox.showerror("Error", f"An error occurred: {e}")  # Showing error message
            return  # Exiting function

        # Output encoding and sanitization
        self.country_label.configure(text=country)  # Updating country label

    def clear_fields(self):
        self.phone_number.delete(0, 'end')  # Clearing phone number entry
        self.country_label.configure(text="")  # Clearing country label

if __name__ == "__main__":
    try:
        PhoneTracker = Tk()  # Creating main Tkinter window
        MyApp = Location_Tracker(PhoneTracker)  # Initializing Location_Tracker
        PhoneTracker.mainloop()  # Running the main loop
    except Exception as e:  # Catching exceptions
        # Logging and monitoring
        print(f"An error occurred: {e}")  # Printing error message
        messagebox.showerror("Error", f"An error occurred: {e}")  # Showing error message
