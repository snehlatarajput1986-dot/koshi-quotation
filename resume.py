import streamlit as st

st.set_page_config(page_title="Resume Builder - Koshi Enterprises", page_icon="📄", layout="centered")

# Custom CSS for preview and print styling
st.markdown("""
    <style>
    @media print {
        .no-print { display: none !important; }
        .main { background-color: white !important; }
        body { background-color: white !important; }
    }
    .resume-container {
        background-color: #ffffff;
        padding: 30px;
        border: 1px solid #ddd;
        border-radius: 8px;
        color: #111;
        font-family: Arial, sans-serif;
    }
    .section-head {
        font-weight: bold;
        font-size: 15px;
        border-bottom: 2px solid #333;
        margin-top: 15px;
        margin-bottom: 8px;
        text-transform: uppercase;
        color: #222;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📄 Professional Resume Builder")
st.write("Apni details bharein aur neeche 'Print Resume' par click karein.")

# --- FORM SECTION ---
with st.expander("📝 Enter Your Details Here", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        full_name = st.text_input("Full Name", "PRASHANT KUMAR")
        designation = st.text_input("Designation / Title", "Medical Representative & Sales Professional")
        phone = st.text_input("Phone Number", "+91 8864097233")
        email = st.text_input("Email ID", "Prashantkumar886409@gmail.com")
        address = st.text_input("Address", "At - Batraha, Ward No. 36, PO+PS+Dist: Saharsa, Bihar (852201)")
    
    with col2:
        dob = st.text_input("Date of Birth", "07-04-1999")
        father_name = st.text_input("Father's Name", "Sanjeev Kumar")
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        marital_status = st.selectbox("Marital Status", ["Single", "Married"])
        languages = st.text_input("Languages Known", "Hindi, English, Maithili")

    st.subheader("Work Experience")
    exp1_company = st.text_input("Company 1 Name", "Pharmanova Specialties Pvt. Ltd.")
    exp1_duration = st.text_input("Company 1 Duration", "12-02-2025 - Present")
    exp1_desc = st.text_area("Company 1 Responsibilities", "Responsible for pharmaceutical sales, technical marketing, and client relationship management.")

    exp2_company = st.text_input("Company 2 Name", "Hi-tech Laboratories Pharma")
    exp2_duration = st.text_input("Company 2 Duration", "10-06-2024 - 31-01-2025")
    exp2_desc = st.text_area("Company 2 Responsibilities", "Handled product promotion, doctor visits, and territory sales development.")

    st.subheader("Education Qualification")
    edu_pg = st.text_input("Post Graduation (M.Sc)", "B.N.M.U Madhepura | Passed 2023")
    edu_grad = st.text_input("Graduation (B.Sc)", "B.N.M.U Madhepura | Passed 2020")
    edu_12th = st.text_input("Higher Secondary (12th)", "B.S.E.B Patna | Passed 2016")
    edu_10th = st.text_input("Secondary (10th)", "B.S.E.B Patna | Passed 2014")

    st.subheader("Key Competencies & Technical Qualification")
    tech_qual = st.text_input("Technical Qualification", "ADCA (1 Year Computer Degree)")
    skills = st.text_area("Key Competencies (Comma separated)", "Medicine & Pharma Knowledge, Technical Marketing & Sales, Computer Operations, Client Relationship Management")
    hobbies = st.text_input("Hobbies & Interests", "Watching news & engaged in creative activities.")

# --- PREVIEW & PRINT SECTION ---
st.markdown("---")
st.markdown("<div class='no-print'><h3>👁️ Resume Live Preview</h3></div>", unsafe_allow_html=True)

# Print Button
st.components.v1.html("""
    <button onclick="window.parent.print()" style="background-color: #008CBA; color: white; padding: 10px 20px; border: none; border-radius: 5px; font-size: 15px; cursor: pointer; font-weight: bold;">
        🖨️ Print / Download PDF
    </button>
""", height=50)

# Render formatted Resume preview using st.html
skills_list = [s.strip() for s in skills.split(",") if s.strip()]
skills_html = "".join([f"<li>{s}</li>" for s in skills_list])

resume_code = f"""
<div class="resume-container">
    <div style="border-bottom: 2px solid #222; padding-bottom: 10px; margin-bottom: 15px;">
        <h2 style="margin: 0; font-size: 24px; color: #111;">{full_name}</h2>
        <h4 style="margin: 4px 0; color: #444; font-size: 16px;">{designation}</h4>
        <p style="margin: 2px 0; font-size: 13px;"><b>Address:</b> {address}</p>
        <p style="margin: 2px 0; font-size: 13px;"><b>Phone:</b> {phone} | <b>Email:</b> {email}</p>
    </div>

    <div class="section-head">Work Experience</div>
    <p style="margin: 3px 0 0 0; font-size: 14px;"><b>{exp1_company}</b> ({exp1_duration})</p>
    <p style="margin: 2px 0 8px 0; font-size: 13px; color: #333;">{exp1_desc}</p>
    <p style="margin: 3px 0 0 0; font-size: 14px;"><b>{exp2_company}</b> ({exp2_duration})</p>
    <p style="margin: 2px 0 8px 0; font-size: 13px; color: #333;">{exp2_desc}</p>

    <div class="section-head">Education Qualification</div>
    <ul style="margin: 0; padding-left: 20px; font-size: 13px;">
        <li><b>Post Graduation (M.Sc):</b> {edu_pg}</li>
        <li><b>Graduation (B.Sc):</b> {edu_grad}</li>
        <li><b>Higher Secondary (12th):</b> {edu_12th}</li>
        <li><b>Secondary (10th):</b> {edu_10th}</li>
    </ul>

    <div class="section-head">Technical Qualification</div>
    <p style="margin: 2px 0; font-size: 13px;">{tech_qual}</p>

    <div class="section-head">Key Competencies</div>
    <ul style="margin: 0; padding-left: 20px; font-size: 13px;">
        {skills_html}
    </ul>

    <div class="section-head">Personal Details</div>
    <p style="margin: 2px 0; font-size: 13px;"><b>D.O.B:</b> {dob} | <b>Gender:</b> {gender} | <b>Father's Name:</b> {father_name}</p>
    <p style="margin: 2px 0; font-size: 13px;"><b>Languages:</b> {languages} | <b>Marital Status:</b> {marital_status} | <b>Nationality:</b> Indian</p>

    <div class="section-head">Hobbies & Interests</div>
    <p style="margin: 2px 0; font-size: 13px;">{hobbies}</p>

    <div class="section-head">Declaration</div>
    <p style="margin: 2px 0; font-size: 12px; color: #444;">I hereby declare that all the information provided above is true and correct to the best of my knowledge and belief.</p>
    
    <br><br>
    <table width="100%" style="font-size:13px; border:none;">
        <tr>
            <td style="border:none;"><b>Place:</b> Saharsa<br><b>Date:</b> ___________</td>
            <td align="right" style="border:none;"><b>({full_name})</b></td>
        </tr>
    </table>
</div>
"""

st.html(resume_code)
