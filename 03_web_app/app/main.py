import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def init_session_state():
    """Initialize session state variables"""
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    if 'user_info' not in st.session_state:
        st.session_state.user_info = None
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

def main():
    st.title("Networking Automation Assistant")
    
    init_session_state()
    
    # Sidebar
    with st.sidebar:
        st.header("Navigation")
        page = st.radio(
            "Select a page",
            ["Home", "Profile Analysis", "Message Generation", "Conversation Prep"]
        )
    
    if not st.session_state.authenticated:
        st.warning("Please log in to continue")
        # Add authentication UI here
    else:
        if page == "Home":
            st.write("Welcome to your Networking Assistant!")
            st.write("Choose a function from the sidebar to get started.")
        elif page == "Profile Analysis":
            st.header("Profile Analysis")
            # Profile analysis UI will go here
        elif page == "Message Generation":
            st.header("Message Generation")
            # Message generation UI will go here
        elif page == "Conversation Prep":
            st.header("Conversation Prep")
            # Conversation prep UI will go here

if __name__ == "__main__":
    main() 