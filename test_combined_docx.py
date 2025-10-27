#!/usr/bin/env python3
"""Verify DOCX file contains the combined content"""

import sys
import os
import tempfile
from docx import Document

# Add the current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from resume_windows import ResumeOptimizer

def test_combined_docx():
    """Test that the DOCX file contains combined content"""
    print("🔍 Testing Combined Resume DOCX creation...")
    
    temp_dir = tempfile.mkdtemp()
    print(f"Using temp directory: {temp_dir}")
    
    try:
        optimizer = ResumeOptimizer()
        
        # Mock the style choice input for option 3
        import builtins
        original_input = builtins.input
        inputs = iter(['3'])
        builtins.input = lambda prompt: next(inputs)
        
        try:
            job_description = """Data Scientist position at NASA requiring Python, ML, and statistical analysis."""
            resume_content = """Ryan Thomas Weiler | (561) 906-2118 | ryan_wlr@yahoo.com
            Software Developer with ML experience"""
            
            # Run optimization
            results = optimizer.process_complete_optimization(
                job_description, resume_content, "data scientist", "nasa"
            )
            
            # Save results
            optimizer.save_results_to_files(results, temp_dir)
            
            # Check DOCX file exists
            docx_path = os.path.join(temp_dir, "optimized_resume.docx")
            if os.path.exists(docx_path):
                print("✅ DOCX file created successfully")
                
                # Read DOCX content
                doc = Document(docx_path)
                docx_text = ""
                for paragraph in doc.paragraphs:
                    docx_text += paragraph.text + "\n"
                
                # Check for combined elements
                has_hook = any(emoji in docx_text for emoji in ['🔥', '🔬', '💻', '🌟'])
                has_narrative = 'CAREER NARRATIVE' in docx_text
                has_summary = 'PROFESSIONAL SUMMARY' in docx_text
                has_competencies = 'CORE TECHNICAL COMPETENCIES' in docx_text
                
                print(f"\n📄 DOCX Content Analysis:")
                print(f"   {'✅' if has_hook else '❌'} Hook with emoji")
                print(f"   {'✅' if has_narrative else '❌'} Career Narrative")
                print(f"   {'✅' if has_summary else '❌'} Professional Summary")
                print(f"   {'✅' if has_competencies else '❌'} Technical Competencies")
                
                total = sum([has_hook, has_narrative, has_summary, has_competencies])
                
                if total >= 3:
                    print(f"\n🎉 SUCCESS: DOCX contains combined resume content!")
                    print(f"   • {total}/4 key elements found in DOCX")
                else:
                    print(f"\n⚠️  Issue: Only {total}/4 elements found in DOCX")
                
                # Show preview
                preview = docx_text[:400] + "..."
                print(f"\n📖 DOCX Preview:\n{preview}")
                
            else:
                print("❌ DOCX file not found")
                
        finally:
            builtins.input = original_input
            
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        
    finally:
        # Cleanup
        import shutil
        try:
            shutil.rmtree(temp_dir)
        except:
            pass

if __name__ == "__main__":
    test_combined_docx()