import cv2

def decrypt_image(image_path, password, stored_password):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found!")
        return

    if password != stored_password:
        print("YOU ARE NOT AUTHORIZED!")
        return

    height, width, _ = img.shape
    decrypted_msg = ""
    
    for n in range(height):
        for m in range(width):
            for z in range(3):
                char = chr(img[n, m, z])
                if char == chr(0):  # Stop at the null character
                    print("Decryption message:", decrypted_msg)
                    return
                decrypted_msg += char

# User Input
image_path = "encryptedImage.jpg"  # Encrypted image
password = input("Enter passcode for Decryption: ")

# Use the same stored password as in encryption
stored_password = "your_saved_password_here"  # Replace with actual password

decrypt_image(image_path, password, stored_password)
























