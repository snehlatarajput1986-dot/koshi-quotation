import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Koshi Enterprises Web Portal",
    page_icon="🏢",
    layout="wide"
)

# Hide Streamlit Default Header, Menu & Footer
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stAppDeployButton {display:none;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Main Title Section
st.markdown("<h1 style='text-align: center;'>🏢 KOSHI ENTERPRISES WEB PORTAL</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Aapka central workspace — Kisi bhi tool ko open karne ke liye niche click karein:</p>", unsafe_allow_html=True)

st.write("---")

# Quick Metrics Row
col_m1, col_m2, col_m3 = st.columns(3)
with col_m1:
    st.metric(label="📊 Quick Status", value="Active")
with col_m2:
    st.metric(label="📝 Tools Available", value="2")
with col_m3:
    st.metric(label="🌐 System", value="Online")

st.write("---")

# Tools Cards Section
col1, col2 = st.columns(2)

# Tool 1: Quotation Generator
with col1:
    with st.container(border=True):
        st.subheader("📝 Quotation Generator")
        st.write("Generate L1, L2, L3 Quotations quickly with automated formatting.")
        st.write("")  # Spacing
        # Link to Quotation Generator
        st.link_button(
            label="Open Quotation Generator 🚀",
            url="https://koshi-quotation-opgwbqipckeu9vji2vewe6.streamlit.app/",
            use_container_width=True
        )

# Tool 2: Letterhead Generator
with col2:
    with st.container(border=True):
        st.subheader("📝 Letterhead Generator")
        st.write("Create official Koshi Enterprises letterheads in standard layout.")
        st.write("")  # Spacing
        # Link to Letterhead Generator
        st.link_button(
            label="Open Letterhead Generator 🚀",
            url="https://koshi-letterhead-hg9ddeynmdfufmtvascpah.streamlit.app/",
            use_container_width=True
        )
