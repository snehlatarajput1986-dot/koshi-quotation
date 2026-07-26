import streamlit as st

st.set_page_config(
    page_title="Resume Builder - Koshi Enterprises",
    page_icon="📄",
    layout="wide"
)

# Custom Styling for Web Page Preview
st.markdown("""
    <style>
    .main-title {
        color: #1E3A8A;
        font-weight: 700;
        margin-bottom: 20px;
    }
    
    .resume-card {
        background-color: #ffffff;
        border: 1px solid #cbd5e1;
        border-radius: 6px;
        padding: 30px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        color: #0f172a;
        font-family: Arial, sans-serif;
    }
    
    .resume-header {
        border-bottom: 2px solid #1E3A8A;
        padding-bottom: 10px;
        margin-bottom: 15px;
    }
    
    .section-title {
        font-weight: bold;
        font-size: 13px;
        color: #1E3A8A;
        border-bottom: 1px solid #94a3b8;
        margin-top: 14px;
        margin-bottom: 6px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .grid-container {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h2 class='main-title'>📄 Professional Resume Builder</h2>", unsafe_allow_html=True)

# --- SIDEBAR: INPUT DETAILS ---
with st.sidebar:
    st.header("📝 Personal & Job Details")
    
    full_name = st.text_input("Full Name", "PRASHANT KUMAR")
    designation = st.text_input("Designation / Title", "Medical Representative & Sales Professional")
    phone = st.text_input("Phone Number", "+91 8864097233")
    email = st.text_input("Email ID", "Prashantkumar886409@gmail.com")
    address = st.text_area("Address", "At - Batraha, Ward No. 36, PO+PS+Dist: Saharsa, Bihar (852201)", height=70)
    
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
    tech_qual = st.text_input("Technical Qualification Title", "ADCA (1 Year Computer Degree)")
    tech_qual_desc = st.text_input("Technical Qualification Subtitle", "Advanced Diploma in Computer Applications.")
    
    edu_pg = st.text_input("M.Sc", "B.N.M.U Madhepura | Passed 2023")
    edu_grad = st.text_input("B.Sc", "B.N.M.U Madhepura | Passed 2020")
    edu_12th = st.text_input("12th", "B.S.E.B Patna | Passed 2016")
    edu_10th = st.text_input("10th", "B.S.E.B Patna | Passed 2014")

    st.markdown("---")
    st.subheader("Personal Details")
    dob = st.text_input("Date of Birth", "07-04-1999")
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    father_name = st.text_input("Father's Name", "Sanjeev Kumar")
    languages = st.text_input("Languages Known", "Hindi, English, Maithili")
    marital_status = st.selectbox("Marital Status", ["Single", "Married"])
    skills = st.text_area("Key Competencies (Comma Separated)", "Medicine & Pharma Knowledge, Technical Marketing & Sales, Computer Operations, Client Relationship Management", height=70)
    hobbies = st.text_input("Hobbies & Interests", "Watching news & engaged in creative activities.")

# --- MAIN PREVIEW & PRINT ---
skills_list = [s.strip() for s in skills.split(",") if s.strip()]
skills_html = "".join([f"<li style='margin-bottom: 2px;'>{s}</li>" for s in skills_list])

# Exact PDF Duplicate HTML
resume_body_html = f"""
    <div class="resume-card" id="resume-printable-area">
        <div class="resume-header" style="text-align: left;">
            <h2 style="margin: 0; font-size: 22px; color: #1E3A8A; text-transform: uppercase;">{full_name}</h2>
            <h4 style="margin: 3px 0 8px 0; color: #2563EB; font-weight: 600; font-size: 14px;">{designation}</h4>
            <p style="margin: 2px 0; font-size: 11.5px; color: #334155;"><b>Address:</b> {address}</p>
            <p style="margin: 2px 0; font-size: 11.5px; color: #334155;"><b>Phone:</b> {phone} &nbsp;|&nbsp; <b>Email:</b> {email}</p>
        </div>

        <div style="display: table; width: 100%; table-layout: fixed;">
            <div style="display: table-cell; width: 50%; vertical-align: top; padding-right: 12px;">
                <div class="section-title">WORK EXPERIENCE</div>
                <p style="margin: 3px 0 1px 0; font-size: 12px;"><b>{exp1_company}</b></p>
                <p style="margin: 0; font-size: 11px; color: #2563EB;"><b>{exp1_duration}</b></p>
                <p style="margin: 2px 0 8px 0; font-size: 11px; color: #334155;">{exp1_desc}</p>
                
                <p style="margin: 3px 0 1px 0; font-size: 12px;"><b>{exp2_company}</b></p>
                <p style="margin: 0; font-size: 11px; color: #2563EB;"><b>{exp2_duration}</b></p>
                <p style="margin: 2px 0 8px 0; font-size: 11px; color: #334155;">{exp2_desc}</p>

                <div class="section-title">TECHNICAL QUALIFICATION</div>
                <p style="margin: 2px 0 0 0; font-size: 12px;"><b>{tech_qual}</b></p>
                <p style="margin: 0 0 8px 0; font-size: 11px; color: #475569;">{tech_qual_desc}</p>

                <div class="section-title">PERSONAL DETAILS</div>
                <table style="width: 100%; font-size: 11px; color: #334155; border: none;">
                    <tr><td style="padding: 1px 0; width: 45%;"><b>D.O.B:</b></td><td>{dob}</td></tr>
                    <tr><td style="padding: 1px 0;"><b>Gender:</b></td><td>{gender}</td></tr>
                    <tr><td style="padding: 1px 0;"><b>Father's Name:</b></td><td>{father_name}</td></tr>
                    <tr><td style="padding: 1px 0;"><b>Languages:</b></td><td>{languages}</td></tr>
                    <tr><td style="padding: 1px 0;"><b>Marital Status:</b></td><td>{marital_status}</td></tr>
                    <tr><td style="padding: 1px 0;"><b>Nationality:</b></td><td>Indian</td></tr>
                </table>
            </div>

            <div style="display: table-cell; width: 50%; vertical-align: top; padding-left: 12px;">
                <div class="section-title">EDUCATION QUALIFICATION</div>
                <p style="margin: 2px 0 0 0; font-size: 11.5px;"><b>Post Graduation (M.Sc)</b></p>
                <p style="margin: 0 0 6px 0; font-size: 11px; color: #475569;">{edu_pg}</p>

                <p style="margin: 2px 0 0 0; font-size: 11.5px;"><b>Graduation (B.Sc)</b></p>
                <p style="margin: 0 0 6px 0; font-size: 11px; color: #475569;">{edu_grad}</p>

                <p style="margin: 2px 0 0 0; font-size: 11.5px;"><b>Higher Secondary (12th - I.Sc)</b></p>
                <p style="margin: 0 0 6px 0; font-size: 11px; color: #475569;">{edu_12th}</p>

                <p style="margin: 2px 0 0 0; font-size: 11.5px;"><b>Secondary (10th)</b></p>
                <p style="margin: 0 0 6px 0; font-size: 11px; color: #475569;">{edu_10th}</p>

                <div class="section-title">KEY COMPETENCIES</div>
                <ul style="margin: 0; padding-left: 15px; font-size: 11px; color: #334155;">
                    {skills_html}
                </ul>

                <div class="section-title">HOBBIES & INTERESTS</div>
                <p style="margin: 2px 0 8px 0; font-size: 11px; color: #334155;">{hobbies}</p>
            </div>
        </div>

        <div class="section-title">DECLARATION</div>
        <p style="margin: 2px 0; font-size: 10.5px; color: #475569; font-style: italic;">I hereby declare that all the information provided above is true and correct to the best of my knowledge and belief.</p>
        
        <br>
        <table width="100%" style="font-size: 11.5px; border: none; color: #334155;">
            <tr>
                <td style="border: none;"><b>Place:</b> Saharsa<br><b>Date:</b> ___________</td>
                <td align="right" style="border: none;"><b>({full_name})</b></td>
            </tr>
        </table>
    </div>
"""

col_preview, col_space = st.columns([0.85, 0.15])

with col_preview:
    st.markdown("<div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;'><h3>👁️ Live Exact Preview</h3></div>", unsafe_allow_html=True)
    
    # Print Script with Side-by-Side PDF Column Support
    st.components.v1.html(f"""
        <script>
        function printResume() {{
            var content = `{resume_body_html}`;
            var printWindow = window.open('', '', 'height=800,width=900');
            printWindow.document.write('<html><head><title>Print Resume</title>');
            printWindow.document.write('<style>');
            printWindow.document.write(`
                @page {{ size: A4; margin: 15mm; }}
                body {{ font-family: Arial, sans-serif; background-color: #fff; margin: 0; padding: 0; }}
                .resume-card {{ padding: 0; color: #0f172a; }}
                .resume-header {{ border-bottom: 2px solid #1E3A8A; padding-bottom: 10px; margin-bottom: 15px; }}
                .section-title {{ font-weight: bold; font-size: 12px; color: #1E3A8A; border-bottom: 1px solid #94a3b8; margin-top: 12px; margin-bottom: 6px; text-transform: uppercase; }}
                table {{ border-collapse: collapse; }}
            `);
            printWindow.document.write('</style></head><body>');
            printWindow.document.write(content);
            printWindow.document.write('</body></html>');
            printWindow.document.close();
            printWindow.focus();
            setTimeout(function() {{
                printWindow.print();
                printWindow.close();
            }}, 500);
        }}
        </script>
        <button onclick="printResume()" style="background-color: #2563EB; color: white; border: none; padding: 10px 20px; border-radius: 6px; font-weight: bold; cursor: pointer; font-size: 14px;">
            🖨️ Print / Download PDF
        </button>
    """, height=50)

    # Render Preview
    st.html(resume_body_html)
