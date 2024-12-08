#! /usr/bin/python3

import string
from ttkwidgets.frames import Tooltip
import tkinter as tk
from tkinter import Tk, Button, Toplevel, Label, StringVar
import re
import math

MorseCodeDict : dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '-.-.--',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', '"': '.-..-.',
    '@': '.--.-.', '=': '-...-', ':': '---...', ';': '-.-.-.', '+': '.----.',
    '-': '-....-', '_': '..--.-', '$': '...-..-', '&': '.-...'
}

# Define the standard English alphabet and its reverse
Alphabet : str = string.ascii_uppercase
ReversedAlphabet : str = Alphabet[::-1]

def Txt2Caeser(InputString : str, KeyInteger : int ) -> str :
    """Encrypts a text string using the Caesar cipher.

    Args:
        InputString: The input text string to be encrypted.
        KeyInteger: The integer shift value for the cipher.

    Returns:
        The encrypted text string.
    """
    EncryptedText : str = ""
    for char in InputString:
        if char.isalpha():  # Check if the character is a letter
            # Shift the letter by KeyInteger using modular arithmetic
            EncryptedText += Alphabet[(Alphabet.index(char) + KeyInteger) % 26]
        else:
            # Keep non-alphabetic characters unchanged
            EncryptedText += char
    return EncryptedText

def Txt2Atbash(InputString : str ) -> str :
    """Encrypts a text string using the Atbash cipher.

    Args:
        InputString: The input text string to be encrypted.

    Returns:
        The encrypted text string.
    """
    EncryptedText = ""
    for char in InputString:
        if char in Alphabet:
            # Reverse the alphabet position of the character
            index : int = Alphabet.index(char)
            EncryptedChar : str = ReversedAlphabet[index]
            EncryptedText += EncryptedChar
        else:
            # Keep non-alphabetic characters unchanged
            EncryptedText += char
    return EncryptedText

def Txt2CaesarSquare(InputString : str ) -> str :
    """Encrypts a text string using the Caesar Square cipher.

    Args:
        InputString: The input text string to be encrypted.

    Returns:
        The encrypted text string.
    """
    # Preprocess the string to remove non-alphanumeric characters
    AlphaNumericString : str = re.sub(r'[^a-zA-Z0-9]', '', InputString)
    NumChars : int = len(AlphaNumericString)

    # Calculate the size of the square matrix
    CeilingNum : int = math.ceil(math.sqrt(NumChars))

    # Create an empty matrix
    EncryptedMatrix = [["" for _ in range(CeilingNum+1)] for _ in range(CeilingNum+1)]

    # Populate the matrix with characters from the input string
    for idx, char in enumerate(AlphaNumericString):
        row : int = idx % CeilingNum
        col : int = idx // CeilingNum
        EncryptedMatrix[row][col] = char

    # Flatten the matrix into a string, separating words with spaces
    EncryptedText : str = " ".join("".join(row).strip() for row in EncryptedMatrix)
    return EncryptedText

def Txt2Vigenere(InputString  : str , InputKey : str ) -> str :
    """Encrypts a text string using the Vigenère cipher.

    Args:
        InputString: The input text string to be encrypted.
        InputKey: The key used for encryption.

    Returns:
        The encrypted text string.
    """
    EncryptedText : str = ""
    key_index : int = 0
    key_length : int = len(InputKey)
    InputKey : str = InputKey.upper()  # Ensure the key is uppercase

    if not key_length:
        return EncryptedText

    for char in InputString:
        if char.isalpha():
            # Calculate the shift using the current key character
            shift : int  = Alphabet.index(InputKey[key_index % key_length])
            EncryptedChar : str = Alphabet[(Alphabet.index(char) + shift + 1) % 26]
            EncryptedText += EncryptedChar
            key_index += 1
        else:
            # Keep non-alphabetic characters unchanged
            EncryptedText += char

    return EncryptedText

def Txt2MorseCode(InputString : str ) -> str :
    """Encodes a text string into Morse code.

    Args:
        InputString: The input text string to be encoded.

    Returns:
        The Morse code representation of the input text.
    """
    EncryptedText = ""
    for char in InputString:
        if char in MorseCodeDict:
            EncryptedText += MorseCodeDict[char] + " "
        else:
            EncryptedText += char + "/"  # Keep non-Morse characters

    return EncryptedText.strip()

