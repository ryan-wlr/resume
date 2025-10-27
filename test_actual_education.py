#!/usr/bin/env python3
"""Test that actual resume education (UCF) is used instead of hardcoded FAU"""

import sys
import os
import tempfile
import shutil

# Add the current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from resume_windows import ResumeOptimizer

def test_actual_education():
    """Test that University of Central Florida education is used from actual resume"""
    print("🔍 Testing actual education extraction (UCF instead of FAU)...")
    
    # Create temp output directory
    temp_dir = tempfile.mkdtemp()
    print(f"Using temp directory: {temp_dir}")
    
    try:
        # Initialize optimizer
        optimizer = ResumeOptimizer()
        
        # Mock detected field
        optimizer.current_detected_field = 'optical_engineer'
        
        # Create mock results with narrative content that includes actual UCF education
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

PROFESSIONAL EXPERIENCE:
• Designed revolutionary laser systems improving efficiency by 40%
• Developed fiber optic communication systems enabling 10Gbps data transmission
"""
        }
        
        # Create the DOCX
        optimizer.create_formatted_docx_resume(mock_results, temp_dir)
        
        # Check if DOCX was created
        docx_path = os.path.join(temp_dir, 'optimized_resume.docx')
        if os.path.exists(docx_path):
            print("✅ DOCX created successfully")
            
            # Try to read the DOCX to check education content
            try:
                from docx import Document
                doc = Document(docx_path)
                
                # Get all paragraphs and their text
                content_lines = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
                
                print(f"\n📄 All content lines ({len(content_lines)} total):")
                for i, line in enumerate(content_lines):
                    print(f"  {i+1:2d}. {line}")
                
                # Look for education content specifically
                ucf_found = False
                valencia_found = False
                fau_found = False
                
                for i, line in enumerate(content_lines):
                    if 'university of central florida' in line.lower():
                        print(f"\n✅ FOUND UCF EDUCATION (line {i+1}): {line}")
                        ucf_found = True
                    if 'valencia college' in line.lower():
                        print(f"✅ FOUND VALENCIA EDUCATION (line {i+1}): {line}")
                        valencia_found = True
                    if 'florida atlantic university' in line.lower():
                        print(f"❌ FOUND OLD FAU EDUCATION (line {i+1}): {line}")
                        fau_found = True
                
                if (ucf_found and valencia_found) and not fau_found:
                    print("\n🎉 SUCCESS: Using actual resume education (UCF + Valencia)!")
                elif not ucf_found and not valencia_found and fau_found:
                    print("\n⚠️  Using fallback FAU education (actual education not extracted)")
                else:
                    print(f"\n❓ Mixed results: UCF={ucf_found}, Valencia={valencia_found}, FAU={fau_found}")
                    
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
    test_actual_education()