from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import cv2

# Load the image
image_path = "C:\\Users\\Lenovo\\Downloads\\Screenshot 2024-10-17 160112.png"  
image = Image.open(image_path)

# Convert image to grayscale
image_gray = np.array(image.convert('L'))

# Apply Gaussian filter
gaussian_filtered = cv2.GaussianBlur(image_gray, (15, 15), 0)

# Adjust the contrast levels for better comparison
vmin, vmax = np.percentile(image_gray, (5, 95))  # Contrast limits for original
vmin_filt, vmax_filt = np.percentile(gaussian_filtered, (5, 95))  # Contrast limits for filtered image


# Plot the original and filtered images
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(image_gray, cmap='gray')
axes[0].set_title('Original Image')
axes[0].axis('off')

axes[1].imshow(gaussian_filtered, cmap='gray')
axes[1].set_title('Gaussian Filtered Image')
axes[1].axis('off')

# Show the images
plt.show()