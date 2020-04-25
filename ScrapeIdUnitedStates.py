#Hey Francisco and Ian, I am going to do all of my explanation on here. This file in general is used to scrape all of the User Id's of the website "maxianetintl.campodata.org. The User Submission Id's will tell us what submission to scrape because each one has it's own page."
# 
# #imports: pretty basic. 
import requests
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import re
import numpy as np
import csv

#This is not necessary to understand as it is just something I have set-up for making the scripts real time.
ChileIDs = pd.read_csv('ChileIDs.csv')
ColombiaIDs = pd.read_csv('ColombiaIDs.csv')
CostaRicaIDs = pd.read_csv('CostaRicaIDs.csv')
EcuadorIDs = pd.read_csv('EcuadorIDs.csv')
MexicoSmartIDs = pd.read_csv('MexicoSmartIDs.csv')
MexicoBeerIDs = pd.read_csv('MexicoBeerIDs.csv')
PeruIDs = pd.read_csv('PeruIDs.csv')
IntlIDs = pd.read_csv('IntlIDs.csv')
ChileID = pd.DataFrame(ChileIDs)
ColombiaID = pd.DataFrame(ColombiaIDs)
CostaRicaID = pd.DataFrame(CostaRicaIDs)
EcuadorID = pd.DataFrame(EcuadorIDs)
MexicoSmartID = pd.DataFrame(MexicoSmartIDs)
MexicoBeerID = pd.DataFrame(MexicoBeerIDs)
PeruID = pd.DataFrame(PeruIDs)
IntlID = pd.DataFrame(IntlIDs)

#Ian this is the main section that I spoke with Ian instructer about to understand why he didn't teach this.
# The main difference between what Ian taught us and what I do here is that I do not utilize Flask or Splinter. I don't utilize it because Beautiful Soup makes it easier in my Opinion. So, I think we were taught Flask and splinter because in the long run they have more capabilities. However, fo now Beautiful Soup will work. 
# The Headers are something that Splinter does automatically. 
# It's Pretty Simple and done the same way as finding Login data that we want to push.
#First go to the login page: maxianetintl.campodata.com. Then open the Insoector and go to "Network." Before going to "Network" you will be on the "Element's" Tab just for reference. After you're here you can actually login at maxianetintl.campodata.com. What you will see is "Network" start to fill up. Click on the first "Sessions" page under the "Name" table. While in "Sessions" you will see many options. However, make sure you're in "Headers."
#Once you're in  "Headers" there will be many more options: General, Response Headers, Request Headers, and more.

# Locate the "Request Headers" portion and you will se some data. In this data you want to look for "User-Agent:" The data here is your User Agent info. You can input it like I have below:
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

#After locating the User-Agent you will want to locate the Login_data. Make sure Headers and Login Data are two different dictionaries since they are two seperate arguments later on.
#login_data can be found in the "Form Data" Section. You can actually use the same login_data I have below, but if you want to learn how to find this that is how.


login_data = {
    'utf8': '✓',
    'user[email]': 'scottys@maxianet.com',
    'user[password]': '1Sandiego!',
    'user[remember_me]': '0'
}

# make sure to include an integer equal to a new variable since we want to tell our beautiful soup what table page to scrape
page = 1
#you will not need this as I use it to tell my script what DataFrame to input the data on since I loop through multiple webpages
dfs = -1
#You will only need one of these. Name it whatever you'd like. This is where you will store the Id's
dfcountry0 = []
dfcountry1 = []
dfcountry2 = []
dfcountry3 = []
dfcountry4 = []
#not needed it is how I know which DF to append in combination with "dfs = -1"
df = [dfcountry0,dfcountry1, dfcountry2, dfcountry3, dfcountry4]
#you won't need this
df2 = []

