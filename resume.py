import streamlit as st
import base64

st.set_page_config(
    page_title="Resume Builder - Koshi Enterprises",
    page_icon="📄",
    layout="wide"
)

# Global Styling & Print CSS for Perfect Full A4 Height & Spacing
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
        padding: 35px 40px;
        color: #000000;
        font-family: 'Segoe UI', Arial, Helvetica, sans-serif;
        max-width: 850px;
        margin: auto;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
        min-height: 1050px;
    }
    
    /* PRINT MEDIA STYLING - FULL A4 COVERAGE */
    @media print {
        body * {
            visibility: hidden !important;
        }
        #resume-printable-area, #resume-printable-area * {
            visibility: visible !important;
        }
        #resume-printable-area {
            position: absolute !important;
            left: 0 !important;
            top: 0 !important;
            width: 100% !important;
            max-width: none !important;
            border: none !important;
            box-shadow: none !important;
            padding: 0 !important;
            margin: 0 !important;
        }
        @page {
            size: A4 portrait;
            margin: 15mm 18mm;
        }
        [data-testid="stSidebar"], .main-title, .stButton, button, iframe {
            display: none !important;
        }
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h2 class='main-title'>📄 Professional Resume Builder</h2>", unsafe_allow_html=True)

# --- SIDEBAR INPUTS ---
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

# Photo Base64 Processing
photo_html = ""
if photo_file is not None:
    bytes_data = photo_file.getvalue()
    base64_image = base64.b64encode(bytes_data).decode()
    photo_html = f'<img src="data:image/png;base64,{base64_image}" style="width: 110px; height: 135px; object-fit: cover; border: 1px solid #000; border-radius: 2px;">'
else:
    photo_html = '<div style="width: 110px; height: 135px; border: 1px dashed #444; display: flex; align-items: center; justify-content: center; font-size: 11px; color: #555; text-align: center; font-weight: 500;">Passport<br>Photo</div>'

# Skills List
skills_list = [s.strip() for s in skills.split(",") if s.strip()]
skills_html = "".join([f"<li style='margin-bottom: 6px;'>{s}</li>" for s in skills_list])

