#Import the library
from bs4 import BeautifulSoup
import urllib.request
import csv

#Specify the URL
urlpage = "http://www.fasttrack.co.uk/league-tables/tech-track-100/league-table/"

#Query the website and return the HTML to the variable 'page'
page = urllib.request.urlopen(urlpage)
#Parse the HTML using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')

print(soup)

#Find results within table
table = soup.find('table', attrs={'class': 'tableSorter2'})
results = table.find_all('tr')
print('Number of results', len(results))

#Create and write headers to a list:
rows = []
rows.append(['Rank', 'Company Name', 'Location', 'Year end', 'Annual sales rise over 3 years', 'Latest sales £000s', 'Staff', 'Comment'])
print(rows)

#Loop over results
for result in results:
    #Find all columns per results 
    data = result.find_all('td')
    #Check that column have data
    if len(data) == 0:
        continue
    #Write columns to variable
    rank = data[0].getText()
    company = data[1].getText()
    location = data[2].getText()
    yearend = data[3].getText()
    salerise = data[4].getText()
    sales = data[5].getText()
    staff = data[6].getText()
    comment = data[7].getText() 
    print('Company is ', company)
    #Company is Revolut
    print('Sales', sales)
    #Sale *25,860
    #Extract description from the name
    companyname = data[1].find('span', attrs={'class':'company-name'}).getText()
    description = company.replace(companyname, '')
    
    #Remove unwanted characters
    sales = sales.strip('*').strip('+').replace(',', '')
    #GO to link and extract company website 
    url = data[1].find('a').get('href')
    page = urllib.request.urlopen(url)
    #Parse the HTML
    soup = BeautifulSoup(page, 'html.parser')
    #Find the last result in table and get the link
    try:
        tableRow = soup.find('table').find_all('tr')[-1]
        webpage = tableRow.find('a').get('href')
    except:
        webpage = None
    #Write each result to rows
    rows.append([rank, companyname, webpage, description, location, yearend, salerise, sales, staff, comment])
print(rows)

#Create csv and write rows to output file
with open('techtrach100.csv', 'w', newline='') as f_output:
    csv_output = csv.writer(f_output)
    csv.output.writerows(rows)