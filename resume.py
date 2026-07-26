import streamlit as st
import base64

st.set_page_config(
    page_title="Resume Builder - Prashant Kumar",
    page_icon="📄",
    layout="wide"
)

# Global Styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

.stApp { background-color: #f1f5f9; }
.main-title { color: #0f172a; font-weight: 700; margin-bottom: 15px; }

#printableArea {
    background-color: #ffffff !important;
    width: 790px;
    padding: 22px;
    margin: auto;
    box-sizing: border-box;
    font-family: 'Inter', sans-serif;
    color: #1e293b;
    border-radius: 4px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}

.resume-header {
    background-color: #1e293b !important;
    color: #ffffff !important;
    border-radius: 6px;
    padding: 14px 18px;
    margin-bottom: 12px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.header-info h1 {
    margin: 0;
    font-size: 20px;
    font-weight: 700;
    color: #ffffff !important;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}
.header-info .sub-title {
    color: #38bdf8 !important;
    font-size: 12px;
    font-weight: 600;
    margin-top: 2px;
    margin-bottom: 6px;
}
.header-contact {
    font-size: 10.5px;
    color: #e2e8f0 !important;
    line-height: 1.4;
}

.photo-box {
    width: 80px;
    height: 95px;
    border-radius: 4px;
    border: 2px solid #38bdf8;
    overflow: hidden;
    background-color: #0f172a;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}
.photo-box img { width: 100%; height: 100%; object-fit: cover; }

.section-title {
    font-size: 11px;
    font-weight: 700;
    color: #0f172a;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    border-bottom: 2px solid #0284c7;
    padding-bottom: 2px;
    margin-bottom: 6px;
    margin-top: 8px;
}

.info-card {
    background-color: #f8fafc !important;
    border-radius: 4px;
    padding: 6px 8px;
    margin-bottom: 5px;
    border-left: 3px solid #0284c7 !important;
}
.info-card-title { font-size: 11px; font-weight: 700; color: #0f172a; }
.info-card-sub { font-size: 10px; color: #0284c7; font-weight: 600; margin-top: 1px; margin-bottom: 2px; }
.info-card-desc { font-size: 10px; color: #475569; line-height: 1.3; }

.competencies-list {
    background-color: #f8fafc !important;
    border-radius: 4px;
    padding: 5px 8px 5px 20px;
    margin: 0 0 5px 0;
    border-left: 3px solid #0284c7 !important;
    font-size: 10px;
    color: #334155;
}
.competencies-list li { margin-bottom: 2px; }

.personal-table {
    width: 100%;
    font-size: 10px;
    color: #334155;
    border-collapse: collapse;
    background-color: #f8fafc !important;
    border-radius: 4px;
    padding: 5px 6px;
    border-left: 3px solid #0284c7 !important;
}
.personal-table td { padding: 2px 3px; }

.declaration-box {
    background-color: #f8fafc !important;
    border-radius: 4px;
    padding: 6px 8px;
    margin-top: 8px;
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
    photo_html = f'<img src="data:image/png;base64,{base64_image}">'
else:
    photo_html = '<div style="font-size:10px; color:#cbd5e1; text-align:center;">Passport<br>Photo</div>'

skills_list = [s.strip() for s in skills.split(",") if s.strip()]
skills_html = "".join([f"<li>{s}</li>" for s in skills_list])

# Enhanced Canvas HTML-to-PDF Downloader with Background Retention
st.components.v1.html("""
<script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>
<button onclick="downloadPDF()" style="background-color: #0284c7; color: white; border: none; padding: 12px 28px; border-radius: 6px; font-weight: bold; cursor: pointer; font-size: 16px; box-shadow: 0 4px 10px rgba(0,0,0,0.15);">
    📥 Download 1-Page Perfect PDF
</button>

<script>
function downloadPDF() {
    const element = window.parent.document.getElementById('printableArea');
    const opt = {
        margin:       [4, 4, 4, 4],
        filename:     'Resume_Prashant_Kumar.pdf',
        image:        { type: 'jpeg', quality: 1.0 },
        html2canvas:  { scale: 3, useCORS: true, letterRendering: true, backgroundColor: '#ffffff' },
        jsPDF:        { unit: 'mm', format: 'a4', orientation: 'portrait' }
    };
    html2pdf().set(opt).from(element).save();
}
</script>
""", height=60)

# Clean HTML with inline styles for color preservation
html_content = f"""<div id="printableArea" style="background-color: #ffffff;">
<div class="resume-header" style="background-color: #1e293b; color: #ffffff; border-radius: 6px; padding: 14px 18px; margin-bottom: 12px; display: flex; justify-content: space-between; align-items: center;">
<div class="header-info">
<h1 style="margin: 0; font-size: 20px; font-weight: 700; color: #ffffff; text-transform: uppercase; letter-spacing: 0.5px;">{full_name}</h1>
<div class="sub-title" style="color: #38bdf8; font-size: 12px; font-weight: 600; margin-top: 2px; margin-bottom: 6px;">{designation}</div>
<div class="header-contact" style="font-size: 10.5px; color: #e2e8f0; line-height: 1.4;">📍 <b>Address:</b> {address}<br>📞 <b>Phone:</b> {phone} &nbsp;|&nbsp; ✉️ <b>Email:</b> {email}</div>
</div>
<div class="photo-box" style="width: 80px; height: 95px; border-radius: 4px; border: 2px solid #38bdf8; overflow: hidden; background-color: #0f172a; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">{photo_html}</div>
</div>

<table style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tr>
<td style="width: 50%; vertical-align: top; padding-right: 8px; border: none;">
<div class="section-title">WORK EXPERIENCE</div>
<div class="info-card" style="background-color: #f8fafc; border-radius: 4px; padding: 6px 8px; margin-bottom: 5px; border-left: 3px solid #0284c7;">
<div class="info-card-title">{exp1_company}</div>
<div class="info-card-sub">{exp1_duration}</div>
<div class="info-card-desc">{exp1_desc}</div>
</div>
<div class="info-card" style="background-color: #f8fafc; border-radius: 4px; padding: 6px 8px; margin-bottom: 5px; border-left: 3px solid #0284c7;">
<div class="info-card-title">{exp2_company}</div>
<div class="info-card-sub">{exp2_duration}</div>
<div class="info-card-desc">{exp2_desc}</div>
</div>

<div class="section-title">EDUCATION QUALIFICATION</div>
<div class="info-card" style="background-color: #f8fafc; border-radius: 4px; padding: 6px 8px; margin-bottom: 5px; border-left: 3px solid #0284c7;">
<div class="info-card-title">Post Graduation (M.Sc)</div>
<div class="info-card-sub" style="color: #475569; font-weight: normal;">{edu_pg}</div>
</div>
<div class="info-card" style="background-color: #f8fafc; border-radius: 4px; padding: 6px 8px; margin-bottom: 5px; border-left: 3px solid #0284c7;">
<div class="info-card-title">Graduation (B.Sc)</div>
<div class="info-card-sub" style="color: #475569; font-weight: normal;">{edu_grad}</div>
</div>
<div class="info-card" style="background-color: #f8fafc; border-radius: 4px; padding: 6px 8px; margin-bottom: 5px; border-left: 3px solid #0284c7;">
<div class="info-card-title">Higher Secondary (12th - I.Sc)</div>
<div class="info-card-sub" style="color: #475569; font-weight: normal;">{edu_12th}</div>
</div>
<div class="info-card" style="background-color: #f8fafc; border-radius: 4px; padding: 6px 8px; margin-bottom: 5px; border-left: 3px solid #0284c7;">
<div class="info-card-title">Secondary (10th)</div>
<div class="info-card-sub" style="color: #475569; font-weight: normal;">{edu_10th}</div>
</div>
</td>

<td style="width: 50%; vertical-align: top; padding-left: 8px; border: none;">
<div class="section-title">TECHNICAL QUALIFICATION</div>
<div class="info-card" style="background-color: #f8fafc; border-radius: 4px; padding: 6px 8px; margin-bottom: 5px; border-left: 3px solid #0284c7;">
<div class="info-card-title">{tech_qual}</div>
<div class="info-card-desc" style="margin-top: 1px;">{tech_qual_desc}</div>
</div>

<div class="section-title">KEY COMPETENCIES</div>
<ul class="competencies-list" style="background-color: #f8fafc; border-radius: 4px; padding: 5px 8px 5px 20px; margin: 0 0 5px 0; border-left: 3px solid #0284c7; font-size: 10px; color: #334155;">{skills_html}</ul>

<div class="section-title">PERSONAL DETAILS</div>
<table class="personal-table" style="background-color: #f8fafc; border-left: 3px solid #0284c7; border-radius: 4px; padding: 5px 6px;">
<tr><td style="width: 40%;"><b>D.O.B:</b></td><td>{dob}</td></tr>
<tr><td><b>Gender:</b></td><td>{gender}</td></tr>
<tr><td><b>Father's Name:</b></td><td>{father_name}</td></tr>
<tr><td><b>Languages:</b></td><td>{languages}</td></tr>
<tr><td><b>Marital Status:</b></td><td>{marital_status}</td></tr>
<tr><td><b>Nationality:</b></td><td>Indian</td></tr>
</table>

<div class="section-title">HOBBIES & INTERESTS</div>
<div class="info-card" style="background-color: #f8fafc; border-radius: 4px; padding: 6px 8px; margin-bottom: 5px; border-left: 3px solid #0284c7;">
<div class="info-card-desc" style="color: #1e293b;">{hobbies}</div>
</div>
</td>
</tr>
</table>

<div class="declaration-box" style="background-color: #f8fafc; border-radius: 4px; padding: 6px 8px; margin-top: 8px; border: 1px solid #e2e8f0;">
<div style="font-size: 10px; font-weight: 700; color: #1e293b; margin-bottom: 2px;">Declaration</div>
<div style="font-size: 9.5px; color: #475569; font-style: italic;">I hereby declare that all the information provided above is true and correct to the best of my knowledge and belief.</div>
<table style="width: 100%; margin-top: 12px; font-size: 10px; color: #1e293b; border: none;">
<tr>
<td style="border: none; padding: 0;"><b>Place:</b> Saharsa<br><b>Date:</b> ___________</td>
<td style="border: none; padding: 0; text-align: right; vertical-align: bottom;"><b>({full_name})</b></td>
</tr>
</table>
</div>
</div>"""

st.markdown(html_content, unsafe_allow_html=True)
