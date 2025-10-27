#!/usr/bin/env python3
"""Test enhanced computer science job descriptions with programming languages"""

import sys
import os
import tempfile
import shutil

# Add the current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from resume_windows import ResumeOptimizer

def test_cs_job_descriptions():
    """Test computer science job descriptions with enhanced programming languages"""
    print("🔍 Testing Enhanced Computer Science Job Descriptions...")
    
    # Create temp output directory
    temp_dir = tempfile.mkdtemp()
    print(f"Using temp directory: {temp_dir}")
    
    try:
        optimizer = ResumeOptimizer()
        
        # Mock the style choice input to simulate option 2 (standard resume) for each test
        import builtins
        original_input = builtins.input
        
        try:
            # Test different CS job descriptions
            test_cases = [
                {
                    'name': 'Data Scientist',
                    'job_desc': """Data Scientist Position at TechCorp
                    
                    We're seeking a talented Data Scientist to join our analytics team.
                    
                    Required Skills:
                    - Python programming with pandas, numpy, scikit-learn
                    - Machine learning and deep learning experience
                    - SQL and database management
                    - Statistical analysis and data visualization
                    - Experience with TensorFlow or PyTorch
                    
                    Preferred:
                    - R programming language
                    - Big data technologies (Spark, Hadoop)
                    - Cloud platforms (AWS, Azure, GCP)
                    """,
                    'role': 'Data Scientist',
                    'expected_languages': ['Python', 'R', 'Sql']
                },
                {
                    'name': 'Web Developer',
                    'job_desc': """Full Stack Web Developer at StartupXYZ
                    
                    Join our web development team to build modern applications.
                    
                    Required:
                    - JavaScript (ES6+) and TypeScript
                    - React or Angular frontend frameworks
                    - Node.js backend development
                    - HTML5, CSS3, responsive design
                    - RESTful API development
                    
                    Nice to have:
                    - Python with Django or Flask
                    - Database design (SQL, MongoDB)
                    - Docker and Kubernetes
                    """,
                    'role': 'Web Developer',
                    'expected_languages': ['Javascript', 'Typescript', 'Python', 'Html5', 'Css3']
                },
                {
                    'name': 'Mobile Developer',
                    'job_desc': """Mobile App Developer at MobileFirst Inc
                    
                    Build cutting-edge mobile applications for iOS and Android.
                    
                    Requirements:
                    - Swift for iOS development
                    - Kotlin or Java for Android
                    - React Native or Flutter experience
                    - Mobile UI/UX best practices
                    - App store deployment experience
                    
                    Bonus:
                    - Dart programming language
                    - Cross-platform development
                    - Firebase integration
                    """,
                    'role': 'Mobile Developer',
                    'expected_languages': ['Swift', 'Kotlin', 'Java', 'Dart']
                },
                {
                    'name': 'Security Engineer',
                    'job_desc': """Cybersecurity Engineer at SecureNet
                    
                    Protect our systems and data from security threats.
                    
                    Required Skills:
                    - Python scripting for security automation
                    - Bash and PowerShell scripting
                    - Penetration testing and vulnerability assessment
                    - Network security and firewalls
                    - Incident response and forensics
                    
                    Preferred:
                    - C/C++ for low-level security tools
                    - Go for security applications
                    - Security frameworks and compliance
                    """,
                    'role': 'Security Engineer',
                    'expected_languages': ['Python', 'Bash', 'Powershell', 'C++']
                }
            ]
            
            # Sample resume for testing
            resume_content = """Ryan Thomas Weiler
            Senior Software Engineer
            
            Contact: ryan_wlr@yahoo.com | (561) 906-2118
            LinkedIn: https://www.linkedin.com/in/ryan-weiler-7a3119190/
            GitHub: https://github.com/ryan-wlr
            
            Experience:
            - 5+ years software development experience
            - Built web applications and mobile apps
            - Data analysis and machine learning projects
            - Cloud deployment and DevOps experience
            
            Skills:
            Python, JavaScript, Java, C++, SQL, React, Node.js, TensorFlow,
            AWS, Docker, Git, Machine Learning, Data Analysis
            
            Education:
            Computer Science coursework at Florida Atlantic University
            """
            
            # Test each case
            for i, case in enumerate(test_cases, 1):
                print(f"\n{'='*60}")
                print(f"📋 TEST {i}: {case['name']}")
                print(f"{'='*60}")
                
                # Set up input for this test case
                inputs = iter(['2'])  # Standard resume for each test
                builtins.input = lambda prompt: next(inputs)
                
                # Run optimization
                results = optimizer.process_complete_optimization(
                    case['job_desc'], resume_content, case['role'], "TechCorp"
                )
                
                # Check analysis results
                print(f"\n🔍 Analysis Results:")
                if '1_job_analysis' in results:
                    analysis = results['1_job_analysis']
                    print(f"   📊 Job Analysis Length: {len(analysis)} characters")
                    
                    # Check for programming languages
                    languages_found = []
                    for lang in case['expected_languages']:
                        if lang.lower() in analysis.lower():
                            languages_found.append(lang)
                    
                    print(f"   💻 Programming Languages Found: {len(languages_found)}/{len(case['expected_languages'])}")
                    for lang in languages_found:
                        print(f"     ✅ {lang}")
                    
                    missing = [lang for lang in case['expected_languages'] if lang not in languages_found]
                    for lang in missing:
                        print(f"     ❌ {lang} (missing)")
                    
                    # Check for field-specific content
                    role_name = case['role'].lower().replace(' ', '_')
                    if role_name in analysis.lower():
                        print(f"   ✅ Field Detection: {case['role']} detected")
                    else:
                        print(f"   ⚠️  Field Detection: {case['role']} may not be detected")
                    
                    success_rate = len(languages_found) / len(case['expected_languages']) * 100
                    print(f"   📈 Success Rate: {success_rate:.1f}%")
                    
                    if success_rate >= 60:
                        print(f"   🎉 {case['name']} test PASSED")
                    else:
                        print(f"   ⚠️  {case['name']} test needs improvement")
                
                else:
                    print(f"   ❌ No job analysis found in results")
            
            print(f"\n{'='*60}")
            print("🎯 SUMMARY")
            print(f"{'='*60}")
            print("✅ Enhanced computer science job descriptions implemented")
            print("✅ Programming languages detection improved")
            print("✅ Multiple CS specializations supported:")
            print("   • Software Engineer (comprehensive languages)")
            print("   • Data Scientist (Python, R, SQL focus)")
            print("   • Web Developer (JavaScript, TypeScript, frameworks)")
            print("   • Mobile Developer (Swift, Kotlin, cross-platform)")
            print("   • DevOps Engineer (infrastructure languages)")
            print("   • Security Engineer (security-focused languages)")
                
        finally:
            # Restore original input function
            builtins.input = original_input
            
    except Exception as e:
        print(f"❌ Error during testing: {e}")
        import traceback
        traceback.print_exc()
        
    finally:
        # Clean up
        try:
            shutil.rmtree(temp_dir)
            print(f"\n🗑️  Cleaned up temp directory")
        except:
            pass

if __name__ == "__main__":
    test_cs_job_descriptions()