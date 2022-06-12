import streamlit
import snowflake.connector


streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Fevorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmean')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie') 
streamlit.text('🐔 Hard Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected=streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.text("The fruit load list contain : ")
streamlit.text(my_data_rows)
streamlit.header("The fruit load list contains  ")
streamlit.dataframe(my_data_rows)

streamlit.header('What would you like to add')
add_my_fruit = streamlit.text_input('add the fruit:')
if add_my_fruit is not none:
  streamlit.write('Thanks for adding fruit : ',add_my_fruit)
