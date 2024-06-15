## Overview

This Python program demonstrates a simple technique to encrypt and decrypt images using basic mathematical operations. The program uses the OpenCV library for image processing and Matplotlib for displaying the images.

## How It Works

The program performs encryption by adding a constant value (key) to each pixel of the image and performs decryption by subtracting the same constant value. The operations are performed modulo 256 to ensure the pixel values remain within the valid range [0, 255].

## Features

Image Encryption: Adds a constant value to each pixel in the image.

Image Decryption: Subtracts the constant value from each pixel to retrieve the original image.

Handles Large Keys: Can use large keys for encryption and decryption.

Display Images: Uses Matplotlib to display the original, encoded, and decoded images side by side.

## Requirements

-Python 3.x

-OpenCV

-NumPy

-Matplotlib

## Notes
Ensure the correct path to the image file is specified.

The key value can be adjusted to any integer for different encryption results.

The operations ensure that pixel values remain valid by using modulo 256 arithmetic.
