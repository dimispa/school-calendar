import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from streamlit_calendar import calendar

# Ρυθμίσεις για εμφάνιση σαν εφαρμογή
st.set_page_config(page_title="School Cal", layout="centered")

# Κρύβουμε τα μενού του Streamlit για να μοιάζει με App
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

st.title("📅 Σχολικό Ημερολόγιο")

# Το link του αρχείου σου
URL = "https://docs.google.com/spreadsheets/d/1ClSPjY3zx1eaDL2deGn1dx_9XYTFxfCQg_zXv8Ny2Cw/edit#gid=0"

# Σύνδεση με το Google Sheets
conn = st.connection("gsheets", type=GSheetsConnection)

try:
    # Διάβασμα δεδομένων - TTL=0 για να ανανεώνεται αμέσως
    df = conn.read(spreadsheet=URL, ttl=0)
    
    # Ρυθμίσεις Ημερολογίου για κινητά
    calendar_options = {
        "initialView": "listWeek",
        "locale": "el",
        "headerToolbar": {
            "left": "prev,next",
            "center": "title",
            "right": "today"
        },
        "buttonText": {"today": "Σήμερα"}
    }
    
    # Εμφάνιση του Ημερολογίου
    calendar(events=df.to_dict(orient='records'), options=calendar_options)
    
    st.write("---")
    st.info("💡 Για να το έχεις ως εφαρμογή: Πάτα τις 3 τελείες στον browser και 'Προσθήκη στην αρχική οθόνη'.")

except Exception as e:
    st.warning("🔄 Γίνεται σύνδεση με το Google Sheets...")
    st.info("Βεβαιωθείτε ότι έχετε κάνει το αρχείο 'Δημόσιο με σύνδεσμο' και ως 'Συντάκτη'.")
