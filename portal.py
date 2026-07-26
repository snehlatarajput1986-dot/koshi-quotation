import streamlit as st

st.set_page_config(
    page_title="Koshi Enterprises - Workspace Portal",
    page_icon="🏢",
    layout="wide"
)

# Custom Workspace Styling
st.markdown("""
    <style>
    .portal-header {
        background: linear-gradient(135deg, #1E1E2E 0%, #2A2D3E 100%);
        padding: 25px;
        border-radius: 12px;
        color: white;
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    .metric-card {
        background: #1E1E2E;
        color: white;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #3A3D52;
        text-align: center;
    }
    .module-card {
        background: #1E1E2E;
        border: 1px solid #3A3D52;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        color: white;
    }
    .btn-link {
        display: inline-block;
        width: 100%;
        background-color: #6366F1;
        color: white !important;
        text-align: center;
        padding: 10px 0;
        border-radius: 6px;
        text-decoration: none;
        font-weight: bold;
        margin-top: 15px;
    }
    .btn-link:hover {
        background-color: #4F46E5;
    }
    </style>
""", unsafe_allow_html=True)

# Workspace Header
st.markdown("""
    <div class="portal-header">
        <span style="background-color: #312E81; color: #A5B4FC; padding: 4px 10px; border-radius: 12px; font-size: 12px; font-weight: bold;">● SYSTEM OPERATIONAL & ONLINE</span>
        <h2 style="margin: 10px 0 5px 0;">🏢 Koshi Enterprises Workspace</h2>
        <p style="margin: 0; color: #9CA3AF;">Centralized portal to access all official business documents and generation tools.</p>
    </div>
""", unsafe_allow_html=True)

# Top Metrics Bar
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("<div class='metric-card'><small>System Status</small><h3>Active</h3></div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='metric-card'><small>Available Tools</small><h3>3 Active</h3></div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div class='metric-card'><small>Security Protocol</small><h3>SSL 256-bit</h3></div>", unsafe_allow_html=True)
with col4:
    st.markdown("<div class='metric-card'><small>Portal Version</small><h3>v2.2 Pro</h3></div>", unsafe_allow_html=True)

st.markdown("<br><h3>⚡ Available Workspace Modules</h3>", unsafe_allow_html=True)

# Module Cards Layout (3 Columns for 3 Tools)
m_col1, m_col2, m_col3 = st.columns(3)

with m_col1:
    st.markdown("""
        <div class="module-card">
            <h4>📊 Quotation Generator</h4>
            <p style="font-size: 13px; color: #9CA3AF; height: 50px;">Quickly generate standard L1, L2, L3 quotation PDFs with automated pricing calculation and company layout.</p>
            <a href="https://koshi-quotation-6q7gyn9uew5juafcpvroes.streamlit.app/" target="_blank" class="btn-link">Open Quotation Generator 🚀</a>
        </div>
    """, unsafe_allow_html=True)

with m_col2:
    st.markdown("""
        <div class="module-card">
            <h4>📄 Letterhead Generator</h4>
            <p style="font-size: 13px; color: #9CA3AF; height: 50px;">Create official Koshi Enterprises letterhead documents with aligned headers, footer details, and printable formatting.</p>
            <a href="https://koshi-quotation-6q7gyn9uew5juafcpvroes.streamlit.app/" target="_blank" class="btn-link">Open Letterhead Generator 🚀</a>
        </div>
    """, unsafe_allow_html=True)

with m_col3:
    st.markdown("""
        <div class="module-card">
            <h4>📝 Resume Builder</h4>
            <p style="font-size: 13px; color: #9CA3AF; height: 50px;">Create professional resumes with live preview, customizable sections, and instant print/PDF download option.</p>
            <a href="https://koshi-quotation-finzqjhfwlm8nsc8pxnguq.streamlit.app/" target="_blank" class="btn-link">Open Resume Builder 🚀</a>
        </div>
    """, unsafe_allow_html=True)
