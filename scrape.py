from lxml import html
from stop_words import stop_words
import requests
import re
import io

urls = [
    "https://en.m.wikipedia.org/wiki/List_of_S%26P_500_companies"
]

fileName = [
    "sp500"
]

urlXpath = [
    '//table[@id="constituents"]/tbody/tr/td[position()=1]/a/text()'
]

def getCompanies():
    companies = []
    print("Getting companies")
    for i in range(len(urls)):
        page = requests.get(urls[i])
        tree = html.fromstring(page.content)
        companies += tree.xpath(urlXpath[i])
        compileOutput(companies, fileName[i], 'true')
        compileOutput(companies, fileName[i], 'false')
    return companies

def compileOutput(companies, fileName, removeSw):
    print("Compiling output")
    output = 'companies = ['

    for index in range(len(companies)):
        output += '\n"'
        if removeSw == 'true':
            output += removeStopWords(companies[index])
        else:
            output += companies[index].lower()

        if index != (len(companies) - 1):
            output += '",'
        else:
            output += '"'
    output += "\n]"

    if removeSw == 'true':
        fileName += '_no_stop_words'
    
    writeCompaniesToFile(output, fileName)

def removeStopWords(word):
    word = word.lower()
    for stop_word in stop_words:
        word = re.sub(r"\b%s\b|\B\.\B" % stop_word, '', word)
        word = word.replace('  ', ' ')
        word = word.strip()
    return word

def writeCompaniesToFile(output, fileName):
    print("Writing companies to file")
    tmpFileName = fileName + '_list.py'
    file = open(tmpFileName, 'w')
    file.write(output)
    return file.close()

def main():
    companies = getCompanies()
    compileOutput(companies, 'companies', 'false')
    compileOutput(companies, 'companies', 'true')

if __name__ == '__main__':
    main()