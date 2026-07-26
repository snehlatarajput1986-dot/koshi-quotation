import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

st.set_page_config(page_title="Custom Multi-Format Quotation Generator", page_icon="📄", layout="wide")

# --- FACEBOOK-INSPIRED THEME CSS ---
st.markdown("""
<style>
    /* Main Streamlit App Background */
    .stApp {
        background-color: #f0f2f5;
        color: #1c1e21;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #ced0d4;
    }
    
    /* Input Fields Styling */
    input, textarea, select {
        background-color: #ffffff !important;
        color: #1c1e21 !important;
        border: 1px solid #ccd0d5 !important;
        border-radius: 6px !important;
        font-size: 14px !important;
        max-width: 100% !important;
    }
    
    /* Input Labels Readability */
    .stTextInput label, .stTextArea label, .stRadio label {
        color: #4b4f56 !important;
        font-weight: 600 !important;
    }
    
    /* Buttons Styling (Facebook Blue) */
    .stButton>button, .stDownloadButton>button {
        background-color: #1877f2 !important;
        color: white !important;
        border: none;
        border-radius: 6px;
        font-weight: bold;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    .stButton>button:hover, .stDownloadButton>button:hover {
        background-color: #166fe5 !important;
    }

    /* Headers Styling */
    h1, h2, h3 {
        color: #1877f2 !important;
    }

    /* Page Scrolling & Stability */
    html, body, [data-testid="stAppViewContainer"] {
        overflow-x: hidden !important;
        scroll-behavior: smooth;
    }

    [data-testid="stVerticalBlock"] {
        transform: translateZ(0);
        backface-visibility: hidden;
    }
</style>
""", unsafe_allow_html=True)

st.title("📄 Multi-Format Comparative Quotation Generator")

st.sidebar.header("⚙️ Select Firm & Layout")
comp_selection = st.sidebar.radio(
    "Choose Firm:",
    ["1. KOSHI ENTERPRISES (L1)", 
     "2. R.T. ENTERPRISES (L2)", 
     "3. NEW MANORMA ENTERPRISES (L3)"]
)

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📋 Input Details")
    
    if "1. KOSHI ENTERPRISES" in comp_selection:
        seller_name = "KOSHI ENTERPRISES"
        ref_prefix = "KE/2026/Q-"
        rate_multiplier = 1.0
    elif "2. R.T. ENTERPRISES" in comp_selection:
        seller_name = "R.T. ENTERPRISES"
        ref_prefix = "RTE/2026/Q-"
        rate_multiplier = 1.025
    else:
        seller_name = "NEW MANORMA ENTERPRISES"
        ref_prefix = "NME/2026/Q-"
        rate_multiplier = 1.0507

    st.success(f"Selected Firm Layout: **{seller_name}**")

    ref_no = st.text_input("Quotation Ref No.", value=f"{ref_prefix}104")
    q_date = st.text_input("Date", value="25-07-2026")
    billed_to = st.text_area("Billed To", value="DPO SSA MADHEPURA\nDistrict Project Office, Samagra Shiksha Abhiyan\nMadhepura, Bihar", height=90)
    
    st.subheader("📦 Base Item Details (Koshi L1 Rates)")
    
    default_items = pd.DataFrame([
        {"DESCRIPTION": "HP ALL IN ONE 27-CR0417IN\nSerial No: 8CC5261H81", "QTY": 1, "BASE_RATE": 87500.0}
    ])

    edited_df = st.data_editor(
        default_items,
        num_rows="dynamic",
        use_container_width=True,
        column_config={
            "QTY": st.column_config.NumberColumn("QTY", min_value=1, step=1),
            "BASE_RATE": st.column_config.NumberColumn("Base Rate (₹)", min_value=0.0, format="₹%.2f"),
        }
    )

    st.subheader("📝 Words & Remarks")
    amt_words = st.text_input("Amount in Words", value="Enter amount in words...")

# --- GENERATE SPECIFIC HTML LAYOUTS WITH FACEBOOK THEME ---
items_list = []
grand_total = 0.0

for idx, row in edited_df.iterrows():
    desc = row.get("DESCRIPTION", "")
    qty = row.get("QTY", 1) or 1
    base_rate = row.get("BASE_RATE", 0.0) or 0.0
    actual_rate = round(base_rate * rate_multiplier, 2)
    amount = qty * actual_rate
    grand_total += amount
    items_list.append({
        "sn": idx + 1,
        "desc": desc.replace('\n', '<br>'),
        "qty": qty,
        "rate": actual_rate,
        "amount": amount
    })

