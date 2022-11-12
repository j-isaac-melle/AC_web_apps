
     
#dont run anything past while troubleshooting:
import streamlit

streamlit.title('Air Canada Webpage')

streamlit.header('Users & Roles')
streamlit.text('USER: An identiy recognized by Snowflake, associated to Person or Program (Azure x Air Canada).\n')
streamlit.text('ROLE: An entity to which privileges can be granted.')
streamlit.text('\tRoles are assigned to users.')
streamlit.text('\tRoles may also be assigned to other roles, creating a role hierarchy.')
streamlit.header('Chck out our users:')

#streamlit.multiselect(

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
