import streamlit as st
import pandas as pd 
from data_retrieval.entsoe_data import fetch_generation_data
from visualization_management.graph import generate_time_serie_graph, correlation_matrix

st.title('Energy Generation Data Visualization')

st.sidebar.header("Select the data range:")
start_date = st.sidebar.date_input('Start date', pd.Timestamp('2024-01-01', tz='Europe/Zurich'))
end_date = st.sidebar.date_input('End date', pd.Timestamp('2024-01-04', tz='Europe/Zurich'))

#fetch energy generation data
country_code = '10YCH-SWISSGRIDZ'
df_generation = fetch_generation_data(country_code, start_date, end_date)

#Display data in streamlit  
st.write("Energy Generation Data")
st.write(df_generation)

#Generate time serie graph
st.subheader("Energy Generation Time Serie")
fig = generate_time_serie_graph(df_generation)
st.plotly_chart(fig)

#Generate correlation matrix
st.subheader("Correlation Matrix")
fig_corr = correlation_matrix(df_generation)
if fig_corr:
    st.plotly_chart(fig_corr)
else:
    st.write("Correlation matrix cannot be generated with a single column")