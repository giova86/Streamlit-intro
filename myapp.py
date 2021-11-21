import yfinance as yf
import streamlit as st
import pandas as pd
import datetime
import altair as alt
import time



st.write("""
# My first APP

This is the first app in streamlit showing the stock **Closing** price and **Volume**
"""
)

option = st.sidebar.selectbox(
'How would you like to be contacted?',
('GOOGL', 'AAPL', 'TSLA', 'FB', 'TSM', 'HD', 'JNJ'))

start = st.sidebar.date_input(
    "Select Start Period",
    datetime.date(2019, 7, 6))

stop = st.sidebar.date_input(
    "Select Stop Period",
    datetime.date.today())
st.write(f'Stock price from {start} to {stop}')

tickerData = yf.Ticker(option)
tickerDF = tickerData.history(period='id',start=start, end=stop)

st.write('You selected:', option)

col1, col2 = st.columns(2)
with col1:
    st.line_chart(tickerDF.Close)
with col2:
    st.line_chart(tickerDF.Volume)



c = alt.Chart(tickerDF).mark_circle().encode(
    x='Close',
    y='Volume',
    size='Volume',
    color='Volume',
    #tooltip=['a', 'b', 'c']
    )
st.altair_chart(c, use_container_width=True)
