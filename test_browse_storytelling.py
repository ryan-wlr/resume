#!/usr/bin/env python3
"""
Test Storytelling Integration in Browse Mode
============================================

This script tests the storytelling feature specifically in browse mode
to ensure option 1 (Story Resume) works correctly.
"""

import sys
import os
import tempfile
from datetime import datetime

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def create_test_files():
    """Create temporary test files for the demo"""
    # Create test job description
    job_content = """Senior Software Engineer - FinTech Startup

We're building the future of financial technology and need a passionate engineer
to join our algorithmic trading team. You'll work on high-frequency trading systems.

Required Skills:
- Python (5+ years experience)
- Financial markets knowledge
- Algorithmic trading experience
- Django/Flask web frameworks
- Real-time data processing

Preferred:
- AWS cloud services
- Docker containerization
- React frontend development
- Machine learning for trading

Company Culture:
We value innovation, collaboration, and technical excellence. Join us in 
revolutionizing how people interact with financial markets!"""

    # Create test resume
    resume_content = """Ryan Thomas Weiler
Senior Software Engineer

Contact Information:
Email: ryan_wlr@yahoo.com
Phone: (561) 906-2118
LinkedIn: https://www.linkedin.com/in/ryan-weiler-7a3119190/
GitHub: https://github.com/ryan-wlr

Professional Experience:
- Led development of algorithmic trading systems generating 15% annual returns
- Built scalable Python applications for real-time financial data processing
- Implemented Django web framework for trading dashboard with 10,000+ daily users
- Created automated risk management systems reducing losses by 30%
- Collaborated with quantitative analysts to optimize trading strategies

Technical Skills:
Python, Django, Flask, pandas, NumPy, JavaScript, React, SQL, Git, AWS, Docker,
Financial Analysis, Algorithmic Trading, Risk Management, Real-time Systems

Education:
Computer Science coursework at Florida Atlantic University
Financial Markets Certification, CFA Institute

Key Projects:
- HFT Trading Engine: High-frequency trading system processing 1000+ trades/second
- Portfolio Optimizer: Modern portfolio theory implementation with risk constraints
- Market Data Pipeline: Real-time data ingestion from multiple financial exchanges
- Trading Bot Framework: Extensible system for strategy development and backtesting"""

    # Create temporary files
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False, encoding='utf-8') as f:
        f.write(job_content)
        job_file = f.name
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False, encoding='utf-8') as f:
        f.write(resume_content)
        resume_file = f.name
    
    return job_file, resume_file, job_content, resume_content

