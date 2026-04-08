import streamlit as st
from datetime import datetime

# 1. Page Configuration
st.set_page_config(page_title="First Test Probability", layout="centered")

st.title("🚗 הטסט הראשון שלי")
st.markdown("הכנס נתונים כדי לחשב סיכוי לעבור טסט ראשון")

# 2. Input Fields
with st.form("test_calculator"):
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input("גיל", min_value=16, max_value=100, value=25)
        place = st.selectbox("מיקום (איזור) ", ["Jerusalem", "Tel Aviv", "Haifa", "Beer Sheva", "Other"])
    
    with col2:
        test_date = st.date_input("תאריך הטסט", value=datetime.today())
        test_hour = st.time_input("שעת הטסט", value=datetime.now().time())
        
    car_type = st.radio("סוג הרכב", ["ידני", "אוטומאט"], horizontal=True)

    # Submit button for the form
    submit = st.form_submit_button("חשב!")

# 3. Logic & Formula
if submit:
    # Example Formula Logic (Replace with your actual math)
    # High traffic at peak hours (8am or 4pm) might lower probability
    hour_penalty = 5 if (8 <= test_hour.hour <= 9 or 16 <= test_hour.hour <= 17) else 0
    
    # Base probability calculation
    base_prob = 65  # Starting point
    result = base_prob + (age * 0.2) - hour_penalty
    
    # Ensure result stays between 0 and 100
    final_prob = max(0, min(100, round(result, 2)))

    # 4. Display Result
    st.divider()
    if final_prob > 50:
        st.success(f"### Estimated Pass Probability: {final_prob}%")
        st.balloons()
    else:
        st.warning(f"### Estimated Pass Probability: {final_prob}%")
    
    st.info("Tip: Practice more in heavy traffic if your test is during rush hour!")