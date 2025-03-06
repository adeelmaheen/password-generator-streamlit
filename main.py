import streamlit as st
import random 
import string 

def generate_password(length,use_digits, use_special):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits  # add digits to the characters
    if use_special:
        characters += string.punctuation
    
    
    password = ''.join(random.choice(characters) for _ in range(length)) # _ represent the loop have no specific limits
    return password

st.title("Password Generator")

length = st.slider("Select the length of the password", min_value=6, max_value=32, value=12)
use_digits = st.checkbox("Include digits")
use_special = st.checkbox("Include special characters")

if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.success(f"Generated Password: {password}")

st.write("---")
st.write("Made with ❤️ by [Maheen Arif](https://github.com/adeelmaheen)")



