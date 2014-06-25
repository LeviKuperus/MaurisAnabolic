#!/usr/bin/env python
# numpy and biopython are required -- pip install numpy biopython
 
from Bio import Entrez
from Bio import Medline
import os
import mysql.connector
import time

MAX_COUNT = 4

organism = ''
org_id = '323453'

tox_id = '1'
name = ''
abstract = 'abstract'

info_id = '1'
info = 'info'

TERM = ''
abstracts = []
titles = []

records = ''
publications = ""
def setOrganism(org):
    global organism
    organism = org
	
def setToxic(tox):
    global name
    name = tox

def fetch_abstract(pmid):
    handle = Entrez.efetch(db='pubmed', id=pmid, retmode='xml')
    xml_data = Entrez.read(handle)[0]
    try:
        article = xml_data['MedlineCitation']['Article']
        abstract = article['Abstract']['AbstractText'][0]
        title = article['ArticleTitle']
        titles.append(title)
        return abstract
    except IndexError:
        return None
    except KeyError:
        return "No abstract found..."
 
def textmine():
    global publications
    global TERM
    global organism
    global name
    if not organism and not name:
	    pass
    else:
        TERM = organism + ' ' + name
        publications += 'Organism: ' + organism + '\nToxic Compound: ' + name + '\n'
        print('Getting {0} publications containing {1}...'.format(MAX_COUNT, TERM))
        Entrez.email = 'A.N.Other@example.com'
        h = Entrez.esearch(db='pubmed', retmax=MAX_COUNT, term=TERM)
        result = Entrez.read(h)
        print('Total number of publications containing {0}: {1}'.format(TERM, result['Count']))
        ids = result['IdList']
        h = Entrez.efetch(db='pubmed', id=ids, rettype='medline', retmode='text')
        records = Medline.parse(h)
        authors = []
        for record in records:
            au = record.get('AU', '?')
            for a in au: 
                if a not in authors:
                    authors.append(a)
            authors.sort()
        print('Authors: {0}'.format(', '.join(authors)))
        for id in ids:
            abstracts.append(fetch_abstract(id))
        #publications += '\nAUTHORS:\n'.join(authors)
        for abstract in abstracts:
            publications += '\nABSTRACT:\n' + abstract
        for title in titles:
            publications += '\nTITLE:\n' + title
        #createquery()
        createTable()
        return publications.encode('utf-8')
        
def setRecords():
    global records
    global organism
    global name
    global TERM    
    if not name and not organism:
        pass
    else:
        TERM = organism + ' ' + name
        MAX_COUNT = 4
        Entrez.email = 'A.N.Other@example.com'
        h = Entrez.esearch(db='pubmed', term=TERM, retmax=MAX_COUNT)
        result = Entrez.read(h)
        ids = result['IdList']
        h = Entrez.efetch(db='pubmed', id=ids, rettype='medline', retmode='text')
        records = Medline.parse(h)
    
def getRecords():
    global records
    return records

def createTable():
    records = getRecords()
    if not records:
        pass
    else:
        tableContent = ""
            
        for record in records:
                writers = lambda writers : writers if len(writers) <= 3 else writers[0:3]     
                tableContent += "<tr><td width='22%'>"+str(record.get("TI"))+"</td>"\
                "<td width='5%'>"+str(record.get("DP"))+"</td>"\
                "<td width='5%'>"+str(writers(record.get("FAU")))+"</td>"\
                "<td width='5%'>"+str(record.get("AB"))+"</td></tr>"\
    #            "<td width='5%'>"+str(record.get("JT"))+"</td>"\
    #            "<td width='5%'>"+str(TERM)+"</td>"\
                
    #            "<a href='http://www.ncbi.nlm.nih.gov/pubmed/"+str(record.get("PMID"))+"'></a>"\
                
                    
        print(tableContent)

def createquery():
    time = getTime()
    date = getDate()
    query1 = "INSERT INTO Organism (Name) VALUES ('"+organism+"')"
    print('query 1 = '+query1)
    connectDB(query1)
    query2 = "INSERT INTO Toxics (Date, Time, Name, Abstract) VALUES ('"+date+"', '"+time+"', '"+name+"', 'abstract'"
    print('query 2 = '+query2)
    global abstracts
    for abstract in abstracts:
        query2 = "INSERT INTO Toxics (Date, Time, Name, Abstract) VALUES ('"+date+"', '"+time+"', '"+name+"', '"+abstract+"')"
        connectDB(query2)
    #query3 = "INSERT INTO Information (Info_ID, Info) VALUES ('"+info_id+"', '"+info+"')"
    #print('query 3 = '+query3)
def connectDB(query):
    conn = mysql.connector.connect(host = "127.0.0.1",
                                   user = "bi2_pg1",
                                   password = "blaat1234",
                                   db="bi2_pg1")
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()
    
def getTime():
    return time.strftime("%H:%M:%S")
    
def getDate():
    return time.strftime("%d/%m/%Y")
    
def main():
    textmine()

setRecords()
createTable()
