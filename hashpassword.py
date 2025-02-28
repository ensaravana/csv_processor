# import streamlit_authenticator as stauth
# passwords = ["naga@123"]
# print(stauth.Hasher(passwords).generate())

import yaml
import streamlit as st
import streamlit_authenticator as stauth
# from yaml.loader import SafeLoader

# with open('credential.yaml','w') as file:
#     config = yaml.load(file,Loader=SafeLoader)
#     print(config['credentials'])

def read_one_block_of_yaml_data(filename):
    with open(f'{filename}.yaml','r') as f:
        output = yaml.safe_load(f)
        print(output)
        data = stauth.Hasher.hash_passwords(output['credentials'])
        print(data)
   
read_one_block_of_yaml_data('credentials')