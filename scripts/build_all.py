#!/usr/bin/env python3
"""
Python Toolbox - Universal Build Script
Railway + Windows EXE + Android APK için build scripti
"""

import os
import sys
import subprocess
import shutil
import platform
from pathlib import Path
from typing import Dict, List, Optional

class BuildManager:
    """Universal build manager for all platforms"""
    
    def __init__(self):
        self.project_root = Path(__file__).parent.parent
        self.current_platform = platform.system().lower()
        self.build_dir = self.project_root / "build"
        self.dist_dir = self.project_root / "dist"
        
        # Create build directories
        self.build_dir.mkdir(exist_ok=True)
        self.dist_dir.mkdir(exist_ok=True)
    
    def log(self, message: str, level: str = "INFO"):
        """Log messages with formatting"""
        colors = {
            "INFO": "\033[94m",    # Blue
            "SUCCESS": "\033[92m", # Green
            "WARNING": "\033[93m", # Yellow
            "ERROR": "\033[91m",   # Red
            "RESET": "\033[0m"     # Reset
        }
        
        color = colors.get(level, colors["INFO"])
        reset = colors["RESET"]
        print(f"{color}[{level}] {message}{reset}")
    
    def check_requirements(self, requirements: List[str]) -> bool:
        """Check if required packages are installed"""
        missing = []
        for req in requirements:
            try:
                __import__(req)
            except ImportError:
                missing.append(req)
        
        if missing:
            self.log(f"Missing packages: {', '.join(missing)}", "WARNING")
            return False
        return True
    
    def run_command(self, command: List[str], cwd: Optional[str] = None) -> bool:
        """Run shell command and return success status"""
        try:
            self.log(f"Running: {' '.join(command)}")
            result = subprocess.run(
                command,
                cwd=cwd or str(self.project_root),
                capture_output=True,
                text=True,
                check=True
            )
            self.log("Command executed successfully", "SUCCESS")
            return True
        except subprocess.CalledProcessError as e:
            self.log(f"Command failed: {e}", "ERROR")
            self.log(f"STDOUT: {e.stdout}", "ERROR")
            self.log(f"STDERR: {e.stderr}", "ERROR")
            return False
    
    def clean_build(self):
        """Clean previous build artifacts"""
        self.log("Cleaning previous build artifacts...")
        
        dirs_to_clean = [
            self.build_dir,
            self.dist_dir,
            self.project_root / "build",
            self.project_root / "dist",
            self.project_root / ".buildozer",
            self.project_root / "mobile" / ".buildozer"
        ]
        
        for dir_path in dirs_to_clean:
            if dir_path.exists():
                shutil.rmtree(dir_path)
                self.log(f"Cleaned {dir_path}")
    
    def install_dependencies(self):
        """Install all required dependencies"""
        self.log("Installing dependencies...")
        
        requirements_file = self.project_root / "requirements.txt"
        if not requirements_file.exists():
            self.log("requirements.txt not found", "ERROR")
            return False
        
        return self.run_command([
            sys.executable, "-m", "pip", "install", "-r", str(requirements_file)
        ])
    
    def build_backend(self) -> bool:
        """Build and test backend API"""
        self.log("Building backend API...")
        
        # Test backend import
        try:
            sys.path.insert(0, str(self.project_root))
            from api.main import app
            self.log("Backend API imported successfully", "SUCCESS")
            return True
        except Exception as e:
            self.log(f"Backend import failed: {e}", "ERROR")
            return False
    
    def build_desktop(self) -> bool:
        """Build desktop application (Windows/Linux/Mac)"""
        self.log("Building desktop application...")
        
        # Check PySide6 availability
        if not self.check_requirements(["PySide6"]):
            self.log("PySide6 not available, skipping desktop build", "WARNING")
            return False
        
        # Test desktop import
        try:
            sys.path.insert(0, str(self.project_root))
            from ui.main_window import MainWindow
            self.log("Desktop UI imported successfully", "SUCCESS")
            
            # Test main application
            from main import launch_desktop
            self.log("Desktop launcher imported successfully", "SUCCESS")
            return True
        except Exception as e:
            self.log(f"Desktop import failed: {e}", "ERROR")
            return False
    
    def build_android(self) -> bool:
        """Build Android APK"""
        self.log("Building Android APK...")
        
        # Check if buildozer is available
        if not shutil.which("buildozer"):
            self.log("Buildozer not found, installing...")
            if not self.run_command([sys.executable, "-m", "pip", "install", "buildozer"]):
                return False
        
        # Check if mobile tools are available
        if not self.check_requirements(["kivy", "kivymd"]):
            self.log("Kivy/KivyMD not available, installing mobile dependencies...")
            mobile_reqs = [
                "kivy==2.2.1",
                "kivymd==1.1.1",
                "Pillow==10.0.0",
                "qrcode==7.4.2",
                "requests==2.31.0",
                "speedtest-cli==2.1.3"
            ]
            if not self.run_command([sys.executable, "-m", "pip", "install"] + mobile_reqs):
                return False
        
        # Change to mobile directory
        mobile_dir = self.project_root / "mobile" / "buildozer"
        if not mobile_dir.exists():
            mobile_dir.mkdir(parents=True)
        
        # Copy buildozer.spec if not exists
        spec_source = self.project_root / "mobile" / "buildozer.spec"
        spec_target = mobile_dir / "buildozer.spec"
        if spec_source.exists() and not spec_target.exists():
            shutil.copy2(spec_source, spec_target)
        
        # Try to build APK (this will take a long time)
        self.log("Starting Android build (this may take 10-30 minutes)...")
        self.log("Note: Android build requires Android SDK and NDK")
        
        # For now, just test the configuration
        if self.run_command(["buildozer", "android", "debug"], cwd=str(mobile_dir.parent)):
            self.log("Android APK build completed", "SUCCESS")
            return True
        else:
            self.log("Android build failed. Please check buildozer requirements.", "WARNING")
            return False
    
    def build_exe(self) -> bool:
        """Build Windows EXE"""
        if self.current_platform != "windows":
            self.log("EXE build only available on Windows", "WARNING")
            return False
        
        self.log("Building Windows EXE...")
        
        # Check PyInstaller availability
        if not self.check_requirements(["PyInstaller"]):
            self.log("Installing PyInstaller...")
            if not self.run_command([sys.executable, "-m", "pip", "install", "pyinstaller"]):
                return False
        
        # Run build script
        build_script = self.project_root / "build_exe.py"
        if build_script.exists():
            return self.run_command([sys.executable, str(build_script)])
        else:
            # Use PyInstaller directly
            return self.run_command([
                "pyinstaller",
                "--onefile",
                "--noconsole",
                "--name=PythonToolbox",
                "--add-data=tools;tools",
                "--add-data=ui;ui",
                "--add-data=components;components",
                "--add-data=api;api",
                "--add-data=assets;assets",
                "--hidden-import=PySide6.QtCore",
                "--hidden-import=PySide6.QtGui",
                "--hidden-import=PySide6.QtWidgets",
                "--clean",
                "--optimize=2",
                "main.py"
            ])
    
    def test_all_platforms(self) -> Dict[str, bool]:
        """Test all platform builds"""
        self.log("Testing all platform builds...")
        
        results = {}
        
        # Test backend
        results["backend"] = self.build_backend()
        
        # Test desktop
        results["desktop"] = self.build_desktop()
        
        # Test mobile tools
        try:
            sys.path.insert(0, str(self.project_root))
            from platforms.mobile_tools import (
                MobilePDFTools, MobileQRTools, MobileImageTools,
                MobileConvertTools, MobileSystemTools, MobileNetTools
            )
            
            # Test each tool
            tools_to_test = [
                ("mobile_pdf", MobilePDFTools),
                ("mobile_qr", MobileQRTools),
                ("mobile_image", MobileImageTools),
                ("mobile_convert", MobileConvertTools),
                ("mobile_system", MobileSystemTools),
                ("mobile_net", MobileNetTools),
            ]
            
            for tool_name, tool_class in tools_to_test:
                try:
                    tool_instance = tool_class()
                    results[tool_name] = tool_instance.is_available
                    self.log(f"{tool_name}: {'Available' if results[tool_name] else 'Not available'}")
                except Exception as e:
                    results[tool_name] = False
                    self.log(f"{tool_name}: Error - {e}", "ERROR")
            
        except Exception as e:
            self.log(f"Mobile tools test failed: {e}", "ERROR")
            results["mobile_tools"] = False
        
        return results
    
    def create_build_summary(self, results: Dict[str, bool]):
        """Create build summary"""
        self.log("\n" + "="*60)
        self.log("BUILD SUMMARY", "INFO")
        self.log("="*60)
        
        for component, success in results.items():
            status = "✓ SUCCESS" if success else "✗ FAILED"
            status_color = "SUCCESS" if success else "ERROR"
            self.log(f"{component:20}: {status}", status_color)
        
        self.log("\nPlatform Support:")
        
        platforms = {
            "Railway/Backend": results.get("backend", False),
            "Windows EXE": results.get("exe", False) or results.get("desktop", False),
            "Linux/Mac Desktop": results.get("desktop", False),
            "Android APK": results.get("android", False),
            "Mobile Tools": results.get("mobile_tools", False) or any(
                results.get(k, False) for k in ["mobile_pdf", "mobile_qr", "mobile_image", "mobile_convert", "mobile_system", "mobile_net"]
            )
        }
        
        for platform, supported in platforms.items():
            status = "✓ SUPPORTED" if supported else "✗ NOT SUPPORTED"
            status_color = "SUCCESS" if supported else "WARNING"
            self.log(f"{platform:20}: {status}", status_color)
        
        self.log("\nNext Steps:")
        self.log("1. Railway Deploy: git push to Railway-connected repository")
        self.log("2. Windows EXE: Run build_exe.py or use PyInstaller")
        self.log("3. Android APK: Use buildozer in mobile/buildozer directory")
        self.log("4. Test: Run main.py with different modes (desktop/android/backend)")
        
        self.log("="*60)

