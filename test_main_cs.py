#!/usr/bin/env python3
"""Quick test of enhanced CS job description with the main program"""

import sys
import os

# Add the current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_main_program():
    """Test the main program with a computer science job description"""
    print("🔍 Testing Main Program with Enhanced CS Support...")
    
    # Create a sample CS job description file
    cs_job_desc = """Senior Full Stack Developer Position at TechCorp

We're seeking an experienced Full Stack Developer to join our engineering team.

Required Programming Languages:
- JavaScript (ES6+) and TypeScript for frontend development
- Python or Java for backend services
- SQL for database operations
- HTML5 and CSS3 for markup and styling

Required Frameworks & Technologies:
- React, Angular, or Vue.js for frontend
- Node.js, Django, or Spring Boot for backend
- PostgreSQL or MongoDB for databases
- Docker and Kubernetes for containerization
- AWS, Azure, or GCP for cloud deployment

Preferred Skills:
- Go or Rust for performance-critical services
- Machine Learning with TensorFlow or PyTorch
- DevOps tools like Jenkins, GitLab CI, or GitHub Actions
- Mobile development with React Native or Flutter

Responsibilities:
- Design and implement scalable web applications
- Build responsive user interfaces with modern frameworks
- Develop RESTful APIs and microservices
- Deploy applications using cloud platforms
- Collaborate with cross-functional teams using Agile methodologies
- Write comprehensive tests and maintain code quality

Experience Level: 3-5 years in full stack development
Company: Leading technology company with excellent benefits
"""
    
    # Write to file
    with open('test_cs_job.txt', 'w', encoding='utf-8') as f:
        f.write(cs_job_desc)
    
    print("✅ Created test_cs_job.txt with comprehensive CS job description")
    print("📋 Job includes languages: JavaScript, TypeScript, Python, Java, SQL, HTML5, CSS3, Go, Rust")
    print("🛠️  Frameworks: React, Angular, Vue.js, Node.js, Django, Spring Boot, TensorFlow, PyTorch")
    print("☁️  Cloud: Docker, Kubernetes, AWS, Azure, GCP")
    print()
    print("🚀 You can now test this by running:")
    print("   python resume_windows.py")
    print("   Then select option 1 (file browser) and choose test_cs_job.txt")
    print()
    print("Expected Results:")
    print("   • Enhanced language detection for all mentioned programming languages")
    print("   • Better framework and technology matching")
    print("   • Improved ATS optimization for technical roles")
    print("   • More accurate field detection (likely as 'web_developer' or 'software_engineer')")

if __name__ == "__main__":
    test_main_program()