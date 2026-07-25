import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Koshi Enterprises | Central Workspace Portal",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Advanced Custom CSS Styling
custom_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Hide Streamlit Header, Footer, and Menu */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stAppDeployButton {display: none;}
    [data-testid="stHeader"] {display: none;}
    
    /* Global App Background */
    .stApp {
        background-color: #F8FAFC;
    }

    /* Hero Banner Styling */
    .hero-container {
        background: linear-gradient(135deg, #0F172A 0%, #1E3A8A 50%, #1E293B 100%);
        border-radius: 20px;
        padding: 40px;
        color: white;
        margin-bottom: 30px;
        box-shadow: 0 20px 25px -5px rgba(15, 23, 42, 0.25);
        position: relative;
        overflow: hidden;
    }

    .hero-title {
        font-size: 38px;
        font-weight: 800;
        margin: 0;
        letter-spacing: -0.5px;
        background: linear-gradient(90deg, #FFFFFF 0%, #93C5FD 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero-subtitle {
        color: #94A3B8;
        font-size: 16px;
        margin-top: 8px;
        margin-bottom: 0;
    }

    .status-badge {
        display: inline-flex;
        align-items: center;
        background: rgba(34, 197, 94, 0.15);
        border: 1px solid rgba(34, 197, 94, 0.4);
        color: #4ADE80;
        padding: 6px 14px;
        border-radius: 50px;
        font-size: 13px;
        font-weight: 600;
        margin-bottom: 16px;
    }

    .pulse-dot {
        height: 8px;
        width: 8px;
        background-color: #22C55E;
        border-radius: 50%;
        display: inline-block;
        margin-right: 8px;
        box-shadow: 0 0 10px #22C55E;
    }

    /* Stat Cards */
    .stat-card {
        background: white;
        border: 1px solid #E2E8F0;
        border-radius: 16px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        transition: all 0.3s ease;
    }
    
    .stat-card:hover {
        border-color: #3B82F6;
        box-shadow: 0 10px 15px -3px rgba(59, 130, 246, 0.1);
    }

    .stat-value {
        font-size: 26px;
        font-weight: 800;
        color: #0F172A;
    }

    .stat-label {
        font-size: 13px;
        color: #64748B;
        font-weight: 500;
        margin-top: 4px;
    }

    /* Tool Cards Container */
    .tool-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 20px;
        padding: 30px;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.04);
        transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
    }

    .tool-card:hover {
        transform: translateY(-6px);
        box-shadow: 0 20px 25px -5px rgba(37, 99, 235, 0.12);
        border-color: #3B82F6;
    }

    .tool-icon {
        width: 52px;
        height: 52px;
        border-radius: 14px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 26px;
        margin-bottom: 20px;
    }

    .icon-blue { background: #EFF6FF; color: #2563EB; }
    .icon-purple { background: #F5F3FF; color: #7C3AED; }
    .icon-gray { background: #F1F5F9; color: #94A3B8; }

    .tool-title {
        font-size: 22px;
        font-weight: 700;
        color: #0F172A;
        margin-bottom: 10px;
    }

    .tool-desc {
        font-size: 14px;
        color: #64748B;
        line-height: 1.6;
        margin-bottom: 20px;
    }

    .tag-container {
        display: flex;
        gap: 8px;
        flex-wrap: wrap;
        margin-bottom: 25px;
    }

    .tag {
        font-size: 11px;
        font-weight: 600;
        padding: 4px 10px;
        border-radius: 6px;
        background: #F1F5F9;
        color: #475569;
    }

    /* Custom Open Button Style */
    .btn-link {
        display: block;
        width: 100%;
        text-align: center;
        background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%);
        color: white !important;
        text-decoration: none !important;
        font-weight: 600;
        font-size: 15px;
        padding: 14px 20px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
        transition: all 0.2s ease;
    }

    .btn-link:hover {
        background: linear-gradient(135deg, #1D4ED8 0%, #1E40AF 100%);
        box-shadow: 0 6px 18px rgba(37, 99, 235, 0.45);
        transform: scale(1.01);
    }

    .btn-disabled {
        background: #E2E8F0;
        color: #94A3B8 !important;
        cursor: not-allowed;
        box-shadow: none;
    }

    /* Section Title */
    .section-title {
        font-size: 18px;
        font-weight: 700;
        color: #334155;
        margin-top: 10px;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# 3. Hero Header Section
st.markdown("""
<div class="hero-container">
    <div class="status-badge">
        <span class="pulse-dot"></span> System Operational & Online
    </div>
    <h1 class="hero-title">🏢 Koshi Enterprises Central Workspace</h1>
    <p class="hero-subtitle">Select any module below to quickly launch standard office generators and tools.</p>
</div>
""", unsafe_allow_html=True)

# 4. Quick Metrics Section
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
        <div class="stat-value">2</div>
        <div class="stat-label">Live Tools</div>
    </div>
    """, unsafe_allow_html=True)

with col_s3:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-value">SSL</div>
        <div class="stat-label">Encrypted Connection</div>
    </div>
    """, unsafe_allow_html=True)

with col_s4:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-value">v2.0</div>
        <div class="stat-label">Portal Version</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 5. Core Active Applications Section
st.markdown('<div class="section-title">⚡ Available Workspace Modules</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

# Tool 1: Quotation Generator
with col1:
    st.markdown("""
    <div class="tool-card">
        <div>
            <div class="tool-icon icon-blue">📊</div>
            <div class="tool-title">Quotation Generator</div>
            <p class="tool-desc">Create professional L1, L2, and L3 quotations with automated pricing formulas, GST compliance, and standard printable formatting.</p>
            <div class="tag-container">
                <span class="tag">⚡ Instant PDF</span>
                <span class="tag">🏷️ L1 / L2 / L3</span>
                <span class="tag">🧾 GST Formatting</span>
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
            <p class="tool-desc">Generate official Koshi Enterprises letterheads with pre-aligned corporate layouts, digital signatures, and high-resolution exports.</p>
            <div class="tag-container">
                <span class="tag">📄 Official Design</span>
                <span class="tag">🖨️ Print Ready</span>
                <span class="tag">✍️ Signature Support</span>
            </div>
        </div>
        <a href="https://koshi-letterhead-hg9ddeynmdfufmtvascpah.streamlit.app/" target="_blank" class="btn-link">
            Open Letterhead Generator 🚀
        </a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# 6. Future Expansion / Upcoming Tools Section (Optional)
st.markdown('<div class="section-title">🔮 Upcoming Modules (Under Development)</div>', unsafe_allow_html=True)

col3, col4 = st.columns(2)

with col3:
    st.markdown("""
    <div class="tool-card" style="opacity: 0.7;">
        <div>
            <div class="tool-icon icon-gray">📑</div>
            <div class="tool-title">GST Invoice & Billing</div>
            <p class="tool-desc">Automated tax invoices, payment receipt generator, and ledger tracker for quick billing.</p>
            <div class="tag-container">
                <span class="tag">Coming Soon</span>
            </div>
        </div>
        <a class="btn-link btn-disabled">Coming Soon 🔒</a>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="tool-card" style="opacity: 0.7;">
        <div>
            <div class="tool-icon icon-gray">📦</div>
            <div class="tool-title">Inventory & Stock Tracker</div>
            <p class="tool-desc">Real-time stock monitoring, vendor management, and automated stock alert dashboard.</p>
            <div class="tag-container">
                <span class="tag">Under Development</span>
            </div>
        </div>
        <a class="btn-link btn-disabled">Coming Soon 🔒</a>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<hr style="border: none; border-top: 1px solid #E2E8F0; margin-top: 40px; margin-bottom: 20px;">
<div style="text-align: center; color: #94A3B8; font-size: 13px;">
    © Koshi Enterprises Central Portal • Secure Internal Workspace
</div>
""", unsafe_allow_html=True)
