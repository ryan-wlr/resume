#!/usr/bin/env python3
"""Test to see exactly where education duplication occurs in storytelling DOCX"""

import sys
import os
import tempfile
import shutil

# Add the current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from resume_windows import ResumeOptimizer

def test_education_duplication():
    """Test to identify exactly where education duplication happens"""
    print("🔍 Testing education duplication in storytelling DOCX...")
    
    # Create temp output directory
    temp_dir = tempfile.mkdtemp()
    print(f"Using temp directory: {temp_dir}")
    
    try:
        # Initialize optimizer
        optimizer = ResumeOptimizer()
        
        # Mock detected field
        optimizer.current_detected_field = 'ai_researcher'
        
        # Create mock results with narrative content
        mock_results = {
            '7_narrative_resume': """
CAREER STORY RESUME FOR AI RESEARCHER

🔬 THE AI VISIONARY WHO TRANSFORMS DATA INTO INTELLIGENT SOLUTIONS

RYAN WEILER

CONTACT INFORMATION:
📞 (561) 906-2118 | ✉️ ryan_wlr@yahoo.com
🔗 LinkedIn: https://www.linkedin.com/in/ryan-weiler-7a3119190/
💻 GitHub: https://github.com/ryan-wlr

PROFESSIONAL NARRATIVE:
As an innovative AI researcher with expertise in machine learning algorithms and neural networks, I bring a unique blend of theoretical knowledge and practical implementation skills to drive breakthrough solutions in artificial intelligence.

TECHNICAL COMPETENCIES:
• Advanced Machine Learning & Deep Learning Frameworks (TensorFlow, PyTorch, Scikit-learn)
• Neural Network Architectures (CNNs, RNNs, Transformers, GANs)
• Natural Language Processing & Computer Vision Systems
• Data Science Pipeline Development (Python, R, SQL)
• Research Methodology & Statistical Analysis
• Cloud Computing Platforms (AWS, Google Cloud, Azure)

PROFESSIONAL EXPERIENCE:
• Led development of novel neural network architectures for image classification
• Implemented state-of-the-art NLP models for sentiment analysis
• Published research papers on reinforcement learning applications
• Collaborated on interdisciplinary AI projects with academic institutions
• Designed and deployed machine learning models in production environments
• Conducted extensive experiments with hyperparameter optimization
• Developed data preprocessing pipelines for large-scale datasets
• Mentored junior researchers in machine learning methodologies
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
    test_education_duplication()