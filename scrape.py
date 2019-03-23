from lxml import html
import requests
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
        compileOutput(companies, fileName[i])
    return companies

def compileOutput(companies, fileName):
    print("Compiling output")
    output = 'companies = ['

    for index in range(len(companies)):
        output += '\n"'
        output += companies[index]

        if index != (len(companies) - 1):
            output += '",'
        else:
            output += '"'
    output += "\n]"
    
    writeCompaniesToFile(output, fileName)

def writeCompaniesToFile(output, fileName):
    print("Writing companies to file")
    tmpFileName = fileName + '_list.py'
    file = open(tmpFileName, 'w')
    file.write(output)
    return file.close()

def main():
    companies = getCompanies()
    output = compileOutput(companies, 'companies')

if __name__ == '__main__':
    main()