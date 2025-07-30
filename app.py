import streamlit as st
import joblib
import pandas as pd

# Load the best model
model = joblib.load('best_model.pkl')

# Define the Streamlit app
st.set_page_config(
    page_title = "Employee Salary Prediction App",
    page_icon = r"E:\IBM_Single\image.png",
    layout = "wide"
)

st.title("Employee Salary Prediction App")
st.markdown(
    "Predict the salary scale of an employee based on their attributes."
)

# Sidebar for user input
st.sidebar.header("User Input")
st.sidebar.write("Please enter the following information:")

# Giving the user input fields according to the datasets's acctual columns and the atributes
age = st.sidebar.number_input(
    "Age",
    min_value=18,
    max_value=70
)
educational_qualification = st.sidebar.selectbox(
    "Educational Qualification", [
        "Less than High School", "High School", "Bachelor's Degree", "Master's Degree", "PhD", "Other"
    ]
)
gender = st.sidebar.selectbox(
    "Gender", [
        "Male", "Female", "Other"
    ]
)
job_type = st.sidebar.selectbox(
    "Job Type", [
        "Private", "Unemployed", "Government", "Self-employed", "Other"
    ]
)
job_title = st.sidebar.selectbox(
    "Job Title", [
        "Clerk", "Electrician", "Mechanic", "Teacher", "Nurse", "Sales Executive", "Doctor",
        "Manager", "Software Engineer", "Data Analyst"
    ]
)
job_location = st.sidebar.selectbox(
    "Job Location", [
        "Delhi", "Chennai", "Bangalore", "Jaipur", "Mumbai", "Ahmedabad",
        "Pune", "Kolkata", "Hyderabad", "Lucknow", "Other"
    ]
)
job_rating = st.sidebar.slider(
    "Job Rating",
    min_value=1,
    max_value=5,
)
working_hours = st.sidebar.number_input(
    "Working Hours (Weekly)",
    min_value=0,
    max_value=100
)
work_experience = st.sidebar.number_input(
    "Work Experience (Year)",
    min_value=0,
    max_value=30
)

# Create a DataFrame from the user input
input_data = pd.DataFrame({
    "Age": [age],
    "Educational Qualification": [educational_qualification],
    "Gender": [gender],
    "Job Type": [job_type],
    "Job Title": [job_title],
    "Job Location": [job_location],
    "Job Rating": [job_rating],
    "Working Hours (Weekly)": [working_hours],
    "Work Experience (Year)": [work_experience]
})

st.subheader("User🔎 Input Data")
st.write(input_data)

# Prediction Button
if st.button("Predict Salary Scale"):
    # Preprocess the input data
    input_data['Educational Qualification'] = input_data['Educational Qualification'].map({
        "Less than High School": 0, "High School": 1, "Bachelor's Degree": 2,
        "Master's Degree": 3, "PhD": 4, "Other": 5
    })
    input_data['Gender'] = input_data['Gender'].map({
        "Male": 0, "Female": 1, "Other": 2
    })
    input_data['Job Type'] = input_data['Job Type'].map({
        "Private": 0, "Unemployed": 1, "Government": 2,
        "Self-employed": 3, "Other": 4
    })
    input_data['Job Title'] = input_data['Job Title'].map({
        "Clerk": 0, "Electrician": 1, "Mechanic": 2, "Teacher": 3,
        "Nurse": 4, "Sales Executive": 5, "Doctor": 6,
        "Manager": 7, "Software Engineer": 8, "Data Analyst": 9
    })
    input_data['Job Location'] = input_data['Job Location'].map({
        "Delhi": 0, "Chennai": 1, "Bangalore": 2, "Jaipur": 3,
        "Mumbai": 4, "Ahmedabad": 5, "Pune": 6,
        "Kolkata": 7, "Hyderabad": 8, "Lucknow": 9, "Other": 10
    })

    # Make predictions
    prediction = model.predict(input_data)

    # Display the prediction result
    st.subheader("Prediction Result")
    st.write(f"The predicted salary scale is: {prediction[0]}")
