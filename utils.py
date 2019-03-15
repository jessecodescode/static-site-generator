import sys
import os
import readline
import glob
import json
from jinja2 import Template

# Prints the contents of a directory .
def directoryStatus(folder, fileNames):
	print('\nThe current state of the \'' + folder + '\' directory is:\n')
	if len(fileNames) > 1:
		for filename in fileNames:
			print('    ', filename)
	else:
		print('The \'' + folder + '\' directory is empty! :)\n')
	print('\n')

def deleteFileList(files):
	for file in files:
		os.remove(file)
	print('\nHTML files in output directory have been removed.\nNow I will start building...')

def getAdditionalMetaData(file, contentMetaData):
	name = file.split('/')[1]
	# print('22',name)
	for item in contentMetaData["pages"]:
		# print('24',item)
		if item['Filename'] == name:
			return item

def readJsonData():
	data = open('contentMetaData.json', ).read()
	jsonData = json.loads(data)
	# print('31',jsonData)
	return jsonData
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
# Build the pages
def buildPages(contentMetaData, inputDir, outputDir):
	inputFiles = glob.glob('content/*.*')
	directoryStatus(inputDir, inputFiles)
	for item in inputFiles:
		additionalMetaData = getAdditionalMetaData(item, contentMetaData)
		item_html = open(item).read()
		if additionalMetaData is not None:
			# print('42',additionalMetaData)
			# print('43', len(additionalMetaData))
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
			# print('54')
			# print('output')
			output = outputDir + '/' + additionalMetaData['Filename']
			open(output, 'w+').write(finished_item)

def buildSite():
	# print('running buildSite function')
### Cleansing the output directory ###
	outputDir = 'docs'
	outputFiles = glob.glob(outputDir+'/'+'*.html')
	# print('73')
	# print(outputFiles)
	# Print current status of /docs directory.
	# directoryStatus(outputDir, outputFiles)

	# Remove all HTML files in /docs directory.
	deleteFileList(outputFiles)
### Additonal Content MetaData & Build Preparation ###
	#template = 'templates/base.html' ### DELETE?

	inputDir = 'content'
	contentMetaData = readJsonData()
	# print('84',contentMetaData)
### Generating the Output ###
	buildPages(contentMetaData, inputDir, outputDir)

def nameNewPage():
	if os.path.exists('content/new_content_page.html'):
		i = 0
		while os.path.exists('content/new_content_page%s.html' % i):
			i += 1
		return 'new_content_page%s.html' % i
	else:
		return 'new_content_page.html'

def newPage():
	# print('running newPage function')
	newPageName = nameNewPage()
	placeHolderContent = '''
		<h1>New Content!</h1>
    	<p>New content...</p>
	'''
	placeHolderMetaData = {
			'Title': 'Placeholder Title',
			'Date': 'Today\'s Date',
			'Author': 'Author Name',
			'Filename': newPageName,
		}
	open('content/'+ newPageName, 'w+').write(placeHolderContent)
	metaCurrent = open('contentMetaData.json', 'r').read()
	jsonData = json.loads(metaCurrent)
	# print('100')
	print('114', jsonData)
	jsonData['pages'].append(placeHolderMetaData)
	# print('103')
	print('117', jsonData)
	print(type(jsonData))
	# open('contentMetaData.json', 'w+').write(jsonData)
	with open('contentMetaData.json', 'w') as outfile:
		json.dump(jsonData, outfile)
	buildSite()

def main():
	# print('running main function')
	command = sys.argv
	try:
		# print(command)
		# print('Recieved the following argument: ' + command[1])
		if command[1] == 'build':
			buildSite()
			print('Building the site has completed.\n')
			outputDir = 'docs'
			outputFiles = glob.glob(outputDir+'/'+'*.html')
			directoryStatus(outputDir, outputFiles)
			print('Visit the new homepage at:')
			print('file://' + os.path.abspath('') + '/docs/index.html')
		elif command[1] == 'new':
			newPage()
			print('I added a new page to the site!')
		else:
			print('''
Recieved the following argument: \'''' + command[1] + '''\'
Please specify \'new\' or \'build\'
			''')
	except:
		print('''
No argument recieved:
Please specify \'new\' or \'build\'
			''')