#! /usr/bin/python3

"""
Cipher App

This Python script implements a simple graphical user interface (GUI) application
for performing various cipher operations. Users can enter a message and select a cipher
from available options. The application validates the input message to ensure it
contains only allowed characters and then performs the chosen cipher operation,
displaying the ciphered message in the output field.

Supported Ciphers:
  - Caesar Cipher: Shifts letters by a specified number of positions.
  - Atbash Cipher: Swaps each letter with its opposite in the alphabet (e.g., 'a' becomes 'z').
  - Caesar Square Cipher: Encrypts text by combining letter shifts with a grid-based transposition.
  - Vigenère Cipher: Uses a keyword to perform a more complex letter shifting.
  - Morse Code: Converts the message to Morse code representation.

The application uses the tkinter library for creating the GUI elements.
"""

__version__ = "0.1"
__author__ = "Eashan Polwatta Gallage"
__email__ = "eashanpol@gmail.com"

import re   
from CipherInfo import * # Import cipher information, methods
from OtherGUIs import * # Import additional GUI elements

class CipherButton:
    """
    Represents a button on the UI for selecting a cipher.

    This class creates a button with the cipher's name, binds a click event handler, and
    associates a tooltip with the button for displaying additional information.

    **Expected Cipher Object:**

    The `cipher` object passed to the constructor should have the following attributes:

    * `name` (str): The name of the cipher to be displayed on the button.
    * `name_ext` (str, optional): An extended name for the tooltip (can be the same as `name`).
    * `description` (str): A description of the cipher for the tooltip.
    * `func_name` (str): The name of the method within the `CipherButton` class that implements the cipher logic.
    """

    def __init__(self, parent : tk.Widget, cipher):
        """
        Initializes a CipherButton instance.

        Args:
            parent (tk.Widget): The parent widget where the button will be placed.
            cipher (Cipher): The cipher object associated with the button.
        """

        self.button : tk.Button = tk.Button(
            parent,
            text=cipher.name,
            width=10,
            relief="raised",  # Raised appearance for a more prominent button
            state="disabled",
            borderwidth=2,
            highlightthickness=2,
            fg="black",
            bg="lightgrey",  # Match typical "active" button color
            disabledforeground="black",  # Ensures text is readable even when disabled
        )
        self.button.pack()

        self.button.bind(
            "<Button-1>",
            lambda event: self.handle_button(cipher.func_name),  # Using func_name captured by lambda
        )
      
        self.tooltip : Tooltip = Tooltip(self.button, cipher.name_ext, cipher.description)
    
    def handle_button(self, func_name : str):
        """
        Handles button click events.

        Args:
            func_name (str): The name of the function to be called.
        """

        # Get the input message, converting it to uppercase
        self.msg : str = app.InputMessageBox.get("1.0", "end-1c").upper()

        # Validate the input message
        if not CheckMessage(self.msg):
            return

        # Dynamically call the appropriate cipher function
        method_name : str = func_name
        method = getattr(self, method_name, self.Default_Action)
        method()

    def Caesar_Cipher_Func(self):
        """
        Performs the Caesar cipher operation.
        """
        shift_by : StartCaesarGUI = StartCaesarGUI(app.window)
        app.l.config(text=f"Caesar Cipher! Shifted by {shift_by}")
        ciphered_text = Txt2Caeser(self.msg, shift_by)
        app.Output.delete("1.0", "end")
        app.Output.insert("end", ciphered_text)
        app.Output.config(fg="black")

    def Atbash_Cipher_Func(self):
        """
        Performs the Atbash cipher operation.
        """
        ciphered_text = Txt2Atbash(self.msg)
        app.l.config(text=f"Atbash Cipher!")
        app.Output.delete("1.0", "end")
        app.Output.insert("end", ciphered_text)
        app.Output.config(fg="black")

    def Caesar_Square_Func(self):
        """
        Performs the Caesar Square cipher operation.
        """
        ciphered_text = Txt2CaesarSquare(self.msg)
        app.l.config(text=f"Caesar Square Cipher!")
        app.Output.delete("1.0", "end")
        app.Output.insert("end", ciphered_text)
        app.Output.config(fg="black")

    def Vigenere_Cipher_Func(self):
        """
        Performs the Vigenère cipher operation.
        """
        input_key = StartVigenereGUI(app.window)
        ciphered_text = Txt2Vigenere(self.msg, input_key)
        app.l.config(text=f"Vigenère Code! Key is {input_key}")
        app.Output.delete("1.0", "end")
        app.Output.insert("end", ciphered_text)
        app.Output.config(fg="black")

    def Morse_Code_Func(self):
        """
        Performs the Morse code encoding operation.
        """
        ciphered_text = Txt2MorseCode(self.msg)
        app.l.config(text=f"Morse Code!")
        app.Output.delete("1.0", "end")
        app.Output.insert("end", ciphered_text)
        app.Output.config(fg="black")

    def Default_Action(self):
        """
        Default action to be performed if the specified method is not found.
        """
        print("Default action: No specific method defined")

    def get_button(self):
        """Return the button widget."""
        return self.button

