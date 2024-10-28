import os
import cv2
import numpy as np
import torch
import torchvision.transforms as transforms
from torchvision.models import resnet50
from PIL import Image
from storeEmbeddingFaiss import *

def generate_embeddings(video_file_name):
    print("Embedding generation started.")
    video_folder = 'recorded_videos'
    
    # Construct the full path to the video file
    video_file_path = os.path.join(video_folder, video_file_name)

    # Check if the specified video file exists
    if not os.path.isfile(video_file_path):
        print(f"Error: {video_file_name} does not exist in {video_folder}.")
        return

    # Load the pre-trained ResNet model
    model = resnet50(weights='IMAGENET1K_V1')  # Update to use the weights argument
    model.eval()  # Set the model to evaluation mode

    # Define the transformations
    transform = transforms.Compose([
        transforms.Resize((224, 224)),  # Resize to match ResNet input
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

    # Initialize list to hold embeddings
    embeddings = []

    # Open the video file
    cap = cv2.VideoCapture(video_file_path)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert BGR (OpenCV format) to RGB and then to PIL image
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(frame_rgb)

        # Apply the transformations
        frame_tensor = transform(pil_image).unsqueeze(0)  # Add batch dimension
        
        # Generate the embedding
        with torch.no_grad():
            embedding = model(frame_tensor).numpy()  # Get the output from ResNet

        embeddings.append(embedding)

    cap.release()

    # Convert embeddings to a NumPy array and average them
    embeddings = np.array(embeddings).squeeze()
    average_embedding = np.mean(embeddings, axis=0)  # Average over all frames

    print("Embedding generation complete.")
    store_embeddings_faiss(average_embedding)
    return average_embedding

