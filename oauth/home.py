import streamlit as st

def show_home_page():
    st.title("Home Page")
    st.write("Welcome to the home page!")
    
    if st.button("Logout"):
        # Set the session state to logged out
        st.session_state.logged_in = False  
        st.session_state.current_page = 'login'  # Navigate back to login page

        # Show a logout success message and navigate back to login
        st.session_state.logout_success = True
        
        # Clear other session states if necessary
        for key in list(st.session_state.keys()):
            if key != 'current_page' and key != 'logout_success':
                del st.session_state[key]
        
        # Redirect the user to the login page by setting the query params
        st.experimental_set_query_params(page="login")
