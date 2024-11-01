import streamlit as st
import analytics.bowling as bowling
import analytics.preprocessing as pre

st.title('Bowling')

st.pyplot(bowling.get_top_5_bowlers())
st.pyplot(bowling.get_top_5_bowling_styles())
bowler = st.selectbox('Choose a bowler:', pre.bowling['bowlerName'].unique())


fig, team = bowling.get_bowler_metrics(bowler)
st.write(f'Name = {bowler}; team = {team}')
st.table(fig)
st.pyplot(bowling.get_bowler_trend(bowler))
