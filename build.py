# Importing dependencies
import os
import readline
import glob
from jinja2 import Template


def directoryStatus(folder, fileNames):
	print('The current state of the', folder, 'directory is:')
	if len(fileNames) > 1:
		print(fileNames)
	else:
		print('The', folder, 'directory is empty! :)')

def deleteFileList(files):
	for file in files:
		os.remove(file)

	# Extract HTML from input files
def extractHTML(file):
	# print(file)
	extracted = ''
	lines = file.splitlines()
	for line in lines:
		if not line.startswith('***'):
			extracted = extracted + line
	return extracted

# Build the pages
def buildPages(contentMetaData, templates, inputDir, outputDir):
	print('31')
	print(contentMetaData)
	print('33')
	print(templates)
	print('35')
	print(inputDir)
	print('37')
	print(outputDir)

	for item in contentMetaData:
		# print('41')
		# print(item['Filename'])
		item_html = open(inputDir + '/' + item['Filename'])
		# print(item_html)

		title = item['Title']
		date = item['Date']
		author = item['Author']

		template_html = open(templates).read()
		template = Template(template_html)

		finished_item = template.render(
			title=title,
			date=date,
			author=author,
			content=item_html,
			)
		
		open(item[outputDir + '/' + item['Filename']], 'w+').write(finished_item)
		

def main():
####################################################
### Cleansing the output directory ###
####################################################
	outputDir = 'docs'
	outputFiles = glob.glob(outputDir+'/'+'*.html')

	# Print current status of /docs directory.
	directoryStatus(outputDir, outputFiles)

	# Remove all HTML files in /docs directory.
	deleteFileList(outputFiles)
####################################################
### Building the Content MetaData ###
####################################################
	template = 'templates/base.html'

	inputDir = 'content'
	inputFiles = glob.glob(inputDir+'/'+'*.*')

	contentMetaData = [
		{
			'Title': 'Homepage',
			'Date': '2/20/2019',
			'Author': 'jbot',
			'Filename': 'index.html',
		},
		{
			'Title': 'About',
			'Date': '2/21/2019',
			'Author': 'jbot',
			'Filename': 'about.html',
		},
		{
			'Title': 'Contact',
			'Date': '2/22/2019',
			'Author': 'jbot',
			'Filename': 'contact.html',
		},
	]
####################################################
### Generating the Output ###
####################################################
	buildPages(contentMetaData, template, inputDir, outputDir)
####################################################

if __name__ == "__main__":
	main()