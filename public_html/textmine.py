#!/usr/bin/env python
# numpy and biopython are required -- pip install numpy biopython
# -*- coding: utf-8 -*-
 
from Bio import Entrez
from Bio import Medline
 
MAX_COUNT = 10
TERM = ("mtor")
abstracts = []
titles = []
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
    
def main():
    #print ('Getting {0} publications containing {1}...'.format(MAX_COUNT, TERM))
    Entrez.email = 'A.N.Other@example.com'
    h = Entrez.esearch(db='pubmed', retmax=MAX_COUNT, term=TERM)
    result = Entrez.read(h)
    #print ('Total number of publications containing {0}: {1}'.format(TERM, result['Count']))
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
    #print ('Authors: {0}'.format(', '.join(authors)))
    publications = ""
    for id in ids:
        abstracts.append(fetch_abstract(id))
        publications += '\n-----ABSTRACT-----'.join(abstracts)
        publications += '\n-----TITLE-----'.join(titles)
        #print('\n-----ABSTRACT-----'.join(abstracts))
        #print('\n-----TITLE-----'.join(titles))
    return publications.encode('utf-8')
main()
