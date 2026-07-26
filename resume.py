import streamlit as st

st.set_page_config(
    page_title="Resume Builder - Koshi Enterprises",
    page_icon="📄",
    layout="wide"
)

# Custom Styling
st.markdown("""
    <style>
    .main-title {
        color: #1E3A8A;
        font-weight: 700;
        margin-bottom: 15px;
    }
    .resume-card {
        background-color: #ffffff;
        border: 1px solid #cbd5e1;
        border-radius: 4px;
        padding: 25px 30px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        color: #000000;
        font-family: Arial, Helvetica, sans-serif;
        max-width: 800px;
        margin: auto;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h2 class='main-title'>📄 Professional Resume Builder</h2>", unsafe_allow_html=True)

# --- SIDEBAR INPUTS ---
with st.sidebar:
    st.header("📝 Personal & Job Details")
    
    full_name = st.text_input("Full Name", "PRASHANT KUMAR")
    designation = st.text_input("Designation / Title", "Medical Representative & Sales Professional")
    address = st.text_area("Address", "At - Batraha, Ward No. 36, PO+PS+Dist: Saharsa, Bihar (852201)", height=60)
    phone = st.text_input("Phone Number", "+91 8864097233")
    email = st.text_input("Email ID", "Prashantkumar886409@gmail.com")
    
    st.markdown("---")
    st.subheader("Work Experience")
    exp1_company = st.text_input("Company 1", "Pharmanova Specialties Pvt. Ltd.")
    exp1_duration = st.text_input("Duration 1", "12-02-2025 - Present")
    exp1_desc = st.text_area("Responsibilities 1", "Responsible for pharmaceutical sales, technical marketing, and client relationship management.", height=60)

    exp2_company = st.text_input("Company 2", "Hi-tech Laboratories Pharma")
    exp2_duration = st.text_input("Duration 2", "10-06-2024 - 31-01-2025")
    exp2_desc = st.text_area("Responsibilities 2", "Handled product promotion, doctor visits, and territory sales development.", height=60)

    st.markdown("---")
    st.subheader("Technical & Education")
    tech_qual = st.text_input("Technical Title", "ADCA (1 Year Computer Degree)")
    tech_qual_desc = st.text_input("Technical Details", "Advanced Diploma in Computer Applications.")
    
    edu_pg = st.text_input("M.Sc", "B.N.M.U Madhepura | Passed 2023")
    edu_grad = st.text_input("B.Sc", "B.N.M.U Madhepura | Passed 2020")
    edu_12th = st.text_input("12th", "B.S.E.B Patna | Passed 2016")
    edu_10th = st.text_input("10th", "B.S.E.B Patna Passed 2014")

    st.markdown("---")
    st.subheader("Personal Info")
    dob = st.text_input("Date of Birth", "07-04-1999")
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    father_name = st.text_input("Father's Name", "Sanjeev Kumar")
    languages = st.text_input("Languages Known", "Hindi, English, Maithili")
    marital_status = st.selectbox("Marital Status", ["Single", "Married"])
    skills = st.text_area("Key Competencies (Comma Separated)", "Medicine & Pharma Knowledge, Technical Marketing & Sales, Computer Operations, Client Relationship Management", height=70)
    hobbies = st.text_input("Hobbies & Interests", "Watching news & engaged in creative activities.")

# Format Skills List
skills_list = [s.strip() for s in skills.split(",") if s.strip()]
skills_html = "".join([f"<li style='margin-bottom: 3px;'>{s}</li>" for s in skills_list])

# HTML Layout matching original PDF
resume_body_html = f"""
<div class="resume-card" id="resume-printable-area">
    <!-- Header -->
    <div style="border-bottom: 1.5px solid #000; padding-bottom: 6px; margin-bottom: 12px;">
        <h1 style="margin: 0; font-size: 22px; font-weight: bold; color: #000; text-transform: uppercase;">{full_name}</h1>
        <div style="font-size: 13px; font-weight: bold; color: #1D4ED8; margin-top: 2px;">{designation}</div>
        <div style="font-size: 11px; color: #000; margin-top: 4px;"><b>Address:</b> {address}</div>
        <div style="font-size: 11px; color: #000; margin-top: 2px;"><b>Phone:</b> {phone} &nbsp;|&nbsp; <b>Email:</b> {email}</div>
    </div>

    <!-- 2 Column Table Layout -->
    <table style="width: 100%; border-collapse: collapse; table-layout: fixed;">
        <tr>
            <!-- Left Column -->
            <td style="width: 50%; vertical-align: top; padding-right: 12px; border: none;">
                
                <div style="font-weight: bold; font-size: 12px; border-bottom: 1px solid #000; margin-bottom: 6px; padding-bottom: 2px; text-transform: uppercase;">WORK EXPERIENCE</div>
                
                <div style="font-size: 12px; font-weight: bold; color: #000;">{exp1_company}</div>
                <div style="font-size: 11px; color: #1D4ED8; font-weight: bold; margin-bottom: 2px;">{exp1_duration}</div>
                <div style="font-size: 11px; color: #333; margin-bottom: 10px; line-height: 1.3;">{exp1_desc}</div>

                <div style="font-size: 12px; font-weight: bold; color: #000;">{exp2_company}</div>
                <div style="font-size: 11px; color: #1D4ED8; font-weight: bold; margin-bottom: 2px;">{exp2_duration}</div>
                <div style="font-size: 11px; color: #333; margin-bottom: 12px; line-height: 1.3;">{exp2_desc}</div>

                <div style="font-weight: bold; font-size: 12px; border-bottom: 1px solid #000; margin-bottom: 6px; padding-bottom: 2px; text-transform: uppercase;">TECHNICAL QUALIFICATION</div>
                <div style="font-size: 11.5px; font-weight: bold; color: #000;">{tech_qual}</div>
                <div style="font-size: 11px; color: #444; margin-bottom: 12px;">{tech_qual_desc}</div>

                <div style="font-weight: bold; font-size: 12px; border-bottom: 1px solid #000; margin-bottom: 6px; padding-bottom: 2px; text-transform: uppercase;">PERSONAL DETAILS</div>
                <table style="width: 100%; font-size: 11px; color: #000; border-collapse: collapse;">
                    <tr><td style="width: 40%; padding: 1px 0; border: none;"><b>D.O.B:</b></td><td style="border: none;">{dob}</td></tr>
                    <tr><td style="padding: 1px 0; border: none;"><b>Gender:</b></td><td style="border: none;">{gender}</td></tr>
                    <tr><td style="padding: 1px 0; border: none;"><b>Father's Name:</b></td><td style="border: none;">{father_name}</td></tr>
                    <tr><td style="padding: 1px 0; border: none;"><b>Languages:</b></td><td style="border: none;">{languages}</td></tr>
                    <tr><td style="padding: 1px 0; border: none;"><b>Marital Status:</b></td><td style="border: none;">{marital_status}</td></tr>
                    <tr><td style="padding: 1px 0; border: none;"><b>Nationality:</b></td><td style="border: none;">Indian</td></tr>
                </table>

            </td>

            <!-- Right Column -->
            <td style="width: 50%; vertical-align: top; padding-left: 12px; border: none;">
                
                <div style="font-weight: bold; font-size: 12px; border-bottom: 1px solid #000; margin-bottom: 6px; padding-bottom: 2px; text-transform: uppercase;">EDUCATION QUALIFICATION</div>
                
                <div style="font-size: 11.5px; font-weight: bold; color: #000;">Post Graduation (M.Sc)</div>
                <div style="font-size: 11px; color: #444; margin-bottom: 6px;">{edu_pg}</div>

                <div style="font-size: 11.5px; font-weight: bold; color: #000;">Graduation (B.Sc)</div>
                <div style="font-size: 11px; color: #444; margin-bottom: 6px;">{edu_grad}</div>

                <div style="font-size: 11.5px; font-weight: bold; color: #000;">Higher Secondary (12th - I.Sc)</div>
                <div style="font-size: 11px; color: #444; margin-bottom: 6px;">{edu_12th}</div>

                <div style="font-size: 11.5px; font-weight: bold; color: #000;">Secondary (10th)</div>
                <div style="font-size: 11px; color: #444; margin-bottom: 12px;">{edu_10th}</div>

                <div style="font-weight: bold; font-size: 12px; border-bottom: 1px solid #000; margin-bottom: 6px; padding-bottom: 2px; text-transform: uppercase;">KEY COMPETENCIES</div>
                <ul style="margin: 0 0 12px 0; padding-left: 16px; font-size: 11px; color: #000;">
                    {skills_html}
                </ul>

                <div style="font-weight: bold; font-size: 12px; border-bottom: 1px solid #000; margin-bottom: 6px; padding-bottom: 2px; text-transform: uppercase;">HOBBIES & INTERESTS</div>
                <div style="font-size: 11px; color: #000; margin-bottom: 12px;">{hobbies}</div>

            </td>
        </tr>
    </table>

    <!-- Declaration -->
    <div style="margin-top: 10px;">
        <div style="font-weight: bold; font-size: 12px; border-bottom: 1px solid #000; margin-bottom: 6px; padding-bottom: 2px; text-transform: uppercase;">DECLARATION</div>
        <div style="font-size: 10.5px; color: #333; font-style: italic;">I hereby declare that all the information provided above is true and correct to the best of my knowledge and belief.</div>
    </div>

    <!-- Signatures -->
    <div style="margin-top: 35px;">
        <table style="width: 100%; font-size: 11.5px; border: none;">
            <tr>
                <td style="border: none; padding: 0;"><b>Place:</b> Saharsa<br><b>Date:</b> ___________</td>
                <td style="border: none; padding: 0; text-align: right;"><b>({full_name})</b></td>
            </tr>
        </table>
    </div>
</div>
"""

col_preview, col_space = st.columns([0.85, 0.15])

with col_preview:
    st.markdown("<div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;'><h3>👁️ Live Exact Preview</h3></div>", unsafe_allow_html=True)
    
    # Precise Full-Page A4 Print Engine Script
    st.components.v1.html(f"""
        <script>
        function printResume() {{
            var content = `{resume_body_html}`;
            var printWindow = window.open('', '_blank', 'width=1000,height=1000');
            printWindow.document.write('<!DOCTYPE html><html><head><title>Print Resume</title>');
            printWindow.document.write('<style>');
            printWindow.document.write(`
                @page {{
                    size: A4 portrait;
                    margin: 12mm 15mm;
                }}
                html, body {{
                    width: 100%;
                    height: 100%;
                    margin: 0;
                    padding: 0;
                    background-color: #fff;
                    font-family: Arial, Helvetica, sans-serif;
                    -webkit-print-color-adjust: exact;
                }}
                .resume-card {{
                    width: 100% !important;
                    max-width: none !important;
                    box-shadow: none !important;
                    border: none !important;
                    padding: 0 !important;
                    margin: 0 !important;
                }}
                ul {{
                    padding-left: 16px !important;
                }}
            `);
            printWindow.document.write('</style></head><body>');
            printWindow.document.write(content);
            printWindow.document.write('</body></html>');
            printWindow.document.close();
            
            printWindow.onload = function() {{
                setTimeout(function() {{
                    printWindow.focus();
                    printWindow.print();
                    printWindow.close();
                }}, 300);
            }};
        }}
        </script>
        <button onclick="printResume()" style="background-color: #2563EB; color: white; border: none; padding: 11px 22px; border-radius: 6px; font-weight: bold; cursor: pointer; font-size: 14px; box-shadow: 0 2px 4px rgba(0,0,0,0.2);">
            🖨️ Print / Download PDF
        </button>
    """, height=55)

    # Render Preview on Streamlit page
    st.html(resume_body_html)
