import streamlit as st

# Centered main heading using HTML for styling.
st.markdown("<h1 style='text-align: center;'>Simple Calculator</h1>", unsafe_allow_html=True)

# Create a form for user input.
with st.form("calculator_form"):
    first_num = st.number_input("Enter first number", value=0.0)
    second_num = st.number_input("Enter second number", value=0.0)
    operation = st.selectbox("Select operation", ["+", "-", "*", "/"])
    submitted = st.form_submit_button("Calculate")

if submitted:
    result = None

    # Perform the calculation based on the selected operation.
    if operation == "+":
        result = first_num + second_num
    elif operation == "-":
        result = first_num - second_num
    elif operation == "*":
        result = first_num * second_num
    elif operation == "/":
        if second_num != 0:
            result = first_num / second_num
        else:
            st.error("Error: Division by zero is not allowed!")

    # Display the result in bold and large font.
    if result is not None:
        st.markdown(f"<h2 style='font-weight: bold;'>The result is: {result}</h2>", unsafe_allow_html=True)

    # "Play Again" button to reset the app.
    if st.button("Play Again"):
        st.experimental_rerun()

    # Final thank-you message.
    st.markdown("<h3 style='text-align: center;'>Thank you for using Simple Calculator</h3>", unsafe_allow_html=True)
