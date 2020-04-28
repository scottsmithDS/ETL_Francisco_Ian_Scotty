import requests
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import re
import csv
import numpy as np
pd.set_option('display.max_columns', None)
# importss above

newvariablesIntl = pd.read_csv('IntlIDs.csv')
newvariablesIntl = pd.DataFrame(newvariablesIntl)
newvariablesIntl = newvariablesIntl.drop("Unnamed: 0", axis=1, inplace = False)
newvariablesPeru = pd.read_csv('PeruIDs.csv')
newvariablesPeru = pd.DataFrame(newvariablesPeru)
newvariablesPeru = newvariablesperu.drop("Unnamed: 0", axis=1, inplace = False)
newvariablesEcuador = pd.read_csv('EcuadorIDs.csv')
newvariablesEcuador = pd.DataFrame(newvariablesEcuador)
newvariablesEcuador = newvariablesEcuador.drop("Unnamed: 0", axis=1, inplace = False)
newvariablesMexB = pd.read_csv('MexBeerIDs.csv')
newvariablesMexB = pd.DataFrame(newvariablesMexB)
newvariablesMexB = newvariablesMexB.drop("Unnamed: 0", axis=1, inplace = False)

for value in newvariablesIntl['ID']:
    change = {value: "/submissions/" + str(value) + "/webview"}
    newvariablesIntl.replace(change, inplace = True)
    newvariablesIntl.dropna(how ='all', inplace = True)
for value in newvariablesPeru['ID']:
    change = {value: "/submissions/" + str(value) + "/webview"}
    newvariablesPeru.replace(change, inplace = True)
    newvariablesParu.dropna(how ='all', inplace = True)
for value in newvariablesEcuador['ID']:
    change = {value: "/submissions/" + str(value) + "/webview"}
    newvariablesEcuador.replace(change, inplace = True)
    newvariablesEcuador.dropna(how ='all', inplace = True)
for value in newvariablesMexB['ID']:
    change = {value: "/submissions/" + str(value) + "/webview"}
    newvariablesMexB.replace(change, inplace = True)
    newvariablesMexB.dropna(how ='all', inplace = True)

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

login_data = {
    'utf8': '✓',
    'user[email]': 'scottys@maxianet.com',
    'user[password]': '1Sandiego!',
    'user[remember_me]': '0'
    
}
imageurls = []
times = []

timecheck_in = []
    
full_path = "hello"+'.jpg'
timerss = []

timedf = {}
lat = {}
lng = {}
name = {}
locname ={}
Brand1 = {}
Brand2 = {}
Brand3 = {}
Brand4 = {}
Brand5 = {}
Brand6 = {}
Brand7 = {}
Brand8 = {}
Brand9 = {}
Brand10 = {}
Brand11= {}
Brand12 = {}
Brand13 = {}
Brand14 = {}
user = {}
timedf4 = {}
lat4 = {}
lng4 = {}
name4 = {}
locname4 ={}
Brand14 = {}
Brand24 = {}
Brand34 = {}
Brand44 = {}
Brand54 = {}
Brand64 = {}
Brand74 = {}
Brand84 = {}
Brand94 = {}
Brand104 = {}
Brand114= {}
Brand124 = {}
Brand134 = {}
Brand144 = {}

df = []
url = []

