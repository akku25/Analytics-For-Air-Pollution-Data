import streamlit as st
from prepareData import loadData
import plotly.express as px
sidebar = st.sidebar
sidebar.title('Analysis of Air Pollution Data')
selOption = sidebar.selectbox('Select One',['View Dataset','View Analysis'])

df=loadData('city_day.csv')

def init():
    st.title("Analysis of Air Pollution Data")
    st.image('air.jpeg')
    st.subheader('In this Project we will analyze the Air Pollution in various Cities in India...')
init()

def showData():
    st.header('Dataset used in this Project ')
    st.markdown('_ _ _')
    st.dataframe(df)


def analyseData():
    st.header('Visualizations here')
    st.subheader('Comparison of O3 in different cities')
    st.plotly_chart(px.bar(title ="Comparison of O3 level in cities",data_frame=df,x='City',y='O3',template="seaborn"))
    st.subheader('Comparison of NO2 level in Cities')
    st.plotly_chart(px.bar(data_frame=df,x='City',y='NO2'))
    st.subheader('Comparison of CO level in Cities')
    st.plotly_chart(px.bar(data_frame=df,x='City',y='CO'))
    st.subheader('Comparison  of SO2 level in Cities')
    st.plotly_chart(px.bar(data_frame=df,x='City',y='SO2'))
    st.subheader('Comparison of NO level in Cities')
    st.plotly_chart(px.bar(data_frame=df,x='City',y='NO'))
    st.subheader('Comparison of NH3 level in Cities')
    st.plotly_chart(px.bar(data_frame=df,x='City',y='NH3'))
    st.subheader('Comaprison of NOx level in Cities')
    st.plotly_chart(px.bar(data_frame=df,x='City',y='NOx'))
    st.subheader('Comparison of Benzene level in Cities')
    st.plotly_chart(px.bar(data_frame=df,x='City',y='Benzene'))

if selOption =='View Dataset':
    showData()
elif selOption =='View Analysis':
    analyseData()
