# Importing dependencies
import sys
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

def getAdditionalMetaData(file, contentMetaData):
	print('19')
	name = file.split('/')[1]
	print(name)
	for item in contentMetaData:
		if item['Filename'] == name:
			return item

# Build the pages
def buildPages(contentMetaData, inputDir, outputDir):
	inputFiles = glob.glob('content/*.*')
	print('21')
	print(inputFiles)

	for item in inputFiles:
		additionalMetaData = getAdditionalMetaData(item, contentMetaData)
		item_html = open(item).read()
		# print('26')
		# print(contentMetaData)

		title = additionalMetaData['Title']
		date = additionalMetaData['Date']
		author = additionalMetaData['Author']
		me = additionalMetaData['Filename']

		template_html = open('templates/base.html').read()
		template = Template(template_html)

		finished_item = template.render(
			title=title,
			date=date,
			author=author,
			content=item_html,
			me=me,
			pages=contentMetaData,
			)
		print('54')
		print('output')
		output = outputDir + '/' + additionalMetaData['Filename']
		open(output, 'w+').write(finished_item)
		

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
######################################################
### Additonal Content MetaData & Build Preparation ###
######################################################
	template = 'templates/base.html'

	inputDir = 'content'

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
	buildPages(contentMetaData, inputDir, outputDir)
####################################################


def main():
	command = sys.argv
	try:
		if command[1] == 'build':
			print('building')
		elif command[1] == 'new':
			print('new build')
		else:
			print('New or Build - nothing else.')
	except:
		print('No argument specified. Choose \'new\' or \'build.\'')