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
newvariablesPeru = newvariablesPeru.drop("Unnamed: 0", axis=1, inplace = False)
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
    newvariablesPeru.dropna(how ='all', inplace = True)
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
        r = s.get(u, headers=headers)
        soup = BeautifulSoup(r.content, 'html5lib')
        login_data['authenticity_token'] = soup.find('input', attrs={'name': 'authenticity_token'})['value']
        if u is 'https://maxianetintl.campodata.com/sessions':
            for weburls,weburl in zip(newvariablesIntl['ID'],newvariablesIntl['Form']):
                if weburl == 'Brand Price Audit': 
                    login_data['user[redirect_to]'] = f'{weburls}'
                    r2 = s.post(u, data=login_data,headers=headers)
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


timedfarraydf = timedfarraydf1.T
lngarraydf = lngarraydf1.T
latarraydf = latarraydf1.T
namearraydf = namearraydf1.T
locnamearraydf = locnamearraydf1.T

listofBr = [Brand1array, Brand2array, Brand3array, Brand4array, Brand5array, Brand6array, Brand7array, Brand8array, Brand9array, Brand10array, Brand11array, Brand12array, Brand13array, Brand14array]         
          Brand1array1 = {}
Brand2array1 ={}
Brand3array1 ={}
Brand4array1 ={}
Brand5array1 ={}
Brand6array1 ={}
Brand7array1 ={}
Brand8array1 ={}
Brand9array1 ={}
Brand10array1 ={}
Brand11array1 ={}
Brand12array1 ={}
Brand13array1 ={}
Brand14array1={}
listofBr2 = [Brand1array1, Brand2array1, Brand3array1, Brand4array1, Brand5array1, Brand6array1, Brand7array1, Brand8array1, Brand9array1, Brand10array1, Brand11array1, Brand12array1, Brand13array1, Brand14array1]      
listofdf = [locnamearraydf, timedfarraydf, latarraydf, lngarraydf, namearraydf]
LocationDF = {}
TimeDF = {}
LatDF = {}
LngDF = {}
NameDF = {}
listofdftosaveto = [LocationDF, TimeDF, LatDF, LngDF, NameDF]

for Brand in listofBr:
    for row in Brand:
        if Brand[row][0] != 'Add New Brand':
            Brand[row].insert(0, 'Add New Brand')
for Brand in listofBr:
        for row in Brand: 
            if len(Brand[row]) == 6:
                Brand[row].insert(5, 'Qty Unknown')

for Brand in listofBr:
    for row in Brand:
        if len(Brand[row]) != 7:
            print(Brand[row])

for (dframe,dframey) in zip(listofBr,listofBr2):
    dframe = pd.DataFrame(dframe)
    dframe = dframe.T
    listy = dframe.index.tolist()
    numberindf = 0
    numbertoappend = 0
    for row in listy:
        row = row.partition('submissions/')[2]
        row = row.partition('/')[0]
        dframey[str(row)] = [dframe[0][numberindf],dframe[1][numberindf], dframe[2][numberindf], dframe[3][numberindf], dframe[4][numberindf], dframe[5][numberindf], dframe[6][numberindf]]
        numberindf = numberindf + 1

for (dframe,dframey) in zip(listofdf,listofdftosaveto):
    listy = dframe.index.tolist()
    numberindf = 0
    numbertoappend = 0
    for row in listy:
        row = row.partition('submissions/')[2]
        row = row.partition('/')[0]
        dframey[str(row)] = [dframe[0][numberindf]]
        numberindf = numberindf + 1
        
LocationDF = pd.DataFrame(LocationDF)
LocationDF = LocationDF.T
LocationDF.columns = ['Location']
TimeDF = pd.DataFrame(TimeDF)
TimeDF = TimeDF.T
TimeDF.columns = ['Time_of_Submission']
LatDF = pd.DataFrame(LatDF)
LatDF = LatDF.T
LatDF.columns = ['Latitude']
NameDF = pd.DataFrame(NameDF)
NameDF = NameDF.T
NameDF.columns = ['Auditor']
LngDF = pd.DataFrame(LngDF)
LngDF = LngDF.T
LngDF.columns = ['Longitude']      

