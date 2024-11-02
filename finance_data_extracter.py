# Save this script as app.py
import streamlit as st
import yfinance as yf
import pandas as pd

# Title for the app
st.title("Yahoo Finance Data Extractor")

# Input fields for ticker, start date, end date, and interval
ticker = st.text_input("Enter stock ticker (e.g., AAPL, SPY):", "SPY")
start_date = st.date_input("Start Date:", pd.to_datetime("2018-01-01"))
end_date = st.date_input("End Date:", pd.to_datetime("2021-12-31"))
interval = st.selectbox("Select Data Interval:", ["1d", "1wk", "1mo"])

# Fetch the data
if st.button("Get Data"):
    try:
        # Use yfinance to get the data
        data = yf.download(ticker, start=start_date, end=end_date, interval=interval)
        if not data.empty:
            # Display data in the app
            st.write(f"Displaying {interval} data for {ticker} from {start_date} to {end_date}")
            st.write(data)

            # Option to download data
            csv = data.to_csv().encode('utf-8')
            st.download_button(
                label="Download data as CSV",
                data=csv,
                file_name=f'{ticker}_{interval}_data.csv',
                mime='text/csv',
            )
        else:
            st.write("No data found for the selected parameters.")
    except Exception as e:
        st.write(f"An error occurred: {e}")
