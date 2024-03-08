import os
import re
import shutil
import hashlib
import requests
from tqdm import tqdm

home_directory = os.path.expanduser("~")
roblox_sounds_cache_path = os.path.join(home_directory, 'Library', 'Caches', 'com.roblox.Roblox', 'sounds')
extracted_assets_output_path = os.path.join(home_directory, 'Downloads', 'extracted_assets')

# Create the output directory if it doesn't exist
if not os.path.exists(extracted_assets_output_path):
    print(f"The following path: {extracted_assets_output_path} doesn't exist! Creating it...")
    os.makedirs(extracted_assets_output_path)

already_extracted_assets = []

print(f"Initializing... Searching through sounds cache path: {roblox_sounds_cache_path}")

# Extracting audio files
for filename in tqdm(os.listdir(roblox_sounds_cache_path), desc="Extracting audio files"):
    file_path = os.path.join(roblox_sounds_cache_path, filename)

    if os.path.isfile(file_path):
        with open(file_path, "r", encoding="latin-1", errors="ignore") as file:
            file_content = file.read()

        if "OggS" in file_content:
            new_file_path = os.path.join(extracted_assets_output_path, os.path.splitext(filename)[0] + ".ogg")
            shutil.copyfile(file_path, new_file_path)
            
            print("Extracted OGG file.")
        elif "WAVE" in file_content:
            new_file_path = os.path.join(extracted_assets_output_path, os.path.splitext(filename)[0] + ".wav")
            shutil.copyfile(file_path, new_file_path)
            
            print("Extracted WAV file.")

print("Done. Finished extracting audio files.")
