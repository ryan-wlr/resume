#!/usr/bin/env python3
"""Debug field detection for machine learning job descriptions"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from resume_windows import ResumeOptimizer

def test_machine_learning_detection():
    """Test what field is detected for machine learning descriptions"""
    print("🔍 Testing Machine Learning Field Detection...")
    
    optimizer = ResumeOptimizer()
    
    # Test various machine learning related inputs
    test_inputs = [
        "machine learning engineer",
        "machine learning",
        "ML engineer", 
        "artificial intelligence",
        "deep learning engineer",
        "AI researcher",
        "machine learning scientist"
    ]
    
    print("\n📊 Field Detection Results:")
    for test_input in test_inputs:
        detected_field = optimizer.detect_career_field(test_input.lower())
        print(f"   '{test_input}' → detected as: '{detected_field}'")
    
    # Test with a sample machine learning job description
    sample_ml_job = """
    Machine Learning Engineer Position
    
    We are seeking a talented Machine Learning Engineer to join our AI team.
    
    Requirements:
    - Strong programming skills in Python, TensorFlow, PyTorch
    - Experience with deep learning, neural networks
    - Knowledge of data science, statistics, and machine learning algorithms
    - Experience with cloud platforms (AWS, GCP, Azure)
    - Strong background in mathematics and statistics
    
    Responsibilities:
    - Develop and deploy machine learning models
    - Work with large datasets and data pipelines
    - Collaborate with data scientists and software engineers
    - Optimize model performance and scalability
    """
    
    print(f"\n🧪 Sample ML Job Description Detection:")
    detected_field = optimizer.detect_career_field(sample_ml_job.lower())
    print(f"   Detected field: '{detected_field}'")
    
    # Show what field data this would generate
    field_data = optimizer.get_field_data(detected_field)
    print(f"\n📋 Field Data Summary:")
    print(f"   Experience Title: {field_data['experience_title']}")
    print(f"   Education: {field_data['education'][:50]}...")
    print(f"   Skills Categories: {len(field_data['skills'])} skill groups")
    print(f"   First Skills: {field_data['skills'][0] if field_data['skills'] else 'None'}")

if __name__ == "__main__":
    test_machine_learning_detection()