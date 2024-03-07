import os
import shutil
import requests

home_directory = os.path.expanduser("~")
roblox_sounds_cache_path = os.path.join(home_directory, 'AppData', 'Local', 'Temp', 'Roblox', 'sounds')
extracted_audio_output_path = os.path.join(home_directory, 'YOUR_OUTPUT_PATH_FOR_EXTRACTED_AUDIO')

already_downloaded_files = []

if not os.path.exists(extracted_audio_output_path):
    print(f"The following path: {extracted_audio_output_path} doesn't exist! Creating it...")
    os.makedirs(extracted_audio_output_path)

print(f"Initializing... Searching through sounds cache path: {roblox_sounds_cache_path}")

for filename in os.listdir(roblox_sounds_cache_path):
    file_path = os.path.join(roblox_sounds_cache_path, filename)

    if os.path.isfile(file_path):
        with open(file_path, "rb") as file:
            file_content = file.read()

        if b"OggS" in file_content:
            new_file_path = os.path.join(extracted_audio_output_path, os.path.splitext(filename)[0] + ".ogg")
            shutil.copyfile(file_path, new_file_path)
            
            print("Downloaded OGG file:", filename)
            already_downloaded_files.append(filename)
        elif b"WAVE" in file_content:
            new_file_path = os.path.join(extracted_audio_output_path, os.path.splitext(filename)[0] + ".wav")
            shutil.copyfile(file_path, new_file_path)
            
            print("Downloaded WAV file:", filename)
            already_downloaded_files.append(filename)

print("Deleting cache files...")

for filename in os.listdir(roblox_sounds_cache_path):
    file_path = os.path.join(roblox_sounds_cache_path, filename)
    
    if filename not in already_downloaded_files:
        os.remove(file_path)
        print("Deleted:", filename)

print("Done. Finished downloading and deleting cache files.")
