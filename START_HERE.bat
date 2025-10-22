@echo off
REM Complete Resume Optimizer Launcher for Windows
REM This script provides a complete menu system for the resume optimizer

title AI Resume Optimizer - Complete System

echo.
echo ========================================
echo    AI-POWERED RESUME OPTIMIZER
echo ========================================
echo Complete system for ANY profession!
echo.
echo 🔧 Checking system...

REM Check if Python is available
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python not found! Please install Python 3.6+ first.
    pause
    exit /b 1
)

REM Check if we're in the right directory
if not exist "resume_windows.py" (
    echo ❌ Error: resume_windows.py not found!
    echo    Make sure you're running this from the resume folder.
    pause
    exit /b 1
)

echo ✅ Python found
echo ✅ Resume optimizer files found

REM Check and install dependencies
echo.
echo 📦 Checking dependencies...
python -c "import docx" 2>nul
if %errorlevel% neq 0 (
    echo 📥 Installing python-docx...
    pip install python-docx
    if %errorlevel% neq 0 (
        echo ❌ Failed to install python-docx
        echo    Please run: pip install python-docx
        pause
        exit /b 1
    )
    echo ✅ python-docx installed successfully!
) else (
    echo ✅ python-docx already available
)

:menu
echo.
echo ==========================================
echo           MAIN MENU
echo ==========================================
echo.
echo Choose your option:
echo.
echo   1. 🗂️  Browse Mode (Select files with dialogs)
echo   2. 🎯 Demo Mode (Use sample files - works immediately)
echo   3. ⌨️  Manual Mode (Enter text directly)
echo   4. 🧪 Test System (Verify everything works)
echo   5. 📚 Help and Documentation
echo   6. 🚪 Exit
echo.
set /p choice="Enter your choice (1-6): "

if "%choice%"=="1" goto browse_mode
if "%choice%"=="2" goto demo_mode
if "%choice%"=="3" goto manual_mode
if "%choice%"=="4" goto test_mode
if "%choice%"=="5" goto help_mode
if "%choice%"=="6" goto exit_program

echo ❌ Invalid choice. Please select 1-6.
goto menu

:browse_mode
echo.
echo 🗂️ Starting Browse Mode...
echo This will open file dialogs to select your files.
echo.
pause
python browse_mode_fixed.py
goto menu

:demo_mode
echo.
echo 🎯 Starting Demo Mode...
echo This uses sample files and works immediately!
echo.
pause
python demo_quick.py
goto menu

:manual_mode
echo.
echo ⌨️ Manual Mode - Direct Python usage
echo.
echo Examples:
echo   python resume_windows.py --browse
echo   python resume_windows.py "job description" --resume "resume text"
echo.
echo Press Enter to start interactive mode...
pause
python resume_windows.py --browse
goto menu

:test_mode
echo.
echo 🧪 Running System Tests...
echo.
python test_optimizer.py
echo.
echo Test completed. Press any key to return to menu...
pause
goto menu

:help_mode
echo.
echo 📚 HELP AND DOCUMENTATION
echo ==========================
echo.
echo 📖 Available Files:
if exist "README.md" echo   ✅ README.md - Main documentation
if exist "TROUBLESHOOTING.md" echo   ✅ TROUBLESHOOTING.md - Common issues and solutions
if exist "README_RESUME.md" echo   ✅ README_RESUME.md - Resume-specific guide
echo.
echo 💡 Quick Tips:
echo   • This system works for ANY profession (brain surgeon, plumber, engineer, etc.)
echo   • If you have DOCX file issues, save as .txt instead
echo   • Demo mode always works and shows the full system
echo   • Browse mode uses file dialogs to select your files
echo.
echo 🔧 Common Solutions:
echo   • DOCX errors: Save your Word files as .txt files instead
echo   • File not found: Make sure files are on your local drive, not OneDrive
echo   • Permission errors: Copy files to Desktop first
echo.
pause
goto menu

:exit_program
echo.
echo 👋 Thank you for using the AI Resume Optimizer!
echo    Your optimized resumes are saved in timestamped folders.
echo.
pause
exit /b 0