import streamlit as st
import pandas as pd
import numpy as np 
import os 

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
st.write(FILE_DIR)
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
st.write(PARENT_DIR)
dir_of_interest = os.path.join(PARENT_DIR, "resources")
st.write(dir_of_interest)
data_path= os.path.join(dir_of_interest, "data","open_pubs1.csv")
st.write(data_path)
data_path = data_path.replace("/..",'')
data = pd.read_csv(data_path)

#data = pd.read_csv(r'/Users/vamsi/Downloads/open_pubs1.csv')

local_authority= st.selectbox(
        'select the loacal authority',
        list(np.sort(data['local_authority'].unique())))


if st.button('local_authority'):
    loca1 = data[data['local_authority']==local_authority][['latitude','longitude']]
    st.map(loca1)


postal_code= st.selectbox(
    'select the loacal authority',
    list(np.sort(data['postcode'].unique())))


if st.button('postal_code'):
    post1 = data[data['postcode']==postal_code][['latitude','longitude']]
    st.map(post1)


