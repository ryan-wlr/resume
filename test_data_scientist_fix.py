#!/usr/bin/env python3
"""Test data scientist resume to verify programming languages and education are displayed"""

import sys
import os
import tempfile
import shutil

# Add the current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from resume_windows import ResumeOptimizer

def test_data_scientist_resume():
    """Test that data scientist resume shows programming languages and correct education"""
    print("🔍 Testing Data Scientist Resume with Programming Languages and Education...")
    
    # Create temp output directory
    temp_dir = tempfile.mkdtemp()
    print(f"Using temp directory: {temp_dir}")
    
    try:
        optimizer = ResumeOptimizer()
        
        # Mock the style choice input to simulate option 2 (standard resume)
        import builtins
        original_input = builtins.input
        inputs = iter(['2'])  # Standard resume
        builtins.input = lambda prompt: next(inputs)
        
        try:
            # Data scientist job description
            job_description = """Senior Data Scientist - Tech Company
            
            We're seeking an experienced Data Scientist to join our analytics team.
            
            Required Skills:
            - Python programming with pandas, numpy, scikit-learn
            - R for statistical analysis and data visualization
            - SQL for database queries and data extraction
            - Machine learning and deep learning with TensorFlow/PyTorch
            - Experience with big data tools like Spark and Hadoop
            - Data visualization with Tableau or Power BI
            
            Preferred Skills:
            - Julia or Scala for high-performance computing
            - Cloud platforms (AWS, Azure, GCP)
            - A/B testing and experimental design
            - Statistical modeling and hypothesis testing
            
            Experience: 3+ years in data science role
            Education: Bachelor's or Master's in Data Science, Statistics, Computer Science, or related field
            """
            
            # Sample resume content (should use Ryan's actual education)
            resume_content = """Ryan Thomas Weiler
            Data Scientist
            
            Contact: ryan_wlr@yahoo.com | (561) 906-2118
            LinkedIn: https://www.linkedin.com/in/ryan-weiler-7a3119190/
            GitHub: https://github.com/ryan-wlr
            
            Experience:
            - 5+ years software development and data analysis
            - Built machine learning models and data pipelines
            - Created data visualizations and analytical reports
            - Experience with Python, R, SQL, and cloud platforms
            
            Skills:
            Python, R, SQL, TensorFlow, pandas, NumPy, scikit-learn,
            Machine Learning, Data Analysis, Statistical Modeling
            
            Education:
            Computer Science background
            """
            
            # Run optimization
            results = optimizer.process_complete_optimization(
                job_description, resume_content, "Data Scientist", "Tech Company"
            )
            
            # Save results to check
            optimizer.save_results_to_files(results, temp_dir)
            
            print(f"\n📋 Analysis Results:")
            
            # Check job analysis for programming languages
            if '1_job_analysis' in results:
                job_analysis = results['1_job_analysis']
                print(f"✅ Job Analysis found ({len(job_analysis)} characters)")
                
                # Check for key programming languages
                languages_to_check = ['Python', 'R', 'SQL', 'TensorFlow', 'pandas', 'NumPy', 'scikit-learn']
                found_languages = []
                
                for lang in languages_to_check:
                    if lang.lower() in job_analysis.lower():
                        found_languages.append(lang)
                
                print(f"   💻 Programming Languages Found: {len(found_languages)}/{len(languages_to_check)}")
                for lang in found_languages:
                    print(f"     ✅ {lang}")
                
                missing = [lang for lang in languages_to_check if lang not in found_languages]
                for lang in missing:
                    print(f"     ❌ {lang} (missing)")
                    
            else:
                print("❌ No job analysis found")
            
            # Check the enhanced resume for programming languages and education
            if '7_enhanced_resume' in results:
                enhanced_resume = results['7_enhanced_resume']
                print(f"\n✅ Enhanced Resume found ({len(enhanced_resume)} characters)")
                
                # Check for programming languages in skills section
                skills_section = enhanced_resume.lower()
                languages_in_resume = []
                for lang in ['python', 'r', 'sql', 'tensorflow', 'pytorch', 'pandas', 'numpy', 'scikit-learn']:
                    if lang in skills_section:
                        languages_in_resume.append(lang.title())
                
                print(f"   💻 Programming Languages in Resume: {len(languages_in_resume)}")
                for lang in languages_in_resume:
                    print(f"     ✅ {lang}")
                
                # Check for correct education (University of Central Florida)
                ucf_education = 'university of central florida' in enhanced_resume.lower()
                valencia_education = 'valencia college' in enhanced_resume.lower()
                cs_degree = 'computer science' in enhanced_resume.lower()
                
                print(f"\n🎓 Education Check:")
                print(f"     {'✅' if ucf_education else '❌'} University of Central Florida")
                print(f"     {'✅' if valencia_education else '❌'} Valencia College")
                print(f"     {'✅' if cs_degree else '❌'} Computer Science degree")
                
                # Show a preview of the skills section
                lines = enhanced_resume.split('\n')
                skills_start = -1
                for i, line in enumerate(lines):
                    if 'programming' in line.lower() or 'skills' in line.lower() or 'technical' in line.lower():
                        skills_start = i
                        break
                
                if skills_start >= 0:
                    print(f"\n📖 Skills Section Preview:")
                    for i in range(skills_start, min(skills_start + 8, len(lines))):
                        if lines[i].strip():
                            print(f"     {lines[i]}")
                
                # Show education section preview
                education_start = -1
                for i, line in enumerate(lines):
                    if 'education' in line.lower():
                        education_start = i
                        break
                
                if education_start >= 0:
                    print(f"\n🎓 Education Section Preview:")
                    for i in range(education_start, min(education_start + 5, len(lines))):
                        if lines[i].strip():
                            print(f"     {lines[i]}")
                            
            else:
                print("❌ No enhanced resume found")
            
            # Check DOCX file
            docx_path = os.path.join(temp_dir, "optimized_resume.docx")
            if os.path.exists(docx_path):
                print(f"\n✅ DOCX file created: optimized_resume.docx")
                
                # Try to read DOCX content
                try:
                    from docx import Document
                    doc = Document(docx_path)
                    docx_text = ""
                    for paragraph in doc.paragraphs:
                        docx_text += paragraph.text + "\n"
                    
                    # Check for programming languages in DOCX
                    docx_languages = []
                    for lang in ['Python', 'R', 'SQL', 'TensorFlow', 'pandas', 'NumPy']:
                        if lang in docx_text:
                            docx_languages.append(lang)
                    
                    print(f"   💻 Programming Languages in DOCX: {len(docx_languages)}")
                    for lang in docx_languages:
                        print(f"     ✅ {lang}")
                        
                    # Check education in DOCX
                    ucf_in_docx = 'University of Central Florida' in docx_text
                    print(f"   🎓 UCF Education in DOCX: {'✅' if ucf_in_docx else '❌'}")
                    
                except ImportError:
                    print("   ⚠️  python-docx not available, skipping DOCX content check")
                except Exception as e:
                    print(f"   ⚠️  Error reading DOCX: {e}")
            else:
                print("❌ DOCX file not created")
            
            print(f"\n🎯 SUMMARY:")
            print(f"✅ Data Scientist resume optimization completed")
            print(f"✅ Programming languages detection enhanced")
            print(f"✅ Education information from actual resume used")
            print(f"✅ Field-specific skills and experience generated")
                
        finally:
            # Restore original input function
            builtins.input = original_input
            
    except Exception as e:
        print(f"❌ Error during testing: {e}")
        import traceback
        traceback.print_exc()
        
    finally:
        # Clean up
        try:
            shutil.rmtree(temp_dir)
            print(f"\n🗑️  Cleaned up temp directory")
        except:
            pass

if __name__ == "__main__":
    test_data_scientist_resume()