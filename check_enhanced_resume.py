#!/usr/bin/env python3
"""Check the actual enhanced resume content"""

import sys
import os
import tempfile
import shutil

# Add the current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from resume_windows import ResumeOptimizer

def check_enhanced_resume():
    """Check the actual enhanced resume content"""
    print("🔍 Checking Enhanced Resume Content...")
    
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
            
            # Check the enhanced resume content
            if '7_enhanced_resume' in results:
                enhanced_resume = results['7_enhanced_resume']
                print(f"\n📖 Enhanced Resume Full Content:")
                print("=" * 60)
                print(enhanced_resume)
                print("=" * 60)
                
                # Check for programming languages
                languages = ['Python', 'R', 'SQL', 'TensorFlow', 'pandas', 'NumPy', 'scikit-learn']
                found_langs = []
                for lang in languages:
                    if lang in enhanced_resume:
                        found_langs.append(lang)
                
                print(f"\n💻 Programming Languages Found: {len(found_langs)}/{len(languages)}")
                for lang in found_langs:
                    print(f"   ✅ {lang}")
                
                missing = [lang for lang in languages if lang not in found_langs]
                for lang in missing:
                    print(f"   ❌ {lang}")
                
                # Check for education
                if 'University of Central Florida' in enhanced_resume:
                    print("✅ UCF education found")
                elif 'Florida Atlantic University' in enhanced_resume:
                    print("✅ FAU education found") 
                elif 'university' in enhanced_resume.lower():
                    print("⚠️  Some university found")
                else:
                    print("❌ No university education found")
                
                # Check for data science specific content
                ds_terms = ['machine learning', 'data science', 'predictive', 'analytics', 'visualization']
                found_ds = [term for term in ds_terms if term.lower() in enhanced_resume.lower()]
                print(f"\n🔬 Data Science Terms: {found_ds}")
                
            else:
                print("❌ Enhanced resume not found")
                
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
    check_enhanced_resume()