with requests.Session() as s:
    url = ['https://maxianetec.campodata.com/sessions','https://maxianetintl.campodata.com/sessions', 'https://maxianetpe.campodata.com/sessions', 'https://maxianetsmartmx.campodata.com/sessions','https://maxianetmex.campodata.com/sessions']
        for u in url: 
        r = s.get(url, headers=headers)
        soup = BeautifulSoup(r.content, 'html5lib')
        login_data['authenticity_token'] = soup.find('input', attrs={'name': 'authenticity_token'})['value']
        if u is 'https:maxianetintl.campodata.com.sign_in':
            for weburls in (newvariablesIntl['ID'] for newvariablesIntl['Form'] in newvariablesIntl if newvariablesIntl['Form'] = 'Brand Price Audit'):
                if

                login_data['user[redirect_to]'] = weburls
                r2 = s.post(url, data=login_data,headers=headers)
                soup2 = BeautifulSoup(r2.content, 'html5lib')
                data  = soup2.find("script")
                data2 = data.string
                res = data2.partition('lat')[2]
                reslng =data2.partition('lng')[2]
                lat[str(weburls)] = res[2:12]
                lng[str(weburls)] = reslng[2:12]
                name[str(weburls)] = soup2.find('h5',{'class':'text-secondary'}).text
                table = soup2.find('table')
                table_rows = table.find_all('tr')
                for tr in table_rows:
                    td = tr.find_all('td')
                    th = tr.find_all('th')
                    rowy = [i.text for i in th]
                    row = [i.text for i in td]
                    rowers = 0
                    Stone = ['Stone']
                    rowwe = 0
                    for rowie in rowy:
                        if rowie is 'Quantity of Unities in the pack':
                            rowers = rowers + 1              
                    if rowers is 0:
                        row.insert(5, "Size Unknown")
                    rowers = 0
                    df.append(row)
                try: Brand1[str(weburls)] = df[1][0:7]
                except Exception as exception: pass  
                try: Brand2[str(weburls)] = df[2][0:7]
                except Exception as exception: pass
                try: Brand3[str(weburls)] = df[3][0:7]
                except Exception as exception: pass
                try: Brand4[str(weburls)] = df[4][0:7]
                except Exception as exception: pass 
                try: Brand5[str(weburls)] = df[5][0:7]
                except Exception as exception: pass 
                try: Brand6[str(weburls)] = df[6][0:7]
                except Exception as exception: pass
                try: Brand7[str(weburls)] = df[7][0:7]
                except Exception as exception: pass  
                try: Brand8[str(weburls)] = df[8][0:7]
                except Exception as exception: pass
                try: Brand9[str(weburls)] = df[9][0:7]
                except Exception as exception: pass
                try: Brand10[str(weburls)] = df[10][0:7]
                except Exception as exception: pass 
                try: Brand11[str(weburls)] = df[11][0:7]
                except Exception as exception: pass 
                try: Brand12[str(weburls)] = df[12][0:7]
                except Exception as exception: pass
                try: Brand13[str(weburls)] = df[13][0:7]
                except Exception as exception: pass  
                try: Brand14[str(weburls)] = df[14][0:7]
                except Exception as exception: pass
                df = []
                timedf1 = soup2.find('input',{'class': 'form-control-plaintext bg-panel-tint pl-4 input-lg'})['value'],
                timedf[str(weburls)] = soup2.find('input',{'class': 'form-control-plaintext bg-panel-tint pl-4 input-lg'})['value'],
                try: locname[str(weburls)] = soup2.find('h3',{'class':'page-heading'}).text
                except Exception as exception: pass

for x,y in Brand1.items():
    if len(y[0]) is 5 or len(y[0]) is 6:
        Brand1[x].insert(0,"Add New Brand")
    if len(Brand1[x]) is 6:
        Brand1[x].insert(7 ,"BE")
    if len(Brand1[x]) is 8:
        del Brand1[x][5]


for x,y in Brand2.items():
    if len(y[0]) is 5 or len(y[0]) is 6:
        Brand2[x].insert(0,"Add New Brand")
    if len(Brand2[x]) is 6:
        Brand2[x].insert(7 ,"BE")
    if len(Brand2[x]) is 8:
        del Brand2[x][5]
        
for x,y in Brand3.items():
    if len(y[0]) is 5 or len(y[0]) is 6:
        Brand3[x].insert(0,"Add New Brand")
    if len(Brand3[x]) is 6:
        Brand3[x].insert(7 ,"BE")
    if len(Brand3[x]) is 8:
        del Brand3[x][5]
        
for x,y in Brand4.items():
    if len(y[0]) is 5 or len(y[0]) is 6:
        Brand4[x].insert(0,"Add New Brand")
    if len(Brand4[x]) is 6:
        Brand4[x].insert(7 ,"BE")
    if len(Brand4[x]) is 8:
        del Brand4[x][5]
        
for x,y in Brand5.items():
    if len(y[0]) is 5 or len(y[0]) is 6:
        Brand5[x].insert(0,"Add New Brand")
    if len(Brand5[x]) is 6:
        Brand5[x].insert(7 ,"BE")
    if len(Brand5[x]) is 8:
        del Brand5[x][5]
        
