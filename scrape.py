from lxml import html
import requests
import io

def getCompanies():
    print("Getting companies")
    page = requests.get('https://en.m.wikipedia.org/wiki/List_of_S%26P_500_companies')
    tree = html.fromstring(page.content)
    companies = tree.xpath('//table[@id="constituents"]/tbody/tr/td[position()=1]/a/text()')
    return companies

def compileOutput(companies):
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
    
    return output

def writeCompaniesToFile(output):
    print("Writing companies to file")
    file = open('companies_list.py','w')
    file.write(output)
    return file.close()

def main():
    companies = getCompanies()
    output = compileOutput(companies)
    writeCompaniesToFile(output)

if __name__ == '__main__':
    main()