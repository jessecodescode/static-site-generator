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
			input_file_path = 'content/'+file
			output_file_path = 'docs/'+file
			content = open(input_file_path).read()
			lines = content.splitlines()
			count = 1
			page = {'input_file_path': input_file_path, 'output_file_path': output_file_path,}
			#content_array = []
			#print(path)
			for line in lines:
				if line.startswith('***'):
					line = line.strip('*')
					key = line.split(":", maxsplit=1)[0]
					value = line.split(": ", maxsplit=1)[1]
					#dictionary_term = {key:value}
					page[key] = value
				# else:
				# 	content_array.append(line)
			pages.append(page)
			count += 1
			# print(content_array)
	# print("51")
	print(pages)
	# print("53")
	def extract_html(file):
		# print(file)
		extracted = ''
		lines = file.splitlines()
		for line in lines:
			if line.startswith('***'):
				print(line)
			else:
				extracted = extracted + line
		return extracted

	# Build the pages
	for file in content_file_list:
	#    print('content/'+ file)
		file_content = open('content/'+ file).read()
	#    print(file_content)
		html_content = extract_html(file_content)
		#print(html_content)
		open('docs/'+file, 'w+').write(template_top+html_content+template_bottom)
	
	# Optionally open in web browser
	def open_firefox(pages):
		docs_path = "file://" + os.path.abspath('') + "/"
		for page in pages:
			page_path = docs_path + page['output_file_path']
			print(page_path)
			webbrowser.open(page_path)
	open_firefox(pages)
if __name__ == "__main__":
    main()