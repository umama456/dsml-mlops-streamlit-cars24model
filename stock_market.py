import streamlit as st 
import pandas as pd 
import yfinance as yf 


st.title('Stock Market App')

st.write('This is the stock price of TESLA ')
st.write('website created by Umaa using streamlit ')

ticker_symbol= st.text_input('enter the stock ticker symbol', 'TSLA')

ticker_data = yf.Ticker(ticker_symbol) 

start_date = st.date_input("Enter the starting date", value= pd.to_datetime("2023-01-10" ))

end_date = st.date_input("Enter the ending date", value=pd.to_datetime("today" ))

hist = ticker_data.history(start=start_date, end=end_date) 

st.write('Please go through the stock prices of tesla')

st.write(hist) 

# st.write('This plot is for volume of the stock')

# st.line_chart(hist.Volume)

# st.write('This plot is for price of the stock')

# st.line_chart(hist.Close) 

import streamlit as st

col1, col2 = st.columns(2)

with col1:
   st.write("This plot is for volume of the stock")
   st.line_chart(hist.Volume)

with col2:
   st.write("This plot is for price of the stock")
   st.line_chart(hist.Close) 

