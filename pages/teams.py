import streamlit as st
from analytics.win_percentage import fig as win_percentage
from analytics.win_method import fig as win_method
st.title("Teams")

st.pyplot(win_percentage)
st.pyplot(win_method)