for x,y in Brand6.items():
    if len(y[0]) is 5 or len(y[0]) is 6:
        Brand6[x].insert(0,"Add New Brand")
    if len(Brand6[x]) is 6:
        Brand6[x].insert(7 ,"BE")
    if len(Brand6[x]) is 8:
        del Brand6[x][5]
for x,y in Brand7.items():
    if len(y[0]) is 5 or len(y[0]) is 6:
        Brand7[x].insert(0,"Add New Brand")
    if len(Brand7[x]) is 6:
        Brand7[x].insert(7 ,"BE")
    if len(Brand7[x]) is 8:
        del Brand7[x][5]
for x,y in Brand8.items():
    if len(y[0]) is 5 or len(y[0]) is 6:
        Brand8[x].insert(0,"Add New Brand")
    if len(Brand8[x]) is 6:
        Brand8[x].insert(7 ,"BE")
    if len(Brand8[x]) is 8:
        del Brand8[x][5]
for x,y in Brand9.items():
    if len(y[0]) is 5 or len(y[0]) is 6:
        Brand9[x].insert(0,"Add New Brand")
    if len(Brand9[x]) is 6:
        Brand9[x].insert(7 ,"BE")
    if len(Brand9[x]) is 8:
        del Brand9[x][5]
for x,y in Brand10.items():
    if len(y[0]) is 5 or len(y[0]) is 6:
        Brand10[x].insert(0,"Add New Brand")
    if len(Brand10[x]) is 6:
        Brand10[x].insert(7 ,"BE")
    if len(Brand10[x]) is 8:
        del Brand10[x][5]
for x,y in Brand11.items():
    if len(y[0]) is 5 or len(y[0]) is 6:
        Brand11[x].insert(0,"Add New Brand")
    if len(Brand11[x]) is 6:
        Brand11[x].insert(7 ,"BE")
    if len(Brand11[x]) is 8:
        del Brand11[x][5]
for x,y in Brand12.items():
    if len(y[0]) is 5 or len(y[0]) is 6:
        Brand12[x].insert(0,"Add New Brand")
    if len(Brand12[x]) is 6:
        Brand12[x].insert(7 ,"BE")
    if len(Brand12[x]) is 8:
        del Brand12[x][5]
for x,y in Brand13.items():
    if len(y[0]) is 5 or len(y[0]) is 6:
        Brand13[x].insert(0,"Add New Brand")
    if len(Brand13[x]) is 6:
        Brand13[x].insert(7 ,"BE")
    if len(Brand13[x]) is 8:
        del Brand13[x][5]
for x,y in Brand14.items():
    if len(y[0]) is 5 or len(y[0]) is 6:
        Brand14[x].insert(0,"Add New Brand")
    if len(Brand14[x]) is 6:
        Brand14[x].insert(7 ,"BE")
    if len(Brand14[x]) is 8:
        del Brand14[x][5]

locnamearray = [locname]
timedfarray = [timedf]
latarray = [lat]
lngarray = [lng]
namearray = [name]
Brand1array = [Brand1][0]
Brand2array = [Brand2][0]
Brand3array = [Brand3][0]
Brand4array = [Brand4][0]
Brand5array = [Brand5][0]
Brand6array = [Brand6][0]
Brand7array = [Brand7][0]
Brand8array = [Brand8][0]
Brand9array = [Brand9][0]
Brand10array = [Brand10][0]
Brand11array = [Brand11][0]
Brand12array = [Brand12][0]
Brand13array = [Brand13][0]
Brand14array = [Brand14][0]

locnamearraydf1 = pd.DataFrame(locnamearray)
timedfarraydf1 = pd.DataFrame(timedfarray)
latarraydf1 = pd.DataFrame(latarray)
lngarraydf1 = pd.DataFrame(lngarray)
namearraydf1 = pd.DataFrame(namearray)
Brand11arraydf =  pd.DataFrame(Brand1array)
Brand21arraydf =  pd.DataFrame(Brand2array)
Brand31arraydf =  pd.DataFrame(Brand3array)
Brand41arraydf =  pd.DataFrame(Brand4array)
Brand51arraydf =  pd.DataFrame(Brand5array)
Brand61arraydf =  pd.DataFrame(Brand6array)
Brand71arraydf =  pd.DataFrame(Brand7array)
Brand81arraydf =  pd.DataFrame(Brand8array)
Brand91arraydf =  pd.DataFrame(Brand9array)
Brand101arraydf =  pd.DataFrame(Brand10array)
Brand111arraydf =  pd.DataFrame(Brand11array)
Brand121arraydf =  pd.DataFrame(Brand12array)
Brand131arraydf =  pd.DataFrame(Brand13array)
Brand141arraydf =  pd.DataFrame(Brand14array)

