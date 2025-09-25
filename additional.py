import streamlit as st

st.title("ADDITIONAL")

num1 = st.number_input("Enter a number", step=1)
num2 = st.number_input("Enter another number", step=1)

st.write(f"{num1} + {num2} = {num1 + num2}")
