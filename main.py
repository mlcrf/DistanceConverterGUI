import tkinter as tk
from tkinter import StringVar, OptionMenu

# Start window
main = tk.Tk()
main.title("Distance Converter")

# Welcome Label
welcomeText = tk.Label(main, text="Welcome to the distance converter GUI", font="Helvetica")
welcomeText.grid(row=0, columnspan=2, padx=10, pady=10)

# Dropdown menu Options
options = ['Milimetres', 'Centimetres', 'Metres', 'Kilometres', 'Inches', 'Feet', 'Yards', 'Miles']

# ------------------------------------1st Dropdown------------------------------------------------------

# Convert From (Text)
convertFromText = tk.Label(main, text="Convert from:")
convertFromText.grid(row=1, column=0, padx=10, pady=10)

# Entry input
entryInput = tk.Entry(main)
entryInput.grid(row=1, column=2, padx=10, pady=10)

# Selected Option (1st menu)
selected_option_input = StringVar(main)  # variable to be set at
selected_option_input.set(options[1])  # Default selection

# Dropdown Menu (1st menu)
dropdownInput = OptionMenu(main, selected_option_input, *options)  # Create dropdown
dropdownInput.grid(row=1, column=1, padx=10, pady=10)

# ------------------------------------2nd Dropdown------------------------------------------------------

# Convert To - Text
convertToText = tk.Label(main, text="Convert to:")
convertToText.grid(row=2, column=0, padx=10, pady=10)

# Selected Option (2nd menu)
selected_option_output = StringVar(main)  # variable to be set at
selected_option_output.set(options[4])  # Default selection

# Dropdown Menu (2nd menu)
dropdownOutput = OptionMenu(main, selected_option_output, *options)  # Create dropdown
dropdownOutput.grid(row=2, column=1, padx=10, pady=10)

# ------------------------------------Converter------------------------------------------------------

# Function to handle conversions and print result
def converter():
    conversions = {'Milimetres': 1000, 'Centimetres': 100, 'Metres': 1, 'Kilometres': 0.001, 'Inches': 39.3701,
                   'Feet': 3.28084, 'Yards': 1.09361, 'Miles': 0.000621371}
    conversionInput = float(entryInput.get()) / conversions[selected_option_input.get()]
    final_result = conversionInput * conversions[selected_option_output.get()]

    global labelConversion  # Declare labelConversion as global
    
    labelConversion = tk.Label(main, text=final_result)
    labelConversion.grid(row=2, column=2, padx=10, pady=10)

    # Clear the text of labelConversion before updating it (DOESNT WORK WTF)
    labelConversion.config(text="")

    # Update the text of labelConversion with the new result
    labelConversion.config(text=final_result)
    

button = tk.Button(main, text="Convert", command=converter)
button.grid(row=4, columnspan=3, padx=10, pady=10)

# Run Window
main.mainloop()
