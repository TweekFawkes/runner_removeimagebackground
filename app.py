import sys
import os
from rembg import remove
from PIL import Image

def main():
    # Check if command line argument is provided
    if len(sys.argv) < 2:
        print("Error: Please provide a file name as an argument")
        sys.exit(1)
    
    file_name = sys.argv[1]
    input_path = os.path.join(os.getcwd(), "inputs", file_name)
    
    # Create output filename by replacing the extension with .png
    output_filename = os.path.splitext(file_name)[0] + '.png'
    output_path = os.path.join(os.getcwd(), "outputs", output_filename)
    
    # Verify if the input file exists
    if not os.path.exists(input_path):
        print(f"Error: File not found at {input_path}")
        sys.exit(1)
    
    # Create outputs directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Remove background
    print(f"Processing image: {file_name}")
    input_image = Image.open(input_path)
    output_image = remove(input_image)
    output_image.save(output_path)
    
    print(f"Background removed successfully! Saved as: {output_filename}")

if __name__ == "__main__":
    main()