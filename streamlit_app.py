import pandas
import streamlit
import requests

streamlit.title('my Parents new healthy dinner')
streamlit.header('🍌Breakfast Menu')
streamlit.text('🥭Omega 3 & Blueberry Oatmeal')
streamlit.text('🍇Kale, Spinach & Rocket Smoothie')
streamlit.text('🥝Hard-Boiled Free-Range Egg')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Banana'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
#streamlit.multiselect("pick from fruits:", list(my_fruit_list.index),['Avocado','Strawberry'])
streamlit.dataframe(fruits_to_show)

# Let's put a pick list here so they can pick the fruit they want to include 


#fruits_selected=streamlit.multiselect("pick from fruits:", list(my_fruit_list.index),['Avocado','Strawberry'])
#fruits_to_show = my_fruit_list.loc[fruits_selected]
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
#streamlit.dataframe(my_fruit_list)


#New Section to display fuityvice aspi response
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
#fruit_choice = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['kiwi','jackfruit'])

streamlit.write('The user entered ', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
streamlit.text(fruityvice_response)
#streamlit.text(fruityvice_response.json())

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
my_data_row = my_cur.fetchone()
streamlit.text("The Fruit Load List Contains:")
streamlit.text(my_data_row)

streamlit.header("The Fruit Load List in  Contains:")
streamlit.dataframe(my_data_row)

my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
my_data_row = my_cur.fetchall()
streamlit.header("The Fruit Load List DataFrame Contains:")
streamlit.dataframe(my_data_row)
fruit_choice = streamlit.text_input('What fruit would you like information about?','jackfruit')

streamlit.write('Thanks for Adding', add_my_fruit)
my_cur.execute("insert into fruit_load_list values('farom streamlit')")




