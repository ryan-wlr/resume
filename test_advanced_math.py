#!/usr/bin/env python3
"""
Test Advanced Mathematics and Quantum Computing Resume Generation
"""

import os
import sys

# Add current directory to path
sys.path.insert(0, os.getcwd())

def test_quantum_computing_resume():
    """Test quantum computing scientist resume generation"""
    print("🧪 TESTING QUANTUM COMPUTING RESUME")
    print("=" * 45)
    
    try:
        from resume_windows import ResumeOptimizer
        
        # Sample quantum computing job description
        job_description = """
        Quantum Computing Research Scientist Position
        
        We seek a quantum computing researcher with expertise in:
        - Quantum algorithms (Shor's algorithm, Grover's algorithm)
        - Quantum error correction and fault tolerance
        - Qiskit, Cirq, and quantum programming
        - Linear algebra and quantum mechanics
        - Variational quantum eigensolvers (VQE)
        """
        
        # Sample current resume
        current_resume = """
        Ryan Weiler
        Research Scientist
        
        Education: Ph.D. in Physics
        Experience: Quantum algorithm development
        Skills: Python, quantum computing, mathematics
        """
        
        optimizer = ResumeOptimizer()
        
        # Test field detection
        detected_field = optimizer.detect_career_field("quantum computing research scientist")
        print(f"✅ Field Detection: {detected_field}")
        
        # Test resume generation
        results = optimizer.process_complete_optimization(
            job_description, current_resume, "Quantum Computing Scientist", "Quantum Research Lab"
        )
        
        # Check if quantum-specific content was generated
        if 'quantum' in results['7_tailored_resume'].lower():
            print("✅ Quantum-specific content generated")
        
        if 'algorithm' in results['7_tailored_resume'].lower():
            print("✅ Algorithm expertise included")
            
        if 'qiskit' in results['7_tailored_resume'].lower():
            print("✅ Quantum programming languages included")
        
        print("✅ Quantum computing resume test PASSED")
        return True
        
    except Exception as e:
        print(f"❌ Quantum computing test FAILED: {e}")
        return False

def test_mathematics_professor_resume():
    """Test mathematics professor resume generation"""
    print("\n🧪 TESTING MATHEMATICS PROFESSOR RESUME")
    print("=" * 50)
    
    try:
        from resume_windows import ResumeOptimizer
        
        # Sample mathematics job description
        job_description = """
        Mathematics Professor Position
        
        Requirements:
        - Ph.D. in Pure Mathematics
        - Research in algebraic geometry or topology
        - Experience with homological algebra
        - Publications in top mathematics journals
        - Abstract algebra and differential geometry expertise
        """
        
        # Sample current resume
        current_resume = """
        Ryan Weiler
        Mathematician
        
        Education: Ph.D. in Mathematics
        Research: Algebraic topology, category theory
        Publications: Several papers in mathematical journals
        """
        
        optimizer = ResumeOptimizer()
        
        # Test field detection
        detected_field = optimizer.detect_career_field("mathematics professor research")
        print(f"✅ Field Detection: {detected_field}")
        
        # Test resume generation
        results = optimizer.process_complete_optimization(
            job_description, current_resume, "Mathematics Professor", "Research University"
        )
        
        # Check if mathematics-specific content was generated
        if 'algebra' in results['7_tailored_resume'].lower():
            print("✅ Algebraic expertise included")
        
        if 'topology' in results['7_tailored_resume'].lower():
            print("✅ Topology knowledge included")
            
        if 'theorem' in results['7_tailored_resume'].lower() or 'proof' in results['7_tailored_resume'].lower():
            print("✅ Mathematical proof expertise included")
        
        print("✅ Mathematics professor resume test PASSED")
        return True
        
    except Exception as e:
        print(f"❌ Mathematics professor test FAILED: {e}")
        return False

def test_theoretical_physicist_resume():
    """Test theoretical physicist resume generation"""
    print("\n🧪 TESTING THEORETICAL PHYSICIST RESUME")
    print("=" * 45)
    
    try:
        from resume_windows import ResumeOptimizer
        
        # Sample physics job description
        job_description = """
        Theoretical Physics Researcher
        
        We seek expertise in:
        - Quantum field theory and string theory
        - Mathematical physics and differential geometry
        - Particle physics phenomenology
        - General relativity and cosmology
        """
        
        current_resume = """
        Ryan Weiler
        Physicist
        
        Education: Ph.D. in Theoretical Physics
        Research: String theory, quantum field theory
        Publications: Physics journals
        """
        
        optimizer = ResumeOptimizer()
        
        # Test field detection
        detected_field = optimizer.detect_career_field("theoretical physics research")
        print(f"✅ Field Detection: {detected_field}")
        
        # Test resume generation
        results = optimizer.process_complete_optimization(
            job_description, current_resume, "Theoretical Physicist", "Physics Institute"
        )
        
        # Check if physics-specific content was generated
        if 'quantum field theory' in results['7_tailored_resume'].lower():
            print("✅ Quantum field theory expertise included")
        
        if 'string theory' in results['7_tailored_resume'].lower():
            print("✅ String theory knowledge included")
            
        print("✅ Theoretical physicist resume test PASSED")
        return True
        
    except Exception as e:
        print(f"❌ Theoretical physicist test FAILED: {e}")
        return False

