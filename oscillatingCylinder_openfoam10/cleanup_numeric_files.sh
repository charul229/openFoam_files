#!/bin/bash

# Enable safe globbing (avoids literal patterns when no match)
# shopt -s nullglob

# Loop through all files starting with a digit
for file in [0-9]* processor*; do

    # Skip if no match (glob safety)
    [ -e "$file" ] || continue

    # Skip file named exactly "0"
    if [ "$file" = "0" ]; then
        continue
    fi

    # Remove file (safe handling for files/dirs)
    rm -rf -- "$file"

   #echo "Deleted: $file"
done
