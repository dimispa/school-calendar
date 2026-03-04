import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from streamlit_calendar import calendar

# Ρύθμιση για εμφάνιση σαν εφαρμογή κινητού
st.set_page_config(page_title="School Cal", layout="centered")

st.markdown("""
    <style>
    /* Κρύβουμε τα περιττά του Streamlit για να μοιάζει με APK */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

st.title("📅 Σχολικό Ημερολόγιο")

# Σύνδεση χωρίς Secrets JSON - Μόνο με το Link
url = "https://docs.google.com/spreadsheets/d/1ENw07twtEbduCWifb4tt0_sQo2iT8SiAoB9QlXnMeY0/edit?usp=sharing"
conn = st.connection("gsheets", type=GSheetsConnection)

try:
    df = conn.read(spreadsheet=url, ttl=0)
    
    # Εμφάνιση Ημερολογίου προσαρμοσμένου για κινητά
    calendar_options = {
        "initialView": "listWeek", # Λίστα για να βολεύει στο κινητό
        "locale": "el",
        "headerToolbar": {
            "left": "prev,next",
            "center": "title",
            "right": "today"
        }
    }
    
    calendar(events=df.to_dict(orient='records'), options=calendar_options)
    
    # Κουμπί Νέας Καταχώρησης
    with st.expander("➕ Προσθήκη Διαγωνίσματος"):
        with st.form("new_event"):
            teacher = st.text_input("Καθηγητής")
            date = st.date_input("Ημερομηνία")
            type_ev = st.selectbox("Τύπος", ["Διαγώνισμα", "Τεστ"])
            submit = st.form_submit_button("Αποθήκευση")
            
            if submit:
                # Εδώ θα προσθέσουμε τη λογική αποθήκευσης μόλις δουλέψει η ανάγνωση
                st.success("Η αποθήκευση ενεργοποιείται...")
except Exception as e:
    st.error("Σύνδεση σε εξέλιξη... Παρακαλώ περιμένετε.")

