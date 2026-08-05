import streamlit as st

st.set_page_config(
    page_title="Koshi Enterprises - Workspace Portal",
    page_icon="🏢",
    layout="wide"
)

# --- FACEBOOK-INSPIRED PREMIUM THEME CSS ---
st.markdown("""
    <style>
    /* Main Streamlit App Background */
    .stApp {
        background-color: #f0f2f5;
        color: #1c1e21;
        font-family: Helvetica, Arial, sans-serif;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #ced0d4;
        padding-top: 20px;
    }
    
    [data-testid="stSidebar"] .stRadio label {
        color: #1c1e21 !important;
        font-weight: 600 !important;
    }

    /* Portal Header Banner */
    .portal-header {
        background: linear-gradient(135deg, #1877f2 0%, #166fe5 100%);
        padding: 25px;
        border-radius: 10px;
        color: white;
        margin-bottom: 25px;
        box-shadow: 0 2px 6px rgba(24, 119, 242, 0.3);
    }
    
    /* Metric Card */
    .metric-card {
        background: #ffffff;
        color: #1c1e21;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #ccd0d5;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    
    /* Module Card */
    .module-card {
        background: #ffffff;
        border: 1px solid #ccd0d5;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        color: #1c1e21;
        box-shadow: 0 2px 4px rgba(0,0,0,0.08);
    }
    
    /* Action Link Button Styling */
    .btn-link {
        display: inline-block;
        width: 100%;
        background-color: #1877f2;
        color: white !important;
        text-align: center;
        padding: 10px 0;
        border-radius: 6px;
        text-decoration: none;
        font-weight: bold;
        margin-top: 15px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .btn-link:hover {
        background-color: #166fe5;
    }

    h1, h2, h3, h4 {
        color: #1c1e21 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION & HELP CENTER ---
st.sidebar.image("https://img.icons8.com/color/96/company.png", width=65)
st.sidebar.markdown("### 🏢 Koshi Workspace")
st.sidebar.markdown("---")

nav_selection = st.sidebar.radio(
    "📌 Navigation Menu",
    ["🏠 Dashboard Home", "📊 Quotation Generator", "📄 Letterhead Generator", "📝 Resume Builder"]
)

st.sidebar.markdown("---")
st.sidebar.header("🛠️ Available Modules")
st.sidebar.markdown("""
- **L1, L2, L3 Quotation Engine**
- **Official Letterhead Module**
- **Professional Resume Builder**
""")

st.sidebar.markdown("---")
st.sidebar.header("🆘 Help Center & Support")
st.sidebar.markdown("""
<div style="background-color: #e7f3ff; padding: 12px; border-radius: 6px; font-size: 13px; color: #1c1e21; border: 1px solid #b8daff;">
    <b>Need Assistance?</b><br><br>
    📞 <b>Helpline:</b> +91 8541887622<br>
    ✉️ <b>Support:</b> support@koshienterprises.in<br>
    🕒 <b>Timing:</b> 9:00 AM - 7:00 PM
</div>
""", unsafe_allow_html=True)

# --- MAIN CONTENT AREA DYNAMIC ROUTING ---
if nav_selection == "🏠 Dashboard Home":
    
    # Workspace Header Banner
    st.markdown("""
        <div class="portal-header">
            <span style="background-color: rgba(255,255,255,0.2); color: white; padding: 4px 10px; border-radius: 12px; font-size: 12px; font-weight: bold; border: 1px solid rgba(255,255,255,0.4);">● SYSTEM OPERATIONAL & ONLINE</span>
            <h2 style="margin: 10px 0 5px 0; color: white !important;">🏢 Koshi Enterprises Workspace</h2>
            <p style="margin: 0; color: #f0f2f5; font-size: 14px;">Centralized portal to access all official business documents and generation tools securely.</p>
        </div>
    """, unsafe_allow_html=True)

    # Top Metrics Bar
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("<div class='metric-card'><small style='color:#65676b;'>System Status</small><h3 style='color:#1877f2 !important; margin:5px 0 0 0;'>Active</h3></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='metric-card'><small style='color:#65676b;'>Available Tools</small><h3 style='color:#1877f2 !important; margin:5px 0 0 0;'>3 Active</h3></div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='metric-card'><small style='color:#65676b;'>Security Protocol</small><h3 style='color:#1877f2 !important; margin:5px 0 0 0;'>SSL 256-bit</h3></div>", unsafe_allow_html=True)
    with col4:
        st.markdown("<div class='metric-card'><small style='color:#65676b;'>Portal Version</small><h3 style='color:#1877f2 !important; margin:5px 0 0 0;'>v3.0 Pro</h3></div>", unsafe_allow_html=True)

    st.markdown("<br><h3>⚡ Available Workspace Modules</h3>", unsafe_allow_html=True)

    # Module Cards Layout (3 Columns for 3 Tools with original links)
    m_col1, m_col2, m_col3 = st.columns(3)

    with m_col1:
        st.markdown("""
            <div class="module-card">
                <h4 style="color:#1877f2 !important;">📊 Quotation Generator</h4>
                <p style="font-size: 13px; color: #65676b; height: 50px;">Quickly generate standard L1, L2, L3 quotation PDFs with automated pricing calculation and company layout.</p>
                <a href="https://koshi-quotation-opgwbqipckeu9vji2vewe6.streamlit.app/" target="_blank" class="btn-link">Open Quotation Generator 🚀</a>
            </div>
        """, unsafe_allow_html=True)

    with m_col2:
        st.markdown("""
            <div class="module-card">
                <h4 style="color:#1877f2 !important;">📄 Letterhead Generator</h4>
                <p style="font-size: 13px; color: #65676b; height: 50px;">Create official Koshi Enterprises letterhead documents with aligned headers, footer details, and printable formatting.</p>
                <a href="https://koshi-letterhead-hg9ddeynmdfufmtvascpah.streamlit.app/" target="_blank" class="btn-link">Open Letterhead Generator 🚀</a>
            </div>
        """, unsafe_allow_html=True)

    with m_col3:
        st.markdown("""
            <div class="module-card">
                <h4 style="color:#1877f2 !important;">📝 Resume Builder</h4>
                <p style="font-size: 13px; color: #65676b; height: 50px;">Create professional resumes with live preview, customizable sections, and instant print/PDF download option.</p>
                <a href="https://koshi-quotation-finzqjhfwlm8nsc8pxnguq.streamlit.app/" target="_blank" class="btn-link">Open Resume Builder 🚀</a>
            </div>
        """, unsafe_allow_html=True)

elif nav_selection == "📊 Quotation Generator":
    st.header("📊 Quotation Generator Module")
    st.markdown("Aap direct bhi link open kar sakte hain ya apna quotation tool yahan embed kar sakte hain:")
    st.markdown("[Click here to open Quotation App in New Tab](https://koshi-quotation-opgwbqipckeu9vji2vewe6.streamlit.app/)", unsafe_allow_html=True)

elif nav_selection == "📄 Letterhead Generator":
    st.header("📄 Letterhead Generator Module")
    st.markdown("Aap direct bhi link open kar sakte hain:")
    st.markdown("[Click here to open Letterhead App in New Tab](https://koshi-letterhead-hg9ddeynmdfufmtvascpah.streamlit.app/)", unsafe_allow_html=True)

elif nav_selection == "📝 Resume Builder":
    st.header("📝 Resume Builder Module")
    st.markdown("Aap direct bhi link open kar sakte hain:")
    st.markdown("[Click here to open Resume Builder App in New Tab](https://koshi-quotation-finzqjhfwlm8nsc8pxnguq.streamlit.app/)", unsafe_allow_html=True)
