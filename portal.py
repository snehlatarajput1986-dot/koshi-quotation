import streamlit as st
from datetime import datetime

# 1. Page Configuration
st.set_page_config(
    page_title="Koshi Enterprises | Central Workspace Portal",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Advanced Clean & Scaled CSS Styling
custom_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    * {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Hide Streamlit Header, Footer, Menu & Manage App Button */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stAppDeployButton {display: none;}
    [data-testid="stHeader"] {display: none;}
    [data-testid="manage-app-button"] {display: none !important;}
    div[class*="viewerBadge"] {display: none !important;}

    /* Background Setup */
    .stApp {
        background-color: #F8FAFC;
    }

    /* Premium Hero Banner */
    .hero-container {
        background: linear-gradient(135deg, #0F172A 0%, #1E3A8A 60%, #2563EB 100%);
        border-radius: 20px;
        padding: 35px 40px;
        color: white;
        margin-bottom: 25px;
        box-shadow: 0 15px 30px -5px rgba(15, 23, 42, 0.25);
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .hero-title {
        font-size: 32px !important;
        font-weight: 800;
        margin: 10px 0 5px 0;
        letter-spacing: -0.5px;
        color: #FFFFFF;
    }

    .hero-subtitle {
        color: #CBD5E1;
        font-size: 15px;
        margin: 0;
    }

    .status-badge {
        display: inline-flex;
        align-items: center;
        background: rgba(34, 197, 94, 0.2);
        border: 1px solid rgba(34, 197, 94, 0.5);
        color: #4ADE80;
        padding: 6px 14px;
        border-radius: 50px;
        font-size: 13px;
        font-weight: 600;
    }

    .pulse-dot {
        height: 8px;
        width: 8px;
        background-color: #22C55E;
        border-radius: 50%;
        display: inline-block;
        margin-right: 8px;
        box-shadow: 0 0 8px #22C55E;
    }

    /* Stat Cards */
    .stat-card {
        background: white;
        border: 1px solid #E2E8F0;
        border-radius: 16px;
        padding: 18px;
        text-align: center;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.03);
    }

    .stat-value {
        font-size: 24px;
        font-weight: 800;
        color: #0F172A;
    }

    .stat-label {
        font-size: 13px;
        color: #64748B;
        font-weight: 600;
        margin-top: 4px;
    }

    /* Tool Cards */
    .tool-card {
        background: #FFFFFF;
        border: 1.5px solid #E2E8F0;
        border-radius: 20px;
        padding: 28px;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.04);
        transition: all 0.3s ease;
    }

    .tool-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 30px rgba(37, 99, 235, 0.15);
        border-color: #2563EB;
    }

    .tool-icon {
        width: 50px;
        height: 50px;
        border-radius: 14px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        margin-bottom: 16px;
    }

    .icon-blue { background: #EFF6FF; }
    .icon-purple { background: #F5F3FF; }
    .icon-gray { background: #F1F5F9; }

    .tool-title {
        font-size: 20px;
        font-weight: 700;
        color: #0F172A;
        margin-bottom: 8px;
    }

    .tool-desc {
        font-size: 14px;
        color: #475569;
        line-height: 1.5;
        margin-bottom: 18px;
    }

    .tag-container {
        display: flex;
        gap: 8px;
        flex-wrap: wrap;
        margin-bottom: 22px;
    }

    .tag {
        font-size: 12px;
        font-weight: 600;
        padding: 5px 12px;
        border-radius: 8px;
        background: #F1F5F9;
        color: #334155;
    }

    /* Custom Open Button Style */
    .btn-link {
        display: block;
        width: 100%;
        text-align: center;
        background: #2563EB;
        color: white !important;
        text-decoration: none !important;
        font-weight: 700;
        font-size: 15px;
        padding: 13px 20px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.25);
        transition: all 0.2s ease;
    }

    .btn-link:hover {
        background: #1D4ED8;
        box-shadow: 0 6px 18px rgba(37, 99, 235, 0.4);
    }

    .btn-disabled {
        background: #E2E8F0;
        color: #94A3B8 !important;
        cursor: not-allowed;
        box-shadow: none;
    }

    .section-title {
        font-size: 18px;
        font-weight: 700;
        color: #1E293B;
        margin-top: 15px;
        margin-bottom: 15px;
    }
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# 3. Sidebar Setup
with st.sidebar:
    st.markdown("### 🏢 Koshi Enterprises")
    st.markdown("**Central Workspace Portal**")
    st.write("---")
    
    st.markdown("#### 📌 Quick Nav")
    st.markdown("• [Quotation Generator](https://koshi-quotation-opgwbqipckeu9vji2vewe6.streamlit.app/)")
    st.markdown("• [Letterhead Generator](https://koshi-letterhead-hg9ddeynmdfufmtvascpah.streamlit.app/)")
    
    st.write("---")
    st.markdown("#### 📞 Support & Info")
    st.caption("For system updates or technical issues, contact admin team.")
    st.caption(f"Last sync: {datetime.now().strftime('%d %b %Y')}")

# 4. Hero Header Section
st.markdown("""
<div class="hero-container">
    <div>
        <div class="status-badge">
            <span class="pulse-dot"></span> System Operational & Online
        </div>
        <div class="hero-title">🏢 Koshi Enterprises Workspace</div>
        <p class="hero-subtitle">Centralized portal to access all official business documents and generation tools.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# 5. Quick Metrics Row
col_s1, col_s2, col_s3, col_s4 = st.columns(4)

with col_s1:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-value" style="color: #16A34A;">Active</div>
        <div class="stat-label">System Status</div>
    </div>
    """, unsafe_allow_html=True)

with col_s2:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-value">2 Active</div>
        <div class="stat-label">Available Tools</div>
    </div>
    """, unsafe_allow_html=True)

with col_s3:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-value">SSL 256-bit</div>
        <div class="stat-label">Security Protocol</div>
    </div>
    """, unsafe_allow_html=True)

with col_s4:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-value">v2.1 Pro</div>
        <div class="stat-label">Portal Version</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 6. Active Tools Section
st.markdown('<div class="section-title">⚡ Available Workspace Modules</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

# Tool 1: Quotation Generator
with col1:
    st.markdown("""
    <div class="tool-card">
        <div>
            <div class="tool-icon icon-blue">📊</div>
            <div class="tool-title">Quotation Generator</div>
            <p class="tool-desc">Quickly generate standard L1, L2, L3 quotation PDFs with automated pricing calculation, tax rules, and company layout.</p>
            <div class="tag-container">
                <span class="tag">📄 Instant PDF Export</span>
                <span class="tag">🏷️ L1 / L2 / L3 Formats</span>
                <span class="tag">🧾 GST Compliant</span>
            </div>
        </div>
        <a href="https://koshi-quotation-opgwbqipckeu9vji2vewe6.streamlit.app/" target="_blank" class="btn-link">
            Open Quotation Generator 🚀
        </a>
    </div>
    """, unsafe_allow_html=True)

# Tool 2: Letterhead Generator
with col2:
    st.markdown("""
    <div class="tool-card">
        <div>
            <div class="tool-icon icon-purple">✉️</div>
            <div class="tool-title">Letterhead Generator</div>
            <p class="tool-desc">Create official Koshi Enterprises letterhead documents with aligned headers, footer details, and printable formatting.</p>
            <div class="tag-container">
                <span class="tag">🏢 Corporate Design</span>
                <span class="tag">🖨️ A4 Print Ready</span>
                <span class="tag">✍️ Signature Line</span>
            </div>
        </div>
        <a href="https://koshi-letterhead-hg9ddeynmdfufmtvascpah.streamlit.app/" target="_blank" class="btn-link">
            Open Letterhead Generator 🚀
        </a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# 7. Future Modules
st.markdown('<div class="section-title">🔮 Upcoming Enterprise Tools</div>', unsafe_allow_html=True)

col3, col4 = st.columns(2)

with col3:
    st.markdown("""
    <div class="tool-card" style="opacity: 0.75;">
        <div>
            <div class="tool-icon icon-gray">📑</div>
            <div class="tool-title">GST Invoice & Billing</div>
            <p class="tool-desc">Generate official GST tax invoices, billing receipts, and keep track of payment entries.</p>
            <div class="tag-container">
                <span class="tag">In Development</span>
            </div>
        </div>
        <a class="btn-link btn-disabled">Coming Soon 🔒</a>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="tool-card" style="opacity: 0.75;">
        <div>
            <div class="tool-icon icon-gray">📦</div>
            <div class="tool-title">Inventory & Stock Tracker</div>
            <p class="tool-desc">Track stock levels, record incoming items, and view real-time low stock notifications.</p>
            <div class="tag-container">
                <span class="tag">In Development</span>
            </div>
        </div>
        <a class="btn-link btn-disabled">Coming Soon 🔒</a>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<hr style="border: none; border-top: 1px solid #E2E8F0; margin-top: 50px; margin-bottom: 20px;">
<div style="text-align: center; color: #64748B; font-size: 13px;">
    © Koshi Enterprises Central Workspace • Internal Business Portal
</div>
""", unsafe_allow_html=True)
