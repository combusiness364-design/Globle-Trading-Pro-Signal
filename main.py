import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="Globle Trading Pro Signal", layout="centered")
st.title("📈 Globle Trading Pro Signal")

symbol = st.text_input("Stock Symbol likho:", "AAPL")
if st.button("Signal Nikalo"):
    data = yf.download(symbol, period="5d", interval="1d")
    if not data.empty:
        last = data['Close'][-1]
        st.success(f"Last Price: ${last:.2f}")
        st.line_chart(data['Close'])
    else:
        st.error("Symbol nahi mila")
