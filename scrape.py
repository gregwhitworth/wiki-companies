from lxml import html
from stop_words import stop_words
import requests
import re
import io

urls = [
    "https://en.m.wikipedia.org/wiki/List_of_S%26P_500_companies",
    "https://en.m.wikipedia.org/wiki/Dow_Jones_Industrial_Average",
    "https://en.m.wikipedia.org/wiki/Nikkei_225"
]

fileName = [
    "sp500",
    "dow",
    "nikei"
]

urlXpath = [
    '//table[@id="constituents"]/tbody/tr/td[position()=1]/a/text()',
    '//table[@id="constituents"]/tbody/tr/td[position()=1]/a/text()',
    '//div[contains(@class, "mf-section-3")]/div/ul/li/a[1]/text()'
]

def getCompanies():
    print("Getting companies")
    allCompanies = []
    for i in range(len(urls)):
        companies = []
        page = requests.get(urls[i])
        tree = html.fromstring(page.content)
        companies = tree.xpath(urlXpath[i])
        allCompanies += companies
        compileOutput(companies, fileName[i], 'true')
        compileOutput(companies, fileName[i], 'false')
    return allCompanies

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
    file = open(tmpFileName, 'w', encoding='utf-8')
    file.write(output)
    return file.close()

def main():
    companies = getCompanies()
    companies = list(set(companies))
    compileOutput(companies, 'companies', 'false')
    compileOutput(companies, 'companies', 'true')

if __name__ == '__main__':
    main()