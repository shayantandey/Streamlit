import streamlit as st
import yfinance as yf
import datetime as dt

st.title("Stock Price Analysis")
st.subheader("Analyze and visualize stock prices over time.")
st.subheader(
    "This app allows you to input a stock ticker symbol and view its historical price data.")
# ticker = yf.Ticker("MSFT")


# ticker_data = ticker.history(period="1y")
col1, col2, col3 = st.columns(3)

with col1:
    ticker = st.text_input(
        "Enter a stock ticker", "MSFT")
ticker = yf.Ticker(ticker)
with col2:
    start_date = st.date_input(
        "Start date", dt.date.today() - dt.timedelta(days=365))

with col3:
    end_date = st.date_input("End date", dt.date.today())

ticker_data = ticker.history(start=start_date, end=end_date)
st.write("### Historical Price Data for")
st.write(ticker_data)

st.subheader("Visualize Stock Price Data")
st.line_chart(ticker_data['Close'])

st.subheader("Volume Movement")
st.bar_chart(ticker_data['Volume'])