# 1. KOSHI ENTERPRISES FORMAT
if "1. KOSHI ENTERPRISES" in comp_selection:
    rows_html = "".join([f"""
    <tr>
        <td style="text-align:center; padding:10px; border-bottom:1px solid #ddd;">{i['sn']}</td>
        <td style="padding:10px; border-bottom:1px solid #ddd; color:#1c1e21;">{i['desc']}</td>
        <td style="text-align:center; padding:10px; border-bottom:1px solid #ddd; color:#1c1e21;">{i['qty']} PCS</td>
        <td style="text-align:right; padding:10px; border-bottom:1px solid #ddd; color:#1c1e21;">₹{i['rate']:,.2f}</td>
        <td style="text-align:right; padding:10px; border-bottom:1px solid #ddd; color:#1c1e21; font-weight:bold;">₹{i['amount']:,.2f}</td>
    </tr>""" for i in items_list])

    quotation_html = f"""
    <!DOCTYPE html><html><head><style>
    * {{ -webkit-print-color-adjust: exact !important; box-sizing: border-box; }}
    body {{ font-family: Helvetica, Arial, sans-serif; margin: 0; padding: 10px; background-color: #f0f2f5; }}
    .q-container {{ max-width: 800px; margin: 0 auto; border: 1px solid #ccd0d5; padding: 25px; background-color: #ffffff !important; color: #1c1e21 !important; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
    .header {{ background-color: #1877f2; color: white; padding: 20px; text-align: center; border-radius: 6px; }}
    .item-table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
    .item-table th {{ background-color: #e7f3ff; color: #1877f2; padding: 10px; text-align: left; font-size: 13px; border-bottom: 2px solid #1877f2; }}
    .total-box {{ background-color: #e7f3ff; border: 1px solid #1877f2; color: #1877f2; padding: 12px; text-align: right; font-size: 16px; font-weight: bold; margin-top: 20px; border-radius: 6px; }}
    </style></head><body>
    <div class="q-container">
        <div class="header">
            <h1 style="margin:0; font-size:28px; letter-spacing:0.5px; color:#ffffff;">KOSHI ENTERPRISES</h1>
            <p style="margin:4px 0; font-size:12px; opacity:0.9;">Sukhasan Uttarwari, Ward No. 07, Madhepura, Bihar - 852113</p>
            <p style="margin:0; font-size:12px; opacity:0.9;">GSTIN: 10CJAPK9167R1ZQ | Mobile: +91 8541887622</p>
            <span style="background:#ffffff; color:#1877f2; padding:3px 12px; font-weight:bold; font-size:12px; margin-top:8px; display:inline-block; border-radius:4px;">QUOTATION</span>
        </div>
        <table style="width:100%; font-size:13px; margin: 20px 0; color: #4b4f56;">
            <tr>
                <td><b>BILLED TO:</b><br><div style="margin-top:4px; line-height:1.5; color:#1c1e21;">{billed_to.replace('\n', '<br>')}</div></td>
                <td style="text-align:right; vertical-align:top;"><b>Ref No:</b> {ref_no}<br><b>Date:</b> {q_date}</td>
            </tr>
        </table>
        <table class="item-table">
            <thead><tr><th style="width:8%; text-align:center;">SL</th><th>DESCRIPTION OF GOODS</th><th style="width:12%; text-align:center;">QTY</th><th style="width:15%; text-align:right;">RATE (₹)</th><th style="width:18%; text-align:right;">AMOUNT (₹)</th></tr></thead>
            <tbody>{rows_html}</tbody>
        </table>
        <div class="total-box">GRAND TOTAL: ₹{grand_total:,.2f}</div>
        <p style="font-size:13px; margin-top:15px; color:#4b4f56;"><b>AMOUNT IN WORDS:</b> <span style="color:#1c1e21;">{amt_words}</span></p>
        <div style="margin-top:35px; display:flex; justify-content:space-between; font-size:12px; color:#65676b;">
            <div><b>TERMS & CONDITIONS:</b><br>• Freight charges & taxes included.<br>• Standard warranty applicable.</div>
            <div style="text-align:center;"><p style="margin-bottom:45px;">For <b>KOSHI ENTERPRISES</b></p><p>Authorized Signatory</p></div>
        </div>
    </div></body></html>"""