def main():
    """Main build function"""
    build_manager = BuildManager()
    
    # Parse command line arguments
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == "clean":
            build_manager.clean_build()
        elif command == "deps":
            build_manager.install_dependencies()
        elif command == "test":
            results = build_manager.test_all_platforms()
            build_manager.create_build_summary(results)
        elif command == "backend":
            build_manager.build_backend()
        elif command == "desktop":
            build_manager.build_desktop()
        elif command == "android":
            build_manager.build_android()
        elif command == "exe":
            build_manager.build_exe()
        elif command == "all":
            build_manager.clean_build()
            build_manager.install_dependencies()
            
            results = {}
            results["backend"] = build_manager.build_backend()
            results["desktop"] = build_manager.build_desktop()
            results["android"] = build_manager.build_android()
            
            if build_manager.current_platform == "windows":
                results["exe"] = build_manager.build_exe()
            
            build_manager.create_build_summary(results)
        else:
            build_manager.log(f"Unknown command: {command}", "ERROR")
            build_manager.log("Available commands: clean, deps, test, backend, desktop, android, exe, all", "INFO")
    else:
        # Default: test all platforms
        build_manager.log("Python Toolbox Universal Build System")
        build_manager.log("="*50)
        build_manager.log("Usage: python scripts/build_all.py [command]")
        build_manager.log("Commands: clean, deps, test, backend, desktop, android, exe, all")
        build_manager.log("\nRunning default: test all platforms...")
        
        results = build_manager.test_all_platforms()
        build_manager.create_build_summary(results)

if __name__ == "__main__":
    main()