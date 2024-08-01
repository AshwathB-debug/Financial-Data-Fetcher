# Importing the necessary modules and libraries to access the API and provide the user with quality information
import pandas as pd
import os
from dotenv import load_dotenv
import webbrowser
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders



# Upon calling this function, it will direct the user to the Nasdaq stock screener website with which they can look for a companies
def openWebsite():
    
    webbrowser.open_new("https://www.nasdaq.com/market-activity/stocks/screener")
    print("To find a companies stock ticker, refer to this website: https://www.nasdaq.com/market-activity/stocks/screener ")


# This function is used to support the user if they are lost or need to refer to something to use the Stock information terminal. 
def helpUser():
    
    return """
          "The functions you can write are the following: ["OVERVIEW", "INCOME_STATEMENT", "BALANCE_SHEET", "CASH_FLOW", "EARNINGS"]
           The stock ticker can be any company you like but if you want more information on a stock, use the link to the Nasdaq stock screener provided.
           The two types of investments you can give as input: 
                1. Equity
                2. Mutual Fund
           Once you have entered the appropriate information, you can access the data in the csv file called stock_data.csv.
           Thank you for using the Stock information terminal!
           """
 
    
# This function has an array of the different functions the user can choose from to get information about a stock. 
def listOfFunctions(function):
    
    arrOfFunctions = ["OVERVIEW", "INCOME_STATEMENT", "BALANCE_SHEET", "CASH_FLOW", "EARNINGS"]
    return function in arrOfFunctions


# This function is used to pass in the ticker symbol and type of investment to find the stock ticker and return it.
def stockInfo(APIkey, ticker, typeOfInvestment):
    
    link = f"https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={ticker}&apikey={APIkey}&datatype=csv"
    df = pd.read_csv(link)
    
    
    try:
        if df[df["symbol"] == ticker] & df[df["type"] == typeOfInvestment]:
            return "The stock ticker exists! "
        else:
            return "The ticker, country, or type of investment you entered does not exist in our database. Please check for incorrect spelling or spaces. Refer to the help command for any doubts."
        
    except:
        return "You have used the stockInfo function too many times. Please try again later. "


# This function reads the link using Python's requests module and writes the data from the link into a csv file and returns it

stock_data = "stock_data.csv"

def companyInfo(FUNCTION, ticker, APIkey):
    
    link = f"https://www.alphavantage.co/query?function={FUNCTION}&symbol={ticker}&apikey={APIkey}"
    
    try:

        r = requests.get(link)
        r.raise_for_status()
        
        with open(stock_data, "wb") as file:
            file.write(r.content)
        sendEmail(stock_data)
        return f"The CSV file for the ticker you entered has been created successfully: {stock_data}"
        
    except Exception as e:
        return f"An unexpected error occurred: {e}"
    

def sendEmail(stock_data):
    
    load_dotenv()
    password = os.getenv("app_password")
    
    sender = input("SENDER EMAIL: ")
    receiver = input("RECEIVER EMAIL: ")
    subject = input("SUBJECT: ")
    
    
    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = subject
    
    file = open(stock_data, "rb")
    
    
    # To encode it in base 64
    file_package = MIMEBase("application", "octet-stream")
    file_package.set_payload((file).read())
    encoders.encode_base64(file_package)
    file_package.add_header("Content-Disposition", "attachment; filename= " + stock_data)
    message.attach(file_package)
    
    text = message.as_string()
    
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login(sender, password)
    s.sendmail(sender, receiver, text)
        
    return f"Email has been sent to {receiver}! "


# The main function executes the functions and accesses the API key to get all the information from Alpha Vantage's website 
  
if __name__ == "__main__":
    load_dotenv()
    APIkey = os.getenv("API_key")
        
    try:
        print("Welcome to my stock information terminal! If you need any help, refer to the helpUser function to get more information. Thank you! ")
        askUser = input("Do you want to refer to the Nasdaq stock screener website to get a companies stock ticker? (Respond with Y or N or N/A (To access the help function)): ").strip().title()
        
        if askUser == "Y":
            openWebsite()
            
        elif askUser == "N":
            nameOfFunction = input("Enter the name of the function: ").strip().upper()
            
            if listOfFunctions(nameOfFunction):
                print("The function exists! ")
                
                ticker = input("Enter stock ticker (Refer to Nasdaq stock screener website if you are not sure: https://www.nasdaq.com/market-activity/stocks/screener): ").strip().upper()
                    
                typeOfInvestment = input("Enter the type of investment: ").strip().title()
                
                print(stockInfo(APIkey, ticker, typeOfInvestment))
                print(companyInfo(nameOfFunction, ticker, APIkey))   
                    
            else:
                print("The function you typed is incorrect. Please refer to the help function. ")
        
        elif askUser == "N/A":
            print(helpUser())
            
        else:
            print("Please type Y or N, or refer to the help function. ")
            
    except:
        print("You have called the API too many times. Please try again later")