def CheckMessage(InputMessage : str) -> bool:
    """
    Validates the input message to ensure it follows the required convention.

    Args:
        InputMessage (str): The input message to be validated.

    Returns:
        str: The validated input message if it's valid, otherwise 0.
    """

    def IsEnglishAlphabetSentence( text : str ) -> bool:
        """
        Checks if a given string is an English alphabet sentence.

        Args:
            text: The input string to be checked.

        Returns:
            True if the string consists only of English alphabet characters and other character of morse code,
            False otherwise.
        """
        return bool(re.match(r'^[A-Z0-9 .,?!/\-()"@=:;+_$&]+$', text))
    
    def PrintError() -> None:
        """
        Clears the output field and inserts an error message indicating
        that the input should only contain characters from the specified set.

        Args:
            None

        Returns:
            None
        """

        app.Output.delete("1.0", "end")  # Clear the entire text widget
        app.Output.insert("end", "Error: Input characters 'a-z','A-Z', ' ', '.', ',', '?', '!', '/', '-', '(', ')', '\"', '@', '=', ':', ';', '+', '_', '$', '&'")  # Insert the error 
        app.Output.config(fg="red")

    ValidMessage : bool = IsEnglishAlphabetSentence(InputMessage)

    if not ValidMessage:
        PrintError()  # Print an error message if the input is invalid
        return 0  # Indicate an invalid input

    return ValidMessage  # Return the valid input message

class CipherAppGUI:
    """
    Main application class for the Cipher App.

    This class handles creating the application window, widgets, and binding events.
    """

    def __init__(self):
        """
        Initializes the application window and its properties.
        """
        self.window: tk.Tk = tk.Tk()
        self.window.title("Cipher App 0.1")
        self.window.geometry("400x350")  # Set window size

        self.create_widgets()
        self.bind_events()

    def create_widgets(self):
        """
        Creates the main UI elements of the application.

        This method creates the main frame, input text box, labels, output text box,
        button frame, buttons for each cipher, and associates them with member variables.
        """

        # Create main frame and input text widget
        self.main_frame: tk.Frame = tk.Frame(self.window)
        self.main_frame.pack(fill="both", expand=True)
        self.main_frame.grid(padx=10, pady=10)

        self.InputMessageBox: tk.Text = tk.Text(self.main_frame, height=8, width=25, bg="#FFC0CB")
        self.InputMessageBox.grid(row=0, column=0)
        self.InputMessageBox.insert("1.0", "Enter message to cipher")

        # Create labels and output text widget
        self.l: tk.Label = tk.Label(self.main_frame, text="Select method of ciphering")
        self.l.grid(row=1, column=0, sticky="w", pady=10)

        self.Output: tk.Text = tk.Text(self.main_frame, height=8, width=25, bg="light green")
        self.Output.grid(row=2, column=0)
        self.Output.insert("1.0", "Ciphered message will appear here")

        # Create button frame and label
        self.button_frame: tk.Frame = tk.Frame(self.main_frame)
        self.button_frame.grid(row=0, column=1, rowspan=3, sticky="n", padx=40, pady=5)

        self.label_buttons: tk.Label = tk.Label(self.button_frame, text="Select Cipher")
        self.label_buttons.pack()

        # Create ButtonHandler instance
        # self.handler: ButtonHandler = ButtonHandler()

        # Create buttons for each cipher
        self.buttons: dict = {}
        for cipher in Ciphers:
            cipher_button: CipherButton = CipherButton(self.button_frame, cipher)
            self.buttons[cipher.name] = cipher_button

    def bind_events(self):
        """
        Binds events to the application window and input text widget.

        This method binds focus events to the window and input text box to handle placeholder text
        and text color changes based on user interaction.
        """

        # Bind focus events to the entry
        self.window.bind("<FocusIn>", self.on_window_entry)
        self.InputMessageBox.bind("<FocusIn>", self.on_entry_click)
        self.InputMessageBox.bind("<FocusOut>", self.on_focusout)

    def on_window_entry(self, event):
        """
        Handles the focus-in event on the output text widget.

        This method checks if the output text widget is empty. If it is, it inserts a placeholder message 
        indicating that the ciphered message will appear there once a cipher operation is performed.
        """
        if self.Output.get("1.0", "end-1c") == "":
            self.Output.insert("1.0", "Ciphered message will appear here")
            self.Output.config(fg="grey")

    def on_entry_click(self, event):
        """
        Handles the click event on the input text widget.

        This method checks if the input text box contains a placeholder message and deletes it
        if clicked, also changing the text color to black for better visibility.
        """
        if self.InputMessageBox.get("1.0", "end-1c") == "Enter message to cipher":
            self.InputMessageBox.delete("1.0", "end")
            self.InputMessageBox.config(fg="black")

    def on_focusout(self, event):
        """
        Handles the focus out event on the input text widget.

        This method checks if the input text box is empty. If it is, it inserts the placeholder message
        and sets the text color to grey.
        """
        if self.InputMessageBox.get("1.0", "end-1c") == "":
            self.InputMessageBox.insert("1.0", "Enter message to cipher")
            self.InputMessageBox.config(fg="grey")

    def start(self):
        """
        Starts the main event loop.
        """
        self.window.mainloop()

if __name__ == "__main__":
    app : CipherAppGUI = CipherAppGUI()
    app.start()