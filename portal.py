import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Koshi Enterprises Portal",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Exact Matching Theme CSS
st.markdown("""
    <style>
    /* Main Background & Fonts */
    .stApp {
        background-color: #FAFAFC;
    }
    
    /* Sleek Blue Hero Banner */
    .hero-box {
        background: linear-gradient(90deg, #2563EB 0%, #3B82F6 100%);
        border-radius: 16px;
        padding: 30px;
        color: white;
        box-shadow: 0 10px 25px -5px rgba(37, 99, 235, 0.25);
        margin-bottom: 25px;
    }
    .status-pill {
        background: rgba(255, 255, 255, 0.2);
        color: #FFFFFF;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 12px;
    }
    .hero-title {
        font-size: 28px;
        font-weight: 800;
        color: #FFFFFF;
        margin-bottom: 6px;
    }
    .hero-desc {
        color: #E0E7FF;
        font-size: 14px;
    }
    
    /* Clean Metric Boxes */
    div[data-testid="stMetric"] {
        background-color: #FFFFFF;
        padding: 15px 20px;
        border-radius: 12px;
        border: 1px solid #E5E7EB;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }

    /* Clean Module Cards */
    .module-card {
        background: #FFFFFF;
        border-radius: 14px;
        padding: 20px;
        border: 1px solid #E5E7EB;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
        margin-bottom: 10px;
    }
    .module-title {
        font-size: 18px;
        font-weight: 700;
        color: #1F2937;
        margin-bottom: 8px;
    }
    .module-desc {
        font-size: 13px;
        color: #6B7280;
        line-height: 1.5;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------- SIDEBAR -----------------
with st.sidebar:
    st.markdown("### 🏢 Koshi Enterprises")
    st.caption("Central Workspace Portal")
    
    st.divider()
    
    st.markdown("📌 **Quick Nav**")
    st.markdown("• [Quotation Generator](https://koshi-quotation-opgwbqipckeu9vji2vewe6.streamlit.app/)")
    st.markdown("• [Letterhead Generator](https://koshi-letterhead-hg9ddeynmdfufmtvascpah.streamlit.app/)")
    
    st.divider()
    
    # Updated Support & Info Details
    st.markdown("📞 **Support & Info**")
    st.caption("For system updates or technical issues, contact admin team.")
    
    st.markdown("📱 **Phone:** +91 8864097233")
    st.markdown("✉️ **Email:** prashantkumarsaharsa5@gmail.com")
    
    st.caption("Last sync: 25 Jul 2026")

# ----------------- MAIN PORTAL -----------------

# Top Hero Banner
st.markdown("""
    <div class="hero-box">
        <div class="status-pill">🟢 System Operational & Online</div>
        <div class="hero-title">🏢 Koshi Enterprises Workspace</div>
        <div class="hero-desc">Centralized portal to access all official business documents and generation tools.</div>
    </div>
""", unsafe_allow_html=True)

# Status Metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric(label="System Status", value="Active")
col2.metric(label="Available Tools", value="2 Active")
col3.metric(label="Security Protocol", value="SSL 256-bit")
col4.metric(label="Portal Version", value="v2.1 Pro")

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("### ⚡ Available Workspace Modules")

# Module Cards & Open Buttons
col_a, col_b = st.columns(2)

with col_a:
    st.markdown("""
        <div class="module-card">
            <div class="module-title">📊 Quotation Generator</div>
            <div class="module-desc">Quickly generate standard L1, L2, L3 quotation PDFs with automated pricing calculation, tax rules, and company layout.</div>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("Open Quotation Generator 🚀", "https://koshi-quotation-opgwbqipckeu9vji2vewe6.streamlit.app/", use_container_width=True)

with col_b:
    st.markdown("""
        <div class="module-card">
            <div class="module-title">📑 Letterhead Generator</div>
            <div class="module-desc">Create official Koshi Enterprises letterhead documents with aligned headers, footer details, and printable formatting.</div>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("Open Letterhead Generator 🚀", "https://koshi-letterhead-hg9ddeynmdfufmtvascpah.streamlit.app/", use_container_width=True)

st.markdown("---")
st.caption("© 2026 Koshi Enterprises. All rights reserved.")
