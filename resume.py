import streamlit as st
import base64

st.set_page_config(
    page_title="Resume Builder - Prashant Kumar",
    page_icon="📄",
    layout="wide"
)

# Base CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

.stApp { background-color: #f1f5f9; }
.main-title { color: #0f172a; font-weight: 700; margin-bottom: 15px; }

#printableArea {
    background-color: #ffffff;
    width: 780px;
    padding: 24px;
    margin: auto;
    box-sizing: border-box;
    font-family: 'Inter', Arial, sans-serif;
    color: #1e293b;
    border-radius: 4px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
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
    address = st.text_area("Address", "At - Batraha, Ward No. 36, PO+PS+Dist: Saharsa, Bihar (852201)", height=50)
    phone = st.text_input("Phone Number", "+91 8864097233")
    email = st.text_input("Email ID", "Prashantkumar886409@gmail.com")
    
    st.markdown("---")
    st.subheader("Work Experience")
    exp1_company = st.text_input("Company 1", "Pharmanova Specialties Pvt. Ltd.")
    exp1_duration = st.text_input("Duration 1", "12-02-2025 – Present")
    exp1_desc = st.text_area("Responsibilities 1", "Responsible for pharmaceutical sales, technical marketing, and client relationship management.", height=50)

    exp2_company = st.text_input("Company 2", "Hi-tech Laboratories Pharma")
    exp2_duration = st.text_input("Duration 2", "10-06-2024 – 31-01-2025")
    exp2_desc = st.text_area("Responsibilities 2", "Handled product promotion, doctor visits, and territory sales development.", height=50)

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
    skills = st.text_area("Key Competencies (Comma Separated)", "Medicine & Pharma Knowledge, Technical Marketing & Sales, Computer Operations, Client Relationship Management", height=60)

    st.markdown("---")
    st.subheader("Personal Info")
    dob = st.text_input("Date of Birth", "07-04-1999")
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    father_name = st.text_input("Father's Name", "Sanjeev Kumar")
    languages = st.text_input("Languages Known", "Hindi, English, Maithili")
    marital_status = st.selectbox("Marital Status", ["Single", "Married"])
    hobbies = st.text_input("Hobbies & Interests", "Watching news & engaged in creative activities.")

# Photo Base64
if photo_file is not None:
    bytes_data = photo_file.getvalue()
    base64_image = base64.b64encode(bytes_data).decode()
    photo_html = f'<img src="data:image/png;base64,{base64_image}" style="width:100%; height:100%; object-fit:cover;">'
else:
    photo_html = '<div style="font-size:11px; color:#cbd5e1; text-align:center; padding-top:28px;">Passport<br>Photo</div>'

skills_list = [s.strip() for s in skills.split(",") if s.strip()]
skills_html = "".join([f'<li style="margin-bottom:3px;">{s}</li>' for s in skills_list])

# Perfect PDF Downloader Script
st.components.v1.html("""
<script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>
<button onclick="downloadPDF()" style="background-color: #0284c7; color: white; border: none; padding: 12px 28px; border-radius: 6px; font-weight: bold; cursor: pointer; font-size: 16px; box-shadow: 0 4px 10px rgba(0,0,0,0.15);">
    📥 Download Perfect Single-Page PDF
</button>

<script>
function downloadPDF() {
    const element = window.parent.document.getElementById('printableArea');
    const opt = {
        margin:       [3, 3, 3, 3],
        filename:     'Resume_Prashant_Kumar.pdf',
        image:        { type: 'jpeg', quality: 0.98 },
        html2canvas:  { scale: 2, useCORS: true, backgroundColor: '#ffffff', logging: false },
        jsPDF:        { unit: 'mm', format: 'a4', orientation: 'portrait' }
    };
    html2pdf().set(opt).from(element).save();
}
</script>
""", height=60)

# Full Inline HTML Structure (Forces all background colors & borders in PDF)
html_content = f"""
<div id="printableArea" style="background-color: #ffffff; padding: 20px; font-family: 'Inter', Arial, sans-serif;">

    <!-- HEADER BLOCK -->
    <table style="width: 100%; background-color: #1e293b; border-radius: 6px; padding: 14px 18px; border-collapse: collapse; margin-bottom: 14px;">
        <tr>
            <td style="vertical-align: middle; border: none;">
                <h1 style="margin: 0; font-size: 21px; font-weight: 700; color: #ffffff; text-transform: uppercase; letter-spacing: 0.5px;">{full_name}</h1>
                <div style="color: #38bdf8; font-size: 12px; font-weight: 600; margin-top: 3px; margin-bottom: 6px;">{designation}</div>
                <div style="font-size: 10.5px; color: #e2e8f0; line-height: 1.4;">📍 <b>Address:</b> {address}<br>📞 <b>Phone:</b> {phone} &nbsp;|&nbsp; ✉️ <b>Email:</b> {email}</div>
            </td>
            <td style="width: 85px; text-align: right; vertical-align: middle; border: none;">
                <div style="width: 80px; height: 95px; border-radius: 4px; border: 2px solid #38bdf8; background-color: #0f172a; overflow: hidden; display: inline-block;">
                    {photo_html}
                </div>
            </td>
        </tr>
    </table>

    <!-- MAIN TWO COLUMN BODY -->
    <table style="width: 100%; border-collapse: collapse; table-layout: fixed;">
        <tr>
            <!-- LEFT COLUMN -->
            <td style="width: 50%; vertical-align: top; padding-right: 8px; border: none;">
                
                <div style="font-size: 11px; font-weight: 700; color: #0f172a; border-bottom: 2px solid #0284c7; padding-bottom: 2px; margin-bottom: 6px; text-transform: uppercase;">WORK EXPERIENCE</div>
                
                <div style="background-color: #f1f5f9; border-left: 3.5px solid #0284c7; padding: 7px 9px; margin-bottom: 6px; border-radius: 3px;">
                    <div style="font-size: 11px; font-weight: 700; color: #0f172a;">{exp1_company}</div>
                    <div style="font-size: 10px; color: #0284c7; font-weight: 600; margin: 1px 0;">{exp1_duration}</div>
                    <div style="font-size: 10px; color: #334155; line-height: 1.3;">{exp1_desc}</div>
                </div>

                <div style="background-color: #f1f5f9; border-left: 3.5px solid #0284c7; padding: 7px 9px; margin-bottom: 10px; border-radius: 3px;">
                    <div style="font-size: 11px; font-weight: 700; color: #0f172a;">{exp2_company}</div>
                    <div style="font-size: 10px; color: #0284c7; font-weight: 600; margin: 1px 0;">{exp2_duration}</div>
                    <div style="font-size: 10px; color: #334155; line-height: 1.3;">{exp2_desc}</div>
                </div>

                <div style="font-size: 11px; font-weight: 700; color: #0f172a; border-bottom: 2px solid #0284c7; padding-bottom: 2px; margin-bottom: 6px; margin-top: 4px; text-transform: uppercase;">EDUCATION QUALIFICATION</div>
                
                <div style="background-color: #f1f5f9; border-left: 3.5px solid #0284c7; padding: 6px 9px; margin-bottom: 5px; border-radius: 3px;">
                    <div style="font-size: 11px; font-weight: 700; color: #0f172a;">Post Graduation (M.Sc)</div>
                    <div style="font-size: 10px; color: #475569;">{edu_pg}</div>
                </div>
                <div style="background-color: #f1f5f9; border-left: 3.5px solid #0284c7; padding: 6px 9px; margin-bottom: 5px; border-radius: 3px;">
                    <div style="font-size: 11px; font-weight: 700; color: #0f172a;">Graduation (B.Sc)</div>
                    <div style="font-size: 10px; color: #475569;">{edu_grad}</div>
                </div>
                <div style="background-color: #f1f5f9; border-left: 3.5px solid #0284c7; padding: 6px 9px; margin-bottom: 5px; border-radius: 3px;">
                    <div style="font-size: 11px; font-weight: 700; color: #0f172a;">Higher Secondary (12th - I.Sc)</div>
                    <div style="font-size: 10px; color: #475569;">{edu_12th}</div>
                </div>
                <div style="background-color: #f1f5f9; border-left: 3.5px solid #0284c7; padding: 6px 9px; margin-bottom: 5px; border-radius: 3px;">
                    <div style="font-size: 11px; font-weight: 700; color: #0f172a;">Secondary (10th)</div>
                    <div style="font-size: 10px; color: #475569;">{edu_10th}</div>
                </div>
            </td>

            <!-- RIGHT COLUMN -->
            <td style="width: 50%; vertical-align: top; padding-left: 8px; border: none;">
                
                <div style="font-size: 11px; font-weight: 700; color: #0f172a; border-bottom: 2px solid #0284c7; padding-bottom: 2px; margin-bottom: 6px; text-transform: uppercase;">TECHNICAL QUALIFICATION</div>
                
                <div style="background-color: #f1f5f9; border-left: 3.5px solid #0284c7; padding: 7px 9px; margin-bottom: 10px; border-radius: 3px;">
                    <div style="font-size: 11px; font-weight: 700; color: #0f172a;">{tech_qual}</div>
                    <div style="font-size: 10px; color: #334155; margin-top: 2px;">{tech_qual_desc}</div>
                </div>

                <div style="font-size: 11px; font-weight: 700; color: #0f172a; border-bottom: 2px solid #0284c7; padding-bottom: 2px; margin-bottom: 6px; text-transform: uppercase;">KEY COMPETENCIES</div>
                
                <div style="background-color: #f1f5f9; border-left: 3.5px solid #0284c7; padding: 7px 9px 7px 22px; margin-bottom: 10px; border-radius: 3px;">
                    <ul style="margin: 0; padding: 0; font-size: 10px; color: #1e293b;">
                        {skills_html}
                    </ul>
                </div>

                <div style="font-size: 11px; font-weight: 700; color: #0f172a; border-bottom: 2px solid #0284c7; padding-bottom: 2px; margin-bottom: 6px; text-transform: uppercase;">PERSONAL DETAILS</div>
                
                <div style="background-color: #f1f5f9; border-left: 3.5px solid #0284c7; padding: 7px 9px; margin-bottom: 10px; border-radius: 3px;">
                    <table style="width: 100%; font-size: 10px; color: #1e293b; border-collapse: collapse;">
                        <tr><td style="width: 42%; padding: 2px 0; font-weight: bold; border: none;">D.O.B:</td><td style="padding: 2px 0; border: none;">{dob}</td></tr>
                        <tr><td style="font-weight: bold; padding: 2px 0; border: none;">Gender:</td><td style="padding: 2px 0; border: none;">{gender}</td></tr>
                        <tr><td style="font-weight: bold; padding: 2px 0; border: none;">Father's Name:</td><td style="padding: 2px 0; border: none;">{father_name}</td></tr>
                        <tr><td style="font-weight: bold; padding: 2px 0; border: none;">Languages:</td><td style="padding: 2px 0; border: none;">{languages}</td></tr>
                        <tr><td style="font-weight: bold; padding: 2px 0; border: none;">Marital Status:</td><td style="padding: 2px 0; border: none;">{marital_status}</td></tr>
                        <tr><td style="font-weight: bold; padding: 2px 0; border: none;">Nationality:</td><td style="padding: 2px 0; border: none;">Indian</td></tr>
                    </table>
                </div>

                <div style="font-size: 11px; font-weight: 700; color: #0f172a; border-bottom: 2px solid #0284c7; padding-bottom: 2px; margin-bottom: 6px; text-transform: uppercase;">HOBBIES & INTERESTS</div>
                
                <div style="background-color: #f1f5f9; border-left: 3.5px solid #0284c7; padding: 7px 9px; margin-bottom: 5px; border-radius: 3px;">
                    <div style="font-size: 10px; color: #1e293b;">{hobbies}</div>
                </div>

            </td>
        </tr>
    </table>

    <!-- DECLARATION BOX -->
    <div style="background-color: #f8fafc; border: 1px solid #cbd5e1; border-radius: 4px; padding: 8px 10px; margin-top: 8px;">
        <div style="font-size: 10.5px; font-weight: 700; color: #0f172a; margin-bottom: 2px;">Declaration</div>
        <div style="font-size: 9.5px; color: #475569; font-style: italic;">I hereby declare that all the information provided above is true and correct to the best of my knowledge and belief.</div>
        <table style="width: 100%; margin-top: 14px; font-size: 10px; color: #0f172a; border-collapse: collapse;">
            <tr>
                <td style="border: none; padding: 0;"><b>Place:</b> Saharsa<br><b>Date:</b> ___________</td>
                <td style="border: none; padding: 0; text-align: right; vertical-align: bottom;"><b>({full_name})</b></td>
            </tr>
        </table>
    </div>

</div>
"""

st.markdown(html_content, unsafe_allow_html=True)
