import streamlit as st
import base64

st.set_page_config(
    page_title="Resume Builder - Prashant Kumar",
    page_icon="📄",
    layout="wide"
)

# Custom Styling to match the EXACT original UI
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    .stApp {
        background-color: #f8fafc;
    }
    .main-title {
        color: #1e293b;
        font-weight: 700;
        margin-bottom: 15px;
    }

    /* Resume Container */
    .resume-card {
        background-color: #ffffff;
        border-radius: 8px;
        padding: 24px;
        color: #1e293b;
        font-family: 'Inter', -apple-system, sans-serif;
        max-width: 800px;
        margin: auto;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1);
        border: 1px solid #e2e8f0;
    }

    /* Header Banner */
    .resume-header {
        background-color: #1e293b;
        color: #ffffff;
        border-radius: 8px;
        padding: 20px 24px;
        margin-bottom: 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .header-info h1 {
        margin: 0;
        font-size: 24px;
        font-weight: 700;
        letter-spacing: 0.5px;
        color: #ffffff;
        text-transform: uppercase;
    }
    .header-info .sub-title {
        color: #38bdf8;
        font-size: 13.5px;
        font-weight: 600;
        margin-top: 4px;
        margin-bottom: 12px;
    }
    .header-contact {
        font-size: 11.5px;
        color: #cbd5e1;
        line-height: 1.6;
    }

    /* Photo Frame */
    .photo-box {
        width: 100px;
        height: 120px;
        border-radius: 6px;
        border: 2px solid #38bdf8;
        overflow: hidden;
        background-color: #0f172a;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .photo-box img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }

    /* Section Headers */
    .section-title {
        font-size: 13px;
        font-weight: 700;
        color: #1e293b;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        border-bottom: 2px solid #0284c7;
        padding-bottom: 4px;
        margin-bottom: 12px;
        margin-top: 14px;
    }

    /* Content Cards */
    .info-card {
        background-color: #f8fafc;
        border-radius: 6px;
        padding: 10px 12px;
        margin-bottom: 10px;
        border-left: 3px solid #0284c7;
    }
    .info-card-title {
        font-size: 12.5px;
        font-weight: 700;
        color: #0f172a;
    }
    .info-card-sub {
        font-size: 11px;
        color: #0284c7;
        font-weight: 600;
        margin-top: 2px;
        margin-bottom: 4px;
    }
    .info-card-desc {
        font-size: 11px;
        color: #475569;
        line-height: 1.4;
    }

    /* Key Competencies */
    .competencies-list {
        background-color: #f8fafc;
        border-radius: 6px;
        padding: 10px 12px 10px 28px;
        margin: 0 0 10px 0;
        border-left: 3px solid #0284c7;
        font-size: 11px;
        color: #334155;
    }
    .competencies-list li {
        margin-bottom: 4px;
    }

    /* Personal Details Table */
    .personal-table {
        width: 100%;
        font-size: 11px;
        color: #334155;
        border-collapse: collapse;
        background-color: #f8fafc;
        border-radius: 6px;
        padding: 8px 12px;
        border-left: 3px solid #0284c7;
    }
    .personal-table td {
        padding: 3px 6px;
        border: none;
    }

    /* Declaration Section */
    .declaration-box {
        background-color: #f8fafc;
        border-radius: 6px;
        padding: 10px 12px;
        margin-top: 14px;
        border: 1px solid #e2e8f0;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h2 class='main-title'>📄 Professional Resume Builder</h2>", unsafe_allow_html=True)

# --- SIDEBAR CONTROLS ---
with st.sidebar:
    st.header("📝 Personal & Job Details")
    photo_file = st.file_uploader("Upload Passport Size Photo", type=["jpg", "jpeg", "png"])
    
    full_name = st.text_input("Full Name", "PRASHANT KUMAR")
    designation = st.text_input("Designation / Title", "Medical Representative & Sales Professional")
    address = st.text_area("Address", "At - Batraha, Ward No. 36, PO+PS+Dist: Saharsa, Bihar (852201)", height=60)
    phone = st.text_input("Phone Number", "+91 8864097233")
    email = st.text_input("Email ID", "Prashantkumar886409@gmail.com")
    
    st.markdown("---")
    st.subheader("Work Experience")
    exp1_company = st.text_input("Company 1", "Pharmanova Specialties Pvt. Ltd.")
    exp1_duration = st.text_input("Duration 1", "12-02-2025 – Present")
    exp1_desc = st.text_area("Responsibilities 1", "Responsible for pharmaceutical sales, technical marketing, and client relationship management.", height=60)

    exp2_company = st.text_input("Company 2", "Hi-tech Laboratories Pharma")
    exp2_duration = st.text_input("Duration 2", "10-06-2024 – 31-01-2025")
    exp2_desc = st.text_area("Responsibilities 2", "Handled product promotion, doctor visits, and territory sales development.", height=60)

    st.markdown("---")
    st.subheader("Education Qualification")
    edu_pg = st.text_input("M.Sc", "B.N.M.U Madhepura | Passed 2023")
    edu_grad = st.text_input("B.Sc", "B.N.M.U Madhepura | Passed 2020")
    edu_12th = st.text_input("12th", "B.S.E.B Patna | Passed 2016")
    edu_10th = st.text_input("10th", "B.S.E.B Patna Passed 2014")

    st.markdown("---")
    st.subheader("Technical & Competencies")
    tech_qual = st.text_input("Technical Title", "ADCA (1 Year Computer Degree)")
    tech_qual_desc = st.text_input("Technical Details", "Advanced Diploma in Computer Applications.")
    skills = st.text_area("Key Competencies (Comma Separated)", "Medicine & Pharma Knowledge, Technical Marketing & Sales, Computer Operations, Client Relationship Management", height=70)

    st.markdown("---")
    st.subheader("Personal Info")
    dob = st.text_input("Date of Birth", "07-04-1999")
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    father_name = st.text_input("Father's Name", "Sanjeev Kumar")
    languages = st.text_input("Languages Known", "Hindi, English, Maithili")
    marital_status = st.selectbox("Marital Status", ["Single", "Married"])
    hobbies = st.text_input("Hobbies & Interests", "Watching news & engaged in creative activities.")

# Image Base64 Encoding
if photo_file is not None:
    bytes_data = photo_file.getvalue()
    base64_image = base64.b64encode(bytes_data).decode()
    photo_html = f'<img src="data:image/png;base64,{base64_image}">'
else:
    photo_html = '<div style="font-size:10px; color:#cbd5e1; text-align:center;">Passport<br>Photo</div>'

skills_list = [s.strip() for s in skills.split(",") if s.strip()]
skills_html = "".join([f"<li>{s}</li>" for s in skills_list])

# HTML Inner Content for Resume
resume_inner_html = f"""
    <!-- Top Header Banner -->
    <div class="resume-header">
        <div class="header-info">
            <h1>{full_name}</h1>
            <div class="sub-title">{designation}</div>
            <div class="header-contact">
                📍 <b>Address:</b> {address}<br>
                📞 <b>Phone:</b> {phone} &nbsp;|&nbsp; ✉️ <b>Email:</b> {email}
            </div>
        </div>
        <div class="photo-box">
            {photo_html}
        </div>
    </div>

    <!-- 2 Column Section Layout -->
    <table style="width: 100%; border-collapse: collapse; table-layout: fixed;">
        <tr>
            <!-- Left Column: Work Exp & Education -->
            <td style="width: 50%; vertical-align: top; padding-right: 14px; border: none;">
                
                <div class="section-title">WORK EXPERIENCE</div>
                
                <div class="info-card">
                    <div class="info-card-title">{exp1_company}</div>
                    <div class="info-card-sub">{exp1_duration}</div>
                    <div class="info-card-desc">{exp1_desc}</div>
                </div>

                <div class="info-card">
                    <div class="info-card-title">{exp2_company}</div>
                    <div class="info-card-sub">{exp2_duration}</div>
                    <div class="info-card-desc">{exp2_desc}</div>
                </div>

                <div class="section-title">EDUCATION QUALIFICATION</div>

                <div class="info-card">
                    <div class="info-card-title">Post Graduation (M.Sc)</div>
                    <div class="info-card-sub" style="color: #475569; font-weight: normal;">{edu_pg}</div>
                </div>

                <div class="info-card">
                    <div class="info-card-title">Graduation (B.Sc)</div>
                    <div class="info-card-sub" style="color: #475569; font-weight: normal;">{edu_grad}</div>
                </div>

                <div class="info-card">
                    <div class="info-card-title">Higher Secondary (12th - I.Sc)</div>
                    <div class="info-card-sub" style="color: #475569; font-weight: normal;">{edu_12th}</div>
                </div>

                <div class="info-card">
                    <div class="info-card-title">Secondary (10th)</div>
                    <div class="info-card-sub" style="color: #475569; font-weight: normal;">{edu_10th}</div>
                </div>

            </td>

            <!-- Right Column: Tech, Competencies, Personal Details, Hobbies -->
            <td style="width: 50%; vertical-align: top; padding-left: 14px; border: none;">
                
                <div class="section-title">TECHNICAL QUALIFICATION</div>
                <div class="info-card">
                    <div class="info-card-title">{tech_qual}</div>
                    <div class="info-card-desc" style="margin-top: 2px;">{tech_qual_desc}</div>
                </div>

                <div class="section-title">KEY COMPETENCIES</div>
                <ul class="competencies-list">
                    {skills_html}
                </ul>

                <div class="section-title">PERSONAL DETAILS</div>
                <table class="personal-table">
                    <tr><td style="width: 42%;"><b>D.O.B:</b></td><td>{dob}</td></tr>
                    <tr><td><b>Gender:</b></td><td>{gender}</td></tr>
                    <tr><td><b>Father's Name:</b></td><td>{father_name}</td></tr>
                    <tr><td><b>Languages:</b></td><td>{languages}</td></tr>
                    <tr><td><b>Marital Status:</b></td><td>{marital_status}</td></tr>
                    <tr><td><b>Nationality:</b></td><td>Indian</td></tr>
                </table>

                <div class="section-title">HOBBIES & INTERESTS</div>
                <div class="info-card">
                    <div class="info-card-desc" style="color: #1e293b;">{hobbies}</div>
                </div>

            </td>
        </tr>
    </table>

    <!-- Declaration -->
    <div class="declaration-box">
        <div style="font-size: 11.5px; font-weight: 700; color: #1e293b; margin-bottom: 4px;">Declaration</div>
        <div style="font-size: 10.5px; color: #475569; font-style: italic;">I hereby declare that all the information provided above is true and correct to the best of my knowledge and belief.</div>
        
        <table style="width: 100%; margin-top: 25px; font-size: 11px; color: #1e293b; border: none;">
            <tr>
                <td style="border: none; padding: 0;"><b>Place:</b> Saharsa<br><b>Date:</b> ___________</td>
                <td style="border: none; padding: 0; text-align: right; vertical-align: bottom;"><b>({full_name})</b></td>
            </tr>
        </table>
    </div>
"""

# Guaranteed Direct Window Print Script
print_button_script = f"""
    <script>
    function triggerPrint() {{
        var printWin = window.open('', '_blank', 'width=900,height=1000');
        printWin.document.open();
        printWin.document.write(`
            <!DOCTYPE html>
            <html>
            <head>
                <title>Resume - {full_name}</title>
                <style>
                    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
                    @page {{
                        size: A4 portrait;
                        margin: 10mm;
                    }}
                    body {{
                        font-family: 'Inter', sans-serif;
                        margin: 0;
                        padding: 0;
                        background: #ffffff;
                        -webkit-print-color-adjust: exact !important;
                        print-color-adjust: exact !important;
                    }}
                    .resume-card {{
                        width: 100%;
                        background: #ffffff;
                    }}
                    .resume-header {{
                        background-color: #1e293b !important;
                        color: #ffffff !important;
                        border-radius: 6px;
                        padding: 16px 20px;
                        margin-bottom: 16px;
                        display: flex;
                        justify-content: space-between;
                        align-items: center;
                    }}
                    .header-info h1 {{
                        margin: 0;
                        font-size: 22px;
                        font-weight: 700;
                        color: #ffffff !important;
                        text-transform: uppercase;
                    }}
                    .header-info .sub-title {{
                        color: #38bdf8 !important;
                        font-size: 13px;
                        font-weight: 600;
                        margin-top: 4px;
                        margin-bottom: 8px;
                    }}
                    .header-contact {{
                        font-size: 11px;
                        color: #cbd5e1 !important;
                        line-height: 1.5;
                    }}
                    .photo-box {{
                        width: 95px;
                        height: 115px;
                        border-radius: 4px;
                        border: 2px solid #38bdf8;
                        overflow: hidden;
                        background-color: #0f172a;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                    }}
                    .photo-box img {{
                        width: 100%;
                        height: 100%;
                        object-fit: cover;
                    }}
                    .section-title {{
                        font-size: 12px;
                        font-weight: 700;
                        color: #1e293b;
                        text-transform: uppercase;
                        border-bottom: 2px solid #0284c7;
                        padding-bottom: 3px;
                        margin-bottom: 10px;
                        margin-top: 12px;
                    }}
                    .info-card {{
                        background-color: #f8fafc !important;
                        border-radius: 4px;
                        padding: 8px 10px;
                        margin-bottom: 8px;
                        border-left: 3px solid #0284c7 !important;
                    }}
                    .info-card-title {{ font-size: 12px; font-weight: 700; color: #0f172a; }}
                    .info-card-sub {{ font-size: 10.5px; color: #0284c7; font-weight: 600; margin-top: 2px; }}
                    .info-card-desc {{ font-size: 10.5px; color: #475569; line-height: 1.35; }}
                    .competencies-list {{
                        background-color: #f8fafc !important;
                        border-radius: 4px;
                        padding: 8px 10px 8px 24px;
                        margin: 0 0 8px 0;
                        border-left: 3px solid #0284c7 !important;
                        font-size: 10.5px;
                        color: #334155;
                    }}
                    .personal-table {{
                        width: 100%;
                        font-size: 10.5px;
                        color: #334155;
                        border-collapse: collapse;
                        background-color: #f8fafc !important;
                        border-radius: 4px;
                        padding: 6px 10px;
                        border-left: 3px solid #0284c7 !important;
                    }}
                    .personal-table td {{ padding: 2px 4px; }}
                    .declaration-box {{
                        background-color: #f8fafc !important;
                        border-radius: 4px;
                        padding: 8px 10px;
                        margin-top: 10px;
                        border: 1px solid #e2e8f0;
                    }}
                </style>
            </head>
            <body>
                <div class="resume-card">
                    {resume_inner_html}
                </div>
            </body>
            </html>
        `);
        printWin.document.close();
        printWin.focus();
        setTimeout(function() {{
            printWin.print();
            printWin.close();
        }}, 500);
    }}
    </script>
    <button onclick="triggerPrint()" style="background-color: #0284c7; color: white; border: none; padding: 12px 28px; border-radius: 6px; font-weight: bold; cursor: pointer; font-size: 15px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); margin-bottom: 15px;">
        🖨️ Print / Save as PDF
    </button>
"""

st.components.v1.html(print_button_script, height=60)

# Screen Preview Box
st.html(f'<div class="resume-card">{resume_inner_html}</div>')
