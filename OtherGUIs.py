#! /usr/bin/python3

import tkinter as tk

def StartCaesarGUI(window):
    """
    Creates a GUI window to get the shift value for the Caesar cipher.

    Args:
        window: The main application window.

    Returns:
        The integer shift value entered by the user.
    """

    InputShiftValue : int = 0

    def on_submit():
        """Handles the submission of the shift value."""
        nonlocal InputShiftValue
        ShiftValue : str = CaesarKey.get()
        if ShiftValue.isdigit():  # Validate if input is an integer
            ShiftValue : int = int(ShiftValue) % 26
            ResultLabel.config(text=f"Shift value: {ShiftValue}")
            CaesarCipherGUI.destroy()
            InputShiftValue = ShiftValue
        else:
            ResultLabel.config(text="Please enter an integer from 0 - 25!")

    # Create the main window for the Caesar cipher shift input
    CaesarCipherGUI : tk.Toplevel = tk.Toplevel(window)
    CaesarCipherGUI.title("Caesar Cipher Shift")

    # Add an instruction label
    InstructionLabel : tk.Label = tk.Label(CaesarCipherGUI, text="Enter an integer (0 - 25) to move characters by\n \"CAR\" + 2 = \"ECT\"")
    InstructionLabel.pack(pady=10)

    # Add an entry field for the shift value
    CaesarKey : tk.Entry = tk.Entry(CaesarCipherGUI)
    CaesarKey.pack(pady=5)

    # Add a submit button
    SubmitButton : tk.Button = tk.Button(CaesarCipherGUI, text="Submit", command=on_submit)
    SubmitButton.pack(pady=5)

    # Add a label to display the result or error message
    ResultLabel : tk.Label = tk.Label(CaesarCipherGUI, text="", fg="blue")
    ResultLabel.pack(pady=10)

    # Prevent further interaction with the main window until this window is closed
    window.wait_window(CaesarCipherGUI)

    return InputShiftValue

def StartVigenereGUI(window):
    """
    Creates a GUI window to get the key for the Vigenère cipher.

    Args:
        window: The main application window.

    Returns:
        The key entered by the user.
    """

    InputKey = ""

    def on_submit():
        """Handles the submission of the Vigenère key."""
        nonlocal InputKey
        VigenereKey : str = KeyInput.get()
        if VigenereKey.isalpha():  # Validate if input is alphabetical
            ResultLabel.config(text=f"Repeat Key: {VigenereKey}")
            VigenereCipherGUI.destroy()
            InputKey = VigenereKey.upper()  # Convert the key to uppercase
        else:
            ResultLabel.config(text="Please enter letters A-Z or a-z only.")

    # Create the main window for the Vigenère cipher key input
    VigenereCipherGUI : tk.Toplevel = tk.Toplevel(window)
    VigenereCipherGUI.title("Vigenère Cipher Key")

    # Add an instruction label
    InstructionLabel : tk.Label = tk.Label(VigenereCipherGUI, text="Enter the Vigenère key (a single word):")
    InstructionLabel.pack(pady=10)

    # Add an entry field for the key
    KeyInput : tk.Entry = tk.Entry(VigenereCipherGUI)
    KeyInput.pack(pady=5)

    # Add a submit button
    SubmitButton : tk.Button = tk.Button(VigenereCipherGUI, text="Submit", command=on_submit)
    SubmitButton.pack(pady=5)

    # Add a label to display the result or error message
    ResultLabel : tk.Label = tk.Label(VigenereCipherGUI, text="", fg="blue")
    ResultLabel.pack(pady=10)

    # Prevent further interaction with the main window until this window is closed
    window.wait_window(VigenereCipherGUI)

    return InputKey