import streamlit as st

st.set_page_config(page_title="KOSHI ENTERPRISES - Web Portal", page_icon="🏢", layout="centered")

st.markdown("""
    <style>
    .stButton>button, .stLinkButton>a {
        width: 100% !important;
        height: 65px !important;
        font-size: 18px !important;
        font-weight: bold !important;
        border-radius: 10px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🏢 KOSHI ENTERPRISES WEB PORTAL")
st.write("Niche kisi bhi tool par click karke direct page open karein:")

st.markdown("---")

# Link 1: Quotation Generator
st.link_button("📄 Open Quotation Generator (L1, L2, L3)", "https://koshi-quotation-opgwbqipckeu9vji2vewe6.streamlit.app/") 

st.write("") 

# Link 2: Letterhead Generator
st.link_button("📝 Open Letterhead Generator", "https://koshi-letterhead-hg9ddeynmdfufmtvascpah.streamlit.app/")

st.markdown("---")
st.caption("Powered by Koshi Enterprises")
