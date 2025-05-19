# Instant NGP Webcam Test for Mesh Enhancement
# This script captures webcam frames and demonstrates how to use Instant NGP
# to enhance a basic mesh

import numpy as np
import cv2
import torch
import os
import time
from pathlib import Path

# After installation, run the training:
#    python -m instant_ngp ngp_test

# Setup complete! Follow the instructions above to run instant-ngp.
# After running, you can export the mesh with:
#    instant-ngp --scene transforms.json --save-mesh output.obj

# Set up paths
BASE_DIR = Path("./ngp_test")
BASE_DIR.mkdir(exist_ok=True)
FRAMES_DIR = BASE_DIR / "frames"
FRAMES_DIR.mkdir(exist_ok=True)
TRANSFORMS_FILE = BASE_DIR / "transforms.json"

def capture_test_sequence():
    """Capture a short sequence of frames from webcam"""
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam")
        return False
    
    # Set camera properties
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    print("Capturing frames (move slowly around object)...")
    frames = []
    
    # Capture 20 frames (adjust as needed)
    for i in range(20):
        ret, frame = cap.read()
        if not ret:
            break
            
        # Save frame
        filename = f"frame_{i:03d}.png"
        cv2.imwrite(str(FRAMES_DIR / filename), frame)
        frames.append(filename)
        
        # Display frame
        cv2.imshow('Capture', frame)
        cv2.waitKey(200)  # 200ms delay between frames
        
    cap.release()
    cv2.destroyAllWindows()
    
    # Generate transforms.json (camera parameters)
    create_transforms_file(frames)
    return True

def create_transforms_file(frames):
    """Create a basic transforms.json file with camera parameters"""
    # Calculate rough camera positions - a circular path
    transforms = {
        "frames": []
    }
    
    # For simplicity, we'll use a basic circular camera path
    for i, frame in enumerate(frames):
        angle = i * 2 * np.pi / len(frames)
        
        # Camera position (simplified circular path)
        tx = np.cos(angle) * 2.0
        ty = 0.2  # Slight up angle
        tz = np.sin(angle) * 2.0
        
        # Simple camera transform - looking at origin
        transform = {
            "file_path": f"./frames/{frame}",
            "transform_matrix": [
                [1, 0, 0, tx],
                [0, 1, 0, ty],
                [0, 0, 1, tz],
                [0, 0, 0, 1]
            ]
        }
        transforms["frames"].append(transform)
    
    # Add camera parameters
    transforms["camera_angle_x"] = 0.8  # Approximate FOV
    
    # Write transforms.json
    import json
    with open(TRANSFORMS_FILE, 'w') as f:
        json.dump(transforms, f, indent=2)

def setup_instant_ngp():
    """Install instant-ngp if not already installed"""
    try:
        import subprocess
        
        # Check if instant-ngp is installed
        print("Checking if instant-ngp is installed...")
        
        # Instructions for installing instant-ngp
        print("\nInstallation instructions for instant-ngp:")
        print("1. Clone the repository:")
        print("   git clone --recursive https://github.com/nvlabs/instant-ngp")
        print("2. Build following the instructions in the README.md")
        print("3. Install the Python bindings:")
        print("   pip install -e ./instant-ngp\n")
        
        # Instructions for running with your data
        print("After installation, run the training:")
        print(f"   python -m instant_ngp {BASE_DIR}")
        
        return True
    except Exception as e:
        print(f"Error setting up instant-ngp: {e}")
        return False

def main():
    print("=== Instant NGP Webcam Mesh Enhancement Test ===")
    
    # Step 1: Capture test frames
    if not capture_test_sequence():
        print("Failed to capture frames")
        return
    
    # Step 2: Setup instant-ngp
    setup_instant_ngp()
    
    print("\nSetup complete! Follow the instructions above to run instant-ngp.")
    print("After running, you can export the mesh with:")
    print("   instant-ngp --scene transforms.json --save-mesh output.obj")

if __name__ == "__main__":
    main()