Brand1arraydf =  Brand11arraydf.T
Brand2arraydf =  Brand21arraydf.T
Brand3arraydf =  Brand31arraydf.T
Brand4arraydf =  Brand41arraydf.T
Brand5arraydf =  Brand51arraydf.T
Brand6arraydf =  Brand61arraydf.T
Brand7arraydf =  Brand71arraydf.T
Brand8arraydf =  Brand81arraydf.T
Brand9arraydf =  Brand91arraydf.T
Brand10arraydf =  Brand101arraydf.T
Brand11arraydf =  Brand111arraydf.T
Brand12arraydf =  Brand121arraydf.T
Brand13arraydf =  Brand131arraydf.T
Brand14arraydf =  Brand141arraydf.T

timedfarraydf = timedfarraydf1.T
lngarraydf = lngarraydf1.T
latarraydf = latarraydf1.T
namearraydf = namearraydf1.T
locnamearraydf = locnamearraydf1.T



DateDF = timedfarraydf
DateDF['Submissions_Url'] = DateDF.index
DateDF.columns = ['Date', 'Submission_Url']
LongitudeDF = lngarraydf
LongitudeDF['Submission_Url'] = LongitudeDF.index
LongitudeDF.columns = ['Lng','Submission_Url']
LatitudeDF = latarraydf
LatitudeDF['Submission_Url'] = LatitudeDF.index
LatitudeDF.columns = ['Lat','Submission_Url']
UserNameDF = namearraydf
UserNameDF['Submission_Url'] = UserNameDF.index
UserNameDF.columns = ['User','Submission_Url']
UserNameDF.reset_index(drop=True, inplace=True)
UserNameDF["Submission_Url"] = UserNameDF["Submission_Url"].str.partition("#", True)[2]
LocationNameDF = locnamearraydf
LocationNameDF['Submission_Url'] = LocationNameDF.index
LocationNameDF.columns = ['Location','Submission_Url']
LocationNameDF.reset_index(drop=True, inplace=True)
LocationNameDF["Submission_Url"] = LocationNameDF["Submission_Url"].str.partition("#", True)[2]
Brand1DataFrame = Brand1arraydf
Brand1DataFrame['Submission_Url'] = Brand1DataFrame.index
Brand1DataFrame.columns = ['Submission_Url','Add','Brand', 'Style', 'Size', 'Size2', 'Size3','Price']
Brand1DataFrame.reset_index(drop=True, inplace=True)
Brand1DataFrame["Submission_Url"] = Brand1DataFrame["Submission_Url"].str.partition("#", True)[2]
Brand2DataFrame = Brand2arraydf
Brand2DataFrame.reset_index()
Brand2DataFrame.columns = ['Submission_Url','Add','Brand', 'Style', 'Size', 'Size2', 'Size3','Price']
Brand2DataFrame["Submission_Url"] = Brand2DataFrame["Submission_Url"].str.partition("#", True)[2]
Brand3DataFrame = Brand3arraydf
Brand3DataFrame.reset_index()
Brand3DataFrame.columns = ['Submission_Url','Add','Brand', 'Style', 'Size', 'Size2', 'Size3','Price']
Brand3DataFrame["Submission_Url"] = Brand3DataFrame["Submission_Url"].str.partition("#", True)[2]
Brand4DataFrame = Brand4arraydf
Brand4DataFrame.reset_index()
Brand4DataFrame.columns = ['Submission_Url','Add','Brand', 'Style', 'Size', 'Size2', 'Size3','Price']
Brand4DataFrame["Submission_Url"] = Brand4DataFrame["Submission_Url"].str.partition("#", True)[2]
Brand5DataFrame = Brand5arraydf
Brand5DataFrame.reset_index()
Brand5DataFrame.columns = ['Submission_Url','Add','Brand', 'Style', 'Size', 'Size2', 'Size3','Price']
Brand5DataFrame["Submission_Url"] = Brand5DataFrame["Submission_Url"].str.partition("#", True)[2]
Brand6DataFrame = Brand6arraydf
Brand6DataFrame.reset_index()
Brand6DataFrame.columns = ['Submission_Url','Add','Brand', 'Style', 'Size', 'Size2', 'Size3','Price']
Brand6DataFrame["Submission_Url"] = Brand6DataFrame["Submission_Url"].str.partition("#", True)[2]
Brand7DataFrame = Brand7arraydf
Brand7DataFrame.reset_index()
Brand7DataFrame.columns = ['Submission_Url','Add','Brand', 'Style', 'Size', 'Size2', 'Size3','Price']
Brand7DataFrame["Submission_Url"] = Brand7DataFrame["Submission_Url"].str.partition("#", True)[2]

