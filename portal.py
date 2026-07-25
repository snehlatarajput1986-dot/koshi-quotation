import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Koshi Enterprises Portal",
    page_icon="🏢",
    layout="wide"
)

# Custom CSS for UI Enhancement
st.markdown("""
    <style>
    .main-title {
        text-align: center;
        color: #1E3A8A;
        font-size: 32px;
        font-weight: bold;
        margin-bottom: 5px;
    }
    .sub-title {
        text-align: center;
        color: #4B5563;
        font-size: 16px;
        margin-bottom: 25px;
    }
    .card {
        background-color: #F8FAFC;
        padding: 20px;
        border-radius: 12px;
        border-left: 5px solid #2563EB;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.05);
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.markdown('<div class="main-title">🏢 KOSHI ENTERPRISES WEB PORTAL</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Aapka central workspace — Kisi bhi tool ko open karne ke liye niche click karein:</div>', unsafe_allow_html=True)

st.divider()

# Quick Metrics Row
col1, col2, col3 = st.columns(3)
col1.metric(label="📊 Quick Status", value="Active")
col2.metric(label="📑 Tools Available", value="2")
col3.metric(label="🌐 System", value="Online")

st.divider()

# Tools Cards Layout
col_a, col_b = st.columns(2)

with col_a:
    st.markdown("""
        <div class="card">
            <h3>📝 Quotation Generator</h3>
            <p>Generate L1, L2, L3 Quotations quickly with automated formatting.</p>
        </div>
    """, unsafe_allow_html=True)
    # Quotation Generator Link
    st.link_button("Open Quotation Generator 🚀", "https://koshi-quotation-opgwbqipckeu9vji2vewe6.streamlit.app/", use_container_width=True)

with col_b:
    st.markdown("""
        <div class="card">
            <h3>📑 Letterhead Generator</h3>
            <p>Create official Koshi Enterprises letterheads in standard layout.</p>
        </div>
    """, unsafe_allow_html=True)
    # Letterhead Generator Link
    st.link_button("Open Letterhead Generator 🚀", "https://koshi-letterhead-hg9ddeynmdfufmtvascpah.streamlit.app/", use_container_width=True)

# Footer
st.markdown("---")
st.caption("Powered by Koshi Enterprises | Internal Portal")
