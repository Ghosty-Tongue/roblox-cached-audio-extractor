# Roblox Cached Audios Extractor

This Python script extracts cached audios (OGG/WAV) from the Roblox cache folder.

When you participate in a Roblox experience, your client automatically caches images and audios in a temporary folder. You may want to clear that folder, which is located in `%Temp%/Roblox/http`, if you want to extract assets from a specific experience.

If the `http` folder doesn't exist, you must manually create it for audios to be cached there.

## Requirements

- Python <= 3.11.0
- Windows (Operating System)
- Requests (Python Library)

### Initial Setup

1. If you don't have Python, install it from [here](https://www.python.org/downloads/).
2. Download the latest release, unzip it, and delete `README.md`.
3. Open a new Command Prompt, type: `pip install requests`
4. Open and Edit the `audios_extractor.py` file, change `YOUR_OUTPUT_PATH_FOR_EXTRACTED_AUDIOS` to the path where you want the extracted files to be saved. (Example: `Downloads/extracted_audios`)

### Executing the Script

1. Copy the path/location where the `audios_extractor.py` file is downloaded.
2. Open a new Command Prompt and type: `cd PATH_HERE` and change `PATH_HERE` to the copied path.
3. Then type `python audios_extractor.py` and the script will execute.

**NOTE:** This script was created to check which assets have been cached on your computer because sometimes assets aren't cached and are missing in the experience. Do not extract assets to infringe Intellectual Property or redistribute them, as that is against [Roblox Terms Of Service](https://en.help.roblox.com/hc/en-us/articles/115004647846).

**Recommended to use only on your OWN EXPERIENCES.**
