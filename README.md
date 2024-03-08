# Roblox Audio Extractor

This Python script extracts cached audio files (OGG/WAV) from the Roblox cache folder.

When you participate in a Roblox experience, your client automatically caches audio files in a temporary folder. You may want to clear that folder, which is located at `~/Library/Caches/com.roblox.Roblox/sounds`, if you want to extract audio assets from a specific experience.

If the `sounds` folder doesn't exist, you must manually create it for audio files to be cached there.

## Requirements

- Python <= 3.11.0
- macOS (Operating System)
- Requests (Python Library)

### Executing the Script

1. Copy the path/location where the `audio_extractor.py` file is downloaded.
2. Open a Terminal and type: `cd PATH_HERE` and change `PATH_HERE` to the copied path.
3. Then type `python audio_extractor.py` and the script will execute.

Alternatively, you can execute the shell script directly from GitHub using the following command:

```
curl -LJs "https://raw.githubusercontent.com/Ghosty-Tongue/roblox-cached-audio-extractor/MacOS/sh/extractor.sh" | bash
```

**Note:** We highly recommend using the shell script option for its simplicity and ease of use.

### Initial Setup

1. If you don't have Python, install it from [here](https://www.python.org/downloads/).
2. Download the latest release, unzip it, and delete `README.md`.
3. Open a Terminal, type: `pip install requests`
4. Open and Edit the `audio_extractor.py` file, change `YOUR_OUTPUT_PATH_FOR_EXTRACTED_AUDIO` to the path where you want the extracted audio files to be saved. (Example: `Downloads/extracted_audios`)

**Note:** The Python script option is provided for advanced users who prefer Python or have specific requirements. However, the shell script option is highly recommended for simplicity and ease of use.

**WARNING:** This script is designed to extract OGG and WAV audio files only. It was created to check which audio assets have been cached on your computer because sometimes assets aren't cached and are missing in the experience. Do not extract assets to infringe Intellectual Property or redistribute them, as that is against [Roblox Terms Of Service](https://en.help.roblox.com/hc/en-us/articles/115004647846).

**Recommended to use only on your OWN EXPERIENCES.**
