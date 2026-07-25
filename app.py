import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

st.set_page_config(page_title="KOSHI Comparative Quotation Generator", page_icon="📑", layout="wide")

st.title("📑 Comparative Quotation Generator (L1, L2, L3)")

# Sidebar to select firm
st.sidebar.header("⚙️ Select Quotation Firm")
comp_selection = st.sidebar.radio(
    "Choose Company:",
    ["1. KOSHI ENTERPRISES (L1 - Base)", 
     "2. R.T. ENTERPRISES (L2 - +2.5%)", 
     "3. NEW MANORMA ENTERPRISES (L3 - +5%)"]
)

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🏢 Firm & Quotation Details")
    
    if "1. KOSHI ENTERPRISES" in comp_selection:
        seller_name = "KOSHI ENTERPRISES"
        seller_address = "Sukhasan Uttarwari, Ward No. 07, Madhepura, Bihar - 852113"
        seller_gstin = "10CJAPK9167R1ZQ"
        seller_mobile = "+91 8541887622"
        ref_prefix = "KE/2026/Q-"
        rate_multiplier = 1.0  # Base Rate
        badge_text = "QUOTATION (L1)"
        
    elif "2. R.T. ENTERPRISES" in comp_selection:
        seller_name = "R.T. ENTERPRISES"
        seller_address = "New Colony, Saharsa, Bihar - 852201"
        seller_gstin = "10CIRPT5717JIZU"
        seller_mobile = "+91 9113164314"
        ref_prefix = "RTE/2026/Q-"
        rate_multiplier = 1.025  # ~2.5% Higher for L2
        badge_text = "QUOTATION (L2)"
        
    else:
        seller_name = "NEW MANORMA ENTERPRISES"
        seller_address = "Rajendra Nagar, Ward No. 02, Supaul, Bihar"
        seller_gstin = "10AZGPM9227L1Z7"
        seller_mobile = "+91 7362821383"
        ref_prefix = "NME/2026/Q-"
        rate_multiplier = 1.0507  # ~5% Higher for L3
        badge_text = "QUOTATION (L3)"

    st.info(f"**Selected Firm:** {seller_name}\n\n**GSTIN:** {seller_gstin} | **Address:** {seller_address}")

    ref_no = st.text_input("Quotation Ref No.", value=f"{ref_prefix}104")
    q_date = st.text_input("Date", value="25-07-2026")
    billed_to = st.text_area("Billed To", value="DPO SSA MADHEPURA\nDistrict Project Office, Samagra Shiksha Abhiyan\nMadhepura, Bihar", height=90)
    
    st.subheader("📦 Base Item Details (Enter Koshi L1 Rates)")
    
    default_items = pd.DataFrame([
        {"DESCRIPTION": "HP ALL IN ONE 27-CR0417IN (SN-8CC5261H81)", "QTY": 1, "BASE_RATE": 87500.0}
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

    items_html_rows = ""
    grand_total = 0.0

    for idx, row in edited_df.iterrows():
        desc = row.get("DESCRIPTION", "")
        qty = row.get("QTY", 1) or 1
        base_rate = row.get("BASE_RATE", 0.0) or 0.0
        
        # Calculate calculated rate for selected firm
        actual_rate = round(base_rate * rate_multiplier, 2)
        amount = qty * actual_rate
        grand_total += amount
        
        items_html_rows += f"""
        <tr>
            <td style="text-align:center;">{idx + 1:02d}</td>
            <td>{desc}</td>
            <td style="text-align:center;">{qty} PCS</td>
            <td style="text-align:right;">₹{actual_rate:,.2f}</td>
            <td style="text-align:right;">₹{amount:,.2f}</td>
        </tr>
        """

    st.subheader("📝 Terms & Amount in Words")
    amt_words = st.text_input("Amount in Words", value="Enter amount in words...")

with col2:
    st.subheader("📄 Live Quotation Preview")

    quotation_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            * {{ -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; box-sizing: border-box; }}
            body {{ font-family: Arial, sans-serif; margin: 0; padding: 10px; background-color: #ffffff; }}
            .q-container {{ max-width: 800px; margin: 0 auto; border: 2px solid #0052cc; padding: 20px; background: #fff; }}
            .header {{ background: linear-gradient(135deg, #002b80, #0052cc) !important; color: white !important; padding: 15px; text-align: center; border-radius: 5px; margin-bottom: 20px; }}
            .item-table {{ width: 100%; border-collapse: collapse; margin-top: 15px; }}
            .item-table th {{ background-color: #002b80 !important; color: white !important; padding: 8px 10px; text-align: left; font-size: 13px; }}
            .item-table td {{ border: 1px solid #ddd; padding: 8px 10px; font-size: 13px; }}
            .total-box {{ background-color: #f0f4f9 !important; border: 1px solid #0052cc; padding: 10px; text-align: right; font-size: 16px; font-weight: bold; color: #002b80; margin-top: 15px; }}
        </style>
    </head>
    <body>
        <div class="q-container">
            <div class="header">
                <h1 style="margin:0; font-size:22px;">{seller_name}</h1>
                <p style="margin:5px 0 0 0; font-size:12px;">{seller_address}</p>
                <p style="margin:2px 0 0 0; font-size:12px;">GSTIN: {seller_gstin} | Mobile: {seller_mobile}</p>
                <h3 style="margin:10px 0 0 0; background:#ff9900; color:#000; padding:3px 8px; display:inline-block; border-radius:3px; font-size:13px;">{badge_text}</h3>
            </div>

            <table style="width:100%; font-size:13px; margin-bottom:15px;">
                <tr>
                    <td style="width:60%; vertical-align:top;">
                        <b>QUOTATION ISSUED TO:</b><br>
                        {billed_to.replace('\n', '<br>')}
                    </td>
                    <td style="vertical-align:top; text-align:right;">
                        <b>Ref No:</b> {ref_no}<br>
                        <b>Date:</b> {q_date}
                    </td>
                </tr>
            </table>

            <table class="item-table">
                <thead>
                    <tr>
                        <th style="width:8%; text-align:center;">S.N.</th>
                        <th style="width:52%;">DESCRIPTION OF GOODS</th>
                        <th style="width:10%; text-align:center;">QTY</th>
                        <th style="width:15%; text-align:right;">RATE (₹)</th>
                        <th style="width:15%; text-align:right;">AMOUNT (₹)</th>
                    </tr>
                </thead>
                <tbody>
                    {items_html_rows}
                </tbody>
            </table>

            <div class="total-box">
                TOTAL AMOUNT: ₹{grand_total:,.2f}
            </div>

            <p style="font-size:12px; margin-top:10px;"><b>Amount in Words:</b> {amt_words}</p>

            <div style="margin-top:30px; display:flex; justify-content:space-between; align-items:flex-end;">
                <div style="font-size:11px; color:#555;">
                    <b>Terms & Conditions:</b><br>
                    • All Freight and Taxes Included in the above rate.<br>
                    • Covered under manufacturer's standard warranty.<br>
                    • Payment terms as per agreed protocol.
                </div>
                <div style="text-align:center; font-size:12px;">
                    <p style="margin-bottom:40px;">For <b>{seller_name}</b></p>
                    <p style="margin:0;">Authorized Signatory/Stamp</p>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

    st.download_button(
        label=f"📥 Download {seller_name} Quotation",
        data=quotation_html,
        file_name=f"Quotation_{seller_name.replace(' ', '_')}_{ref_no.replace('/', '_')}.html",
        mime="text/html",
        use_container_width=True
    )

    components.html(quotation_html, height=700, scrolling=True)
