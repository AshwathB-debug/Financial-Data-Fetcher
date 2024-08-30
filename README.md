# Stock Information Project


## Project Description
The Stock Information Project is designed to help investors in retrieving comprehensive financial data on companies based in the US which could be highly beneficial when making decisions on whether or not to buy, sell, or hold a stock. It leverages the Alpha Vantage API to fetch data and send the data to the user as an email with a CSV file attachment. 


## Features
1. Data Retrieval: The project retrieves data from the Alpha Vantage API leveraging requests to access the data and writes it to a CSV file.
2. API key security: The project utilizes an environment file to encrypt the API key from landing into the wrong hands.
3. Email functionality: Sends an email with a file attachment to a person utilizing the smptlib module. 
4. User assistance: If the user needs help, there is a help function and another function that leads them to the Nasdaq website to find stock tickers and guide the user.


## Usage
If you'd like to run the project on your own, follow these steps:
1. Clone the repository or download the files
2. Install the required modules utilizing the requirements.txt file. Copy the line below and paste it into your terminal:
   pip install -r requirements.txt 


## Learning Resources
1. Email functionality: Gained insights on sending emails in Python from this tutorial: https://www.youtube.com/watch?v=ueqZ7RL8zxM&t=199s
2. Sending attachments through emails: Applied concepts of sending email attachments through this tutorial: https://www.youtube.com/watch?v=Sddnn6dpqk0
3. Alpha Vantage API documentation website: Developed using guidance from: https://www.alphavantage.co/documentation/