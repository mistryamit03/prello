import streamlit as st
import pandas as pd
import pickle  # To load the trained model


# Load the trained model (Make sure 'model.pkl' exists in the same directory)
with open("app/linear_regression_model_RF_Prello.pkl", "rb") as file:
    model = pickle.load(file)


# Create a form
with st.form(key="property form"):
    # name = st.text_input("Name", placeholder="Enter your full name")
    	
    municipality_code = st.text_input("Municipality Code", placeholder="Enter the Municipality Code")
    department_code = st.text_input("Department Code", placeholder = "Enter the Department Code" )

    # Button to Submit Data
    if st.form_submit_button("Predict Price"):
        # Format input data as a DataFrame
        input_data = pd.DataFrame({
            # "name": [name],
            "department_code": [department_code],
            "municipality_code": [municipality_code]

        })
        
        # Make Prediction
        prediction = model.predict(input_data)[0]

        
        # Display the Prediction
        st.write(f"Estimated Property Price: ${prediction:,.2f}")





    # surface_area_sq_mt = st.text_input("Surface Area in sq mts", placeholder = "Enter the surface area in sq mts" )
    # rating = st.slider("Rate our service (1-5)", 1, 5, 3)
    # feedback = st.text_area("Feedback", placeholder="Share your thoughts...")
    
# # Submit button
#     submit_button = st.form_submit_button("Submit")

