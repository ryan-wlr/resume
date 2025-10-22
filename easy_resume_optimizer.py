#!/usr/bin/env python3
"""
Easy Resume Optimizer - Simple Menu Interface
"""

import os
import sys
import subprocess

def main():
    print("=" * 50)
    print("    AI RESUME OPTIMIZER - EASY MODE")
    print("=" * 50)
    print()
    print("Available options:")
    print("1. Generate PLUMBER resume")
    print("2. Generate ELECTRICIAN resume") 
    print("3. Use browse mode (select your own files)")
    print("4. Enter custom file names")
    print()
    
    while True:
        try:
            choice = input("Choose option (1-4): ").strip()
            
            if choice == "1":
                print("\n🔧 Running PLUMBER resume optimizer...")
                cmd = [
                    sys.executable, "resume_windows.py", 
                    "plumber_job_description.txt", 
                    "--resume", "ryan_plumber_resume.txt",
                    "--role", "Plumber",
                    "--company", "Local Plumbing Services"
                ]
                subprocess.run(cmd)
                break
                
            elif choice == "2":
                print("\n⚡ Running ELECTRICIAN resume optimizer...")
                cmd = [
                    sys.executable, "resume_windows.py",
                    "electrician_job_description.txt",
                    "--resume", "ryan_electrician_resume.txt", 
                    "--role", "Industrial Electrician",
                    "--company", "M.E.P. Services"
                ]
                subprocess.run(cmd)
                break
                
            elif choice == "3":
                print("\n📁 Opening browse mode...")
                cmd = [sys.executable, "resume_windows.py", "--browse"]
                subprocess.run(cmd)
                break
                
            elif choice == "4":
                print("\n📝 Custom file mode...")
                job_file = input("Enter job description file name: ").strip()
                resume_file = input("Enter resume file name: ").strip()
                role = input("Enter target role (e.g., Plumber): ").strip()
                company = input("Enter company name: ").strip()
                
                if job_file and resume_file and role:
                    cmd = [
                        sys.executable, "resume_windows.py",
                        job_file, "--resume", resume_file,
                        "--role", role, "--company", company or "Target Company"
                    ]
                    subprocess.run(cmd)
                else:
                    print("❌ Missing required information!")
                    continue
                break
                
            else:
                print("❌ Please choose 1, 2, 3, or 4")
                continue
                
        except KeyboardInterrupt:
            print("\n\nExiting...")
            break
        except Exception as e:
            print(f"❌ Error: {e}")
            break
    
    print("\n✅ Done!")

if __name__ == "__main__":
    main()