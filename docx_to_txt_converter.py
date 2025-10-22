#!/usr/bin/env python3
"""
DOCX to TXT Converter - Fix for corrupted or problematic DOCX files

This utility helps when python-docx can't read a DOCX file.
It provides alternative methods to extract text content.
"""

import os
import sys
import zipfile
import xml.etree.ElementTree as ET

def extract_text_from_docx_zip(docx_path):
    """
    Extract text from DOCX by treating it as a ZIP file and parsing the XML.
    This method works even when python-docx fails.
    """
    try:
        text_content = []
        
        # DOCX files are ZIP archives containing XML
        with zipfile.ZipFile(docx_path, 'r') as zip_file:
            # The main document is in word/document.xml
            if 'word/document.xml' in zip_file.namelist():
                xml_content = zip_file.read('word/document.xml')
                
                # Parse XML to extract text
                root = ET.fromstring(xml_content)
                
                # Find all text elements (namespace aware)
                namespaces = {
                    'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
                }
                
                # Extract text from all paragraph runs
                for para in root.findall('.//w:p', namespaces):
                    para_text = []
                    for run in para.findall('.//w:t', namespaces):
                        if run.text:
                            para_text.append(run.text)
                    
                    if para_text:
                        text_content.append(''.join(para_text))
                
                return '\n'.join(text_content)
            else:
                return "Error: Not a valid DOCX file (missing document.xml)"
                
    except zipfile.BadZipFile:
        return "Error: File is not a valid ZIP/DOCX format"
    except Exception as e:
        return f"Error extracting text: {e}"

def convert_docx_to_txt(input_path, output_path=None):
    """Convert a DOCX file to TXT using ZIP extraction method"""
    
    if not output_path:
        base_name = os.path.splitext(input_path)[0]
        output_path = f"{base_name}_converted.txt"
    
    print(f"🔄 Converting: {os.path.basename(input_path)}")
    print(f"📄 Output will be: {os.path.basename(output_path)}")
    
    # Extract text using ZIP method
    content = extract_text_from_docx_zip(input_path)
    
    if content.startswith("Error:"):
        print(f"❌ {content}")
        return None
    
    # Save to text file
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Successfully converted!")
        print(f"📊 Extracted {len(content)} characters")
        print(f"💾 Saved to: {output_path}")
        
        # Show preview
        preview = content[:200].replace('\n', ' ')
        print(f"📝 Preview: {preview}...")
        
        return output_path
        
    except Exception as e:
        print(f"❌ Failed to save: {e}")
        return None

def main():
    print("🔧 DOCX to TXT Converter")
    print("=" * 30)
    print("This tool helps extract text from problematic DOCX files")
    print()
    
    if len(sys.argv) < 2:
        print("Usage: python docx_to_txt_converter.py <input_file.docx> [output_file.txt]")
        print()
        print("Example:")
        print("  python docx_to_txt_converter.py brain_surgeon.docx")
        print("  python docx_to_txt_converter.py C:/Users/ryan_/OneDrive/Documents/brain_surgeon.docx")
        return
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    if not os.path.exists(input_file):
        print(f"❌ File not found: {input_file}")
        return
    
    result = convert_docx_to_txt(input_file, output_file)
    
    if result:
        print(f"\n🎉 Conversion complete!")
        print(f"You can now use '{result}' in the resume optimizer.")

if __name__ == "__main__":
    main()