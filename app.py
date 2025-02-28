import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import time
def authen():
    with open('credentials.yaml') as file:
        config = yaml.load(file,Loader=SafeLoader)
    authenticator = stauth.Authenticate(
   
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        cookie_expiry_days = config['cookie']['expiry_days']
        
    )
    try:    
        authenticator.login(location="main")
    except Exception as e:
        st.write(e)

    
    if st.session_state['authentication_status']:
        time.sleep(3)
        st.switch_page("pages/calculation.py") 


    elif st.session_state['authentication_status'] is False:
        st.error('Username/password is incorrect')
    elif st.session_state['authentication_status'] is None:
        st.warning('Please enter your username and password')     

    def logoutt():
       authenticator.logout()
       st.session_state.clear()
       st.rerun()

    st.session_state["logout"] = logoutt
     
    
if __name__ == "__main__":
    authen()

   
