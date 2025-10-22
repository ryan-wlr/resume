#!/usr/bin/env python3
"""
Main Resume Optimizer Launcher
Complete standalone version for the resume folder
"""

import os
import sys
import subprocess

def check_dependencies():
    """Check and install required dependencies"""
    print("🔧 Checking dependencies...")
    
    required_packages = ['python-docx']
    missing_packages = []
    
    for package in required_packages:
        try:
            if package == 'python-docx':
                import docx
                print(f"✅ {package}: Available")
        except ImportError:
            missing_packages.append(package)
            print(f"❌ {package}: Missing")
    
    if missing_packages:
        print("\n📦 Installing missing packages...")
        for package in missing_packages:
            try:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
                print(f"✅ Installed {package}")
            except subprocess.CalledProcessError:
                print(f"❌ Failed to install {package}")
                return False
    
    return True

def main_menu():
    """Display main menu for resume optimizer"""
    print("\n🚀 AI-POWERED RESUME OPTIMIZER")
    print("=" * 50)
    print("Complete standalone version - works for ANY profession!")
    print()
    print("📋 Choose your option:")
    print("   1. Browse Mode (Select files with dialogs)")
    print("   2. Demo Mode (Use sample files)")
    print("   3. Command Line Mode")
    print("   4. Test System")
    print("   5. View Documentation")
    print("   6. Exit")
    print()
    
    while True:
        choice = input("Select option (1-6): ").strip()
        
        if choice == '1':
            run_browse_mode()
            break
        elif choice == '2':
            run_demo_mode()
            break
        elif choice == '3':
            run_command_line_mode()
            break
        elif choice == '4':
            run_tests()
            break
        elif choice == '5':
            show_documentation()
            break
        elif choice == '6':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select 1-6.")

def run_browse_mode():
    """Run the browse mode with file dialogs"""
    print("\n🗂️  BROWSE MODE")
    print("=" * 20)
    
    if os.path.exists('browse_mode_fixed.py'):
        try:
            subprocess.run([sys.executable, 'browse_mode_fixed.py'])
        except Exception as e:
            print(f"❌ Error running browse mode: {e}")
    else:
        print("❌ browse_mode_fixed.py not found")

def run_demo_mode():
    """Run the demo with sample files"""
    print("\n🎯 DEMO MODE")
    print("=" * 15)
    
    if os.path.exists('demo_quick.py'):
        try:
            subprocess.run([sys.executable, 'demo_quick.py'])
        except Exception as e:
            print(f"❌ Error running demo: {e}")
    else:
        print("❌ demo_quick.py not found")

def run_command_line_mode():
    """Provide instructions for command line usage"""
    print("\n⌨️  COMMAND LINE MODE")
    print("=" * 25)
    print("Use the resume optimizer directly from command line:")
    print()
    print("📝 Basic Usage:")
    print('   python resume_windows.py "job description" --resume "resume content"')
    print()
    print("📁 With Files:")
    print('   python resume_windows.py job.txt --resume resume.txt --role "Brain Surgeon"')
    print()
    print("🔧 Browse Mode:")
    print('   python resume_windows.py --browse')
    print()

def run_tests():
    """Run the test suite"""
    print("\n🧪 TESTING SYSTEM")
    print("=" * 20)
    
    if os.path.exists('test_optimizer.py'):
        try:
            subprocess.run([sys.executable, 'test_optimizer.py'])
        except Exception as e:
            print(f"❌ Error running tests: {e}")
    else:
        print("❌ test_optimizer.py not found")

def show_documentation():
    """Display available documentation"""
    print("\n📚 DOCUMENTATION")
    print("=" * 20)
    
    docs = [
        ('README.md', 'Main documentation'),
        ('README_RESUME.md', 'Resume-specific guide'),
        ('README_RESUME_DOCX.md', 'DOCX formatting guide'),
        ('TROUBLESHOOTING.md', 'Common issues and solutions'),
        ('PACKAGE_SUMMARY.md', 'Package overview')
    ]
    
    print("📖 Available documentation:")
    for filename, description in docs:
        if os.path.exists(filename):
            print(f"   ✅ {filename} - {description}")
        else:
            print(f"   ❌ {filename} - Missing")
    
    print("\n💡 Quick Help:")
    print("   • The system works for ANY profession (brain surgeon, plumber, etc.)")
    print("   • Use .txt files if .docx files cause issues")
    print("   • Run demo_quick.py for a working demonstration")
    print("   • Check TROUBLESHOOTING.md for common problems")

def main():
    """Main launcher function"""
    print("🎯 RESUME OPTIMIZER LAUNCHER")
    print("Complete standalone system for ANY profession")
    print()
    
    # Check if we're in the right directory
    if not os.path.exists('resume_windows.py'):
        print("❌ Error: resume_windows.py not found!")
        print("   Make sure you're in the correct directory.")
        return
    
    # Check dependencies
    if not check_dependencies():
        print("❌ Dependency check failed. Please install required packages manually.")
        return
    
    # Show main menu
    main_menu()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()