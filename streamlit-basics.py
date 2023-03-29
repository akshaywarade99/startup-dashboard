import streamlit as st
import  pandas as pd
import time

st.title("Startup DashBoard")
st.header('I am learning streamlit')
st.subheader('Akshay')

st.write('write a text')

st.markdown('''
# Movies
- PK
- 3 Idiots
''')

st.code('''
def f(x):
    return x**2
x=f(2)
''')

st.latex('x^2 + y^2 + 9 = 0')

df=pd.DataFrame({
    'Name':['Akshay', 'G1', 'Mangesh'],
    'Marks':[95,88,35],
    'package': [11,12,13]
})
st.dataframe(df)

st.metric('Revenue', 'Rs. 3L', '3%')

st.metric('Revenue', 'Rs. 3L', '-5%')

st.json({
    'Name':['Akshay', 'G1', 'Mangesh'],
    'Marks':[95,88,35],
    'package': [11,12,13]
})

# Displaying Images

st.image('AI_wallpaper.jpg')

col1, col2 = st.columns(2)  # we can any no of columns

with col1:
    st.image('AI_wallpaper.jpg')
with col2:
    st.image('AI2.jpg')

# How to creat LayOuts
# - SideBar
# - Columns

st.sidebar.title('SideBar Title')

# Status messages

st.error('Login Failed')

st.success('Login Sucsessful')

st.info('Login Sucsessful')

st.warning('Login Problem')

# Showing Status
# Progress Bar

st.markdown('### Task Progress Bar')

bar= st.progress(0)

for i in range(1,101):
    time.sleep(0.001)
    bar.progress(i)

# Taking User Input
# Text input-> number Input --> Date input
# Button --> baloons
# Dropdown
# File Uploader

email = st.text_input('Enter Email')

Number = st.number_input('Enter Age')

st.date_input('Enter Registration Date')


# Taking User Input
# Text input-> number Input --> Date input
# Button --> baloons
# Dropdown
# File Uploader


# buttons
email = st.text_input('Enter Email')
password= st.text_input('Enter Password')

btn= st.button('Login')

if btn:    # means if button clicked
    if email=='aks@gamil.com' and password=='1818':
        st.success('Login Successful')
        st.balloons()
    else:
        st.error('Login Failed')


# Dropdown

gender= st.selectbox('Select gender', ['Male', 'Female', 'Other'])

st.markdown('### Gender of user')
st.write(gender)


# File uploader

file= st.file_uploader('Upload a csv file')

if file is not None:
    df= pd.read_csv(file)
    st.dataframe(df.describe())