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

# Note: In URLs ko apni Streamlit deployed apps ke links se update kar sakte hain
st.link_button("📄 Open Quotation Generator (L1, L2, L3)", "https://share.streamlit.io") 

st.write("") 

st.link_button("📝 Open Letterhead Generator", "https://share.streamlit.io")

st.markdown("---")
st.caption("Powered by Koshi Enterprises")
