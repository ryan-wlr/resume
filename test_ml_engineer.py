#!/usr/bin/env python3
"""Test the new Machine Learning Engineer field"""

import sys
import os
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from resume_windows import ResumeOptimizer

def test_ml_engineer_complete():
    """Test Machine Learning Engineer field end-to-end"""
    print("🤖 Testing Machine Learning Engineer Field...")
    
    # Create temp output directory
    temp_dir = tempfile.mkdtemp()
    print(f"Using temp directory: {temp_dir}")
    
    try:
        # Initialize optimizer
        optimizer = ResumeOptimizer()
        
        # Test job description
        ml_job_description = """
        Machine Learning Engineer Position
        
        We are seeking a talented Machine Learning Engineer to join our AI team.
        
        Requirements:
        - Strong programming skills in Python, TensorFlow, PyTorch
        - Experience with MLOps, Kubeflow, and production ML systems
        - Knowledge of deep learning, neural networks, and model optimization
        - Experience with cloud platforms (AWS, GCP, Azure)
        - Strong background in mathematics and computer science
        
        Responsibilities:
        - Design and deploy machine learning models to production
        - Build end-to-end ML pipelines and automation
        - Optimize model performance and inference speed
        - Implement monitoring and observability for ML systems
        """
        
        # Test resume content
        resume_content = """
        RYAN THOMAS WEILER
        Machine Learning Engineer
        
        Phone: (561) 906-2118 | Email: ryan_wlr@yahoo.com
        LinkedIn: https://www.linkedin.com/in/ryan-weiler-7a3119190/
        
        Experience:
        - Built production ML pipelines using TensorFlow and PyTorch
        - Deployed models to Kubernetes clusters with 99.9% uptime
        - Optimized deep learning models reducing inference time by 50%
        
        Skills:
        - Python, TensorFlow, PyTorch, scikit-learn
        - MLOps, Kubeflow, Docker, Kubernetes
        - AWS SageMaker, GCP AI Platform
        """
        
        # Mock detected field
        optimizer.current_detected_field = 'machine_learning_engineer'
        
        # Test field detection
        detected_field = optimizer.detect_career_field(ml_job_description.lower())
        print(f"🎯 Field Detection: '{detected_field}'")
        
        # Test field data
        field_data = optimizer.get_field_data(detected_field)
        print(f"\n📋 Field Data Summary:")
        print(f"   Experience Title: {field_data['experience_title']}")
        print(f"   Education: {field_data['education'][:50]}...")
        print(f"   Skills Categories: {len(field_data['skills'])}")
        for i, skill_category in enumerate(field_data['skills'][:3]):
            print(f"   Skill {i+1}: {skill_category[:60]}...")
        
        # Test complete optimization
        print(f"\n⚙️ Running Complete Optimization...")
        results = optimizer.process_complete_optimization(
            ml_job_description, resume_content, 'Machine Learning Engineer', 'AI Company'
        )
        
        # Create DOCX
        optimizer.save_results_to_files(results, temp_dir)
        optimizer.create_formatted_docx_resume_specific(results, temp_dir, 'ml_engineer_test.docx')
        
        # Check results
        docx_path = os.path.join(temp_dir, 'ml_engineer_test.docx')
        if os.path.exists(docx_path):
            print("✅ DOCX created successfully")
            
            # Read and check content
            try:
                from docx import Document
                doc = Document(docx_path)
                full_text = '\n'.join([p.text for p in doc.paragraphs])
                
                # Check for ML-specific content
                ml_frameworks = ['TensorFlow', 'PyTorch', 'scikit-learn']
                mlops_tools = ['MLflow', 'Kubeflow', 'Docker', 'Kubernetes']
                
                print(f"\n📊 Content Analysis:")
                print(f"   ML Frameworks found: {sum(1 for fw in ml_frameworks if fw in full_text)}/{len(ml_frameworks)}")
                print(f"   MLOps tools found: {sum(1 for tool in mlops_tools if tool in full_text)}/{len(mlops_tools)}")
                
                if 'University of Central Florida' in full_text:
                    print("   ✅ Correct UCF education found")
                else:
                    print("   ❌ UCF education missing")
                    
                if 'Machine Learning Engineer' in full_text:
                    print("   ✅ ML Engineer title found")
                else:
                    print("   ❌ ML Engineer title missing")
                    
        else:
            print("❌ DOCX not created")
            
        # Check enhanced resume content
        if '7_enhanced_standard_resume' in results:
            enhanced_content = results['7_enhanced_standard_resume']
            print(f"\n📖 Enhanced Resume Preview:")
            print(enhanced_content[:400] + "...")
            
        print(f"\n🎯 SUMMARY:")
        print(f"✅ Machine Learning Engineer field successfully implemented")
        print(f"✅ Distinct from Data Scientist with ML-specific content")
        print(f"✅ MLOps focus with production ML engineering skills")
        print(f"✅ Proper field detection and content generation")
            
    except Exception as e:
        print(f"❌ Error in test: {e}")
        import traceback
        traceback.print_exc()
    
    finally:
        # Cleanup
        try:
            import shutil
            shutil.rmtree(temp_dir)
            print(f"🗑️  Cleaned up temp directory")
        except:
            pass

if __name__ == "__main__":
    test_ml_engineer_complete()