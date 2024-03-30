#import easyocr

def ocr(imagepath, format="pretty"):


    reader = easyocr.Reader(['en']) # this needs to run only once to load the model into memory
    result = reader.readtext(imagepath)


    if format=="pretty":
        text=""

        for i in result:
            text+=i[1]

        return(text)
    else:
        return(result)





import cv2
import os
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
import tensorflow as tf
from tensorflow.keras import layers, models


# Function to load images from a directory
def load_images_from_folder(folder):
    images = []
    labels = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
            # Assuming the label is in the filename (e.g., circle_001.jpg)
            label = filename.split('_')[0]  # Extract the shape label
            labels.append(label)
    return images, labels

# Function to preprocess images
def preprocess_images(images):
    processed_images = []
    for img in images:
        # Resize image to a fixed size
        resized_img = cv2.resize(img, (image_width, image_height))
        # Normalize pixel values to range [0, 1]
        normalized_img = resized_img / 255.0
        processed_images.append(normalized_img)
    return np.array(processed_images)

image_width = 64
image_height = 64
num_classes = 3  # Number of shape classes (e.g., circle, square, triangle)
num_epochs = 2
data_dir = 'Translator/images/ModelTraining'

# Load images and labels
images, labels = load_images_from_folder(data_dir)

# Preprocess images
processed_images = preprocess_images(images)

# Convert labels to numerical format
label_dict = {'circle_corner': 0, 'upper_right_corner': 1}
numeric_labels = []

# Iterate over each label in the list
for label in labels:
    # Retrieve the corresponding numerical label from the dictionary
    if label.split(".")[0][0]=="c":
        numerical_label=0
    if label.split(".")[0][0]=="r":
        numerical_label=1

    # Append the numerical label to the list
    numeric_labels.append(numerical_label)

# Split dataset into training, validation, and testing sets
train_images, test_images, train_labels, test_labels = train_test_split(processed_images, numeric_labels, test_size=0.2, random_state=42)
train_images, val_images, train_labels, val_labels = train_test_split(train_images, train_labels, test_size=0.2, random_state=42)

# Convert labels to one-hot encoded format
train_labels = to_categorical(train_labels, num_classes=num_classes)
val_labels = to_categorical(val_labels, num_classes=num_classes)
test_labels = to_categorical(test_labels, num_classes=num_classes)

# Data batching is typically handled by the training loop in TensorFlow/Keras





#exit()




# Define the CNN architecture
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(image_height, image_width, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(num_classes, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(train_images, train_labels, epochs=num_epochs, validation_data=(val_images, val_labels))

# Evaluate the model
test_loss, test_acc = model.evaluate(test_images, test_labels)
print('Test accuracy:', test_acc)





#main("Translator/arbitrarysymboltestimage.jpg")
