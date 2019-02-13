#!/bin/bash

rm production/*.html

declare -a filenames
cd content/
# echo "Start"
# find *.html
# echo "Found"
for file in *.html; do
    filenames=("${filenames[@]}" "$file")
done
cd ../
echo "Building with this content:"
for filename in ${filenames[@]}; do
    echo "  $filename"
done
for filename in ${filenames[@]}; do
    cat templates/top.html content/$filename templates/bottom.html > production/$filename
done
#sleep 1
#open -a Firefox production/home.html