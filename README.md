# Cipher App V0.1

This is a Python application that implements a graphical user interface (GUI) for performing various cipher operations. Users can enter a message and select a cipher from the available options. The application validates the input message and then performs the chosen cipher operation, displaying the ciphered message in the output field.

**Supported Ciphers:**

* Caesar Cipher: Shifts letters by a specified number of positions.
* Atbash Cipher: Swaps each letter with its opposite in the alphabet (e.g., 'a' becomes 'z').
* Caesar Square Cipher: Ecrypts text by combining letter shifts with a grid-based transposition.
* Vigenère Cipher: Uses a keyword to perform a more complex letter shifting.
* Morse Code: Converts the message to Morse code representation.

**Installation**

1. Make sure you have Python 3 installed on your system. You can check by running `python3 --version` or `python --version` in your terminal.
2. Clone or download this repository.
3. Open a terminal window and navigate to the downloaded directory.
4. Install any required dependencies using `./install.sh` (if you have a `requirements.txt` file).

**Usage**

1. Run the application using `./CipherApp.py`
2. Enter your message in the input text field.
3. Select the desired cipher from the buttons.
4. The ciphered message will be displayed in the output text field.

**Author**

* Eashan Polwatta Gallage (eashanpol@gmail.com)

**Further Development (Optional)**

* Add more methods of ciphers.
* Add decryption to the app.
