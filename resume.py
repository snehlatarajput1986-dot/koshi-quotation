import streamlit as st

st.set_page_config(
    page_title="Resume Builder - Koshi Enterprises",
    page_icon="📄",
    layout="wide"
)

# Custom Styling for Professional Webpage Theme
st.markdown("""
    <style>
    .main-title {
        color: #1E3A8A;
        font-weight: 700;
        margin-bottom: 20px;
    }
    
    .resume-card {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 35px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        color: #1f2937;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    .resume-header {
        border-bottom: 2px solid #1E3A8A;
        padding-bottom: 12px;
        margin-bottom: 20px;
    }
    
    .section-title {
        font-weight: bold;
        font-size: 14px;
        color: #1E3A8A;
        border-bottom: 1px solid #cbd5e1;
        margin-top: 18px;
        margin-bottom: 8px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    </style>
""", unsafe_allow_html=True)

# Header Section
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
    st.subheader("Personal Info")
    dob = st.text_input("Date of Birth", "07-04-1999")
    father_name = st.text_input("Father's Name", "Sanjeev Kumar")
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    marital_status = st.selectbox("Marital Status", ["Single", "Married"])
    languages = st.text_input("Languages Known", "Hindi, English, Maithili")

    st.markdown("---")
    st.subheader("Work Experience")
    exp1_company = st.text_input("Company 1", "Pharmanova Specialties Pvt. Ltd.")
    exp1_duration = st.text_input("Duration 1", "12-02-2025 - Present")
    exp1_desc = st.text_area("Responsibilities 1", "Responsible for pharmaceutical sales, technical marketing, and client relationship management.", height=70)

    exp2_company = st.text_input("Company 2", "Hi-tech Laboratories Pharma")
    exp2_duration = st.text_input("Duration 2", "10-06-2024 - 31-01-2025")
    exp2_desc = st.text_area("Responsibilities 2", "Handled product promotion, doctor visits, and territory sales development.", height=70)

    st.markdown("---")
    st.subheader("Education & Skills")
    edu_pg = st.text_input("M.Sc", "B.N.M.U Madhepura | Passed 2023")
    edu_grad = st.text_input("B.Sc", "B.N.M.U Madhepura | Passed 2020")
    edu_12th = st.text_input("12th", "B.S.E.B Patna | Passed 2016")
    edu_10th = st.text_input("10th", "B.S.E.B Patna | Passed 2014")

    tech_qual = st.text_input("Technical Qualification", "ADCA (1 Year Computer Degree)")
    skills = st.text_area("Key Competencies", "Medicine & Pharma Knowledge, Technical Marketing & Sales, Computer Operations, Client Relationship Management", height=80)
    hobbies = st.text_input("Hobbies & Interests", "Watching news & engaged in creative activities.")

# --- MAIN CONTENT AREA: LIVE PREVIEW & PRINT ---
col_preview, col_space = st.columns([0.85, 0.15])

skills_list = [s.strip() for s in skills.split(",") if s.strip()]
skills_html = "".join([f"<li style='margin-bottom: 3px;'>{s}</li>" for s in skills_list])

