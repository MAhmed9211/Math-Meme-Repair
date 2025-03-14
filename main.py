import streamlit as st

# Set title
st.title("Simple Streamlit App")

# Add a text input
name = st.text_input("Enter your name:")

# Button to display greeting
if st.button("Greet Me"):
    st.write(f"Hello, {name}!")

# Add a slider
number = st.slider("Pick a number", 1, 100, 50)
st.write(f"You selected: {number}")

# Add an image (optional)
st.image("https://via.placeholder.com/150", caption="Placeholder Image")
