import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Koshi Enterprises Portal",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Futuristic Dark Purple Neon Theme
st.markdown("""
    <style>
    /* Main Dark Background with Neon Gradient Glow */
    .stApp {
        background: radial-gradient(circle at top center, #2e0854 0%, #0d021a 70%, #05010a 100%);
        color: #ffffff;
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #0b0314;
        border-right: 1px solid #3b1366;
    }
    
    /* Glowing Hero Banner */
    .hero-box {
        background: linear-gradient(135deg, rgba(147, 51, 234, 0.2) 0%, rgba(79, 70, 229, 0.2) 100%);
        border: 1px solid #a855f7;
        border-radius: 16px;
        padding: 35px;
        text-align: center;
        box-shadow: 0 0 25px rgba(168, 85, 247, 0.3);
        margin-bottom: 30px;
    }
    .status-pill {
        background: #a855f7;
        color: #ffffff;
        padding: 4px 14px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 700;
        display: inline-block;
        margin-bottom: 12px;
        box-shadow: 0 0 10px #a855f7;
    }
    .hero-title {
        font-size: 32px;
        font-weight: 800;
        color: #ffffff;
        text-shadow: 0 0 10px rgba(255, 255, 255, 0.5);
    }
    .hero-desc {
        color: #d8b4fe;
        font-size: 15px;
    }

    /* Metric Cards Glow */
    div[data-testid="stMetric"] {
        background: rgba(20, 7, 38, 0.8);
        padding: 15px 20px;
        border-radius: 12px;
        border: 1px solid #581c87;
        box-shadow: 0 4px 15px rgba(147, 51, 234, 0.15);
    }

    /* Module Cards Neon Effect */
    .module-card {
        background: rgba(23, 10, 41, 0.9);
        border-radius: 14px;
        padding: 24px;
        border: 1px solid #7e22ce;
        box-shadow: 0 0 15px rgba(126, 34, 206, 0.2);
        margin-bottom: 15px;
    }
    .module-title {
        font-size: 20px;
        font-weight: 700;
        color: #f3e8ff;
        margin-bottom: 8px;
    }
    .module-desc {
        font-size: 14px;
        color: #c084fc;
        line-height: 1.5;
    }
    
    /* Neon Link Buttons */
    .stButton>button, div.stLinkButton>a {
        background: linear-gradient(90deg, #9333ea 0%, #c084fc 100%) !important;
        color: white !important;
        border: none !important;
        font-weight: bold !important;
        box-shadow: 0 0 12px rgba(168, 85, 247, 0.5) !important;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------- SIDEBAR -----------------
with st.sidebar:
    st.markdown("### 🔮 Koshi Enterprises")
    st.caption("Central Workspace Portal")
    
    st.divider()
    
    st.markdown("📌 **Quick Nav**")
    st.markdown("• [Quotation Generator](https://koshi-quotation-opgwbqipckeu9vji2vewe6.streamlit.app/)")
    st.markdown("• [Letterhead Generator](https://koshi-letterhead-hg9ddeynmdfufmtvascpah.streamlit.app/)")
    
    st.divider()
    
    st.markdown("📞 **Support & Info**")
    st.caption("For system updates or technical issues, contact admin team.")
    
    st.markdown("📱 **Phone:** +91 8864097233")
    st.markdown("✉️ **Email:** prashantkumarsaharsa5@gmail.com")
    
    st.caption("Last sync: 25 Jul 2026")

# ----------------- MAIN PORTAL -----------------

# Top Hero Banner
st.markdown("""
    <div class="hero-box">
        <div class="status-pill">⚡ SYSTEM ONLINE</div>
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
