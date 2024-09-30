import streamlit as st
from auth_functions import sign_in  # Adjust this import based on your project structure

def show_login_page():
    st.title("Login Page")
    
    # Display logout success message if applicable
    if 'logout_success' in st.session_state and st.session_state.logout_success:
        st.success("Signed out successfully!")
        st.session_state.logout_success = False  # Reset after displaying the message

    # Display warning or success messages
    if 'auth_warning' in st.session_state:
        st.error(st.session_state.auth_warning)

    if 'auth_success' in st.session_state:
        st.success(st.session_state.auth_success)

    # Login form
    with st.form("login_form"):
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        login_button = st.form_submit_button("Login")
        
        if login_button:
            # Call the sign_in function from auth_functions
            success = sign_in(email, password)
            if success:
                st.session_state.auth_success = "Successfully signed in!"
                st.session_state.current_page = 'home'  # Navigate to home page after login
            else:
                st.session_state.auth_warning = "Invalid email or password."

    # Link to the registration page
    if st.button("Create an Account"):
        st.session_state.current_page = 'register'  # Navigate to the registration page
