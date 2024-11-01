import streamlit as st

import analytics.batting as batting
import analytics.preprocessing as pre

st.title('Batting')
col1, col2 = st.columns(2)
with col1:
    st.pyplot(batting.get_top_5_batsmen_on_strike_rate())

with col2:
    st.pyplot(batting.get_batsmen_with_most_half_centuries())

col1, col2 = st.columns(2)

with col1:
    st.pyplot(batting.get_batting_style_counts())

with col2:
    st.pyplot(batting.get_avg_strike_rate_per_batting_style())

bastman_name =st.selectbox("choose a batsman",pre.batting['batsmanName'].unique().tolist())

st.pyplot(batting.get_batsman_metrics(bastman_name))
st.pyplot(batting.get_batsman_trend(bastman_name))