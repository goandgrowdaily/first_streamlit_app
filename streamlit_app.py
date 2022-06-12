import streamlit
import snowflake.connector
import pandas
import requests
from urllib.error import URLError

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Fevorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmean')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie') 
streamlit.text('🐔 Hard Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected=streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

#new sectioin to dispaly fruitvice api response
streamlit.header('Fruitvice Fruit Advice !  ')
try:
  fruit_choice = streamlit.text_input('What fruit information would like to have?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    fruityvice_responce = request.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_responce.json())
    strealit.dataframe(fruityvice_normalize)
except URLError as e:
  streamlit.error()
  
#stop past run
streamlit.stop()
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from  fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.text("The fruit load list contain : ")
streamlit.text(my_data_rows)
streamlit.header("The fruit load list contains  ")
streamlit.dataframe(my_data_rows)

streamlit.header('What would you like to add')
add_my_fruit = streamlit.text_input('add the fruit:')
streamlit.write('Thanks for adding fruit : ',add_my_fruit)

my_cur.execute("insert into fruit_load_list values ('add_my_fruit')")
