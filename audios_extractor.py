import os
import shutil

def clear_cache(roblox_sounds_cache_path):
    print("Deleting cache files...")
    for filename in os.listdir(roblox_sounds_cache_path):
        file_path = os.path.join(roblox_sounds_cache_path, filename)
        
        if os.path.isfile(file_path):
            os.remove(file_path)
            print("Deleted:", filename)
    print("Cache cleared.")

def extract_audio(roblox_sounds_cache_path, extracted_audio_output_path):
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

    print("Done. Finished extracting audio files.")
    return already_downloaded_files

if __name__ == "__main__":
    home_directory = os.path.expanduser("~")
    roblox_sounds_cache_path = os.path.join(home_directory, 'AppData', 'Local', 'Temp', 'Roblox', 'sounds')
    extracted_audio_output_path = os.path.join(home_directory, 'YOUR_OUTPUT_PATH_FOR_EXTRACTED_AUDIO')

    option = input("Enter '1' to clear cache, '2' to extract audio files: ")

    if option == '1':
        clear_cache(roblox_sounds_cache_path)
    elif option == '2':
        extracted_files = extract_audio(roblox_sounds_cache_path, extracted_audio_output_path)
        print("Extracted files:", extracted_files)
    else:
        print("Invalid option. Please enter '1' or '2'.")
