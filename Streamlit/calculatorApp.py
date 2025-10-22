'''
import streamlit as st

st.title('🧮 Simple Calculator App')

# num1 = st.number_input('Enter first number: ', value = 0) // only integer number
num1 = st.number_input('Enter first number: ', value = 0.0)
num2 = st.number_input('Enter second number: ')
# operation = st.radio('select operation : ', ['+','-','*','/'])
# operation = st.selectbox('select operation : ', ['+','-','*','/'])
operation = st.selectbox('Choose operation:', ['Add', 'Subtract', 'Multiply', 'Divide'])



# st.write(num1,num2,operation)

if st.button('Calculate'):
    if operation == '+':
        st.success(f"Answer : {num1 + num2}")
    elif operation == '-':
        st.success(f"Answer : {num1 - num2}")
    elif operation == '*':
        st.success(f"Answer : {num1 * num2}")
    elif operation == '/':
        st.success(f"Answer : {num1 / num2}")

'''


import streamlit as st
st.title('🧮 Simple Calculator App')
st.divider()

col1, col2 = st.columns(2)
with col1:
    num1 = st.number_input('Enter first number:')

with col2:
    num2 = st.number_input('Enter second number:')

operation = st.selectbox('Choose operation:', ['Add', 'Subtract', 'Multiply', 'Divide'])

if operation == 'Add':
    result = num1 + num2
elif operation == 'Subtract':
    result = num1 - num2
elif operation == 'Multiply':
    result = num1 * num2
elif operation == 'Divide':
    if num2 != 0:
        result = num1 / num2
    else:
        st.error('Cannot divide by zeros')
        result = None

# if st.button('Calculate'):
#     st.success(f"Result: {result}")


if result is not None:
    st.success(f"✅ Result: {result}")

st.divider()
