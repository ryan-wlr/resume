#!/usr/bin/env python3
"""Test the education duplication fix in contact section parsing"""

import sys
import os
import tempfile
import shutil

# Add the current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from resume_windows import ResumeOptimizer

def test_education_fix():
    """Test that education content is filtered out of contact section"""
    print("🔍 Testing education duplication fix...")
    
    # Create temp output directory
    temp_dir = tempfile.mkdtemp()
    print(f"Using temp directory: {temp_dir}")
    
    try:
        # Initialize optimizer
        optimizer = ResumeOptimizer()
        
        # Mock detected field
        optimizer.current_detected_field = 'optical_engineer'
        
        # Create mock results with narrative content that has education in contact section
        mock_results = {
            '7_narrative_resume': """
CAREER STORY RESUME - OPTICAL ENGINEER

🔬 THE LIGHT ARCHITECT: Engineering the future through precision optics and photonic innovation

RYAN THOMAS WEILER
Optical Engineer Professional

CONTACT INFORMATION:
📞 (561) 906-2118 | ✉️ ryan_wlr@yahoo.com
🔗 LinkedIn: https://www.linkedin.com/in/ryan-weiler-7a3119190/ | 💻 GitHub: https://github.com/ryan-wlr
University of Central Florida — B.S. Computer Science, 2013 (Dean's List, GPA 3.8)
Valencia College — A.A., 2011 (Dean's List, GPA 3.7)
Experience & Projects (Continuous Timeline)
- Built, trained, and deployed neural networks (CNNs for vision; RNNs/Transformers for NLP).

PROFESSIONAL NARRATIVE:
Light has always been my medium of choice for solving complex engineering challenges.

TECHNICAL COMPETENCIES:
• Advanced Optical Design & Modeling (Zemax, Code V, LightTools)
• Laser Systems Development & Characterization
• Fiber Optic Communication Systems

PROFESSIONAL EXPERIENCE:
• Designed revolutionary laser systems improving efficiency by 40%
• Developed fiber optic communication systems enabling 10Gbps data transmission
• Led optical modeling projects resulting in 25% cost reduction
"""
        }
        
        # Create the DOCX
        optimizer.create_formatted_docx_resume(mock_results, temp_dir)
        
        # Check if DOCX was created
        docx_path = os.path.join(temp_dir, 'optimized_resume.docx')
        if os.path.exists(docx_path):
            print("✅ DOCX created successfully")
            
            # Try to read the DOCX to check for education duplication
            try:
                from docx import Document
                doc = Document(docx_path)
                
                # Get all paragraphs and their text
                content_lines = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
                
                print(f"\n📄 All content lines ({len(content_lines)} total):")
                for i, line in enumerate(content_lines):
                    print(f"  {i+1:2d}. {line}")
                
                # Check contact section specifically (should be around position 3-4)
                print(f"\n🔍 Contact section content:")
                for i, line in enumerate(content_lines[:6]):
                    if '📞' in line or 'LinkedIn' in line:
                        print(f"  Contact line {i+1}: {line}")
                        if 'university' in line.lower() or 'college' in line.lower():
                            print(f"    ❌ EDUCATION FOUND IN CONTACT: {line}")
                        else:
                            print(f"    ✅ Clean contact line")
                
                # Count education headers and content
                education_headers = [i for i, line in enumerate(content_lines) if line == 'Education']
                education_content = [i for i, line in enumerate(content_lines) if 'florida atlantic university' in line.lower() or 'university of central florida' in line.lower() or 'valencia college' in line.lower()]
                
                print(f"\n📚 Education header positions: {education_headers}")
                print(f"🎓 Education content positions: {education_content}")
                
                if len(education_headers) <= 1 and len(education_content) <= 1:
                    print("\n🎉 SUCCESS: Education duplication fixed!")
                else:
                    print(f"\n❌ Still have duplication: {len(education_headers)} headers, {len(education_content)} content pieces")
                    
            except ImportError:
                print("⚠️  python-docx not available for content verification")
                
        else:
            print("❌ DOCX file was not created")
            
    except Exception as e:
        print(f"❌ Error during testing: {e}")
        import traceback
        traceback.print_exc()
        
    finally:
        # Clean up
        try:
            shutil.rmtree(temp_dir)
            print(f"\n🗑️  Cleaned up temp directory: {temp_dir}")
        except:
            pass

if __name__ == "__main__":
    test_education_fix()