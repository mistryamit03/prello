import streamlit as st
import pandas as pd

# Set app title
st.title("Property Form")

# Create a form
with st.form(key="property form"):
    name = st.text_input("Name", placeholder="Enter your full name")
    municipality_code = st.text_input("Municipality Code", placeholder="Enter the Municipality Code")
    department_code = st.text_input("Department Code", placeholder = "Enter the Department Code" )
    # surface_area_sq_mt = st.text_input("Surface Area in sq mts", placeholder = "Enter the surface area in sq mts" )
    # rating = st.slider("Rate our service (1-5)", 1, 5, 3)
    # feedback = st.text_area("Feedback", placeholder="Share your thoughts...")
    
# Submit button
    submit_button = st.form_submit_button("Submit")

def return_prediction(df):
    if df['name'][0] == 'Alex':
        return 10
    else: return 4
     

# Display the submitted data if the button is pressed
if submit_button:
        # Format the new data in the form of the dataframe
    d = {
        'name': [name], 
        'municipality_code': [municipality_code], 
        'department_code':[department_code] }
        # 'surface_area_sq_mt':[surface_area_sq_mt]
    df = pd.DataFrame(data=d)
    var = return_prediction(df)
    st.write(var)



