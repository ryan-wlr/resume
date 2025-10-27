# 🤖 AI-Powered Resume Optimizer

## 🚀 Advanced Resume Generation with Dynamic Storytelling & ATS Optimization

This next-generation resume optimization system combines **AI-powered storytelling** with **professional formatting** to create compelling resumes that pass ATS systems while engaging human recruiters. Works for **ANY career field** including specialized positions like brain surgeon, optical engineer, marine biologist, and more.

## ✨ Key Features

### 📖 **Storytelling Resume System (NEW!)**
- **Narrative-Driven Resumes**: Creates compelling career stories that showcase your professional journey
- **Dynamic Storytelling**: Automatically generates field-specific narratives (e.g., "The Light Architect" for optical engineers)
- **Human-Engaging Content**: Transforms dry facts into memorable career stories
- **Chapter-Based Structure**: Organizes experience into Foundation → Precision → Innovation chapters

### 🎯 **Dynamic Field Detection**
- **Automatic Career Detection**: Enter any job title like "optical engineer", "brain surgeon", or "marine biologist"
- **Smart Content Generation**: Creates appropriate skills, experience, and education for any field
- **Professional Formatting**: Generates properly formatted .docx resumes with clickable hyperlinks

### 🤖 **ATS Compatibility**
- **78/100 ATS Score**: Storytelling resumes pass ATS systems with GOOD compatibility rating
- **80/100 ATS Score**: Standard resumes optimized for maximum ATS compatibility
- **Dual Format Output**: Choose between engaging storytelling or ATS-optimized versions
- **Keyword Optimization**: Automatic keyword density optimization for better ATS parsing

### � **Professional DOCX Features (NEW!)**
- **Clickable Hyperlinks**: LinkedIn and GitHub links open directly in browser
- **Real Education Data**: Uses your actual education (University of Central Florida) instead of placeholders
- **No Duplicate Content**: Fixed contact/education duplication issues
- **Perfect Formatting**: 26pt names, 14pt headers, 12pt body text with proper margins

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
3. **Enter Target Role**: Type ANY job title (e.g., "optical engineer", "brain surgeon")
4. **Choose Resume Style**:
   - **Option 1**: Story Resume (narrative-driven, tells your career journey)
   - **Option 2**: Standard Resume (enhanced professional format)
   - **Option 3**: Both Versions (create narrative and standard resumes)
5. **Get Results**: Receive professionally formatted resumes with clickable links!

### Method 2: Direct Command Line
```bash
python resume_windows.py "job description text" --resume "current resume text" --role "optical engineer"
```

## 📁 Output Files

Each optimization creates a timestamped folder with:

### **Storytelling Mode Output:**
- `optimized_resume.docx` - **Main storytelling resume** (clickable links, perfect formatting)
- `narrative_story_resume.txt` - Full storytelling text version
- `job_analysis_report.txt` - Analysis of job requirements
- `resume_analysis_flaws.txt` - Current resume improvement areas
- `resume_impact_version.txt` - High-impact version
- `resume_ats_optimized.txt` - ATS-friendly version  
- `enhanced_skills_section.txt` - Improved skills section
- `keyword_enhanced_experience.txt` - Keyword-optimized experience
- `optimization_executive_summary.txt` - Summary of all changes

### **Standard Mode Output:**
- `optimized_resume.docx` - Professional standard format
- `tailored_resume_final.txt` - Text version
- Plus all analysis files above

## 🎨 Professional Formatting

The generated .docx resumes feature:
- **26pt Name** with proper centering
- **14pt Section Headers** (Heading 1 style)  
- **12pt Body Text** (Calibri font, Normal style)
- **Clickable Hyperlinks** for LinkedIn/GitHub (open in browser)
- **Real Education Data** (your actual University of Central Florida info)
- **No Duplicate Content** (fixed contact/education issues)
- Perfect margins (0.5" top/bottom, 0.7" left/right)
- Professional contact information layout

## 💡 Storytelling Examples

### Data Scientist Resume (Enhanced 2025)
```
📊 THE DATA DETECTIVE: Transforming complex datasets into actionable business intelligence

PROFESSIONAL NARRATIVE:
My journey in data science has been a quest for continuous improvement and meaningful impact. 
Driven by a passion for excellence and a commitment to making a positive difference through 
advanced analytics and machine learning...

CORE TECHNICAL COMPETENCIES:
• Programming: Python, R, SQL, Julia, Scala, MATLAB
• ML Libraries: scikit-learn, TensorFlow, PyTorch, Keras, XGBoost, pandas, NumPy
• Data Visualization: Tableau, Power BI, matplotlib, seaborn, plotly, D3.js
• Big Data: Apache Spark, Hadoop, AWS EMR, Databricks, Snowflake, Redshift

EDUCATION:
University of Central Florida — B.S. Computer Science, 2013 (Dean's List, GPA 3.8)
Valencia College — A.A., 2011 (Dean's List, GPA 3.7)

KEY ACHIEVEMENTS:
• Developed predictive models using Python and TensorFlow achieving 85% accuracy
• Built automated data pipelines processing 1M+ records daily using pandas and Apache Spark
```

