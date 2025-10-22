'''
import streamlit as st

st.title('Streamlit learning')
st.subheader('From AI')
st.write('Hello coder...!!!')

name = st.text_input('Enter your name:')
st.caption('*enter full name')
# st.write(f"Your name is {name}")

age = st.number_input('Enter your age:')
# st.write(f"Your age is {age}")

if st.button('Submit'):
    st.success(f"“Hello, {name}! You are {age} years old.”")

'''

import streamlit as st

st.title('🚀 Streamlit Learning')
st.subheader('From  AI')

st.write('Hello coder...!!!')

name = st.text_input('Enter your name:', placeholder='e.g. John Doe')
st.caption('*Enter yout full name')

age = st.number_input(
    'Enter your age:',
    min_value=0,
    max_value=100,
    help='Enter your age in complete years'
)
st.caption('⚠️ Enter your age in years')

# age_input = st.text_input("Enter your age:", placeholder="e.g. 18")
# if st.button("submit"):
#     if not age_input.isdigit():
#         st.error("Please enter a valid number!")
#     else:
#         age = int(age_input)
#         st.success(f"Your age is {age}")

if st.button('Submit'):
    if name == '':
        st.warning('Please enter your full name first.')
    else:
        st.success(f"Hello, {name}! You are {age} years old.")

