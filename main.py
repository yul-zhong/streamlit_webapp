import streamlit as st
import pandas

data = {
    'series_1':[1,3,4,5,7],
    'series_2':[10,30,40,100,250]
}

df = pandas.DataFrame(data)

st.title('our first streamlit app')
st.subheader('Introducing streamlit in automate everything with python')
st.write('''this is our first web app''')

st.write(df)
st.line_chart(df)
st.area_chart(df)

myslider = st.slider('Celsius')
st.write(myslider,'in Fahrenheit is', myslider * 9/5 +32)