#!/usr/bin/env python3
"""
Python Toolbox - Platform Test Suite
Tüm platformlar için test scriptleri
"""

import sys
import os
import platform
import unittest
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

class TestPlatforms(unittest.TestCase):
    """Test suite for all platforms"""
    
    def setUp(self):
        """Set up test environment"""
        self.current_platform = platform.system().lower()
        self.is_android = hasattr(sys, 'getandroidapilevel')
        self.is_railway = 'RAILWAY' in os.environ or 'DYNO' in os.environ
        
    def test_imports(self):
        """Test core imports"""
        try:
            import main
            self.assertTrue(hasattr(main, 'get_platform'))
            self.assertTrue(hasattr(main, 'launch_desktop'))
            self.assertTrue(hasattr(main, 'launch_android'))
            self.assertTrue(hasattr(main, 'launch_backend'))
        except ImportError as e:
            self.fail(f"Main module import failed: {e}")
    
    def test_tools_imports(self):
        """Test tool imports"""
        tools_to_test = [
            'tools.pdf_tools',
            'tools.qr_tools', 
            'tools.image_tools',
            'tools.convert_tools',
            'tools.system_tools',
            'tools.net_tools'
        ]
        
        for tool_module in tools_to_test:
            try:
                __import__(tool_module)
            except ImportError as e:
                self.fail(f"Tool import failed {tool_module}: {e}")
    
    def test_backend_imports(self):
        """Test backend API imports"""
        try:
            import api.main as api_main
            self.assertTrue(hasattr(api_main, 'app'))
            self.assertTrue(hasattr(api_main, 'health_check'))
        except ImportError as e:
            self.fail(f"Backend import failed: {e}")
    
    def test_desktop_imports(self):
        """Test desktop GUI imports"""
        if self.current_platform in ['windows', 'linux', 'darwin']:
            try:
                import PySide6
                from ui.main_window import MainWindow
                self.assertTrue(hasattr(MainWindow, '__init__'))
            except ImportError:
                self.skipTest("PySide6 not available on this platform")
    
    def test_mobile_imports(self):
        """Test mobile imports"""
        if self.is_android:
            try:
                import kivy
                import kivymd
                from mobile.src.main_app import PythonToolboxApp
                self.assertTrue(hasattr(PythonToolboxApp, 'build'))
            except ImportError:
                self.skipTest("Kivy/KivyMD not available on mobile")
    
    def test_license_manager(self):
        """Test license manager"""
        try:
            from components.license_manager import LicenseManager, ProFeatures
            lm = LicenseManager()
            pf = ProFeatures(lm)
            self.assertTrue(hasattr(lm, 'generate_offline_license'))
            self.assertTrue(hasattr(pf, 'check_pdf_limit'))
        except ImportError as e:
            self.fail(f"License manager import failed: {e}")
    
    def test_platform_detection(self):
        """Test platform detection"""
        from main import get_platform
        
        detected_platform = get_platform()
        self.assertIn(detected_platform, ['android', 'windows', 'linux', 'macos', 'unknown'])
        
        if self.is_android:
            self.assertEqual(detected_platform, 'android')
        elif self.current_platform == 'windows':
            self.assertEqual(detected_platform, 'windows')
        elif self.current_platform == 'linux':
            self.assertEqual(detected_platform, 'linux')
        elif self.current_platform == 'darwin':
            self.assertEqual(detected_platform, 'macos')
    
    def test_tool_functionality(self):
        """Test basic tool functionality"""
        # Test QR tools
        try:
            from tools.qr_tools import QRTools
            qr_tools = QRTools()
            self.assertTrue(hasattr(qr_tools, 'generate_qr'))
            self.assertTrue(hasattr(qr_tools, 'read_qr'))
        except ImportError:
            self.skipTest("QR tools not available")
        
        # Test system tools
        try:
            from tools.system_tools import SystemTools
            sys_tools = SystemTools()
            self.assertTrue(hasattr(sys_tools, 'generate_md5'))
            self.assertTrue(hasattr(sys_tools, 'generate_sha256'))
        except ImportError:
            self.skipTest("System tools not available")
        
        # Test net tools
        try:
            from tools.net_tools import NetTools
            net_tools = NetTools()
            self.assertTrue(hasattr(net_tools, 'test_internet_speed'))
            self.assertTrue(hasattr(net_tools, 'get_public_ip'))
        except ImportError:
            self.skipTest("Network tools not available")
    
    def test_mobile_tools(self):
        """Test mobile-specific tools"""
        try:
            from platforms.mobile_tools import (
                MobilePDFTools, MobileQRTools, MobileImageTools,
                MobileConvertTools, MobileSystemTools, MobileNetTools
            )
            
            # Test availability flags
            tools = [
                MobilePDFTools(),
                MobileQRTools(),
                MobileImageTools(),
                MobileConvertTools(),
                MobileSystemTools(),
                MobileNetTools()
            ]
            
            for tool in tools:
                self.assertIsInstance(tool.is_available, bool)
                
        except ImportError:
            self.skipTest("Mobile tools not available")

def run_tests():
    """Run all tests"""
    print("Python Toolbox Platform Test Suite")
    print("="*50)
    print(f"Platform: {platform.system()}")
    print(f"Python: {sys.version}")
    print(f"Android: {hasattr(sys, 'getandroidapilevel')}")
    print(f"Railway: {'RAILWAY' in os.environ}")
    print()
    
    # Run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestPlatforms)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Summary
    print("\n" + "="*50)
    print("TEST SUMMARY")
    print("="*50)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.failures:
        print("\nFailures:")
        for test, traceback in result.failures:
            print(f"- {test}: {traceback}")
    
    if result.errors:
        print("\nErrors:")
        for test, traceback in result.errors:
            print(f"- {test}: {traceback}")
    
    print(f"\nSuccess: {result.wasSuccessful()}")
    
    # Platform-specific recommendations
    print("\nRecommendations:")
    
    if platform.system().lower() == 'windows':
        print("- PyInstaller ile EXE build yapabilirsiniz")
        print("- Visual C++ Build Tools gereklidir")
    
    elif platform.system().lower() in ['linux', 'darwin']:
        print("- Desktop uygulamasını çalıştırabilirsiniz")
        print("- Development için ideal platform")
    
    if hasattr(sys, 'getandroidapilevel'):
        print("- Android cihazdasınız, Kivy uygulamasını çalıştırabilirsiniz")
    
    if 'RAILWAY' in os.environ or 'DYNO' in os.environ:
        print("- Railway ortamındasınız, backend modu çalışacak")
    
    return result.wasSuccessful()

if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)