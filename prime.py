import streamlit as st

st.title("PRIME NUMBER")


num1 = st.number_input("Enter the first number:", step=1, format="%d")
num2 = st.number_input("Enter the second number:", step=1, format="%d")


if st.button("Check if Sum is Prime"):
    total = num1 + num2
    st.write(f"Sum of {num1} and {num2} is **{total}**")


    n = total
    if n <= 1:
        is_prime = False
    elif n == 2:
        is_prime = True
    elif n % 2 == 0:
        is_prime = False
    else:
        is_prime = True
        i = 3
        while i * i <= n:
            if n % i == 0:
                is_prime = False
                break
            i += 2

    if is_prime:
        st.success(" Prime Number")
    else:
        st.error(" Not a Prime Number")
