import streamlit as st

st.title("TDS Calculator")

salary = st.number_input("Enter your annual salary :")

tds = 0


if salary <= 300000:
    tds = 0

elif salary <= 600000:
    tds = (salary - 300000) * 0.05

elif salary <= 900000:
    tds = (300000 * 0.05) + (salary - 600000) * 0.10

elif salary <= 1500000:
    tds = (300000 * 0.05) + (300000 * 0.10) + (salary - 900000) * 0.15

else:
    tds = (300000 * 0.05) + (300000 * 0.10) + (600000 * 0.15) + (salary - 1500000) * 0.3


monthly_tds = tds / 12
year_tds = tds / 4


st.subheader("Estimated TDS")

st.success(f" Annual TDS: {tds:,.2f}")
st.info(f"Monthly TDS: {monthly_tds:,.2f}")
st.info(f"year TDS: {year_tds:,.2f}")