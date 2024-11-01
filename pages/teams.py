import streamlit as st
import analytics.teams as teams
import analytics.preprocessing as preprocess
st.title("Teams")



st.pyplot(teams.get_win_percentage())
st.pyplot(teams.get_toss_won())

col1, col2 = st.columns(2)

with col1:
    st.pyplot(teams.get_tos_decision())

with col2:
    st.pyplot(teams.get_win_method())



team = st.selectbox("Choose a team: ", list(preprocess.teams))
st.pyplot(teams.get_team_trend(team))