# 2. R.T. ENTERPRISES FORMAT
elif "2. R.T. ENTERPRISES" in comp_selection:
    rows_html = "".join([f"""
    <tr>
        <td style="text-align:center; padding:8px; border-bottom:1px solid #ddd;">0{i['sn']}</td>
        <td style="padding:8px; border-bottom:1px solid #ddd; color:#1c1e21;">{i['desc']}</td>
        <td style="text-align:center; padding:8px; border-bottom:1px solid #ddd; color:#1c1e21;">{i['qty']}</td>
        <td style="text-align:center; padding:8px; border-bottom:1px solid #ddd; color:#1c1e21;">PCS</td>
        <td style="text-align:right; padding:8px; border-bottom:1px solid #ddd; color:#1c1e21;">{i['rate']:,.2f}</td>
        <td style="text-align:right; padding:8px; border-bottom:1px solid #ddd; color:#1c1e21; font-weight:bold;">{i['amount']:,.2f}</td>
    </tr>""" for i in items_list])

    quotation_html = f"""
    <!DOCTYPE html><html><head><style>
    * {{ -webkit-print-color-adjust: exact !important; box-sizing: border-box; }}
    body {{ font-family: Helvetica, Arial, sans-serif; margin: 0; padding: 10px; background-color: #f0f2f5; }}
    .rt-box {{ max-width: 800px; margin: 0 auto; border: 1px solid #ccd0d5; padding: 25px; background-color: #ffffff !important; color: #1c1e21 !important; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
    .title-head {{ border-bottom: 2px solid #1877f2; padding-bottom: 12px; margin-bottom: 15px; display:flex; justify-content:space-between; align-items:center; }}
    .rt-table {{ width: 100%; border-collapse: collapse; margin-top: 10px; }}
    .rt-table th, .rt-table td {{ border: 1px solid #ccd0d5; padding: 8px; font-size: 12px; }}
    </style></head><body>
    <div class="rt-box">
        <div class="title-head">
            <div>
                <h2 style="margin:0; font-size:22px; color:#1877f2;">R.T. ENTERPRISES</h2>
                <p style="margin:2px 0; font-size:11px; color:#65676b;">NEW COLONY, SAHARSA, BIHAR - 852201</p>
                <p style="margin:0; font-size:11px; color:#65676b;">GSTIN: 10CIRPT5717JIZU | Mobile: +91 9113164314</p>
            </div>
            <div style="background:#e7f3ff; border:1px solid #1877f2; padding:6px 15px; font-weight:bold; font-size:15px; color:#1877f2; border-radius:4px;">QUOTATION</div>
        </div>
        <table style="width:100%; font-size:12px; margin-bottom:15px; border-bottom:1px solid #ccd0d5; padding-bottom:10px; color:#4b4f56;">
            <tr>
                <td style="width:50%;"><b>QUOTATION ISSUED TO:</b><br><div style="margin-top:4px; color:#1c1e21;">{billed_to.replace('\n', '<br>')}</div></td>
                <td style="width:50%; vertical-align:top;"><b>SUPPLIER DETAILS:</b><br>R.T. ENTERPRISES<br>Ref No: {ref_no} | Date: {q_date}</td>
            </tr>
        </table>
        <table class="rt-table">
            <thead><tr style="background:#e7f3ff; color:#1877f2;"><th>S.N.</th><th>DESCRIPTION OF GOODS</th><th>QTY</th><th>PER</th><th>RATE (₹)</th><th>AMOUNT (₹)</th></tr></thead>
            <tbody>
                {rows_html}
                <tr><td colspan="5" style="text-align:right; font-weight:bold;">Subtotal</td><td style="text-align:right;">{grand_total:,.2f}</td></tr>
                <tr><td colspan="5" style="text-align:right; font-weight:bold;">Taxes & Freight</td><td style="text-align:right;">INCLUDED</td></tr>
                <tr style="background:#f0f2f5;"><td colspan="5" style="text-align:right; font-weight:bold; color:#1877f2;">TOTAL AMOUNT</td><td style="text-align:right; font-weight:bold; color:#1877f2;">₹{grand_total:,.2f}</td></tr>
            </tbody>
        </table>
        <p style="font-size:12px; margin-top:12px; color:#4b4f56;"><b>Amount in Words:</b> <span style="color:#1c1e21;">{amt_words}</span></p>
        <div style="margin-top:25px; display:flex; justify-content:space-between; font-size:11px; color:#65676b;">
            <div><b>Terms & Conditions:</b><br>• All Freight and Taxes Included.<br>• Standard warranty applicable.</div>
            <div style="text-align:center;"><p style="margin-bottom:40px;">For <b>R.T. ENTERPRISES</b></p><p>Authorized Signatory</p></div>
        </div>
    </div></body></html>"""

