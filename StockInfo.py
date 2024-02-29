import pandas as pd
import os
from dotenv import load_dotenv
import sys


def listOfCountries(country):
    countries = ["United States", "United Kingdom", "Canada", "Germany", "India", "Mainland China", "France", "Spain", "Portugal", "Hong Kong", "Brazil", "South Africa", "Japan", "Mexico"]
    return country in countries


# def marketStatus(APIkey, countryName):
#     link = f"https://www.alphavantage.co/query?function=MARKET_STATUS&apikey={APIkey}"
#     status = pd.read_csv(link)
    
    
#     try:
#         if listOfCountries(countryName):
#             return status["current_status"].iloc[0]
#         else:
#             return f"The country {countryName}, doesn't exist in our database."
#     except:
#         print("Error fetching market status. You may have called the API too many times. Try again later. ")
#         return None
    
    
def stockInfo(APIkey, ticker, countryName, typeOfInvestment):
    link = f"https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={ticker}&apikey={APIkey}&datatype=csv"
    df = pd.read_csv(link)

    try:
        if listOfCountries(countryName) == True and (typeOfInvestment == "Equity" or typeOfInvestment == "Mutual Fund"):
            return df[(df["region"] == countryName) & (df["type"] == typeOfInvestment)]
    except:
        return "The ticker, country, or type of investment you entered does not exist in our database. Please check for incorrect spelling or spaces. Refer to the help command for any doubts. "

    
    
def stockDataByMins(APIkey, ticker, mins):
    link = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval={mins}min&apikey={APIkey}&datatype=csv"
    stock = pd.read_csv(link)
    
    try:
        return stock.head(mins)
    except:
        return "Error fetching stock data. You may have called the API too many times. Try again later. "
    

def stockDataByDays(APIkey, ticker, days):
    link = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&outputsize=full&apikey={APIkey}&datatype=csv"
    stock = pd.read_csv(link)
    
    try:
        return stock.head(days)
    except:
        return "Error fetching stock data. You may have called the API too many times. Try again later. "


if __name__ == "__main__":
    load_dotenv()
    APIkey = os.getenv("API_key")
        
    ticker = input("Enter stock ticker: ").strip().upper()
    countryName = input("Enter the name of the country: ").strip().title()
    typeOfInvestment = input("Enter the type of investment: ").strip().title()
    minsOrDays = input(f"Would you like to see {ticker}'s stock history by mins or days? ").strip().title()
    
        
    try: 
        if minsOrDays == "Mins":
            # print(marketStatus(APIkey, countryName))
            minutes = int(input(f"Enter the number of mins you would like to see for {ticker}'s previous data (Please enter 1, 5, 15, 30, or 60 mins as those are supported): "))
            print(stockInfo(APIkey, ticker, countryName, typeOfInvestment))
            print(stockDataByMins(APIkey, ticker, minutes))
        elif minsOrDays == "Days":
            # print(marketStatus(APIkey, countryName))
            days = int(input(f"Enter the number of days to see more about {ticker}'s price: "))
            print(stockInfo(APIkey, ticker, countryName, typeOfInvestment))
            print(stockDataByDays(APIkey, ticker, days))
        else:
            print("Please type Today or Past. ")
          
    except:
        print("You have called the API too many times. Please try again later")
    
    