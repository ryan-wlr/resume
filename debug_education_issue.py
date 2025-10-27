#!/usr/bin/env python3
"""Debug why education shows wrong university instead of University of Central Florida from ryan_weiler_resume.docx"""

import sys
import os
import tempfile

# Add the current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from resume_windows import ResumeOptimizer

def debug_education_issue():
    """Debug exactly what's happening with education extraction"""
    print("🔍 Debugging education issue...")
    
    # Initialize optimizer
    optimizer = ResumeOptimizer()
    
    # Test 1: Check field data for data scientist
    print("\n1. Field Data Education Check:")
    optimizer.current_detected_field = 'data_scientist'
    field_data = optimizer.get_field_data('data_scientist')
    print(f"   data_scientist education: {field_data['education']}")
    
    # Test 2: Check if ryan_weiler_resume.docx exists and what education it contains
    print("\n2. Actual Resume File Check:")
    resume_file = 'ryan_weiler_resume.docx'
    if os.path.exists(resume_file):
        print(f"   ✅ {resume_file} exists")
        try:
            from docx import Document
            doc = Document(resume_file)
            content = '\n'.join([paragraph.text for paragraph in doc.paragraphs])
            print(f"   Content length: {len(content)} characters")
            
            # Extract education information
            resume_info = optimizer.extract_resume_information(content)
            print(f"   Extracted education: {resume_info['education']}")
            
            # Check for University of Central Florida in content
            if 'University of Central Florida' in content:
                print("   ✅ University of Central Florida found in resume")
            else:
                print("   ❌ University of Central Florida NOT found in resume")
                
            if 'Valencia College' in content:
                print("   ✅ Valencia College found in resume")
            else:
                print("   ❌ Valencia College NOT found in resume")
                
        except Exception as e:
            print(f"   ❌ Error reading resume: {e}")
    else:
        print(f"   ❌ {resume_file} does not exist")
    
    # Test 3: Create test narrative content and see what education is extracted
    print("\n3. Narrative Education Extraction Test:")
    test_narrative = """
CAREER STORY RESUME FOR DATA SCIENTIST

🔬 THE AI VISIONARY WHO TRANSFORMS DATA INTO INTELLIGENT SOLUTIONS

RYAN WEILER

CONTACT INFORMATION:
📞 (561) 906-2118 | ✉️ ryan_wlr@yahoo.com
🔗 LinkedIn: https://www.linkedin.com/in/ryan-weiler-7a3119190/
💻 GitHub: https://github.com/ryan-wlr
University of Central Florida — B.S. Computer Science, 2013 (Dean's List, GPA 3.8)
Valencia College — A.A., 2011 (Dean's List, GPA 3.7)

PROFESSIONAL NARRATIVE:
Light has always been my medium of choice for solving complex challenges.
"""
    
    # Parse narrative content to extract sections like in build_narrative_docx
    lines = test_narrative.split('\n')
    sections = {'hook': '', 'name': '', 'contact': '', 'narrative': '', 'skills': [], 'experience': [], 'education': []}
    
    current_section = None
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Detect key elements
        if '🔥 THE' in line or '🔬 THE' in line or '💻 THE' in line or '🌟 THE' in line:
            sections['hook'] = line
        elif 'CONTACT INFORMATION:' in line:
            current_section = 'contact'
            continue
        elif 'PROFESSIONAL NARRATIVE:' in line:
            current_section = 'narrative'
            continue
        elif line and not line.startswith('CAREER STORY RESUME') and not line.startswith('Chapter'):
            # Extract content based on current section
            if current_section is None and len(line.split()) <= 3 and any(c.isupper() for c in line):
                sections['name'] = line
            elif current_section == 'contact':
                # Extract education content to separate section, filter from contact
                if ('university' in line.lower() or 'college' in line.lower()) and ('b.s.' in line.lower() or 'a.a.' in line.lower() or 'gpa' in line.lower()):
                    sections['education'].append(line)
                elif not ('experience & projects' in line.lower() or 'built, trained' in line.lower()):
                    sections['contact'] += line + '\n'
            elif current_section == 'narrative':
                sections['narrative'] += line + ' '
    
    print(f"   Extracted education lines: {sections['education']}")
    print(f"   Contact section: {sections['contact'][:100]}...")
    
    if sections['education']:
        print("   ✅ Education successfully extracted from narrative")
    else:
        print("   ❌ Education NOT extracted from narrative - will use fallback")

if __name__ == "__main__":
    debug_education_issue()