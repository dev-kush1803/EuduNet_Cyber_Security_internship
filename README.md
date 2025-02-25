# EuduNet_Cyber_Security_internship


## Secure Data Hiding in Images Using Steganography
### Project Description
This project implements image steganography to securely hide text messages inside images. It uses Python and OpenCV to modify pixel values, making the message invisible to the human eye. A password-based decryption mechanism ensures that only authorized users can retrieve the hidden information.

### What is Steganography?
Steganography is the practice of hiding secret information within digital media, such as images, without altering the visible appearance. Unlike encryption, where data is converted into an unreadable format, steganography keeps the hidden message undetectable, making it more secure against unauthorized access.

## How It Works?

### Encryption Process:
1 The user provides an image, a secret message, and a password.
2 The message is converted into ASCII values and embedded into the image pixels.
3 The modified image is saved as an encrypted file.
4 The encrypted image looks identical to the original but contains hidden data.

### Decryption Process:
1 The user enters the password to retrieve the message.
2 The program reads pixel values from the encrypted image.
3 It reconstructs the hidden message and stops at the null character (\0).
4 If the password is incorrect, access is denied.

### Technology Used
1 Python – Programming language used for implementation.
2 OpenCV (cv2) – Image processing library for pixel manipulation.
3 OS (os) – Used for file handling operations.
4 VS Code – Development environment for writing and testing the code.
5 GitHub – Version control platform for project storage and collaboration.

### Usage
1 Run the encryption.py script, enter the message, and set a password.
2 An encrypted image is generated with the hidden message.
3 Run the decryption.py script, enter the correct password to retrieve the message.

### Future Enhancements
1 Implement AES encryption along with steganography for extra security.
2 Develop a GUI-based tool for easy access.
3 Support multiple image formats like PNG, BMP, etc.
4 Integrate cloud storage for secure message exchange.
