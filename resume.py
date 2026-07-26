import streamlit as st

st.set_page_config(page_title="Resume Builder - Koshi Enterprises", page_icon="📄", layout="centered")

# CSS for Print/Layout
st.markdown("""
    <style>
    @media print {
        .no-print { display: none !important; }
        .resume-page { border: none !important; box-shadow: none !important; }
    }
    .resume-page {
        border: 1px solid #ccc;
        padding: 30px;
        background-color: white;
        color: black;
        font-family: Arial, sans-serif;
        border-radius: 5px;
    }
    .resume-header {
        border-bottom: 2px solid #333;
        padding-bottom: 10px;
        margin-bottom: 20px;
    }
    .section-title {
        font-weight: bold;
        font-size: 16px;
        border-bottom: 1px solid #666;
        margin-top: 15px;
        margin-bottom: 10px;
        text-transform: uppercase;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📄 Professional Resume Builder")
st.write("Apni details bharein aur neeche 'Print Resume' par click karein.")

# --- FORM SECTION ---
with st.expander("📝 Enter Your Details Here", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        full_name = st.text_input("Full Name", "PRASHANT KUMAR")[span_1](start_span)[span_1](end_span)
        designation = st.text_input("Designation / Title", "Medical Representative & Sales Professional")[span_2](start_span)[span_2](end_span)
        phone = st.text_input("Phone Number", "+91 8864097233")[span_3](start_span)[span_3](end_span)
        email = st.text_input("Email ID", "Prashantkumar886409@gmail.com")[span_4](start_span)[span_4](end_span)
        address = st.text_input("Address", "At - Batraha, Ward No. 36, PO+PS+Dist: Saharsa, Bihar (852201)")[span_5](start_span)[span_5](end_span)
    
    with col2:
        dob = st.text_input("Date of Birth", "07-04-1999")[span_6](start_span)[span_6](end_span)
        father_name = st.text_input("Father's Name", "Sanjeev Kumar")[span_7](start_span)[span_7](end_span)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])[span_8](start_span)[span_8](end_span)
        marital_status = st.selectbox("Marital Status", ["Single", "Married"])[span_9](start_span)[span_9](end_span)
        languages = st.text_input("Languages Known", "Hindi, English, Maithili")[span_10](start_span)[span_10](end_span)

    st.subheader("Work Experience")[span_11](start_span)[span_11](end_span)
    exp1_company = st.text_input("Company 1 Name", "Pharmanova Specialties Pvt. Ltd.")[span_12](start_span)[span_12](end_span)
    exp1_duration = st.text_input("Company 1 Duration", "12-02-2025 - Present")[span_13](start_span)[span_13](end_span)
    exp1_desc = st.text_area("Company 1 Responsibilities", "Responsible for pharmaceutical sales, technical marketing, and client relationship management.")[span_14](start_span)[span_14](end_span)

    exp2_company = st.text_input("Company 2 Name", "Hi-tech Laboratories Pharma")[span_15](start_span)[span_15](end_span)
    exp2_duration = st.text_input("Company 2 Duration", "10-06-2024 - 31-01-2025")[span_16](start_span)[span_16](end_span)
    exp2_desc = st.text_area("Company 2 Responsibilities", "Handled product promotion, doctor visits, and territory sales development.")[span_17](start_span)[span_17](end_span)

    st.subheader("Education Qualification")[span_18](start_span)[span_18](end_span)
    edu_pg = st.text_input("Post Graduation (M.Sc)", "B.N.M.U Madhepura | Passed 2023")[span_19](start_span)[span_19](end_span)
    edu_grad = st.text_input("Graduation (B.Sc)", "B.N.M.U Madhepura | Passed 2020")[span_20](start_span)[span_20](end_span)
    edu_12th = st.text_input("Higher Secondary (12th)", "B.S.E.B Patna | Passed 2016")[span_21](start_span)[span_21](end_span)
    edu_10th = st.text_input("Secondary (10th)", "B.S.E.B Patna | Passed 2014")[span_22](start_span)[span_22](end_span)

    st.subheader("Key Competencies & Technical Qualification")[span_23](start_span)[span_23](end_span)
    tech_qual = st.text_input("Technical Qualification", "ADCA (1 Year Computer Degree)")[span_24](start_span)[span_24](end_span)
    skills = st.text_area("Key Competencies (Comma separated)", "Medicine & Pharma Knowledge, Technical Marketing & Sales, Computer Operations, Client Relationship Management")[span_25](start_span)[span_25](end_span)
    hobbies = st.text_input("Hobbies & Interests", "Watching news & engaged in creative activities.")[span_26](start_span)[span_26](end_span)

# --- PREVIEW & PRINT SECTION ---
st.markdown("---")
st.markdown("<div class='no-print'><h3>👁️ Resume Live Preview</h3></div>", unsafe_allow_html=True)

# Print Button
st.markdown("""
    <div class="no-print" style="margin-bottom: 20px;">
        <button onclick="window.print()" style="background-color: #008CBA; color: white; padding: 12px 24px; border: none; border-radius: 5px; font-size: 16px; cursor: pointer; font-weight: bold;">
            🖨️ Print / Download PDF
        </button>
    </div>
""", unsafe_allow_html=True)

# Resume Layout
skills_list = [s.strip() for s in skills.split(",") if s.strip()]
skills_html = "".join([f"<li>{s}</li>" for s in skills_list])

resume_html = f"""
<div class="resume-page">
    <div class="resume-header">
        <h2 style="margin:0; text-transform:uppercase;">{full_name}</h2>
        <h4 style="margin:5px 0; color:#555;">{designation}</h4>
        <p style="margin:2px 0; font-size:13px;">Address: {address}</p>
        <p style="margin:2px 0; font-size:13px;">Phone: {phone} | Email: {email}</p>
    </div>

    <div class="section-title">Work Experience</div>
    <p style="margin:2px 0;"><b>{exp1_company}</b> ({exp1_duration})</p>
    <p style="margin:2px 0 10px 0; font-size:13px;">{exp1_desc}</p>
    
    <p style="margin:2px 0;"><b>{exp2_company}</b> ({exp2_duration})</p>
    <p style="margin:2px 0 10px 0; font-size:13px;">{exp2_desc}</p>

    <div class="section-title">Education Qualification</div>
    <ul style="margin:0; padding-left:20px; font-size:13px;">
        <li><b>Post Graduation (M.Sc):</b> {edu_pg}</li>
        <li><b>Graduation (B.Sc):</b> {edu_grad}</li>
        <li><b>Higher Secondary (12th):</b> {edu_12th}</li>
        <li><b>Secondary (10th):</b> {edu_10th}</li>
    </ul>

    <div class="section-title">Technical Qualification</div>
    <p style="margin:2px 0; font-size:13px;">{tech_qual}</p>

    <div class="section-title">Key Competencies</div>
    <ul style="margin:0; padding-left:20px; font-size:13px;">
        {skills_html}
    </ul>

    <div class="section-title">Personal Details</div>
    <p style="margin:2px 0; font-size:13px;"><b>D.O.B:</b> {dob} | <b>Gender:</b> {gender} | <b>Father's Name:</b> {father_name}</p>
    <p style="margin:2px 0; font-size:13px;"><b>Languages:</b> {languages} | <b>Marital Status:</b> {marital_status} | <b>Nationality:</b> Indian</p>

    <div class="section-title">Hobbies & Interests</div>
    <p style="margin:2px 0; font-size:13px;">{hobbies}</p>

    <div class="section-title">Declaration</div>
    <p style="margin:2px 0; font-size:12px;">I hereby declare that all the information provided above is true and correct to the best of my knowledge and belief.</p>
    
    <br>
    <table width="100%" style="font-size:13px;">
        <tr>
            <td><b>Place:</b> ___________<br><b>Date:</b> ___________</td>
            <td align="right"><b>({full_name})</b></td>
        </tr>
    </table>
</div>
"""

st.markdown(resume_html, unsafe_allow_html=True)
