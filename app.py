import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="KOSHI ENTERPRISES - Quotation Generator", page_icon="📄", layout="wide")

st.title("📄 KOSHI ENTERPRISES Quotation Generator")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📋 Quotation Details")
    ref_no = st.text_input("Quotation Ref No.", value="KE/2026/Q-104")
    q_date = st.text_input("Date", value="25-07-2026")
    billed_to = st.text_area("Billed To", value="DPO SSA MADHEPURA\nMadhepura, Bihar", height=90)
    
    st.subheader("📦 Item Details")
    item_desc = st.text_input("Item Description", value="HP ALL IN ONE 27-CR0417IN (SN-8CC5261H81)")
    qty = st.number_input("Quantity", value=1, min_value=1)
    rate = st.number_input("Rate (₹)", value=87500.0, step=500.0)
    
    total_amt = qty * rate
    
    st.subheader("📝 Terms & Amount in Words")
    amt_words = st.text_input("Amount in Words", value="Rupees Eighty-Seven Thousand Five Hundred Only")

with col2:
    st.subheader("📄 Live Quotation Preview")

    quotation_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            * {{
                -webkit-print-color-adjust: exact !important;
                print-color-adjust: exact !important;
                box-sizing: border-box;
            }}
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 10px;
                background-color: #ffffff;
            }}
            .q-container {{
                max-width: 800px;
                margin: 0 auto;
                border: 2px solid #0052cc;
                padding: 20px;
                background: #fff;
            }}
            .header {{
                background: linear-gradient(135deg, #002b80, #0052cc) !important;
                color: white !important;
                padding: 15px;
                text-align: center;
                border-radius: 5px;
                margin-bottom: 20px;
            }}
            .item-table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 15px;
            }}
            .item-table th {{
                background-color: #002b80 !important;
                color: white !important;
                padding: 10px;
                text-align: left;
                font-size: 13px;
            }}
            .item-table td {{
                border: 1px solid #ddd;
                padding: 10px;
                font-size: 13px;
            }}
            .total-box {{
                background-color: #f0f4f9 !important;
                border: 1px solid #0052cc;
                padding: 10px;
                text-align: right;
                font-size: 16px;
                font-weight: bold;
                color: #002b80;
                margin-top: 15px;
            }}
        </style>
    </head>
    <body>
        <div class="q-container">
            <div class="header">
                <h1 style="margin:0; font-size:24px;">KOSHI ENTERPRISES</h1>
                <p style="margin:5px 0 0 0; font-size:12px;">Sukhasan Uttarwari, Ward No. 07, Madhepura, Bihar - 852113</p>
                <p style="margin:2px 0 0 0; font-size:12px;">GSTIN: 10CJAPK9167R1ZQ | Mobile: +91 8541887622</p>
                <h3 style="margin:10px 0 0 0; background:#ff9900; color:#000; padding:3px; display:inline-block; border-radius:3px; font-size:14px;">QUOTATION</h3>
            </div>

            <table style="width:100%; font-size:13px; margin-bottom:15px;">
                <tr>
                    <td style="width:60%; vertical-align:top;">
                        <b>BILLED TO:</b><br>
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
                        <th style="width:8%;">SL</th>
                        <th style="width:52%;">DESCRIPTION OF GOODS</th>
                        <th style="width:10%;">QTY</th>
                        <th style="width:15%;">RATE (₹)</th>
                        <th style="width:15%;">AMOUNT (₹)</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>1</td>
                        <td>{item_desc}</td>
                        <td>{qty} PCS</td>
                        <td>₹{rate:,.2f}</td>
                        <td>₹{total_amt:,.2f}</td>
                    </tr>
                </tbody>
            </table>

            <div class="total-box">
                GRAND TOTAL: ₹{total_amt:,.2f}
            </div>

            <p style="font-size:12px; margin-top:10px;"><b>AMOUNT IN WORDS:</b> {amt_words}</p>

            <div style="margin-top:30px; display:flex; justify-content:space-between; align-items:flex-end;">
                <div style="font-size:11px; color:#555;">
                    <b>TERMS & CONDITIONS:</b><br>
                    • Freight charges & taxes included.<br>
                    • Standard manufacturer warranty applicable.
                </div>
                <div style="text-align:center; font-size:12px;">
                    <p style="margin-bottom:40px;">For <b>KOSHI ENTERPRISES</b></p>
                    <p style="margin:0;">Authorized Signatory</p>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

    st.download_button(
        label="📥 Download Quotation HTML",
        data=quotation_html,
        file_name=f"Quotation_{ref_no.replace('/', '_')}.html",
        mime="text/html",
        use_container_width=True
    )

    components.html(quotation_html, height=650, scrolling=True)
