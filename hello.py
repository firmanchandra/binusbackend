import streamlit as st

st.write(" # Hello World ")

x= 12.34
st.write(x)


import pandas as pd
df = pd.DataFrame({
    'first_column':[1,2,3,4],
    'second_column': [10,20,30,40]
})

st.write(df)


## ----------------------------- MAGIC ----------------------------
st.write("Magic commands")

x=10
x
