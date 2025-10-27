#!/usr/bin/env python3
"""Check the actual generated DOCX for education duplication"""

import sys
import os

# Add the current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def check_latest_docx():
    """Check the latest generated DOCX for education duplication"""
    print("🔍 Checking latest generated DOCX for education duplication...")
    
    # Find the latest browse_mode_output folder
    folders = [f for f in os.listdir('.') if f.startswith('browse_mode_output_')]
    if not folders:
        print("❌ No browse_mode_output folders found")
        return
    
    latest_folder = sorted(folders)[-1]
    docx_path = os.path.join(latest_folder, 'optimized_resume.docx')
    
    print(f"📂 Checking: {docx_path}")
    
    if not os.path.exists(docx_path):
        print("❌ DOCX file not found")
        return
    
    try:
        from docx import Document
        doc = Document(docx_path)
        
        # Get all paragraphs and their text
        content_lines = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
        
        print(f"\n📄 All content lines ({len(content_lines)} total):")
        for i, line in enumerate(content_lines):
            print(f"  {i+1:2d}. {line}")
        
        # Count education headers specifically
        education_headers = [i for i, line in enumerate(content_lines) if line == 'Education']
        print(f"\n📚 Education header positions: {education_headers}")
        
        if len(education_headers) > 1:
            print(f"❌ FOUND {len(education_headers)} Education sections!")
            for pos in education_headers:
                print(f"    Position {pos+1}: '{content_lines[pos]}'")
                if pos + 1 < len(content_lines):
                    print(f"    Next line: '{content_lines[pos+1]}'")
        else:
            print("✅ Only one Education section found")
            
        # Also check for any other education-related content
        education_content = [i for i, line in enumerate(content_lines) if 'florida atlantic university' in line.lower() or 'computer science' in line.lower()]
        print(f"\n🎓 Education content positions: {education_content}")
        
        if len(education_content) > 1:
            print(f"❌ FOUND {len(education_content)} pieces of education content!")
            for pos in education_content:
                print(f"    Position {pos+1}: '{content_lines[pos]}'")
        else:
            print("✅ Only one piece of education content found")
            
    except ImportError:
        print("⚠️  python-docx not available for content verification")
    except Exception as e:
        print(f"❌ Error reading DOCX: {e}")

if __name__ == "__main__":
    check_latest_docx()