# Resume Body HTML
resume_body_html = f"""
    <div class="resume-card" id="resume-printable-area">
        <div class="resume-header">
            <h2 style="margin: 0; font-size: 24px; color: #111827; text-transform: uppercase; letter-spacing: 0.5px;">{full_name}</h2>
            <h4 style="margin: 4px 0 10px 0; color: #2563EB; font-weight: 600; font-size: 15px;">{designation}</h4>
            <p style="margin: 2px 0; font-size: 12.5px; color: #4b5563;"><b>Address:</b> {address}</p>
            <p style="margin: 2px 0; font-size: 12.5px; color: #4b5563;"><b>Phone:</b> {phone} &nbsp;|&nbsp; <b>Email:</b> {email}</p>
        </div>

        <div class="section-title">Work Experience</div>
        <p style="margin: 4px 0 1px 0; font-size: 13.5px;"><b>{exp1_company}</b> <span style="color: #6b7280; font-size: 12px;">({exp1_duration})</span></p>
        <p style="margin: 0 0 8px 0; font-size: 12.5px; color: #374151;">{exp1_desc}</p>
        
        <p style="margin: 4px 0 1px 0; font-size: 13.5px;"><b>{exp2_company}</b> <span style="color: #6b7280; font-size: 12px;">({exp2_duration})</span></p>
        <p style="margin: 0 0 8px 0; font-size: 12.5px; color: #374151;">{exp2_desc}</p>

        <div class="section-title">Education Qualification</div>
        <ul style="margin: 0; padding-left: 18px; font-size: 12.5px; color: #374151;">
            <li style="margin-bottom: 2px;"><b>Post Graduation (M.Sc):</b> {edu_pg}</li>
            <li style="margin-bottom: 2px;"><b>Graduation (B.Sc):</b> {edu_grad}</li>
            <li style="margin-bottom: 2px;"><b>Higher Secondary (12th):</b> {edu_12th}</li>
            <li style="margin-bottom: 2px;"><b>Secondary (10th):</b> {edu_10th}</li>
        </ul>

        <div class="section-title">Technical Qualification</div>
        <p style="margin: 2px 0; font-size: 12.5px; color: #374151;">{tech_qual}</p>

        <div class="section-title">Key Competencies</div>
        <ul style="margin: 0; padding-left: 18px; font-size: 12.5px; color: #374151;">
            {skills_html}
        </ul>

        <div class="section-title">Personal Details</div>
        <p style="margin: 2px 0; font-size: 12.5px; color: #374151;"><b>D.O.B:</b> {dob} &nbsp;|&nbsp; <b>Gender:</b> {gender} &nbsp;|&nbsp; <b>Father's Name:</b> {father_name}</p>
        <p style="margin: 2px 0; font-size: 12.5px; color: #374151;"><b>Languages:</b> {languages} &nbsp;|&nbsp; <b>Marital Status:</b> {marital_status} &nbsp;|&nbsp; <b>Nationality:</b> Indian</p>

        <div class="section-title">Hobbies & Interests</div>
        <p style="margin: 2px 0; font-size: 12.5px; color: #374151;">{hobbies}</p>

        <div class="section-title">Declaration</div>
        <p style="margin: 2px 0; font-size: 11.5px; color: #6b7280; font-style: italic;">I hereby declare that all the information provided above is true and correct to the best of my knowledge and belief.</p>
        
        <br><br>
        <table width="100%" style="font-size: 12.5px; border: none; color: #374151;">
            <tr>
                <td style="border: none;"><b>Place:</b> Saharsa<br><b>Date:</b> ___________</td>
                <td align="right" style="border: none;"><b>({full_name})</b></td>
            </tr>
        </table>
    </div>
"""

with col_preview:
    st.markdown("<div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;'><h3>👁️ Live Exact Preview</h3></div>", unsafe_allow_html=True)
    
    # Clean Print Mechanism Script
    st.components.v1.html(f"""
        <script>
        function printResume() {{
            var content = `{resume_body_html}`;
            var printWindow = window.open('', '', 'height=800,width=900');
            printWindow.document.write('<html><head><title>Print Resume</title>');
            printWindow.document.write('<style>');
            printWindow.document.write(`
                body {{ font-family: Arial, sans-serif; padding: 20px; }}
                .resume-card {{ background-color: #fff; padding: 20px; color: #1f2937; }}
                .resume-header {{ border-bottom: 2px solid #1E3A8A; padding-bottom: 12px; margin-bottom: 20px; }}
                .section-title {{ font-weight: bold; font-size: 14px; color: #1E3A8A; border-bottom: 1px solid #cbd5e1; margin-top: 18px; margin-bottom: 8px; text-transform: uppercase; }}
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

    # Render Preview on Streamlit page
    st.html(resume_body_html)