class Tooltip:
    """
    A class to create tooltips for tkinter widgets.

    Attributes:
        widget: The widget to which the tooltip is attached.
        headertext: The header text of the tooltip.
        text: The main body text of the tooltip.
        width: The maximum width of the tooltip window.
        background: The background color of the tooltip window.
        offset: A tuple specifying the horizontal and vertical offset of the tooltip relative to the mouse pointer.
        showheader: A boolean indicating whether to show a header in the tooltip.
        tooltip_window: The tkinter Toplevel window used to display the tooltip.
        mouse_inside: A boolean indicating whether the mouse pointer is currently inside the widget.

    Methods:
        setup_bindings(): Binds event handlers to the widget to show and hide the tooltip.
        on_enter(event): Shows the tooltip when the mouse enters the widget.
        on_leave(event): Hides the tooltip when the mouse leaves the widget.
        show_tooltip(event): Creates and displays the tooltip window.
        hide_tooltip(): Destroys the tooltip window.
        update_tooltip_position(event): Updates the position of the tooltip window.
    """

    def __init__(self, widget, headertext='', text='', width=200, background="#fef9cd", offset=(10, 20), showheader=True):
        self.widget : any = widget # any object in the GUI can have the tooltip
        self.headertext : str = headertext
        self.text : str = text
        self.width : int  = width
        self.background : str = background
        self.offset : tuple = offset
        self.showheader : bool = showheader
        self.tooltip_window : bool = None
        self.mouse_inside : bool = False  # Track if the pointer is inside the widget
        self.setup_bindings()

    def setup_bindings(self):
        self.widget.bind("<Enter>", self.on_enter)
        self.widget.bind("<Leave>", self.on_leave)
        self.widget.bind("<Motion>", self.update_tooltip_position)

    def on_enter(self, event):
        self.mouse_inside = True
        self.show_tooltip(event)

    def on_leave(self, event):
        self.mouse_inside = False
        self.hide_tooltip()

    def show_tooltip(self, event):
        if self.tooltip_window or not self.mouse_inside:
            return  # Avoid creating multiple tooltip windows

        # Create the tooltip window but do not immediately display it
        self.tooltip_window = Toplevel(self.widget)
        self.tooltip_window.overrideredirect(True)
        self.tooltip_window.configure(bg=self.background)

        # Add header and body text
        if self.showheader and self.headertext:
            header = Label(self.tooltip_window, text=self.headertext, bg=self.background, font=("Arial", 10, "bold"))
            header.pack(anchor="w", padx=5, pady=(5, 0))

        body = Label(self.tooltip_window, text=self.text, bg=self.background, wraplength=self.width, justify="left")
        body.pack(anchor="w", padx=5, pady=(5, 5))

        # Position the tooltip immediately after creating it
        self.update_tooltip_position(event)

    def hide_tooltip(self):
        if self.tooltip_window:
            self.tooltip_window.destroy()
            self.tooltip_window = None

    def update_tooltip_position(self, event):
        if self.tooltip_window and self.mouse_inside:
            # Position tooltip relative to the widget and pointer
            x = self.widget.winfo_rootx() + event.x + self.offset[0]
            y = self.widget.winfo_rooty() + event.y + self.offset[1]
            self.tooltip_window.geometry(f"+{x}+{y}")

class CaesarCipher:
    name = "Caesar"
    name_ext = "Caesar Cipher"
    func_name = "Caesar_Cipher_Func"
    description = f"""Each letter is shifted by a fixed number of positions in the alphabet.\nEg, with a shift of 3, \"HELLO\" becomes \"KHOOR.\""""

class AtbashCipher:
    name = "Atbash" 
    name_ext = "Atbash Cipher" 
    func_name = "Atbash_Cipher_Func"
    description = """A simple substitution cipher where each letter is replaced with its counterpart from the opposite end of the alphabet.\nEg, \"A\" becomes \"Z,\" \"B\" becomes \"Y,\" and so on.\nEg, plaintext \"HELLO THERE\": \"SVOOL GSVIV\""""

class CaesarSquareCipher:
    name = "Caesar Square"
    name_ext =  "Caesar Square Cipher"
    func_name =  "Caesar_Square_Func"
    description = """The text is written into a square grid row by row and then read column by column to create the ciphertext.\nEg, \"We are cool\" with a grid size of 3x3: \"WRO EEO ACL\" \nW\tR\tO\nE\tE\tO\nA\tC\tL"""

class VigenereCipher:
    name = "Vigenère"
    name_ext =  "Vigenère Cipher"
    func_name =  "Vigenere_Cipher_Func"
    description = """Each letter in the plaintext is shifted by a number of positions determined by a repeating keyword. The shift for each letter is based on the corresponding letter in the keyword (A = 0, B = 1, ..., Z = 25).\nEg, PLAINTEXT \"TOOL\" and the keyword \"TEA\": \"MSOE\"\nT+T = M\nO+E = S\nO+A = O\nL+T = E"""

class MorseCode:
    name = "Morse Code"
    name_ext =  "Morse Code"
    func_name =  "Morse_Code_Func"
    description = """Each letter, number, or symbol in the plaintext is encoded into a unique sequence of dots (•) and dashes (−), separated by spaces. Letters are separated by a space, and words are separated by a slash (/).\nEg, Plaintext \"HELLO THERE\": \"•••• • •−•• •−•• −−− / − •••• • •−• •\""""

Ciphers : list = [CaesarCipher,AtbashCipher,CaesarSquareCipher,VigenereCipher,MorseCode]
buttons : dict = {}