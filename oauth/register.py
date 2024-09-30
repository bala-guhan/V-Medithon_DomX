import streamlit as st
from auth_functions import create_account  # Adjust this import based on your project structure

def show_registration_page():
    st.title("Registration Page")

    if 'auth_warning' in st.session_state:
        st.error(st.session_state.auth_warning)

    if 'auth_success' in st.session_state:
        st.success(st.session_state.auth_success)

    # Registration form
    with st.form("registration_form"):
        reg_email = st.text_input("Email for Registration")
        reg_password = st.text_input("Password for Registration", type="password")
        register_button = st.form_submit_button("Register")
        if register_button:
            create_account(reg_email, reg_password)
            st.session_state.auth_success = "Successfully registered!"
            st.session_state.current_page = 'login'  # Navigate to the login page
            st.experimental_set_query_params(page='login')  # Optionally use URL params to control page navigation

    # Link to the login page
    if st.button("Already have an account? Login here"):
        st.session_state.current_page = 'login'  # Navigate back to the login page
        st.experimental_set_query_params(page='login')
