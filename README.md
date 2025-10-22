# AI-Powered Resume Optimizer

## 🚀 Universal Resume Generator with Dynamic Field Detection

This advanced resume optimization system can automatically detect and generate professional resumes for **ANY career field** including specialized positions like brain surgeon, marine biologist, astrophysicist, and more.

## ✨ Key Features

### 🎯 **Dynamic Field Detection**
- **Automatic Career Detection**: Enter any job title like "brain surgeon", "marine biologist", or "video game designer"
- **Smart Content Generation**: Automatically creates appropriate skills, experience, and education for any field
- **Professional Formatting**: Generates properly formatted .docx resumes matching professional standards

### 🏥 **Medical Fields Supported**
- Brain Surgeon / Neurosurgeon
- Cardiologist / Heart Surgeon  
- General Surgeon
- Doctor / Physician
- Nurse (RN, BSN)

### 🔧 **Engineering Fields**
- Software Engineer
- Mechanical Engineer
- Civil Engineer
- Electrical Engineer

### 💼 **Professional Services**
- Lawyer / Attorney
- Accountant / Financial Analyst
- Teacher / Educator

### 🍽️ **Food Service**
- Executive Chef
- Cook
- Dishwasher / Kitchen Staff

### 🔄 **And ANY Other Field**
The system intelligently generates appropriate content for fields not explicitly programmed, including:
- Marine Biologist
- Astrophysicist
- Video Game Designer
- Environmental Scientist
- Archaeologist
- And literally ANY profession!

## 📋 Requirements

```bash
pip install python-docx
```

Optional for GUI file selection:
- tkinter (usually included with Python)

## 🚀 Quick Start

### Method 1: Browse Mode (Recommended)
```bash
python browse_mode_fixed.py
```

1. **Select Job Description**: Choose your .txt or .docx job posting file
2. **Select Current Resume**: Choose your existing resume file  
3. **Enter Target Role**: Type ANY job title (e.g., "brain surgeon", "marine biologist")
4. **Get Results**: Receive a professionally formatted resume in seconds!

### Method 2: Direct Command Line
```bash
python resume_windows.py "job description text" --resume "current resume text" --role "brain surgeon"
```

## 📁 Output Files

Each optimization creates a timestamped folder with:

- `optimized_resume.docx` - **Main resume file** (perfect formatting)
- `tailored_resume_final.txt` - Text version of optimized resume
- `job_analysis_report.txt` - Analysis of job requirements
- `resume_impact_version.txt` - High-impact version
- `ats_optimized.txt` - ATS-friendly version
- `enhanced_skills_section.txt` - Improved skills section
- `optimization_executive_summary.txt` - Summary of changes

## 🎨 Professional Formatting

The generated .docx resumes feature:
- **26pt Name** (Title style)
- **14pt Section Headers** (Heading 1 style)  
- **12pt Body Text** (Normal style)
- Perfect margins and spacing
- Professional contact information layout
- Consistent formatting throughout

## 💡 Examples

### Brain Surgeon Resume
```
Target Role: brain surgeon
Generated Title: Neurosurgeon / Brain Surgeon
Skills: Brain Surgery, Neurosurgical Procedures, Microsurgery, Tumor Removal
Education: Harvard Medical School — Doctor of Medicine (M.D.)
Experience: Complex neurosurgical procedures with 95% success rate
```

### Marine Biologist Resume  
```
Target Role: marine biologist
Generated Title: Marine Biologist & Research Scientist
Skills: Marine Research, Oceanography, Species Analysis, Field Studies
Education: Marine Science Institute — Ph.D. Marine Biology
Experience: Conducted marine ecosystem research and species conservation
```

### Astrophysicist Resume
```
Target Role: astrophysicist
Generated Title: Astrophysicist & Space Research Specialist  
Skills: Astronomical Research, Data Analysis, Space Physics, Theoretical Models
Education: NASA Research Institute — Ph.D. Astrophysics
Experience: Advanced space research and astronomical data analysis
```

## 🔧 Technical Details

### Dynamic Content Generation
The system uses intelligent pattern matching to:
1. **Detect field category** (medical, engineering, legal, etc.)
2. **Generate appropriate skills** based on field requirements
3. **Create relevant experience** with industry-specific achievements  
4. **Suggest proper education** for the career path
5. **Include certifications** and professional development

### Supported File Formats
- **Input**: .txt, .docx files
- **Output**: .docx (professional format), .txt (plain text)

## 🛠️ Troubleshooting

### File Dialog Issues
If file dialogs don't open:
1. Try running as administrator
2. Use direct file paths instead of browse mode
3. Check tkinter installation

### Missing Dependencies
```bash
# Install required packages
pip install python-docx

# For Windows users
pip install pywin32
```

## 📧 Support

For issues or feature requests, ensure you have:
- Python 3.6+
- python-docx installed
- Valid .txt or .docx input files

## 🌟 Why This Tool?

- ✅ **Universal**: Works for ANY career field
- ✅ **Professional**: Perfect .docx formatting  
- ✅ **Fast**: Generate resumes in seconds
- ✅ **Smart**: Automatic field detection and content generation
- ✅ **ATS-Friendly**: Optimized for applicant tracking systems
- ✅ **Complete**: Multiple output formats and detailed analysis

Transform any resume into a professional, field-specific document that stands out to recruiters and passes ATS systems!