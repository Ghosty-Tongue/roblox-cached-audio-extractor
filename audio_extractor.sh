#!/bin/bash

function progress_bar() {
    local duration=$1
    local steps=50
    local progress_char="▇"
    local empty_char="·"
    local sleep_duration=$((duration / steps))

    printf "["
    for ((i = 0; i < steps; i++)); do
        printf "$empty_char"
    done
    printf "]"
    printf "\n"
    printf "\033[F"

    for ((i = 0; i < steps; i++)); do
        printf "\033[1C"
        printf "$progress_char"
        sleep $sleep_duration
    done
    printf "\n"
}

HOME_DIRECTORY="$HOME"
ROBLOX_SOUNDS_CACHE_PATH="$HOME/Library/Caches/com.roblox.Roblox/sounds"
EXTRACTED_AUDIO_OUTPUT_PATH="$HOME/Downloads/extracted"

already_downloaded_files=()

# Create the output directory if it doesn't exist
if [ ! -d "$EXTRACTED_AUDIO_OUTPUT_PATH" ]; then
    echo "The following path: $EXTRACTED_AUDIO_OUTPUT_PATH doesn't exist! Creating it..."
    mkdir -p "$EXTRACTED_AUDIO_OUTPUT_PATH"
fi

echo "Initializing... Searching through sounds cache path: $ROBLOX_SOUNDS_CACHE_PATH"

# Count total files
total_files=$(ls -1 "$ROBLOX_SOUNDS_CACHE_PATH" | wc -l)
current_file=0

# Iterate through files in the cache directory
for filename in "$ROBLOX_SOUNDS_CACHE_PATH"/*; do
    if [ -f "$filename" ]; then
        ((current_file++))
        echo "Processing file $current_file of $total_files..."
        file_content=$(cat "$filename")
        
        # Check if the file is OGG or WAV format
        if grep -q "OggS" <<< "$file_content"; then
            new_file_path="$EXTRACTED_AUDIO_OUTPUT_PATH/$(basename "$filename" .*)".ogg
            cp "$filename" "$new_file_path"
            echo "Downloaded OGG file: $(basename "$filename")"
            already_downloaded_files+=("$(basename "$filename")")
        elif grep -q "WAVE" <<< "$file_content"; then
            new_file_path="$EXTRACTED_AUDIO_OUTPUT_PATH/$(basename "$filename" .*)".wav
            cp "$filename" "$new_file_path"
            echo "Downloaded WAV file: $(basename "$filename")"
            already_downloaded_files+=("$(basename "$filename")")
        fi
    fi
done | progress_bar $total_files

echo "Deleting cache files..."

# Count total files
total_files=$(ls -1 "$ROBLOX_SOUNDS_CACHE_PATH" | wc -l)
current_file=0

# Remove files from the cache directory that were not downloaded
for filename in "$ROBLOX_SOUNDS_CACHE_PATH"/*; do
    if [ -f "$filename" ]; then
        ((current_file++))
        echo "Deleting file $current_file of $total_files..."
        file_basename=$(basename "$filename")
        if ! [[ "${already_downloaded_files[@]}" =~ "$file_basename" ]]; then
            rm "$filename"
            echo "Deleted: $file_basename"
        fi
    fi
done | progress_bar $total_files

echo "Done. Finished downloading and deleting cache files."
