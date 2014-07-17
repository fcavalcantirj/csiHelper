#import library to do http requests:
import urllib2
import sys
#import easy to use xml parser called minidom:
import xml.etree.ElementTree as ET

tree = ET.parse(sys.argv[1])
print tree
root = tree.getroot()
xmlTranslations = root.findall('translations')
print xmlTranslations
xmlQuestions = root.findall('select1')
print xmlQuestions
for select in root.iter('select1'):
	print select