@echo off
REM Quick launch script for Resume Optimizer (Windows)

echo 🚀 AI-POWERED RESUME OPTIMIZER
echo ================================
echo.
echo 🔧 Checking dependencies...

REM Check if python-docx is installed
python -c "import docx" 2>nul
if %errorlevel% neq 0 (
    echo ❌ python-docx not found. Installing...
    pip install python-docx
    echo ✅ Dependencies installed!
) else (
    echo ✅ Dependencies OK!
)

echo.
echo 🚀 Starting Resume Optimizer...
echo    You can optimize resumes for ANY career field:
echo    • Brain Surgeon, Marine Biologist, Astrophysicist  
echo    • Software Engineer, Mechanical Engineer
echo    • Chef, Teacher, Lawyer, Accountant
echo    • And literally ANY other profession!
echo.

python browse_mode_fixed.py
pause