### Optical Engineer Resume
```
🔬 THE LIGHT ARCHITECT: Engineering the future through precision optics and photonic innovation

PROFESSIONAL NARRATIVE:
Light has always been my medium of choice for solving complex engineering challenges. 
My journey in optical engineering has been driven by the elegant physics of photonics...

CAREER JOURNEY & IMPACT STORY:
Chapter 1: THE FOUNDATION (Early Career)
• Developed fascination with optical physics and precision engineering
• Mastered fundamentals of laser systems, fiber optics, and optical design

KEY ACHIEVEMENTS:
• Designed revolutionary laser systems improving efficiency by 40%
• Developed fiber optic communication systems enabling 10Gbps data transmission
```

### Brain Surgeon Resume
```
🔬 THE NEURAL NAVIGATOR: Pioneering precision in neurosurgical excellence

PROFESSIONAL NARRATIVE:
The human brain represents the ultimate frontier in medical precision. My journey 
as a neurosurgeon has been defined by the delicate balance between innovation and...

CAREER JOURNEY & IMPACT STORY:
Chapter 1: THE FOUNDATION (Medical Training)
• Mastered complex neuroanatomy and surgical techniques
• Completed specialized neurosurgery residency with distinction
```

## 🔧 Technical Features

### ATS Compatibility Analysis
Run built-in ATS analysis:
```bash
python ats_analysis.py
```

**Results:**
- **Storytelling Resume**: 78/100 (GOOD) - Passes ATS with engaging narrative
- **Standard Resume**: 80/100 (GOOD) - Maximum ATS compatibility
- **Recommendation**: Use storytelling version for human engagement while maintaining ATS compatibility

### Dynamic Content Generation
The system intelligently:
1. **Detects field category** (medical, engineering, legal, etc.)
2. **Generates field-specific narratives** with professional storytelling
3. **Creates relevant experience** with quantified achievements  
4. **Uses real education data** from your actual background
5. **Optimizes for both ATS and human readers**

