import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

st.set_page_config(page_title="Custom Multi-Format Quotation Generator", page_icon="📄", layout="wide")

st.title("📄 Multi-Format Comparative Quotation Generator")

st.sidebar.header("⚙️ Select Firm & Layout")
comp_selection = st.sidebar.radio(
    "Choose Firm:",
    ["1. KOSHI ENTERPRISES (L1)", 
     "2. R.T. ENTERPRISES (L2)", 
     "3. NEW MANORMA ENTERPRISES (L3)"]
)

# --- SIDEBAR HELP / SUPPORT SECTION ---
st.sidebar.markdown("---")
st.sidebar.subheader("🎧 Help & Support")
st.sidebar.markdown("Koi dikkat ho ya baat karni ho toh seedha WhatsApp par message karein:")
whatsapp_url = "https://wa.me/918864097233?text=Hello,%20mujhe%20is%20quotation%20generator%20ke%20bare%20me%20baat%20karni%20hai"
st.sidebar.markdown(f'<a href="{whatsapp_url}" target="_blank"><button style="width:100%; background-color:#25D366; color:white; padding:10px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;">💬 WhatsApp Help</button></a>', unsafe_allow_html=True)

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

# --- GENERATE SPECIFIC HTML LAYOUTS ---
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
        <td style="text-align:center;">{i['sn']}</td>
        <td>{i['desc']}</td>
        <td style="text-align:center;">{i['qty']} PCS</td>
        <td style="text-align:right;">₹{i['rate']:,.2f}</td>
        <td style="text-align:right;">₹{i['amount']:,.2f}</td>
    </tr>""" for i in items_list])

    quotation_html = f"""
    <!DOCTYPE html><html><head><style>
    * {{ -webkit-print-color-adjust: exact !important; box-sizing: border-box; }}
    body {{ font-family: Arial, sans-serif; margin: 0; padding: 10px; }}
    .q-container {{ max-width: 800px; margin: 0 auto; border: 2px solid #0052cc; padding: 20px; }}
    .header {{ background: linear-gradient(135deg, #002b80, #0052cc); color: white; padding: 15px; text-align: center; border-radius: 5px; }}
    .item-table {{ width: 100%; border-collapse: collapse; margin-top: 15px; }}
    .item-table th {{ background-color: #002b80; color: white; padding: 8px; text-align: left; font-size: 13px; }}
    .item-table td {{ border: 1px solid #ddd; padding: 8px; font-size: 13px; }}
    .total-box {{ background-color: #f0f4f9; border: 1px solid #0052cc; padding: 10px; text-align: right; font-size: 16px; font-weight: bold; color: #002b80; margin-top: 15px; }}
    </style></head><body>
    <div class="q-container">
        <div class="header">
            <h1 style="margin:0;">KOSHI ENTERPRISES</h1>
            <p style="margin:3px 0; font-size:12px;">Sukhasan Uttarwari, Ward No. 07, Madhepura, Bihar - 852113</p>
            <p style="margin:0; font-size:12px;">GSTIN: 10CJAPK9167R1ZQ | Mobile: +91 8541887622</p>
            <span style="background:#ff9900; color:#000; padding:2px 10px; font-weight:bold; font-size:13px; margin-top:5px; display:inline-block;">QUOTATION</span>
        </div>
        <table style="width:100%; font-size:13px; margin: 15px 0;">
            <tr>
                <td><b>BILLED TO:</b><br>{billed_to.replace('\n', '<br>')}</td>
                <td style="text-align:right; vertical-align:top;"><b>Ref No:</b> {ref_no}<br><b>Date:</b> {q_date}</td>
            </tr>
        </table>
        <table class="item-table">
            <thead><tr><th style="width:8%; text-align:center;">SL</th><th>DESCRIPTION OF GOODS</th><th style="width:12%; text-align:center;">QTY</th><th style="width:15%; text-align:right;">RATE (₹)</th><th style="width:18%; text-align:right;">AMOUNT (₹)</th></tr></thead>
            <tbody>{rows_html}</tbody>
        </table>
        <div class="total-box">GRAND TOTAL: ₹{grand_total:,.2f}</div>
        <p style="font-size:12px; margin-top:10px;"><b>AMOUNT IN WORDS:</b> {amt_words}</p>
        <div style="margin-top:30px; display:flex; justify-content:space-between; font-size:11px;">
            <div><b>TERMS & CONDITIONS:</b><br>• Freight charges & taxes included.<br>• Standard warranty applicable.</div>
            <div style="text-align:center; font-size:12px;"><p style="margin-bottom:40px;">For <b>KOSHI ENTERPRISES</b></p><p>Authorized Signatory</p></div>
        </div>
    </div></body></html>"""

# 2. R.T. ENTERPRISES FORMAT
elif "2. R.T. ENTERPRISES" in comp_selection:
    rows_html = "".join([f"""
    <tr>
        <td style="text-align:center;">0{i['sn']}</td>
        <td>{i['desc']}</td>
        <td style="text-align:center;">{i['qty']}</td>
        <td style="text-align:center;">PCS</td>
        <td style="text-align:right;">{i['rate']:,.2f}</td>
        <td style="text-align:right;">{i['amount']:,.2f}</td>
    </tr>""" for i in items_list])

    quotation_html = f"""
    <!DOCTYPE html><html><head><style>
    * {{ -webkit-print-color-adjust: exact !important; box-sizing: border-box; }}
    body {{ font-family: Arial, sans-serif; margin: 0; padding: 10px; }}
    .rt-box {{ max-width: 800px; margin: 0 auto; border: 1.5px solid #000; padding: 20px; }}
    .title-head {{ border-bottom: 2px solid #000; padding-bottom: 10px; margin-bottom: 15px; display:flex; justify-content:space-between; align-items:center; }}
    .rt-table {{ width: 100%; border-collapse: collapse; margin-top: 10px; }}
    .rt-table th, .rt-table td {{ border: 1px solid #000; padding: 6px 8px; font-size: 12px; }}
    </style></head><body>
    <div class="rt-box">
        <div class="title-head">
            <div>
                <h2 style="margin:0; font-size:22px; letter-spacing:1px;">R.T. ENTERPRISES</h2>
                <p style="margin:2px 0; font-size:11px;">NEW COLONY, SAHARSA, BIHAR - 852201</p>
                <p style="margin:0; font-size:11px;">GSTIN: 10CIRPT5717JIZU | Mobile: +91 9113164314</p>
            </div>
            <div style="border:1px solid #000; padding:5px 15px; font-weight:bold; font-size:16px;">QUOTATION</div>
        </div>
        <table style="width:100%; font-size:12px; margin-bottom:15px; border-bottom:1px solid #000; padding-bottom:10px;">
            <tr>
                <td style="width:50%;"><b>QUOTATION ISSUED TO:</b><br>{billed_to.replace('\n', '<br>')}</td>
                <td style="width:50%; vertical-align:top;"><b>SUPPLIER DETAILS:</b><br>R.T. ENTERPRISES<br>New Colony, Saharsa, Bihar 852201<br>Ref No: {ref_no} | Date: {q_date}</td>
            </tr>
        </table>
        <table class="rt-table">
            <thead><tr style="background:#f2f2f2;"><th>S.N.</th><th>DESCRIPTION OF GOODS</th><th>QTY</th><th>PER</th><th>RATE (₹)</th><th>AMOUNT (₹)</th></tr></thead>
            <tbody>
                {rows_html}
                <tr><td colspan="5" style="text-align:right;"><b>Subtotal</b></td><td style="text-align:right;">{grand_total:,.2f}</td></tr>
                <tr><td colspan="5" style="text-align:right;"><b>Taxes & Freight</b></td><td style="text-align:right;">INCLUDED</td></tr>
                <tr><td colspan="5" style="text-align:right;"><b>TOTAL AMOUNT</b></td><td style="text-align:right;"><b>₹{grand_total:,.2f}</b></td></tr>
            </tbody>
        </table>
        <p style="font-size:12px; margin-top:10px;"><b>Amount in Words:</b> {amt_words}</p>
        <div style="margin-top:25px; display:flex; justify-content:space-between; font-size:11px;">
            <div><b>Terms & Conditions:</b><br>• All Freight and Taxes Included in the above rate.<br>• Goods covered under standard warranty.<br>• Payment terms as per government protocol.</div>
            <div style="text-align:center; font-size:12px;"><p style="margin-bottom:40px;">For <b>R.T. ENTERPRISES</b></p><p>Authorized Signatory/Stamp</p></div>
        </div>
    </div></body></html>"""

# 3. NEW MANORMA ENTERPRISES FORMAT
else:
    rows_html = "".join([f"""
    <tr>
        <td style="text-align:center;">{i['sn']}</td>
        <td>{i['desc']}</td>
        <td style="text-align:center;">{i['qty']}</td>
        <td style="text-align:center;">PCS</td>
        <td style="text-align:right;">{i['rate']:,.2f}</td>
        <td style="text-align:right;">{i['amount']:,.2f}</td>
    </tr>""" for i in items_list])

    quotation_html = f"""
    <!DOCTYPE html><html><head><style>
    * {{ -webkit-print-color-adjust: exact !important; box-sizing: border-box; }}
    body {{ font-family: Arial, sans-serif; margin: 0; padding: 10px; }}
    .m-box {{ max-width: 800px; margin: 0 auto; border: 1px solid #888; padding: 20px; }}
    .m-head {{ text-align: center; color: #b30000; border-bottom:2px solid #b30000; padding-bottom:8px; }}
    .m-table {{ width: 100%; border-collapse: collapse; margin-top: 15px; }}
    .m-table th, .m-table td {{ border: 1px solid #aaa; padding: 6px; font-size: 12px; }}
    </style></head><body>
    <div class="m-box">
        <div class="m-head">
            <h2 style="margin:0; font-size:22px; color:#a00000;">NEW MANORMA ENTERPRISES</h2>
            <p style="margin:2px 0; font-size:11px; color:#333;">RAJENDRA NAGAR, WARD NO. 02, SUPAUL</p>
            <p style="margin:0; font-size:11px; color:#333;">GSTIN: 10AZGPM9227L1Z7 | Mobile: +91 7362821383</p>
        </div>
        <table style="width:100%; font-size:12px; margin: 15px 0;">
            <tr>
                <td style="width:60%;"><b>QUOTATION TO:</b><br>{billed_to.replace('\n', '<br>')}</td>
                <td style="text-align:right; vertical-align:top;"><b>REFERENCE & DATE</b><br>Ref No: {ref_no}<br>Date: {q_date}</td>
            </tr>
        </table>
        <table class="m-table">
            <thead><tr style="background:#f9f9f9;"><th>S.N.</th><th>DESCRIPTION OF GOODS</th><th>QTY</th><th>PER</th><th>RATE (₹)</th><th>AMOUNT (₹)</th></tr></thead>
            <tbody>
                {rows_html}
                <tr><td colspan="5" style="text-align:right;"><b>Sub Total:</b></td><td style="text-align:right;">{grand_total:,.2f}</td></tr>
                <tr><td colspan="5" style="text-align:right;"><b>Taxes & Freight:</b></td><td style="text-align:right;">Included</td></tr>
                <tr><td colspan="5" style="text-align:right;"><b>Total Amount:</b></td><td style="text-align:right;"><b>₹{grand_total:,.2f}</b></td></tr>
            </tbody>
        </table>
        <p style="font-size:12px; margin-top:10px;"><b>Amount in Words:</b> {amt_words}</p>
        <p style="font-size:11px; color:#555;"><b>Terms & Conditions:</b><br>• ALL FREIGHT AND TAXES INCLUDED.<br>• Payment as per agreed terms.<br>• Goods once sold will not be taken back without prior approval.</p>
        <p style="text-align:center; font-style:italic; font-size:12px; margin-top:15px;">Thank you for your business!</p>
        <div style="text-align:right; margin-top:20px; font-size:12px;"><p style="margin-bottom:40px;">For <b>NEW MANORMA ENTERPRISES</b></p><p>Authorized Signatory</p></div>
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
