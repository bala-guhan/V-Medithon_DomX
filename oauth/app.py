import streamlit as st
from login import show_login_page
from register import show_registration_page
from home import show_home_page

# Initialize session state for page navigation
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'login'

# Check query params to handle page navigation
query_params = st.experimental_get_query_params()
if "page" in query_params:
    st.session_state.current_page = query_params["page"][0]

# Logic for showing different pages
if st.session_state.current_page == 'login':
    show_login_page()
elif st.session_state.current_page == 'register':
    show_registration_page()
elif st.session_state.current_page == 'home':
    show_home_page()
