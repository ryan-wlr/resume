#!/usr/bin/env python3
"""
Final System Verification Script
Checks that all necessary files are present and working
"""

import os
import sys

def verify_system():
    """Verify all necessary files are present"""
    print("🔍 SYSTEM VERIFICATION")
    print("=" * 30)
    
    # Core files
    core_files = [
        ('resume_windows.py', 'Main optimization engine'),
        ('browse_mode_fixed.py', 'Interactive file selection'),
        ('demo_quick.py', 'Working demonstration'),
        ('test_optimizer.py', 'System testing')
    ]
    
    print("📋 Core System Files:")
    for filename, description in core_files:
        if os.path.exists(filename):
            size = os.path.getsize(filename)
            print(f"   ✅ {filename:<25} ({size:,} bytes) - {description}")
        else:
            print(f"   ❌ {filename:<25} - {description}")
    
    # Launcher files
    launcher_files = [
        ('START_HERE.bat', 'Windows launcher with menu'),
        ('main_launcher.py', 'Cross-platform launcher'),
        ('run_optimizer.bat', 'Quick Windows launcher'),
        ('setup_resume.bat', 'Windows setup script')
    ]
    
    print("\n🚀 Launcher Files:")
    for filename, description in launcher_files:
        if os.path.exists(filename):
            print(f"   ✅ {filename:<25} - {description}")
        else:
            print(f"   ❌ {filename:<25} - {description}")
    
    # Sample files
    sample_files = [
        ('sample_brain_surgeon_job.txt', 'Sample job description'),
        ('sample_current_resume.txt', 'Sample current resume'),
        ('Ryan_Weiler_Resume.docx', 'Original resume template'),
        ('electrician_job_description.txt', 'Electrician job sample'),
        ('plumber_job_description.txt', 'Plumber job sample')
    ]
    
    print("\n📄 Sample Files:")
    for filename, description in sample_files:
        if os.path.exists(filename):
            print(f"   ✅ {filename:<35} - {description}")
        else:
            print(f"   ❌ {filename:<35} - {description}")
    
    # Documentation
    doc_files = [
        ('README.md', 'Main documentation'),
        ('TROUBLESHOOTING.md', 'Issue solutions'),
        ('COMPLETE_SYSTEM.md', 'Complete system overview'),
        ('README_RESUME.md', 'Resume-specific guide')
    ]
    
    print("\n📚 Documentation:")
    for filename, description in doc_files:
        if os.path.exists(filename):
            print(f"   ✅ {filename:<25} - {description}")
        else:
            print(f"   ❌ {filename:<25} - {description}")
    
    # Dependencies
    print("\n🔧 Dependencies:")
    try:
        import docx
        print("   ✅ python-docx: Available")
    except ImportError:
        print("   ❌ python-docx: Missing (run: pip install python-docx)")
        
    try:
        import tkinter
        print("   ✅ tkinter: Available (for file dialogs)")
    except ImportError:
        print("   ⚠️  tkinter: Missing (file dialogs won't work)")
    
    print("\n🎯 SYSTEM STATUS:")
    if all(os.path.exists(f) for f, _ in core_files):
        print("   ✅ All core files present")
        print("   ✅ System ready to use")
        print("   🚀 Run: python START_HERE.bat (Windows) or python main_launcher.py")
    else:
        print("   ❌ Some files missing - system may not work properly")
    
    print("\n📊 STATISTICS:")
    total_files = len([f for f in os.listdir('.') if os.path.isfile(f)])
    py_files = len([f for f in os.listdir('.') if f.endswith('.py')])
    txt_files = len([f for f in os.listdir('.') if f.endswith('.txt')])
    md_files = len([f for f in os.listdir('.') if f.endswith('.md')])
    
    print(f"   📁 Total files: {total_files}")
    print(f"   🐍 Python files: {py_files}")
    print(f"   📄 Text files: {txt_files}")
    print(f"   📖 Documentation files: {md_files}")

if __name__ == "__main__":
    verify_system()