#!/usr/bin/env python3
"""Debug data scientist resume to see actual keys and content"""

import sys
import os
import tempfile
import shutil

# Add the current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from resume_windows import ResumeOptimizer

def debug_data_scientist_resume():
    """Debug the data scientist resume to see actual content"""
    print("🔍 Debugging Data Scientist Resume...")
    
    temp_dir = tempfile.mkdtemp()
    
    try:
        optimizer = ResumeOptimizer()
        
        import builtins
        original_input = builtins.input
        inputs = iter(['2'])
        builtins.input = lambda prompt: next(inputs)
        
        try:
            job_description = """Data Scientist position requiring Python, R, SQL, machine learning."""
            resume_content = """Ryan Thomas Weiler | Data Scientist | ryan_wlr@yahoo.com"""
            
            results = optimizer.process_complete_optimization(
                job_description, resume_content, "Data Scientist", "Tech Company"
            )
            
            print(f"\n📋 Available Result Keys:")
            for key in sorted(results.keys()):
                content_preview = str(results[key])[:100] + "..." if len(str(results[key])) > 100 else str(results[key])
                print(f"   {key}: {content_preview}")
            
            # Look for the tailored resume content
            tailored_keys = [k for k in results.keys() if 'tailored' in k.lower() or 'impact' in k.lower() or 'enhanced' in k.lower()]
            print(f"\n📄 Possible Resume Content Keys: {tailored_keys}")
            
            # Check the impact version
            if '3_resume_impact_version' in results:
                impact_resume = results['3_resume_impact_version']
                print(f"\n📖 Impact Resume Content (first 500 chars):")
                print(impact_resume[:500])
                
                # Check for education
                if 'university of central florida' in impact_resume.lower():
                    print("✅ UCF education found in impact resume")
                elif 'florida atlantic university' in impact_resume.lower():
                    print("✅ FAU education found in impact resume")
                else:
                    print("❌ No specific university found in impact resume")
                    
                # Check for programming languages
                languages = ['Python', 'R', 'SQL', 'TensorFlow', 'pandas', 'NumPy']
                found_langs = [lang for lang in languages if lang in impact_resume]
                print(f"💻 Languages in impact resume: {found_langs}")
            
            # Check enhanced standard resume  
            if '7_enhanced_standard_resume' in results:
                enhanced_resume = results['7_enhanced_standard_resume']
                print(f"\n📖 Enhanced Resume Content (first 500 chars):")
                print(enhanced_resume[:500])
                
                # Check for education
                if 'university of central florida' in enhanced_resume.lower():
                    print("✅ UCF education found in enhanced resume")
                elif 'florida atlantic university' in enhanced_resume.lower():
                    print("✅ FAU education found in enhanced resume")
                else:
                    print("❌ No specific university found in enhanced resume")
                    
                # Check for programming languages
                found_langs = [lang for lang in languages if lang in enhanced_resume]
                print(f"💻 Languages in enhanced resume: {found_langs}")
            
            # Check DOCX content
            docx_path = os.path.join(temp_dir, "optimized_resume.docx")
            if os.path.exists(docx_path):
                try:
                    from docx import Document
                    doc = Document(docx_path)
                    docx_text = ""
                    for paragraph in doc.paragraphs:
                        docx_text += paragraph.text + "\n"
                    
                    print(f"\n📄 DOCX Content (first 500 chars):")
                    print(docx_text[:500])
                    
                    # Check what education is in DOCX
                    if 'university of central florida' in docx_text.lower():
                        print("✅ UCF education found in DOCX")
                    elif 'florida atlantic university' in docx_text.lower():
                        print("✅ FAU education found in DOCX")
                    elif 'university' in docx_text.lower():
                        print("⚠️  Some university mentioned in DOCX")
                        # Find which university
                        lines = docx_text.split('\n')
                        for line in lines:
                            if 'university' in line.lower():
                                print(f"     {line.strip()}")
                    else:
                        print("❌ No university found in DOCX")
                        
                except Exception as e:
                    print(f"Error reading DOCX: {e}")
                    
        finally:
            builtins.input = original_input
            
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        
    finally:
        try:
            shutil.rmtree(temp_dir)
        except:
            pass

if __name__ == "__main__":
    debug_data_scientist_resume()