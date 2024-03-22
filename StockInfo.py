import pandas as pd
import os
from dotenv import load_dotenv
import webbrowser


def helpUser():
    countries = ["United States", "United Kingdom", "Canada", "Germany", "India", "Mainland China", "France", "Spain", "Portugal", "Hong Kong", "Brazil", "South Africa", "Japan", "Mexico"]
    print("To find a companies stock ticker, refer to this website: " + webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open_new("https://finance.yahoo.com/"))
    print(f"The countries in our database are {countries}. ")
    print("The type of investments in our database are: \n 1. Equity\n 2. Mutual Fund. ")


def listOfCountries(country):
    countries = ["United States", "United Kingdom", "Canada", "Germany", "India", "Mainland China", "France", "Spain", "Portugal", "Hong Kong", "Brazil", "South Africa", "Japan", "Mexico"]
    return country in countries
    
    
def stockInfo(APIkey, ticker, countryName, typeOfInvestment):
    link = f"https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={ticker}&apikey={APIkey}&datatype=csv"
    df = pd.read_csv(link)

    try:
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
        
    try:
        print("Welcome to my stock information terminal! If you need any help, refer to the helpUser function to get more information. Thank you! ")
        
        ticker = input("Enter stock ticker: ").strip().upper()
        countryName = input("Enter the name of the country (Please enter the full name of the country): ").strip().title()
        
        if listOfCountries(countryName):
            print("The country exists in our database! ")
            
            typeOfInvestment = input("Enter the type of investment: ").strip().title()
            
            if (typeOfInvestment == "Equity" or typeOfInvestment == "Mutual Fund"):
                print("The type of investment you entered exists! ")
                
                minsOrDays = input(f"Would you like to see {ticker}'s stock history by Mins or Days? (Please type minutes as mins) ").strip().title()
                
                if minsOrDays == "Mins":
                    minutes = int(input(f"Enter the number of mins you would like to see for {ticker}'s previous data (Please enter 1, 5, 15, 30, or 60 mins as those are supported): "))
                    print(stockInfo(APIkey, ticker, countryName, typeOfInvestment))
                    print(stockDataByMins(APIkey, ticker, minutes))
                    
                elif minsOrDays == "Days":
                    days = int(input(f"Enter the number of days to see more about {ticker}'s price: "))
                    print(stockInfo(APIkey, ticker, countryName, typeOfInvestment))
                    print(stockDataByDays(APIkey, ticker, days))
                    
                else:
                    helpUser()
                    print("Please type Mins or Days. ")
                    
            else:
                helpUser()
                print("The type of investment doesn't exist in our database. Please try again. Refer to the help function. ")
        
        else:
            helpUser()
            print("The country doesn't exist in our database. Please try again. Refer to the help function. ")
            
    except:
        print("You have called the API too many times. Please try again later")