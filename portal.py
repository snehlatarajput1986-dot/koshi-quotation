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

# Exact Direct Links mapped from your Streamlit dashboard
st.link_button("📄 Open Quotation Generator (L1, L2, L3)", "https://koshi-quotation-6g7gym9uow5juafcpvrccs.streamlit.app/") 

st.write("") 

st.link_button("📝 Open Letterhead Generator", "https://koshi-letterhead.streamlit.app/")

st.markdown("---")
st.caption("Powered by Koshi Enterprises")
