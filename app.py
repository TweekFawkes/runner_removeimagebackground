print("[+] START: RUNNER RemoveImageBackground")
print("[~] Importing required modules...")

import os
print("[+] os module imported successfully")

import sys
print("[+] sys module imported successfully")

import shutil
print("[+] shutil module imported successfully")

# Print all environment variables
print("[~] All Environment Variables:")
for key, value in os.environ.items():
    print(f"{key}={value}")

print("[~] Setting up numba cache directory...")
numba_cache_dir = '/tmp/numba_cache'
print(f"[~] mkdir {numba_cache_dir}")
os.makedirs(numba_cache_dir, exist_ok=True)
os.chmod(numba_cache_dir, 0o777)
os.environ["NUMBA_CACHE_DIR"] = numba_cache_dir
print(f"[+] NUMBA_CACHE_DIR set to: {os.environ['NUMBA_CACHE_DIR']}")

print("[~] Setting up numba NUMBA_DISABLE_JIT = 1...")
os.environ['NUMBA_DISABLE_JIT'] = '1'
print(f"[+] NUMBA_DISABLE_JIT set to: {os.environ['NUMBA_DISABLE_JIT']}")
# os.environ['NUMBA_DISABLE_JIT'] = '1'
# Alternatively, if you need to keep Numba's JIT capabilities but just want to disable parallel processing, you can use:
from numba import config
config.DISABLE_JIT = True
config.THREADING_LAYER = 'workqueue'
print(f"[+] DISABLE_JIT = {config.DISABLE_JIT}")
print(f"[+] THREADING_LAYER = {config.THREADING_LAYER}")
# print(f"[+] NUMBA_DISABLE_JIT set to: {os.environ['NUMBA_DISABLE_JIT']}")

print("[~] Setting up u2net cache directory...")
model_dir = '/tmp/.u2net'
os.makedirs(model_dir, exist_ok=True)
os.chmod(model_dir, 0o777)
os.environ["U2NET_HOME"] = model_dir
print(f"[+] U2NET_HOME set to: {os.environ['U2NET_HOME']}")
# Define source and destination paths
source_path = '/homeawayfromhome/.u2net/u2net.onnx'
destination_path = os.path.join(model_dir, 'u2net.onnx')
print(f"[~] Copying u2net.onnx from {source_path} to {destination_path}...")
#
try:
    shutil.copy(source_path, destination_path)
    print("[+] u2net.onnx copied successfully.")
except FileNotFoundError:
    print(f"[ERROR] Source file not found: {source_path}")
    sys.exit(1)
except Exception as e:
    print(f"[ERROR] Failed to copy u2net.onnx: {str(e)}")
    sys.exit(1)
#
print(f"[~] Changing permissions for {destination_path} to 777...")
try:
    os.chmod(destination_path, 0o777)
    print("[+] Permissions set to 777 successfully.")
except Exception as e:
    print(f"[ERROR] Failed to change permissions: {str(e)}")
    sys.exit(1)
#
from rembg import remove
print("[+] rembg.remove imported successfully")

print("[~] Setting up HOME cache directory...")
root_dir = '/tmp/root'
os.makedirs(root_dir, exist_ok=True)
os.chmod(root_dir, 0o777)
os.environ["HOME"] = root_dir
print(f"[+] HOME set to: {os.environ['HOME']}")
print("[+] HOME imported successfully")

# Print all environment variables
print("[~] All Environment Variables:")
for key, value in os.environ.items():
    print(f"{key}={value}")

from PIL import Image
print("[+] PIL.Image imported successfully")

try:
    print("[~] check sys arguments")
    print(f"[DEBUG] Number of arguments: {len(sys.argv)}")
    print(f"[DEBUG] Arguments list: {sys.argv}")

    print("[~] sys.argv[1]")
    file_name = sys.argv[1]
    print(f"[DEBUG] file_name: {file_name}")
    print("[~] ---")
    print("[~] Building paths...")
    input_path = os.path.join(os.getcwd(), "inputs", file_name)
    print(f"[DEBUG] Current working directory: {os.getcwd()}")
    print(f"[DEBUG] Full input path: {input_path}")

    print("[~] Creating output filename...")
    output_filename = os.path.splitext(file_name)[0] + '.png'
    print(f"[DEBUG] Base filename without extension: {os.path.splitext(file_name)[0]}")
    print(f"[DEBUG] Output filename: {output_filename}")
    output_path = os.path.join(os.getcwd(), "outputs", output_filename)
    print(f"[DEBUG] Full output path: {output_path}")

    print("[~] Verifying input file...")
    if not os.path.exists(input_path):
        print(f"[ERROR] File not found at {input_path}")
        sys.exit(1)
    print("[+] Input file exists")

    print("[~] Creating output directory...")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    print(f"[+] Output directory verified/created: {os.path.dirname(output_path)}")

    print(f"[~] Processing image: {file_name}")
    print("[~] Opening input image...")
    input_image = Image.open(input_path)
    print(f"[DEBUG] Input image size: {input_image.size}")
    print(f"[DEBUG] Input image mode: {input_image.mode}")

    print("[~] Removing background...")
    output_image = remove(input_image)
    print("[+] Background removal complete")
    print(f"[DEBUG] Output image size: {output_image.size}")
    print(f"[DEBUG] Output image mode: {output_image.mode}")

    print("[~] Saving output image...")
    output_image.save(output_path)
    print(f"[+] Image saved successfully to: {output_path}")
    print(f"[+] Background removed successfully! Saved as: {output_filename}")

except Exception as e:
    print(f"[ERROR] An unexpected error occurred: {str(e)}")
    sys.exit(1)

print("[+] END: RUNNER RemoveImageBackground")
print("[~] ---")
print("[~] ---")
print("[~] ---")
print("[~] ---")
print("[~] ---")
print("[~] ---")
print("[~] ---")
print("[~] ---")
print("[~] ---")
print("[~] ---")
print("[~] ---")