Brand1array1 = pd.DataFrame(Brand1array1)
Brand1array1 = Brand1array1.T
Brand1array1.columns = ['Add', 'Brand', 'Product', 'Size','Measurement', 'Qty', 'Price1']
Brand2array1 = pd.DataFrame(Brand2array1)
Brand2array1 = Brand2array1.T
Brand2array1.columns = ['Add2', 'Brand2', 'Product2', 'Size2','Measurement2', 'Qty2', 'Price2']
Brand3array1 = pd.DataFrame(Brand3array1)
Brand3array1 = Brand3array1.T
Brand3array1.columns = ['Add3', 'Brand3', 'Product3', 'Size3','Measurement3', 'Qty3', 'Price3']
Brand4array1 = pd.DataFrame(Brand4array1)
Brand4array1 = Brand4array1.T
Brand4array1.columns = ['Add4', 'Brand4', 'Product4', 'Size4','Measurement4', 'Qty4', 'Price4']
Brand5array1 = pd.DataFrame(Brand5array1)
Brand5array1 = Brand5array1.T
Brand5array1.columns = ['Add5', 'Brand5', 'Product5', 'Size5','Measurement5', 'Qty5', 'Price5']
Brand6array1 = pd.DataFrame(Brand6array1)
Brand6array1 = Brand6array1.T
Brand6array1.columns = ['Add6', 'Brand6', 'Product6', 'Size6','Measurement6', 'Qty6', 'Price6']
Brand7array1 = pd.DataFrame(Brand7array1)
Brand7array1 = Brand7array1.T
Brand7array1.columns = ['Add7', 'Brand7', 'Product7', 'Size7','Measurement7', 'Qty7', 'Price7']
Brand8array1 = pd.DataFrame(Brand8array1)
Brand8array1 = Brand8array1.T
Brand8array1.columns = ['Add8', 'Brand8', 'Product8', 'Size8','Measurement8', 'Qty8', 'Price8']
Brand9array1 = pd.DataFrame(Brand9array1)
Brand9array1 = Brand9array1.T
Brand9array1.columns = ['Add9', 'Brand9', 'Product9', 'Size9','Measurement9', 'Qty9', 'Price9']
Brand10array1 = pd.DataFrame(Brand10array1)
Brand10array1 = Brand10array1.T
Brand10array1.columns = ['Add10', 'Brand10', 'Product10', 'Size10','Measurement10', 'Qty10', 'Price10']
Brand11array1 = pd.DataFrame(Brand11array1)
Brand11array1 = Brand11array1.T
Brand11array1.columns = ['Add11', 'Brand11', 'Product11', 'Size11','Measurement11', 'Qty11', 'Price11']
Brand12array1 = pd.DataFrame(Brand12array1)
Brand12array1 = Brand12array1.T
Brand12array1.columns = ['Add12', 'Brand12', 'Product12', 'Size12','Measurement12', 'Qty12', 'Price12']
Brand13array1 = pd.DataFrame(Brand13array1)
Brand13array1 = Brand13array1.T
Brand13array1.columns = ['Add13', 'Brand13', 'Product13', 'Size13','Measurement13', 'Qty13', 'Price13']
Brand14array1 = pd.DataFrame(Brand14array1)
Brand14array1 = Brand14array1.T
Brand14array1.columns = ['Add14', 'Brand14', 'Product14', 'Size14','Measurement14', 'Qty14', 'Price14']

USBeerMarket = LocationDF.join([TimeDF,LatDF,LngDF, NameDF])

USBeerMarketBrands = Brand1array1.join([Brand2array1, Brand3array1, Brand4array1, Brand5array1, Brand6array1, Brand7array1, Brand8array1, Brand9array1, Brand10array1, Brand11array1, Brand12array1, Brand13array1, Brand14array1])

USBeerMarket.to_csv('USBeerMarket.csv')
USBeerMarketBrands.to-csv('USBeerMarketBrands.csv')