# HTML Layout
resume_body_html = f"""
<div class="resume-card" id="resume-printable-area">
    <!-- Header with Photo -->
    <table style="width: 100%; border-collapse: collapse; border-bottom: 2px solid #000; padding-bottom: 12px; margin-bottom: 20px;">
        <tr>
            <td style="vertical-align: top; border: none;">
                <h1 style="margin: 0; font-size: 26px; font-weight: bold; color: #000; letter-spacing: 0.5px; text-transform: uppercase;">{full_name}</h1>
                <div style="font-size: 15px; font-weight: bold; color: #1D4ED8; margin-top: 5px;">{designation}</div>
                <div style="font-size: 12.5px; color: #000; margin-top: 8px; line-height: 1.4;"><b>Address:</b> {address}</div>
                <div style="font-size: 12.5px; color: #000; margin-top: 4px;"><b>Phone:</b> {phone} &nbsp;|&nbsp; <b>Email:</b> {email}</div>
            </td>
            <td style="width: 120px; text-align: right; vertical-align: top; border: none;">
                {photo_html}
            </td>
        </tr>
    </table>

    <!-- 2 Column Layout Table -->
    <table style="width: 100%; border-collapse: collapse; table-layout: fixed;">
        <tr>
            <!-- Left Column -->
            <td style="width: 50%; vertical-align: top; padding-right: 20px; border: none;">
                
                <div style="font-weight: bold; font-size: 13.5px; border-bottom: 1.5px solid #000; margin-bottom: 10px; padding-bottom: 3px; text-transform: uppercase; letter-spacing: 0.5px;">WORK EXPERIENCE</div>
                
                <div style="margin-bottom: 16px;">
                    <div style="font-size: 13px; font-weight: bold; color: #000;">{exp1_company}</div>
                    <div style="font-size: 12px; color: #1D4ED8; font-weight: bold; margin-top: 2px; margin-bottom: 4px;">{exp1_duration}</div>
                    <div style="font-size: 12px; color: #222; line-height: 1.45;">{exp1_desc}</div>
                </div>

                <div style="margin-bottom: 22px;">
                    <div style="font-size: 13px; font-weight: bold; color: #000;">{exp2_company}</div>
                    <div style="font-size: 12px; color: #1D4ED8; font-weight: bold; margin-top: 2px; margin-bottom: 4px;">{exp2_duration}</div>
                    <div style="font-size: 12px; color: #222; line-height: 1.45;">{exp2_desc}</div>
                </div>

                <div style="font-weight: bold; font-size: 13.5px; border-bottom: 1.5px solid #000; margin-bottom: 10px; padding-bottom: 3px; text-transform: uppercase; letter-spacing: 0.5px;">TECHNICAL QUALIFICATION</div>
                <div style="margin-bottom: 22px;">
                    <div style="font-size: 12.5px; font-weight: bold; color: #000;">{tech_qual}</div>
                    <div style="font-size: 12px; color: #333; margin-top: 3px;">{tech_qual_desc}</div>
                </div>

                <div style="font-weight: bold; font-size: 13.5px; border-bottom: 1.5px solid #000; margin-bottom: 10px; padding-bottom: 3px; text-transform: uppercase; letter-spacing: 0.5px;">PERSONAL DETAILS</div>
                <table style="width: 100%; font-size: 12px; color: #000; border-collapse: collapse;">
                    <tr><td style="width: 44%; padding: 3px 0; border: none;"><b>D.O.B:</b></td><td style="border: none;">{dob}</td></tr>
                    <tr><td style="padding: 3px 0; border: none;"><b>Gender:</b></td><td style="border: none;">{gender}</td></tr>
                    <tr><td style="padding: 3px 0; border: none;"><b>Father's Name:</b></td><td style="border: none;">{father_name}</td></tr>
                    <tr><td style="padding: 3px 0; border: none;"><b>Languages:</b></td><td style="border: none;">{languages}</td></tr>
                    <tr><td style="padding: 3px 0; border: none;"><b>Marital Status:</b></td><td style="border: none;">{marital_status}</td></tr>
                    <tr><td style="padding: 3px 0; border: none;"><b>Nationality:</b></td><td style="border: none;">Indian</td></tr>
                </table>

            </td>

            <!-- Right Column -->
            <td style="width: 50%; vertical-align: top; padding-left: 20px; border: none;">
                
                <div style="font-weight: bold; font-size: 13.5px; border-bottom: 1.5px solid #000; margin-bottom: 10px; padding-bottom: 3px; text-transform: uppercase; letter-spacing: 0.5px;">EDUCATION QUALIFICATION</div>
                
                <div style="margin-bottom: 10px;">
                    <div style="font-size: 12.5px; font-weight: bold; color: #000;">Post Graduation (M.Sc)</div>
                    <div style="font-size: 12px; color: #333; margin-top: 2px;">{edu_pg}</div>
                </div>

                <div style="margin-bottom: 10px;">
                    <div style="font-size: 12.5px; font-weight: bold; color: #000;">Graduation (B.Sc)</div>
                    <div style="font-size: 12px; color: #333; margin-top: 2px;">{edu_grad}</div>
                </div>

                <div style="margin-bottom: 10px;">
                    <div style="font-size: 12.5px; font-weight: bold; color: #000;">Higher Secondary (12th - I.Sc)</div>
                    <div style="font-size: 12px; color: #333; margin-top: 2px;">{edu_12th}</div>
                </div>

                <div style="margin-bottom: 22px;">
                    <div style="font-size: 12.5px; font-weight: bold; color: #000;">Secondary (10th)</div>
                    <div style="font-size: 12px; color: #333; margin-top: 2px;">{edu_10th}</div>
                </div>

                <div style="font-weight: bold; font-size: 13.5px; border-bottom: 1.5px solid #000; margin-bottom: 10px; padding-bottom: 3px; text-transform: uppercase; letter-spacing: 0.5px;">KEY COMPETENCIES</div>
                <ul style="margin: 0 0 22px 0; padding-left: 18px; font-size: 12px; color: #000; line-height: 1.4;">
                    {skills_html}
                </ul>

                <div style="font-weight: bold; font-size: 13.5px; border-bottom: 1.5px solid #000; margin-bottom: 10px; padding-bottom: 3px; text-transform: uppercase; letter-spacing: 0.5px;">HOBBIES & INTERESTS</div>
                <div style="font-size: 12px; color: #000; margin-bottom: 15px; line-height: 1.4;">{hobbies}</div>

            </td>
        </tr>
    </table>

    <!-- Declaration -->
    <div style="margin-top: 20px;">
        <div style="font-weight: bold; font-size: 13.5px; border-bottom: 1.5px solid #000; margin-bottom: 8px; padding-bottom: 3px; text-transform: uppercase; letter-spacing: 0.5px;">DECLARATION</div>
        <div style="font-size: 11.5px; color: #222; font-style: italic; line-height: 1.4;">I hereby declare that all the information provided above is true and correct to the best of my knowledge and belief.</div>
    </div>

    <!-- Signature Section -->
    <div style="margin-top: 50px;">
        <table style="width: 100%; font-size: 12.5px; border: none;">
            <tr>
                <td style="border: none; padding: 0;"><b>Place:</b> Saharsa<br><br><b>Date:</b> ___________</td>
                <td style="border: none; padding: 0; text-align: right; vertical-align: bottom;"><b>({full_name})</b></td>
            </tr>
        </table>
    </div>
</div>
"""

col_preview, col_space = st.columns([0.85, 0.15])

with col_preview:
    st.markdown("<h3>👁️ Live Exact Preview</h3>", unsafe_allow_html=True)
    
    # Direct Print Trigger
    st.components.v1.html("""
        <button onclick="window.parent.print()" style="background-color: #2563EB; color: white; border: none; padding: 12px 24px; border-radius: 6px; font-weight: bold; cursor: pointer; font-size: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.2); margin-bottom: 15px;">
            🖨️ Print / Save as PDF (Full A4)
        </button>
    """, height=55)

    # Render Preview
    st.html(resume_body_html)
