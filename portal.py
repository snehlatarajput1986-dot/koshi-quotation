import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Koshi Enterprises Portal",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling for Modern Dark/Blue Theme
st.markdown("""
    <style>
    /* Gradient Hero Banner */
    .hero-banner {
        background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
        color: white;
        padding: 24px 32px;
        border-radius: 16px;
        box-shadow: 0 10px 15px -3px rgba(37, 99, 235, 0.2);
        margin-bottom: 25px;
    }
    .hero-status {
        background-color: rgba(255, 255, 255, 0.15);
        color: #e0e7ff;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 13px;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 10px;
    }
    .hero-title {
        font-size: 28px;
        font-weight: 800;
        margin: 0;
        color: white;
    }
    .hero-sub {
        color: #cbd5e1;
        font-size: 14px;
        margin-top: 6px;
    }
    
    /* Modern Cards */
    .card-box {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 24px;
        height: 100%;
        transition: all 0.3s ease;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------- SIDEBAR SECTION -----------------
with st.sidebar:
    st.title("🏢 Koshi Enterprises")
    st.caption("Central Workspace Portal")
    
    st.divider()
    
    st.markdown("### 📌 Quick Nav")
    st.markdown("• [Quotation Generator](https://koshi-quotation-opgwbqipckeu9vji2vewe6.streamlit.app/)")
    st.markdown("• [Letterhead Generator](https://koshi-letterhead-hg9ddeynmdfufmtvascpah.streamlit.app/)")
    
    st.divider()
    
    # Updated Support & Info Section
    st.markdown("### 📞 Support & Info")
    st.caption("For system updates or technical issues, contact admin team.")
    
    st.markdown("📱 **Phone:** +91 8864097233")
    st.markdown("✉️ **Email:** prashantkumarsaharsa5@gmail.com")
    
    st.caption("Last sync: 25 Jul 2026")

# ----------------- MAIN DASHBOARD -----------------

# Top Banner
st.markdown("""
    <div class="hero-banner">
        <div class="hero-status">🟢 System Operational & Online</div>
        <div class="hero-title">🏢 Koshi Enterprises Workspace</div>
        <div class="hero-sub">Centralized portal to access all official business documents and generation tools.</div>
    </div>
""", unsafe_allow_html=True)

# Metric Metrics Row
col1, col2, col3, col4 = st.columns(4)
col1.metric("System Status", "Active")
col2.metric("Available Tools", "2 Active")
col3.metric("Security Protocol", "SSL 256-bit")
col4.metric("Portal Version", "v2.1 Pro")

st.markdown("<br>", unsafe_allow_html=True)
st.subheader("⚡ Available Workspace Modules")

# Tools Cards Layout
col_a, col_b = st.columns(2)

with col_a:
    st.markdown("""
        <div class="card-box">
            <h4>📊 Quotation Generator</h4>
            <p style="color: #64748b; font-size: 14px;">Quickly generate standard L1, L2, L3 quotation PDFs with automated pricing calculation, tax rules, and company layout.</p>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("Open Quotation Generator 🚀", "https://koshi-quotation-opgwbqipckeu9vji2vewe6.streamlit.app/", use_container_width=True)

with col_b:
    st.markdown("""
        <div class="card-box">
            <h4>📄 Letterhead Generator</h4>
            <p style="color: #64748b; font-size: 14px;">Create official Koshi Enterprises letterhead documents with aligned headers, footer details, and printable formatting.</p>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("Open Letterhead Generator 🚀", "https://koshi-letterhead-hg9ddeynmdfufmtvascpah.streamlit.app/", use_container_width=True)

st.markdown("---")
st.caption("© 2026 Koshi Enterprises. All rights reserved.")
