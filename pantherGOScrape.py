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
 				if (cell):
 					cellList.append(str(i))
 				if (bio):
 					bioList.append(str(i))
 				
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
	 	for j in range (45, 52):
	 		currentNum += str(molecList[i][j])
	 	molecListNum.append(currentNum)

	 	for k in range (54, len(molecList[i]) - 4):
	 		currentTerm += str(molecList[i][k])
	 	molecListTerm.append(currentTerm)

	print '\n' + "GO Molecular Function"
	print molecListNum
	print molecListTerm 


	for i in range (len(bioList)):
	 	currentNum = ""
	 	currentTerm = ""
	 	for j in range (45, 52):
	 		currentNum += str(bioList[i][j])
	 	bioListNum.append(currentNum)

	 	for k in range (54, len(bioList[i]) - 4):
	 		currentTerm += str(bioList[i][k])
	 	bioListTerm.append(currentTerm)

	print '\n' + "GO Biological Process"
	print bioListNum
	print bioListTerm 	



	for i in range (len(cellList)):
	 	currentNum = ""
	 	currentTerm = ""
	 	for j in range (45, 52):
	 		currentNum += str(cellList[i][j])
	 	cellListNum.append(currentNum)

	 	for k in range (54, len(cellList[i]) - 4):
	 		currentTerm += str(cellList[i][k])
	 	cellListTerm.append(currentTerm)

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