# beginner_dashboard.py
import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------
# 1. Load Data
# ---------------------
# Read CSV data from URL
data = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv")

# ---------------------
# 2. Dashboard Title
# ---------------------
st.title("📊 Data Visualization Dashboard (Beginner Version)")

# ---------------------
# 3. Sidebar Filters
# ---------------------
st.sidebar.header("Filter Data")
year_list = data['year'].unique().tolist()
selected_year = st.sidebar.selectbox("Select Year", year_list)
continent_list = data['continent'].unique().tolist()
selected_continent = st.sidebar.multiselect("Select Continent", continent_list, default=continent_list)

# ---------------------
# 4. Filter Data Based on User Selection
# ---------------------
filtered_data = data[(data['year'] == selected_year) & (data['continent'].isin(selected_continent))]

# ---------------------
# 5. Scatter Plot (GDP vs Life Expectancy)
# ---------------------
st.subheader("🌍 GDP vs Life Expectancy")
scatter_chart = px.scatter(
    filtered_data,
    x='gdpPercap',
    y='lifeExp',
    size='pop',
    color='continent',
    hover_name='country',
    log_x=True,
    size_max=60
)
st.plotly_chart(scatter_chart)

# ---------------------
# 6. Pie Chart (Population by Continent)
# ---------------------
st.subheader("📈 Population by Continent")
pie_chart = px.pie(
    filtered_data,
    values='pop',
    names='continent',
    hole=0.4
)
st.plotly_chart(pie_chart)

# ---------------------
# 7. Line Chart (Life Expectancy Trend)
# ---------------------
st.subheader("📊 Life Expectancy Trend Over Years")
line_chart = px.line(
    data[data['continent'].isin(selected_continent)],
    x='year',
    y='lifeExp',
    color='continent',
    line_group='country'
)
st.plotly_chart(line_chart)

# ---------------------
# 8. Show Filtered Data Table
# ---------------------
st.subheader("🔎 Filtered Data Table")
st.write(filtered_data)
