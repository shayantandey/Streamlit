import streamlit as st

st.title("Welcome to the Streamlit App!")

if st.checkbox("Check this box to see a message.", key="checkbox_1"):
    st.write("Checkbox 1 selected!")

if st.checkbox("Check this box to see a message.", key="checkbox_2"):
    st.write("Checkbox 2 selected!")

if st.radio("Choose an option:", ("Option 1", "Option 2"), key="radio_1") == "Option 1":
    st.write("You selected Option 1!")


num1 = st.number_input("Enter a number:", key="number_input_1")
num2 = st.number_input("Enter another number:", key="number_input_2")
result = st.button("Calculate Sum")

if result:
    st.write(f"The sum of {num1} and {num2} is {num1 + num2}")
