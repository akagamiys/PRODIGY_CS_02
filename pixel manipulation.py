import cv2
import numpy as np
import matplotlib.pyplot as plt

def encode_image(image, key):
    encoded_image = (image.astype(np.int32) + (key*3)/2) % 256
    return encoded_image.astype(np.uint8)

def decode_image(encoded_image, key):

    decoded_image = (encoded_image.astype(np.int32) - (key*3)/2) % 256
    return decoded_image.astype(np.uint8)

# Load an example image
image_path = r"C:\Users\shash\Desktop\prodigy\door.jpg"  # Make sure to use the correct path to your image file
image = cv2.imread(image_path)

# Check if the image was loaded correctly
if image is None:
    print(f"Error: Could not load image from {image_path}")
else:
    # Encryption key
    key = 250  # Example key, can be any integer

    # Encode the image
    encoded_image = encode_image(image, key)

    # Define paths for saving images
    encoded_image_path = 'encoded_image.jpg'
    decoded_image_path = 'decoded_image.jpg'

    # Save the encoded image
    cv2.imwrite(encoded_image_path, encoded_image)
    print(f"Encoded image saved to {encoded_image_path}")

    # Decode the image
    decoded_image = decode_image(encoded_image, key)

    # Save the decoded image
    cv2.imwrite(decoded_image_path, decoded_image)
    print(f"Decoded image saved to {decoded_image_path}")

    # Convert BGR images to RGB for display with matplotlib
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    encoded_image_rgb = cv2.cvtColor(encoded_image, cv2.COLOR_BGR2RGB)
    decoded_image_rgb = cv2.cvtColor(decoded_image, cv2.COLOR_BGR2RGB)

    # Display the images using matplotlib
    plt.figure(figsize=(15, 5))
    
    plt.subplot(1, 3, 1)
    plt.title('Original Image')
    plt.imshow(image_rgb)
    plt.axis('off')
    
    plt.subplot(1, 3, 2)
    plt.title('Encoded Image')
    plt.imshow(encoded_image_rgb)
    plt.axis('off')
    
    plt.subplot(1, 3, 3)
    plt.title('Decoded Image')
    plt.imshow(decoded_image_rgb)
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()
