#!/bin/bash

# Specify the directory containing the files
directory="."

# Check if the directory exists
if [ -d "$directory" ]; then
    cd "$directory"  # Change to the directory

    # Loop through all files in the directory
    for file in *; do
        # Use the 'file' command to get the MIME type of the file
        mime_type=$(file -b --mime-type "$file")

        # Check if the MIME type indicates an audio file
        if [[ "$mime_type" == audio/* && "$file" != *".wav" ]]; then
            # Rename the file by adding the .wav extension
            new_name="${file}.wav"
            mv "$file" "$new_name"
            echo "Renamed: $file to $new_name"
						echo "Changing Sample rate to 22050 Hz"
            
            # Generate the output filename with the new sample rate
            output_file="${file%.*}_44100.wav"
            
            # Change the sample rate using ffmpeg
            ffmpeg -i "$new_name" -ar 22050 "$output_file"

            # rewrite file
            mv "$output_file" "$new_name"
        fi
    done
else
    echo "Directory not found: $directory"
fi