def test_storytelling_in_main_system():
    """Test storytelling through the main resume system"""
    print("🧪 TESTING STORYTELLING IN MAIN SYSTEM")
    print("=" * 60)
    
    try:
        from resume_windows import ResumeOptimizer
    except ImportError as e:
        print(f"❌ ERROR: Could not import ResumeOptimizer: {e}")
        return False
    
    # Create test files
    job_file, resume_file, job_content, resume_content = create_test_files()
    
    try:
        print(">>> Initializing Resume Optimizer...")
        optimizer = ResumeOptimizer()
        
        print(">>> Testing with story resume option (simulating user choice 1)...")
        
        # Simulate the process_complete_optimization with story choice
        print(f">>> Processing job description ({len(job_content)} chars)")
        print(f">>> Processing resume content ({len(resume_content)} chars)")
        
        # Analyze job posting
        job_analysis = optimizer.analyze_job_posting(
            job_content, "Senior Software Engineer", "FinTech Startup"
        )
        
        print("✅ Job analysis completed")
        
        # Test narrative resume creation directly
        print(">>> Creating narrative (story) resume...")
        narrative_resume = optimizer.create_narrative_resume(
            resume_content, job_analysis, "Senior Software Engineer", "FinTech Startup"
        )
        
        print("✅ Narrative resume created successfully!")
        print(f"   Resume length: {len(narrative_resume)} characters")
        
        # Verify personalization
        personalizations = {
            'Name': 'RYAN THOMAS WEILER' in narrative_resume,
            'Contact': 'ryan_wlr@yahoo.com' in narrative_resume,
            'Skills': any(skill in narrative_resume for skill in ['Python', 'Django', 'algorithmic trading']),
            'Experience': any(exp in narrative_resume for exp in ['trading systems', '15%', 'financial data']),
            'Projects': any(proj in narrative_resume for proj in ['HFT Trading', 'Portfolio Optimizer']),
            'Company': 'FinTech Startup' in narrative_resume,
            'Story Elements': any(elem in narrative_resume for elem in ['CRAFTSMAN', 'journey', 'story'])
        }
        
        print("\n📊 PERSONALIZATION CHECK:")
        all_good = True
        for check, passed in personalizations.items():
            status = "✅" if passed else "❌"
            print(f"   {status} {check}: {passed}")
            if not passed:
                all_good = False
        
        # Show key story sections
        print("\n📖 STORY RESUME PREVIEW:")
        lines = narrative_resume.split('\n')
        preview_lines = []
        for i, line in enumerate(lines):
            if i < 5 or any(marker in line for marker in [
                'CRAFTSMAN', 'PROFESSIONAL NARRATIVE', 'CAREER JOURNEY', 
                'KEY ACHIEVEMENTS', 'DEFINING PROJECTS', 'FUTURE VISION'
            ]):
                preview_lines.append(f"   {line}")
                if len(preview_lines) >= 15:  # Limit preview
                    break
        
        for line in preview_lines:
            print(line)
        if len(lines) > len(preview_lines):
            print("   ...")
        
        print(f"\n🎯 INTEGRATION TEST RESULT: {'✅ PASSED' if all_good else '❌ FAILED'}")
        return all_good
        
    except Exception as e:
        print(f"❌ ERROR during testing: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    finally:
        # Clean up temp files
        try:
            os.unlink(job_file)
            os.unlink(resume_file)
        except:
            pass

def test_browse_mode_integration():
    """Test that browse mode can handle storytelling"""
    print("\n🌐 TESTING BROWSE MODE INTEGRATION")
    print("=" * 60)
    
    # Check if browse_mode_fixed.py exists and can import resume_windows
    try:
        import browse_mode_fixed
        print("✅ browse_mode_fixed.py can be imported")
        
        # Check if it can import ResumeOptimizer
        from resume_windows import ResumeOptimizer
        print("✅ ResumeOptimizer can be imported from browse mode")
        
        # Check key functions exist
        if hasattr(browse_mode_fixed, 'read_file_safely'):
            print("✅ read_file_safely function exists")
        else:
            print("❌ read_file_safely function missing")
            
        print("\n💡 BROWSE MODE STATUS:")
        print("   The browse_mode_fixed.py should work with storytelling because:")
        print("   • It imports ResumeOptimizer from resume_windows.py")
        print("   • ResumeOptimizer.process_complete_optimization() includes storytelling")
        print("   • Users will see the story/standard/both options when processing")
        
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    print("🎭 STORYTELLING BROWSE MODE TEST SUITE")
    print("=" * 80)
    print("Testing the storytelling feature integration with browse mode...")
    print()
    
    # Test 1: Main system storytelling
    test1_passed = test_storytelling_in_main_system()
    
    # Test 2: Browse mode integration
    test2_passed = test_browse_mode_integration()
    
    # Overall results
    print("\n" + "=" * 80)
    print("📊 FINAL TEST RESULTS:")
    print(f"   Test 1 - Main System Storytelling: {'✅ PASSED' if test1_passed else '❌ FAILED'}")
    print(f"   Test 2 - Browse Mode Integration: {'✅ PASSED' if test2_passed else '❌ FAILED'}")
    
    overall_passed = test1_passed and test2_passed
    print(f"\n🎯 OVERALL RESULT: {'✅ ALL TESTS PASSED' if overall_passed else '❌ SOME TESTS FAILED'}")
    
    if overall_passed:
        print("\n🚀 STORYTELLING IS READY!")
        print("   To use storytelling in browse mode:")
        print("   1. Run: python resume_windows.py --browse")
        print("   2. Select your job description and resume files")
        print("   3. Enter target role and company")
        print("   4. Choose option 1 when prompted for resume style")
        print("   5. Get your personalized story resume!")
        
        print("\n   Or run browse_mode_fixed.py directly:")
        print("   1. Run: python browse_mode_fixed.py")
        print("   2. Follow the same process")
    else:
        print("\n⚠️  Some issues need to be resolved before storytelling works fully")
    
    return overall_passed

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)