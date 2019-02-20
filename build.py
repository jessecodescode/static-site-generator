#declare -a filenames
# cd content/
# echo "Start"
# find *.html
# echo "Found"
# for file in *.html; do
#     filenames=("${filenames[@]}" "$file")
# done
# cd ../
# echo "Building with this content:"
# for filename in ${filenames[@]}; do
#     echo "  $filename"
# done
# for filename in ${filenames[@]}; do
#     cat templates/top.html content/$filename templates/bottom.html > production/$filename
# done
#sleep 1
#open -a Firefox production/home.html

# Auditing docs directory.
import os
print("Audit: " + str(os.listdir("docs")))

# Removing all HTML files in docs directory.
remove_list = os.listdir("docs")
for item in remove_list:
    if item.endswith(".html"):
        os.remove("docs/" + item)
#print("Audit after HTML remove: " + os.listdir("docs"))

