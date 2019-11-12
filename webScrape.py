import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

header = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3955.0 Safari/537.36 Edg/80.0.327.0'}
firstURL = 'https://www.gamedevmap.com/'
countryArray = []
developerArray = []
rowArray = []
n = 0

page = requests.get(firstURL, headers=header)
soup = BeautifulSoup(page.content, 'lxml')  

#scrape all rows present 
def scrape():
  newURL = 'https://www.gamedevmap.com/index.php?location=&country='+ countryArray[n] +'&state=&city=&query=&type=&start=1&count=3000'
  page = requests.get(newURL, headers=header)
  soup = BeautifulSoup(page.content, 'lxml')
  for tr in soup.findAll('tr', class_=['row1','row2']):
    tds = tr.find_all('td')
    # print( "Developer: %s, Type: %s, City: %s, State/Province: %s, Country: %s" % \
    #   (tds[0].text, tds[1].text, tds[2].text, tds[3].text, tds[4].text))
    rowArray.append((tds[0].text, tds[1].text, tds[2].text, tds[3].text, tds[4].text))

#Get countries
countries = soup.find(id='countryDropdown')
for option in countries.find_all('option')[1:]:
    countryArray.append(option.text)

while n < len(countryArray) :
  scrape()
  n +=1

# # Debugging while loop
# while n < 40 :
#   scrape()
#   n +=1

# Change to dataframe
rowArray = pd.DataFrame(rowArray)
rowArray.columns = ['Studio','Type','City','State/Province','Country']

#Save to CSV
rowArray.to_csv('allRows.csv')

# Create plot
rowArray.groupby('Country')['Studio'].nunique().plot(kind='bar')
plt.title('Number of Studios by Country')
plt.show()