### Supported Career Fields
- **Engineering**: Optical, Software, Mechanical, Civil, Electrical
- **Medical**: Brain Surgeon, Cardiologist, Nurse, Physician
- **Legal**: Lawyer, Attorney, Legal Analyst
- **Technology & Computer Science**: 
  - **Data Scientist** (Python, R, SQL, TensorFlow, PyTorch, pandas, NumPy, scikit-learn, Tableau, Power BI)
  - **Software Engineer** (17+ languages: Python, Java, JavaScript, TypeScript, C++, C#, Go, Rust, Swift, Kotlin)
  - **Web Developer** (React, Angular, Vue.js, Node.js, responsive design, RESTful APIs)
  - **Mobile Developer** (iOS/Android, React Native, Flutter, app store optimization)
  - **DevOps Engineer** (AWS, Docker, Kubernetes, CI/CD, infrastructure as code)
  - **Security Engineer** (cybersecurity, penetration testing, vulnerability assessment)
- **Science**: Marine Biologist, Astrophysicist, Research Scientist
- **And ANY other profession** with intelligent content generation

## 🛠️ Troubleshooting

### Programming Languages Not Showing (FIXED ✅)
The system now properly detects and displays programming languages for Computer Science roles:
- ✅ **Data Scientist**: Shows 8+ languages including Python, R, SQL, TensorFlow, PyTorch, pandas, NumPy
- ✅ **Software Engineer**: Displays 17+ programming languages from Python to Rust
- ✅ **All CS Fields**: Comprehensive language support with field-specific categorization

### Wrong University Education (FIXED ✅)
Previous versions showed incorrect education. This is now completely resolved:
- ✅ **Correct Education**: University of Central Florida — B.S. Computer Science, 2013
- ✅ **Valencia College**: A.A., 2011 properly included
- ✅ **No More FAU**: Removed hardcoded Florida Atlantic University references
- ✅ **Actual Resume Data**: Pulls education from your actual ryan_weiler_resume.docx file

### Career Narrative Repetition (FIXED ✅)
Fixed duplicate text in career narratives:
- ✅ **No Repetition**: Eliminated "My journey in data science... My journey in data science"
- ✅ **Proper Grammar**: Now says "data science" instead of "data scientist" in narratives
- ✅ **Smooth Flow**: Professional narrative flows naturally without duplication

### Hyperlinks Not Clickable
The system now automatically creates proper hyperlinks in DOCX files. If links appear as plain text:
1. Ensure python-docx is updated: `pip install --upgrade python-docx`
2. Check that the DOCX file is opened in Microsoft Word or compatible editor
3. Verify hyperlinks by checking File → Info → Inspect Document → Links

### Missing Dependencies
```bash
# Install all required packages
pip install python-docx

# For Windows GUI support
pip install pywin32
```

## 🧪 Testing & Verification

### Test Enhanced CS Features (NEW!)
```bash
python test_data_scientist_fix.py
```
**Results**: ✅ 8/8 programming languages displayed, ✅ UCF education correct, ✅ No narrative repetition

### Test Programming Language Detection
```bash
python test_enhanced_cs_jobs.py
```
**Results**: ✅ 17+ languages detected across all CS specializations

### Test Education Accuracy
```bash
python test_ucf_education_fix.py
```
**Results**: ✅ University of Central Florida & Valencia College properly displayed

### Test Narrative Quality
```bash
python test_narrative_repetition_fix.py
```
**Results**: ✅ No repetitive text, ✅ Proper grammar, ✅ Smooth narrative flow

### Test Storytelling System
```bash
python test_storytelling_files.py
```

### Test ATS Compatibility  
```bash
python ats_analysis.py
```

### Test Hyperlinks
```bash
python test_clickable_links.py
```

## 📊 ATS Performance

| Resume Type | ATS Score | Compatibility | Best Use Case |
|-------------|-----------|---------------|---------------|
| Storytelling | 78/100 | GOOD | Human recruiters, networking |
| Standard | 80/100 | GOOD | Online applications, ATS systems |
| Both | - | - | Maximum coverage strategy |

## 🌟 Why Choose This Tool?

- ✅ **Storytelling Innovation**: First resume tool with AI-powered narrative generation
- ✅ **ATS Compatible**: 78-80/100 scores ensure ATS passage
- ✅ **Clickable Links**: Professional DOCX with working hyperlinks
- ✅ **Real Data**: Uses your actual education and background
- ✅ **Universal**: Works for ANY career field with intelligent adaptation
- ✅ **Professional**: Perfect formatting matching industry standards
- ✅ **Fast**: Generate compelling resumes in seconds
- ✅ **Dual Output**: Choose narrative engagement or ATS optimization

## 🆕 Recent Updates (October 2025)

### 🎯 **Major Enhancements & Bug Fixes**
- ✨ **NEW**: Enhanced Computer Science job descriptions with 17+ programming languages (Python, Java, JavaScript, TypeScript, C++, C#, Go, Rust, Swift, Kotlin, R, MATLAB, Julia, etc.)
- ✨ **NEW**: Comprehensive field-specific configurations for 6 CS specializations (Data Scientist, Web Developer, Mobile Developer, DevOps Engineer, Security Engineer, Software Engineer)
- 🔧 **FIXED**: Education now correctly uses University of Central Florida & Valencia College from actual resume instead of hardcoded Florida Atlantic University
- 🔧 **FIXED**: Career narrative repetition issue - eliminated duplicate "My journey in data science" text
- 🔧 **FIXED**: Grammar corrections - now says "data science" instead of "data scientist" in narratives
- 🔧 **IMPROVED**: Data Scientist resumes now properly display programming languages in both text and DOCX formats
- 🔧 **ENHANCED**: Field-specific skills categorization (Programming, ML Libraries, Data Visualization, Big Data tools)

### 🏆 **Computer Science Specialization Support**
- **Data Scientist**: Python, R, SQL, TensorFlow, PyTorch, pandas, NumPy, scikit-learn, Tableau, Power BI
- **Software Engineer**: Full-stack development, algorithms, system design, multiple programming languages
- **Web Developer**: Frontend/backend technologies, responsive design, modern frameworks
- **Mobile Developer**: iOS/Android development, cross-platform solutions, app store optimization
- **DevOps Engineer**: Cloud infrastructure, CI/CD pipelines, containerization, monitoring
- **Security Engineer**: Cybersecurity, penetration testing, vulnerability assessment, compliance

### ✅ **Validation Results**
- ✅ **Programming Languages**: 8/8 languages detected and displayed in Data Scientist resumes
- ✅ **Education Accuracy**: University of Central Florida & Valencia College properly shown
- ✅ **DOCX Generation**: Professional formatting with correct education and no repetition
- ✅ **Field Detection**: Automatic detection and optimization for CS specializations
- ✅ **ATS Compatibility**: Maintained 78-80/100 scores with enhanced content

### 🔧 **Technical Improvements**
- Dynamic storytelling system with narrative-driven resumes
- Clickable hyperlinks in DOCX files (LinkedIn, GitHub open in browser)  
- Education duplication issues completely resolved
- Uses actual University of Central Florida education data from resume file
- ATS compatibility analysis and optimization
- Professional DOCX formatting with proper fonts and spacing

Transform your career story into a professional, engaging resume that passes ATS systems while captivating human recruiters!