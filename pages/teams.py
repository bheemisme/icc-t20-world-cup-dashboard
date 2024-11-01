import streamlit as st
import analytics.teams as teams
import analytics.preprocessing as preprocess
st.title("Teams")


with st.container():
    st.pyplot(teams.get_win_percentage())
    st.pyplot(teams.get_toss_won())

col1, col2 = st.columns(2)

with col1:
    st.pyplot(teams.get_tos_decision())

with col2:
    st.pyplot(teams.get_win_method())



st.selectbox("Choose a team: ", list(preprocess.teams))