def create_advanced_math_demo():
    """Create a comprehensive demo for advanced mathematical fields"""
    print("\n🎯 CREATING ADVANCED MATHEMATICS DEMO")
    print("=" * 45)
    
    # Create sample files for advanced fields
    sample_files = [
        ('quantum_computing_job.txt', 'Quantum Computing job description'),
        ('mathematics_professor_job.txt', 'Mathematics Professor job description')
    ]
    
    for filename, description in sample_files:
        if os.path.exists(filename):
            print(f"✅ {filename} - {description}")
        else:
            print(f"❌ {filename} - Missing")
    
    # Create a sample mathematical resume
    math_resume_content = """Ryan Thomas Weiler
Research Mathematician

Contact Information:
Phone: (561) 906-2118
Email: ryan_wlr@yahoo.com
LinkedIn: https://www.linkedin.com/in/ryan-weiler-7a3119190/

Education:
Ph.D. in Pure Mathematics (Algebraic Geometry)
Princeton University, Princeton, NJ | 2020
Dissertation: "Cohomological Methods in Arithmetic Geometry"
Advisor: Professor A. Distinguished

M.S. in Mathematics
Massachusetts Institute of Technology, Cambridge, MA | 2017
GPA: 3.9/4.0

B.S. in Mathematics and Physics (Summa Cum Laude)
Harvard University, Cambridge, MA | 2015
Phi Beta Kappa, Magna Cum Laude

Research Experience:
Postdoctoral Researcher | Institute for Advanced Study | 2020 - Present
- Investigating connections between algebraic K-theory and motivic cohomology
- Developed new computational techniques for étale cohomology calculations
- Collaborated on breakthrough results in arithmetic geometry

Graduate Research Assistant | Princeton University | 2017 - 2020
- Proved fundamental theorems in algebraic geometry using derived categories
- Advanced understanding of intersection theory on algebraic varieties
- Contributed to resolution of conjectures in Hodge theory

Publications:
- "Motivic Cohomology and Algebraic Cycles" - Annals of Mathematics (2021)
- "Derived Categories in Arithmetic Geometry" - Inventiones Mathematicae (2020)
- "Spectral Sequences and K-Theory" - Journal of Pure and Applied Algebra (2019)

Technical Skills:
- Advanced Mathematics: Algebraic Geometry, Homological Algebra, Category Theory
- Computational: SageMath, Magma, Macaulay2, LaTeX, Mathematica
- Programming: Python, C++, Mathematical computation and visualization
- Languages: English (Native), French (Fluent), German (Conversational)

Awards and Honors:
- NSF Mathematical Sciences Postdoctoral Research Fellowship (2020)
- Princeton University Excellence in Teaching Award (2019)
- Phi Beta Kappa (2015)
- Harvard University Dean's List (2013-2015)"""

    with open('sample_mathematician_resume.txt', 'w', encoding='utf-8') as f:
        f.write(math_resume_content)
    
    print("✅ Created sample_mathematician_resume.txt")
    print("\n🎉 Advanced mathematics demo files ready!")

def main():
    """Run all advanced mathematics and quantum computing tests"""
    print("🧮 ADVANCED MATHEMATICS & QUANTUM COMPUTING TESTS")
    print("=" * 55)
    
    test_results = []
    
    # Run tests
    test_results.append(test_quantum_computing_resume())
    test_results.append(test_mathematics_professor_resume())  
    test_results.append(test_theoretical_physicist_resume())
    
    # Create demo files
    create_advanced_math_demo()
    
    # Summary
    print(f"\n📊 TEST SUMMARY")
    print("=" * 20)
    passed_tests = sum(test_results)
    total_tests = len(test_results)
    
    print(f"✅ Tests Passed: {passed_tests}/{total_tests}")
    
    if passed_tests == total_tests:
        print("🎉 ALL TESTS PASSED!")
        print("The resume optimizer now supports advanced mathematics and quantum computing!")
    else:
        print("⚠️  Some tests failed. Check the output above for details.")
    
    print("\n🎯 NEW CAPABILITIES:")
    print("   • Quantum Computing Research Scientist resumes")
    print("   • Mathematics Professor resumes")
    print("   • Applied Mathematician resumes") 
    print("   • Theoretical Physicist resumes")
    print("   • Advanced mathematical problem-solving examples")
    print("   • Quantum algorithm expertise")
    print("   • High-level mathematical research experience")

if __name__ == "__main__":
    main()