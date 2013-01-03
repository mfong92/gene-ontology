html_doc = " " 
import urllib
import re
import sys

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc)

'''
Input: python pantherGOScrape.py [panther gene family accession number]
ex. python pantherGOScrape.py PTHR10681:SF52
Output: GO accession numbers and GO terms assigned to that gene family
Creates a textfile of the name [pantherID].txt with the same information.
''' 

def pantherGOScrape():

	pantherID = sys.argv[1]
	html_doc = " " 
	opener = urllib.FancyURLopener({})
	f = opener.open("http://pantherdb.org/panther/family.do?clsAccession=" + pantherID)
	html_doc =  f.read()
	soup = BeautifulSoup(html_doc)

	molec = False
	molecList = []
	molecListNum = []
	molecListTerm = []

	cell = False
	cellList = []
	cellListNum = []
	cellListTerm = []

	bio = False
	bioList = []
	bioListNum = []
	bioListTerm = []

	for i in soup.find_all(["a", "td"]):
		if (i in soup.find_all('a')):
 			if ((re.findall("GO", str(i)) != [])):
 				if (molec):
 					molecList.append(str(i))
 					molecListTerm.append(str(i.get_text()))
 				if (cell):
 					cellList.append(str(i))
 					cellListTerm.append(str(i.get_text()))
 				if (bio):
 					bioList.append(str(i))
 					bioListTerm.append(str(i.get_text()))
 				
 		if (i in soup.find_all('td')):
 			if ((re.findall("table", str(i)) == [])):
	  			if ((re.findall("GO Molecular Function", str(i)) != [])):
					molec = True
	 			if ((re.findall("GO Cellular Component", str(i)) != [])):
	 				molec = False
	 				cell = True
	 				bio = False
	 			if ((re.findall("GO Biological Process", str(i)) != [])):
	 				cell = False
	 				bio = True
	 				molec = False

	for i in range (len(molecList)):
	 	currentNum = ""
	 	currentTerm = ""
	 	currentNum = re.findall(r"([0-9][0-9]*)", str(molecList[i]))

	 	molecListNum.append(currentNum)

	print '\n' + "GO Molecular Function"
	print molecListNum
	print molecListTerm 


	for i in range (len(bioList)):
	 	currentNum = ""
	 	currentTerm = ""

		currentNum = re.findall(r"([0-9][0-9]*)", str(bioList[i]))
		bioListNum.append(currentNum)

	print '\n' + "GO Biological Process"
	print bioListNum
	print bioListTerm 	



	for i in range (len(cellList)):
	 	currentNum = ""
	 	currentTerm = ""

		currentNum = re.findall(r"([0-9][0-9]*)", str(cellList[i]))

	print '\n'+ "GO Cellular Component"
	print cellListNum
	print cellListTerm 

	outFile = open(str(pantherID) + '.txt', 'w')
	outFile.write('GO Molecular Function \n')
	outFile.write(str(molecListNum))
	outFile.write('\n')
	outFile.write(str(molecListTerm))
	outFile.write('\n\n GO Biological Process\n')
	outFile.write(str(bioListNum))
	outFile.write('\n')
	outFile.write(str(bioListTerm))
	outFile.write('\n\n GO Cellular Component\n')
	outFile.write(str(cellListNum))
	outFile.write('\n')
	outFile.write(str(cellListTerm))



if __name__=="__main__":
	pantherGOScrape()