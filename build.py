# Importing dependencies
import os
import webbrowser

# Print current status of /docs.
print("Audit bef HTML remove: " + str(os.listdir("docs")))

# Remove all HTML files in /docs.
remove_list = os.listdir("docs")
for item in remove_list:
    if item.endswith(".html"):
        os.remove("docs/" + item)

# Print current status of /docs.
print("Audit aft HTML remove: " + str(os.listdir("docs")))

# Paths to template files, content, output directory
template_top = open('templates/top.html').read()
template_bottom = open('templates/bottom.html').read()
build_list = os.listdir("content")
docs_path = "file://" + os.path.abspath('docs')

# For loop to build site
for file in build_list:
    open('docs/'+file, 'w+').write(template_top+file+template_bottom)
# Optionally open in web browser
    webbrowser.open(docs_path + "/" + file)