#Let's set up our request
with requests.Session() as s:
    #the Url list below is used to loop through the different organizations. However, for your webscrape you will want just: https://maxianetmex.campodata.com
    #You can remove the for loop
    url = ['https://maxianetec.campodata.com/sessions','https://maxianetintl.campodata.com/sessions', 'https://maxianetpe.campodata.com/sessions', 'https://maxianetsmartmx.campodata.com/sessions','https://maxianetmex.campodata.com/sessions']
    for u in url:
        #This portion is also set up because of the for loop. Since, with each request I do I need somewehere different to store it I had to create this, but it is not needed.
        dfs = dfs + 1
        #this is where we get the html file of the url. However, make sure that 'u' is equal to just the one url, not a for loop. 
        #What we are doing here is getting the html file of the url to eventually find the authenticity token in the same session.
        r = s.get(u, headers=headers)
        #then we set it in a html format
        soup = BeautifulSoup(r.content, 'html5lib')
        #then we want to find the authenticity token and append it to the login data dictionary
        login_data['authenticity_token'] = soup.find('input', attrs={'name': 'authenticity_token'})['value']
        #After this we pretty much can login. However, If you remember the table that we are scraping the id's from we know that there are multiple pages. So, we do this below:
        # Basically what we are doing is saying that while the request is working we are going to request the next page after and then again. So we are essentially looping through page 1 of the table, page 2 of the table, and page 3 of the table.
        # Once the page that we request is no longer reachable. Meaning the redirect is false then we know that we have collected all of the data. So we make Johnny False.
        # 

        Johnny = True
        while Johnny is True:
            try:
                #first we append the login_data dicstionary with the correct table page
                login_data['user[redirect_to]'] = f'/admin?order=id_desc&page={page}'
                #Then we post the data to the session as follows: u in url, data=login_data, and headers=headers. 
                #Remember that the 'u' is apart of the original for loop, and since we will just be getting one page then we can request just the maxianetmex.campodata.com

                r2 = s.post(u, data=login_data,headers=headers)
                #Then we will get the HTMl
                soup2 = BeautifulSoup(r2.content, 'html5lib')
                #Then we will find the Table
                table = soup2.find('table')
                #For each table find the row
                table_rows = table.find_all('tr')
                #Then for each tr in tr we will get all of the data and append it to the correct df. 
                for tr in table_rows:
                    td = tr.find_all('td')
                    row = [i.text for i in td]
                    #Keep in mind you did not need this "[dfs]" and the "df" that you append can be whataver you set-up
                    df[dfs].append(row)
                page = page + 1
            #if the request does not work than we need to turn Johnny to False so that it quits adding "1" to the page we are scraping. We can assume the table is done. 
            except: 
                Johnny = False
                page = 1


#set up 2 empty lists. I set up 10 because i was looping through multiple Url's. 

Ecuadordf = []
Intldf = []
Perudf = []
MexSmartdf = [] 
MexBeerdf = []
Ecuadordf2 = [] 
Intldf2 = []
Perudf2 = [] 
MexSmartdf2 = [] 
MexBeerdf2 = []

#Thentake the list of appended "Ids" and make a dataframe Dataframe
#Then drop All of the 'NA'
#Ecaudor was a chosen name, you can choose whatever. 

Ecuadordf = pd.DataFrame(dfcountry0)
Ecuadordf.dropna(how ='all', inplace = True)
#Since what is returned looks more like a string saying this: "View Report #2568798" Then we need to make it just equal to the ID
Ecuadordf[1] = Ecuadordf[1].str.partition("#", True)[2]
#Append that second list with the new values
Ecuadordf2.append(Ecuadordf[1])
#Make it a Datframe
Ecuadordf2 = pd.DataFrame(Ecuadordf2)
#Transpose the data so that it is not sideways
Ecuadordf2 = Ecuadordf2.T
#Set column equal to "ID" and set the types
Ecuadordf2.columns = ["ID"]
Ecuadordf2['ID'] = Ecuadordf2['ID'].astype(str).astype('int')

#You wont need anything from line 144-167

Intldf = pd.DataFrame(dfcountry1)
Intldf.dropna(how ='all', inplace = True)
Intldf[1] = Intldf[1].str.partition("#", True)[2]
Intldf2.append(Intldf[1])
Intldf2 = pd.DataFrame(Intldf2)
Intldf2 = Intldf2.T
Intldf2.columns = ["ID"]
Intldf2['ID'] = Intldf2['ID'].astype(str).astype('int')
Perudf = pd.DataFrame(dfcountry2)
Perudf.dropna(how ='all', inplace = True)
Perudf[1] = Perudf[1].str.partition("#", True)[2]
Perudf2.append(Perudf[1])
Perudf2 = pd.DataFrame(Perudf2)
Perudf2 = Perudf2.T
Perudf2.columns = ["ID"]
Perudf2['ID'] = Perudf2['ID'].astype(str).astype('int')
MexBeerdf = pd.DataFrame(dfcountry4)
MexBeerdf.dropna(how ='all', inplace = True)
MexBeerdf[1] = MexBeerdf[1].str.partition("#", True)[2]
MexBeerdf2.append(MexBeerdf[1])
MexBeerdf2 = pd.DataFrame(MexBeerdf2)
MexBeerdf2 = MexBeerdf2.T
MexBeerdf2.columns = ["ID"]
MexBeerdf2['ID'] = MexBeerdf2['ID'].astype(str).astype('int')


#Send your Dataframe to a CSV File. I am just sending one to a csv because sending all would require so much work for us later on. The requirement is only 2 as well. 

Intldf2.to_csv('IntlIDs.csv')

#The only catch in all of this is that we want to make one difference here. Because we will later scrape the submission ID. We want to know what form this will show as. The form is shown as "Form" in the table. The values are either "Stone", "PreScreen", or something else. We will want to return that along with the submission ID as well. 