# ETL_Francisco_Ian_Scotty
Hello! 

This document will serve as a repository for our ETL Project.

To collect our data, which is on a website without an API, we began by web scraping. What we were we scraping was audits of stores around Latin America and the United States. Each audit correspondes to a type of audit. Either the focus was on many different brands, their presence, or price in each store. Or, the foucs would be on one particular brand. An audit correspondes to one particular person's data entry. So for one country there could be 2 different types of audits and 50 submissions for each one. 

The actual webpage for these individual audits to be scraped follow a url path that correlates to the ID of the audit. For isntance; https://maxianetpe.campodata.com/submissions/2624230/webview

2624230 is the audit number.

So the first thing we wanted to do is to go to the homepage where a table of all audit ID's were available. We scrape this page and return a CSV file correlating to ScrapeidUnitedStates.py and IntlID's.csv respectively. We then take this CSV and read it into our individual looping python file: ScrapeEachSubmission.py. By looping through this list and appending each ID to the redirect page in the session we create a DataFrame of scraped values correlating to the ID. This is then saved to USBeerMarket.csv. Now that we have collected the data we want to transform it.

After each collection process we clean up the Dataframes in the same python file. For instance, USBeerMarket.csv looked a lot different than before. Most of the clean up had to do with null values, and certain individual pages missing information. 

After this we wanted to turn the csv file into a json format for easy upload to MongoDB. This is done at csvtojson.py. 

Then we want to push it to MongoDB: sendtomongoEc.py originally pushed the U.S data, and once that was pushed it was changed to push the Ecuador data. since, it was not able to connect I pushed the file via terminal. You can take a look at the images of the DataBase by refferring to the two screenshot png's.

We then repeated this process for Ecuador. 

To collect ID's : ScrapeIDUnitedStates.py and return EcuadorIDs.csv. (The python loops through all countries)

To scrape individual: ScrapeEcuador.ipnyb return Ecuador.csv

To change to json: ecuadortojson.py

To push: SendtoMongoEC.py.

That wraps it up. 