Brand8DataFrame = Brand8arraydf
Brand8DataFrame.reset_index()
Brand8DataFrame.columns = ['Submission_Url','Add','Brand', 'Style', 'Size', 'Size2', 'Size3','Price']
Brand8DataFrame["Submission_Url"] = Brand8DataFrame["Submission_Url"].str.partition("#", True)[2]
Brand9DataFrame = Brand9arraydf
Brand9DataFrame.reset_index()
Brand9DataFrame.columns = ['Submission_Url','Add','Brand', 'Style', 'Size', 'Size2', 'Size3','Price']
Brand9DataFrame["Submission_Url"] = Brand9DataFrame["Submission_Url"].str.partition("#", True)[2]
Brand10DataFrame = Brand10arraydf
Brand10DataFrame.reset_index()
Brand10DataFrame.columns = ['Submission_Url','Add','Brand', 'Style', 'Size', 'Size2', 'Size3','Price']
Brand10DataFrame["Submission_Url"] = Brand10DataFrame["Submission_Url"].str.partition("#", True)[2]
Brand11DataFrame = Brand11arraydf
Brand11DataFrame.reset_index()
Brand11DataFrame.columns = ['Submission_Url','Add','Brand', 'Style', 'Size', 'Size2', 'Size3','Price']
Brand11DataFrame["Submission_Url"] = Brand11DataFrame["Submission_Url"].str.partition("#", True)[2]
Brand12DataFrame = Brand12arraydf
Brand12DataFrame.reset_index()
Brand12DataFrame.columns = ['Submission_Url','Add','Brand', 'Style', 'Size', 'Size2', 'Size3','Price']
Brand12DataFrame["Submission_Url"] = Brand12DataFrame["Submission_Url"].str.partition("#", True)[2]
Brand13DataFrame = Brand13arraydf
Brand13DataFrame.reset_index()
Brand13DataFrame.columns = ['Submission_Url','Add','Brand', 'Style', 'Size', 'Size2', 'Size3','Price']
Brand13DataFrame["Submission_Url"] = Brand13DataFrame["Submission_Url"].str.partition("#", True)[2]
Brand14DataFrame = Brand14arraydf
Brand14DataFrame.reset_index()
Brand14DataFrame.columns = ['Submission_Url','Add','Brand', 'Style', 'Size', 'Size2', 'Size3','Price']
Brand14DataFrame["Submission_Url"] = Brand14DataFrame["Submission_Url"].str.partition("#", True)[2]




DateDF.to_csv('DateDF.csv')

LongitudeDF.to_csv('LongDF.csv')

LatitudeDF.to_csv('LatDF.csv')

UserNameDF.to_csv('UserNameDF.csv')

LocationNameDF.to_csv('LocationName.csv')

Brand1DataFrame.to_csv('Brand1.csv')

Brand2DataFrame.to_csv('Brand2.csv')

Brand3DataFrame.to_csv('Brand3.csv')

Brand4DataFrame.to_csv('Brand4.csv')

Brand5DataFrame.to_csv('Brand5.csv')

Brand6DataFrame.to_csv('Brand6.csv')

Brand7DataFrame.to_csv('Brand7.csv')


Brand8DataFrame.to_csv('Brand8.csv')

Brand9DataFrame.to_csv('Brand9.csv')

Brand10DataFrame.to_csv('Brand10.csv')

Brand11DataFrame.to_csv('Brand11.csv')

Brand12DataFrame.to_csv('Brand12.csv')


Brand14DataFrame.to_csv('Brand14.csv')


        