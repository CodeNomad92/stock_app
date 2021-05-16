import yfinance as yf
import streamlit as st
import pandas as pd

st.write(""" # Simple Stock App

Shown below are the stocks of dogecoin and closing value

""")
tickerSymbol = 'DOGE-INR'
tickerData = yf.Ticker(tickerSymbol)

tickerDf =tickerData.history(period ='1d',start='2020-1-1' , end='2021-5-15')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)