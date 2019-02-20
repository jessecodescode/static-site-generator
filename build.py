def main():
	# Importing dependencies
	import os
	import webbrowser
	import readline

	# Print current status of /docs.
	#print("Audit bef HTML remove: " + str(os.listdir("docs")))

	# Remove all HTML files in /docs.
	remove_list = os.listdir("docs")
	for item in remove_list:
		if item.endswith(".html"):
			os.remove("docs/" + item)

	# Print current status of /docs.
	#print("Audit aft HTML remove: " + str(os.listdir("docs")))

	# Paths to template files
	template_top = open('templates/top.html').read()
	template_bottom = open('templates/bottom.html').read()

	# Paths to content
	content_file_list = os.listdir("content")

	# Declare 'pages' list
	pages = []

	# Build 'pages' dictionaries
	for file in content_file_list:
		#if file == "home.html":
			path = 'content/'+file
			content = open(path).read()
			lines = content.splitlines()
			count = 1
			content_array = []
			for line in lines:
				if line.startswith('***'):
					line = line.strip('*')
					key = line.split(":", maxsplit=1)[0]
					value = line.split(": ", maxsplit=1)[1]
					dictionary_term = {key:value}
					pages.append(dictionary_term)
				# else:
				# 	content_array.append(line)
				count += 1
			# print(content_array)
	docs_path = "file://" + os.path.abspath('docs')
	print(pages)

	# For loop to build site
	for file in content_file_list:
	#    print('content/'+ file)
		file_content = open('content/'+ file).read()
	#    print(file_content)
		open('docs/'+file, 'w+').write(template_top+file_content+template_bottom)
	# Optionally open in web browser
	#	webbrowser.open(docs_path + "/" + file)
if __name__ == "__main__":
    main()