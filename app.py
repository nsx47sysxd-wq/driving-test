import streamlit as st
from datetime import datetime, time

# 1. Page Configuration
st.set_page_config(page_title="First Test Probability", layout="centered")

st.title("🚗 הטסט הראשון שלי")
st.write("050-2505215 :יהודה שריפי - מורה נהיגה")
st.write("אשקלון והסביבה")

st.divider()

# 2. Input Fields
with st.form("test_calculator"):
    # Age inputs
    col_age_y, col_age_m = st.columns(2)
    with col_age_y:
        year = st.number_input("גיל (שנים)", min_value=16, max_value=99, value=17)
    with col_age_m:
        month = st.number_input("גיל (חודשים)", min_value=1, max_value=12, value=1)
    
    # Place input (Hebrew Locations)
    locations = [
        "הצפון", "חיפה והקריות", "יהודה ושומרון", "תל אביב", 
        "המרכז", "ירושלים", "השפלה (אשקלון ואשדוד)", 
        "באר שבע והדרום", "הערבה", "אילת"
    ]
    place = st.selectbox("מיקום", locations)

    x_date = st.date_input("תאריך טסט פנימי")
    
    # Date and Hour
    test_date = st.date_input("תאריך הטסט")
    test_hour = st.time_input("שעת הטסט (7:00 - 16:00)", value=time(9, 0))
    
    car_type = st.radio("סוג הרכב", ["ידני", "אוטומאט"], horizontal=True)

    submit = st.form_submit_button(" חשב את הסיכוי")

# 3. Validation & Logic
if submit:
    # Check minimum age requirement (16 years and 9 months)
    total_months = (year * 12) + month
    min_months_required = (16 * 12) + 9

    if total_months < min_months_required:
        st.error("Error: You must be at least 16 years and 9 months old to take the test.")
    
    # Check valid hours (7am to 4pm)
    elif not (time(7, 0) <= test_hour <= time(16, 0)):
        st.error("Error: Driving tests are only conducted between 07:00 and 16:00.")
        
    else:
        # --- CALCULATION LOGIC ---
        
        # A. Location Penalty (Example weights)
        location_penalties = {
            "תל אביב": 15, "ירושלים": 12, "חיפה והקריות": 10,
            "המרכז": 8, "השפלה (אשקלון ואשדוד)": 2, "הצפון": 5,
            "באר שבע והדרום": 7, "יהודה ושומרון": 4, "הערבה": 2, "אילת": 3
        }
        loc_penalty = location_penalties.get(place, 5)

        # B. Hour Penalty (Rush hour peaks)
        if 7 <= test_hour.hour <= 8:
            hour_penalty = 1
        elif 9<= test_hour.hour <= 12:
            hour_penalty = 10
        elif 12 <= test_hour.hour <= 14:
            hour_penalty = 5
        elif 15 <= test_hour.hour <= 16:
            hour_penalty = 3
        else:
            hour_penalty = 8

        # C. Age Factor (Penalty reduces with age)
        # As age increases, we subtract less from the pass rate
        age_mitigation = max(0, (year - 17) * 0.5)
        
        # Final Formula
        base_prob = 90
        total_penalty = max(0, (loc_penalty + hour_penalty) - age_mitigation)
        final_prob = round(base_prob - total_penalty, 2)

                
        # 4. Display Result
        st.divider()
        if final_prob > 70:
            st.success(f"### הסיכוי שלך הוא: {final_prob}%")
            st.balloons()
        else:
            st.success(f"### הסיכוי שלך הוא: {final_prob}%")
        st.info(f"Location: {place} | Scheduled Time: {test_hour.strftime('%H:%M')}")
        st.caption("הנתונים מבוססים על נוסחה סטטיסטית ואינם מבטיחים הצלחה בטסט.")
        