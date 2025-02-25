import cv2
import os

def encrypt_image(image_path, message, password, output_path="encryptedImage.jpg"):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found!")
        return False

    height, width, _ = img.shape

    # Ensure message fits in the image
    if len(message) > height * width * 3:
        print("Error: Message too long for the image size!")
        return False

    # Convert message into ASCII values and add a null character at the end
    message += chr(0)
    msg_ascii = [ord(char) for char in message]

    index = 0
    for n in range(height):
        for m in range(width):
            for z in range(3):  # Iterate over RGB channels
                if index < len(msg_ascii):
                    img[n, m, z] = msg_ascii[index]
                    index += 1
                else:
                    break

    cv2.imwrite(output_path, img)
    print(f"Message encrypted successfully! Saved as {output_path}")
    os.system(f"start {output_path}")  # Opens the image (Windows)
    return password  # Return password for decryption verification

# User Input
image_path = "mypic.jpg"  # Replace with your image path
message = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Encrypt and store password (for demo purposes)
stored_password = encrypt_image(image_path, message, password)