# 3. NEW MANORMA ENTERPRISES FORMAT
else:
    rows_html = "".join([f"""
    <tr>
        <td style="text-align:center; padding:8px; border-bottom:1px solid #ddd;">{i['sn']}</td>
        <td style="padding:8px; border-bottom:1px solid #ddd; color:#1c1e21;">{i['desc']}</td>
        <td style="text-align:center; padding:8px; border-bottom:1px solid #ddd; color:#1c1e21;">{i['qty']}</td>
        <td style="text-align:center; padding:8px; border-bottom:1px solid #ddd; color:#1c1e21;">PCS</td>
        <td style="text-align:right; padding:8px; border-bottom:1px solid #ddd; color:#1c1e21;">{i['rate']:,.2f}</td>
        <td style="text-align:right; padding:8px; border-bottom:1px solid #ddd; color:#1c1e21; font-weight:bold;">{i['amount']:,.2f}</td>
    </tr>""" for i in items_list])

    quotation_html = f"""
    <!DOCTYPE html><html><head><style>
    * {{ -webkit-print-color-adjust: exact !important; box-sizing: border-box; }}
    body {{ font-family: Helvetica, Arial, sans-serif; margin: 0; padding: 10px; background-color: #f0f2f5; }}
    .m-box {{ max-width: 800px; margin: 0 auto; border: 1px solid #ccd0d5; padding: 25px; background-color: #ffffff !important; color: #1c1e21 !important; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
    .m-head {{ text-align: center; border-bottom:2px solid #1877f2; padding-bottom:10px; }}
    .m-table {{ width: 100%; border-collapse: collapse; margin-top: 15px; }}
    .m-table th, .m-table td {{ border: 1px solid #ccd0d5; padding: 8px; font-size: 12px; }}
    </style></head><body>
    <div class="m-box">
        <div class="m-head">
            <h2 style="margin:0; font-size:22px; color:#1877f2;">NEW MANORMA ENTERPRISES</h2>
            <p style="margin:2px 0; font-size:11px; color:#65676b;">RAJENDRA NAGAR, WARD NO. 02, SUPAUL</p>
            <p style="margin:0; font-size:11px; color:#65676b;">GSTIN: 10AZGPM9227L1Z7 | Mobile: +91 7362821383</p>
        </div>
        <table style="width:100%; font-size:12px; margin: 15px 0; color:#4b4f56;">
            <tr>
                <td style="width:60%;"><b>QUOTATION TO:</b><br><div style="margin-top:4px; color:#1c1e21;">{billed_to.replace('\n', '<br>')}</div></td>
                <td style="text-align:right; vertical-align:top;"><b>REFERENCE & DATE</b><br>Ref No: {ref_no}<br>Date: {q_date}</td>
            </tr>
        </table>
        <table class="m-table">
            <thead><tr style="background:#e7f3ff; color:#1877f2;"><th>S.N.</th><th>DESCRIPTION OF GOODS</th><th>QTY</th><th>PER</th><th>RATE (₹)</th><th>AMOUNT (₹)</th></tr></thead>
            <tbody>
                {rows_html}
                <tr><td colspan="5" style="text-align:right; font-weight:bold;">Sub Total:</td><td style="text-align:right;">{grand_total:,.2f}</td></tr>
                <tr><td colspan="5" style="text-align:right; font-weight:bold;">Taxes & Freight:</td><td style="text-align:right;">Included</td></tr>
                <tr style="background:#f0f2f5;"><td colspan="5" style="text-align:right; font-weight:bold; color:#1877f2;">Total Amount:</td><td style="text-align:right; font-weight:bold; color:#1877f2;">₹{grand_total:,.2f}</td></tr>
            </tbody>
        </table>
        <p style="font-size:12px; margin-top:12px; color:#4b4f56;"><b>Amount in Words:</b> <span style="color:#1c1e21;">{amt_words}</span></p>
        <p style="font-size:11px; color:#65676b; line-height:1.4;"><b>Terms & Conditions:</b><br>• ALL FREIGHT AND TAXES INCLUDED.<br>• Payment as per agreed terms.</p>
        <div style="text-align:right; margin-top:25px; font-size:12px; color:#4b4f56;"><p style="margin-bottom:40px;">For <b>NEW MANORMA ENTERPRISES</b></p><p>Authorized Signatory</p></div>
    </div></body></html>"""

with col2:
    st.subheader("📄 Live Exact Preview")
    st.download_button(
        label=f"📥 Download {seller_name} Quotation",
        data=quotation_html,
        file_name=f"Quotation_{seller_name.replace(' ', '_')}_{ref_no.replace('/', '_')}.html",
        mime="text/html",
        use_container_width=True
    )
    components.html(quotation_html, height=750, scrolling=True)
