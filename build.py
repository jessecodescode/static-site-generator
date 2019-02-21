# Importing dependencies
import os
import webbrowser
import readline

send_output_to_browser = True #Optional. True opens in Firefox after building site.

def main():	
	# Remove all HTML files in /docs.
	def clear_docs():
		# Print current status of /docs.
		#print("Audit bef HTML remove: " + str(os.listdir("docs")))
		remove_list = os.listdir("docs")
		for item in remove_list:
			if item.endswith(".html"):
				os.remove("docs/" + item)
		# Print current status of /docs.
		#print("Audit aft HTML remove: " + str(os.listdir("docs")))
	clear_docs()

	# Read in the entire template
	template = open('templates/base.html').read()

	# Paths to content
	content_file_list = os.listdir("content")

	# Declare 'pages' list
	pages = []

	# Build 'pages' dictionary
	def build_pages_array():
		for file in content_file_list:
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
	build_pages_array()

	# Extract HTML from input files
	def extract_html(file):
		# print(file)
		extracted = ''
		lines = file.splitlines()
		for line in lines:
			if not line.startswith('***'):
				extracted = extracted + line
		return extracted

	# Build the pages
	def build_pages_with_base():
		for file in content_file_list:
		#    print('content/'+ file)
			file_content = open('content/'+ file).read()
		#    print(file_content)
			html_content = extract_html(file_content)
			#print(html_content)
			
			#open('docs/'+file, 'w+').write(template_top+html_content+template_bottom)
			
			# Use the string replace
			finished_page = template.replace("{{content}}", html_content)
			open('docs/'+file, 'w+').write(finished_page)
	build_pages_with_base()

	# Optionally open output in web browser
	def open_firefox(pages):
		if send_output_to_browser == True:
			docs_path = "file://" + os.path.abspath('') + "/"
			for page in pages:
				page_path = docs_path + page['output_file_path']
				#print(page_path)
				webbrowser.open(page_path)
	open_firefox(pages)
if __name__ == "__main__":
	main()