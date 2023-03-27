import pandas as pd
import streamlit as st
import altair as alt

# Load data
data = pd.read_csv('honeybee_colonies_2023_03_26.csv')
data2 = data[['Year','Period','State' ,'Inventory','Colony Loss']].copy()
data3 = data2.sort_values(by=['State','Year'])
data3.set_index('Period', inplace=True)


# Sidebar filters
year = st.sidebar.selectbox('Select Year', options=data3['Year'].unique())
state = st.sidebar.selectbox('Select State', options=data3['State'].unique())
variable = st.sidebar.radio('Select Variable to View Over Time', ('Inventory', 'Colony Loss'))

# Filter data
filtered_data = data3.loc[(data3['Year'] == year) & (data3['State'] == state)][[ variable]]

filtered_data = filtered_data.reset_index()

# Create bar chart
chart = alt.Chart(filtered_data).mark_bar().encode(
    alt.X('Period:O', title='Quarter',
    sort=['JAN THRU MAR','APR THRU JUN','JUL THRU SEP','OCT THRU DEC']),
    y= alt.Y(variable, title=variable)

).properties(
    width=600,
    height=400,
    title=f"{state} {variable} (number of hives) by quarter for {year}"
)

# Display chart
st.altair_chart(chart)
