import streamlit as st
import pandas as pd

st.title("Real World Fuel Consumption")
st.write(
    "For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

conn = st.connection("snowflake")
df = conn.query("SELECT * FROM CAR_MODELS;", ttl="10m")

st.write(df)