"""
Mobile-Compatible Tool Classes
Android/iOS için optimize edilmiş araçlar
"""

import os
import tempfile
from typing import List, Dict, Optional

class MobilePDFTools:
    """Mobile-compatible PDF tools"""
    
    def __init__(self):
        self.is_available = self._check_availability()
    
    def _check_availability(self) -> bool:
        """Check if PDF tools are available on mobile"""
        try:
            import fitz
            return True
        except ImportError:
            return False
    
    def merge_pdfs(self, pdf_files: List[str], output_path: str) -> str:
        """Merge PDF files (mobile-optimized)"""
        if not self.is_available:
            raise NotImplementedError("PDF tools not available on mobile")
        
        try:
            from tools.pdf_tools import PDFTools
            desktop_tools = PDFTools()
            return desktop_tools.merge_pdfs(pdf_files, output_path)
        except Exception as e:
            raise Exception(f"PDF merge failed: {e}")
    
    def split_pdf(self, pdf_file: str, output_dir: str, split_type: str = "pages") -> List[str]:
        """Split PDF file (mobile-optimized)"""
        if not self.is_available:
            raise NotImplementedError("PDF tools not available on mobile")
        
        try:
            from tools.pdf_tools import PDFTools
            desktop_tools = PDFTools()
            return desktop_tools.split_pdf(pdf_file, output_dir, split_type)
        except Exception as e:
            raise Exception(f"PDF split failed: {e}")
    
    def pdf_to_jpg(self, pdf_file: str, output_dir: str, dpi: int = 150) -> List[str]:
        """Convert PDF to JPG (mobile-optimized with lower DPI)"""
        if not self.is_available:
            raise NotImplementedError("PDF tools not available on mobile")
        
        try:
            from tools.pdf_tools import PDFTools
            desktop_tools = PDFTools()
            return desktop_tools.pdf_to_jpg(pdf_file, output_dir, dpi)
        except Exception as e:
            raise Exception(f"PDF to JPG failed: {e}")
    
    def jpg_to_pdf(self, image_files: List[str], output_path: str) -> str:
        """Convert JPG to PDF (mobile-optimized)"""
        if not self.is_available:
            raise NotImplementedError("PDF tools not available on mobile")
        
        try:
            from tools.pdf_tools import PDFTools
            desktop_tools = PDFTools()
            return desktop_tools.jpg_to_pdf(image_files, output_path)
        except Exception as e:
            raise Exception(f"JPG to PDF failed: {e}")

class MobileQRTools:
    """Mobile-compatible QR tools"""
    
    def __init__(self):
        self.is_available = self._check_availability()
    
    def _check_availability(self) -> bool:
        """Check if QR tools are available on mobile"""
        try:
            import qrcode
            import pyzbar
            return True
        except ImportError:
            return False
    
    def generate_qr(self, data: str, output_path: str, **kwargs) -> str:
        """Generate QR code (mobile-optimized)"""
        if not self.is_available:
            raise NotImplementedError("QR tools not available on mobile")
        
        try:
            from tools.qr_tools import QRTools
            desktop_tools = QRTools()
            return desktop_tools.generate_qr(data, output_path, **kwargs)
        except Exception as e:
            raise Exception(f"QR generation failed: {e}")
    
    def generate_wifi_qr(self, ssid: str, password: str, security_type: str = "WPA", output_path: str = "wifi_qr.png") -> str:
        """Generate WiFi QR code (mobile-optimized)"""
        if not self.is_available:
            raise NotImplementedError("QR tools not available on mobile")
        
        try:
            from tools.qr_tools import QRTools
            desktop_tools = QRTools()
            return desktop_tools.generate_wifi_qr(ssid, password, security_type, output_path)
        except Exception as e:
            raise Exception(f"WiFi QR generation failed: {e}")
    
    def read_qr(self, image_path: str) -> List[Dict]:
        """Read QR code from image (mobile-optimized)"""
        if not self.is_available:
            raise NotImplementedError("QR tools not available on mobile")
        
        try:
            from tools.qr_tools import QRTools
            desktop_tools = QRTools()
            return desktop_tools.read_qr(image_path)
        except Exception as e:
            raise Exception(f"QR reading failed: {e}")
    
    def generate_barcode(self, data: str, barcode_type: str = "code128", output_path: str = "barcode.png") -> str:
        """Generate barcode (mobile-optimized)"""
        if not self.is_available:
            raise NotImplementedError("QR tools not available on mobile")
        
        try:
            from tools.qr_tools import QRTools
            desktop_tools = QRTools()
            return desktop_tools.generate_barcode(data, barcode_type, output_path)
        except Exception as e:
            raise Exception(f"Barcode generation failed: {e}")

class MobileImageTools:
    """Mobile-compatible image tools"""
    
    def __init__(self):
        self.is_available = self._check_availability()
    
    def _check_availability(self) -> bool:
        """Check if image tools are available on mobile"""
        try:
            from PIL import Image
            return True
        except ImportError:
            return False
    
    def convert_image(self, input_path: str, output_path: str, output_format: str) -> str:
        """Convert image format (mobile-optimized)"""
        if not self.is_available:
            raise NotImplementedError("Image tools not available on mobile")
        
        try:
            from tools.image_tools import ImageTools
            desktop_tools = ImageTools()
            return desktop_tools.convert_image(input_path, output_path, output_format)
        except Exception as e:
            raise Exception(f"Image conversion failed: {e}")
    
    def resize_image(self, input_path: str, output_path: str, size: tuple, maintain_aspect: bool = True) -> str:
        """Resize image (mobile-optimized)"""
        if not self.is_available:
            raise NotImplementedError("Image tools not available on mobile")
        
        try:
            from tools.image_tools import ImageTools
            desktop_tools = ImageTools()
            return desktop_tools.resize_image(input_path, output_path, size, maintain_aspect)
        except Exception as e:
            raise Exception(f"Image resize failed: {e}")
    
    def add_text_watermark(self, input_path: str, output_path: str, text: str, **kwargs) -> str:
        """Add text watermark (mobile-optimized)"""
        if not self.is_available:
            raise NotImplementedError("Image tools not available on mobile")
        
        try:
            from tools.image_tools import ImageTools
            desktop_tools = ImageTools()
            return desktop_tools.add_text_watermark(input_path, output_path, text, **kwargs)
        except Exception as e:
            raise Exception(f"Text watermark failed: {e}")
    
    def optimize_image(self, input_path: str, output_path: str, quality: int = 85) -> str:
        """Optimize image (mobile-optimized with lower quality for performance)"""
        if not self.is_available:
            raise NotImplementedError("Image tools not available on mobile")
        
        try:
            from tools.image_tools import ImageTools
            desktop_tools = ImageTools()
            return desktop_tools.optimize_image(input_path, output_path, quality)
        except Exception as e:
            raise Exception(f"Image optimization failed: {e}")
    
    def get_image_info(self, image_path: str) -> dict:
        """Get image information (mobile-optimized)"""
        if not self.is_available:
            raise NotImplementedError("Image tools not available on mobile")
        
        try:
            from tools.image_tools import ImageTools
            desktop_tools = ImageTools()
            return desktop_tools.get_image_info(image_path)
        except Exception as e:
            raise Exception(f"Get image info failed: {e}")

class MobileConvertTools:
    """Mobile-compatible conversion tools"""
    
    def __init__(self):
        self.is_available = self._check_availability()
    
    def _check_availability(self) -> bool:
        """Check if conversion tools are available on mobile"""
        try:
            import pandas
            return True
        except ImportError:
            return False
    
    def excel_to_json(self, excel_file: str, output_path: Optional[str] = None) -> str:
        """Convert Excel to JSON (mobile-optimized)"""
        if not self.is_available:
            raise NotImplementedError("Conversion tools not available on mobile")
        
        try:
            from tools.convert_tools import ConvertTools
            desktop_tools = ConvertTools()
            return desktop_tools.excel_to_json(excel_file, output_path)
        except Exception as e:
            raise Exception(f"Excel to JSON conversion failed: {e}")
    
    def json_to_excel(self, json_file: str, output_path: str) -> str:
        """Convert JSON to Excel (mobile-optimized)"""
        if not self.is_available:
            raise NotImplementedError("Conversion tools not available on mobile")
        
        try:
            from tools.convert_tools import ConvertTools
            desktop_tools = ConvertTools()
            return desktop_tools.json_to_excel(json_file, output_path)
        except Exception as e:
            raise Exception(f"JSON to Excel conversion failed: {e}")
    
    def csv_to_excel(self, csv_file: str, output_path: str) -> str:
        """Convert CSV to Excel (mobile-optimized)"""
        if not self.is_available:
            raise NotImplementedError("Conversion tools not available on mobile")
        
        try:
            from tools.convert_tools import ConvertTools
            desktop_tools = ConvertTools()
            return desktop_tools.csv_to_excel(csv_file, output_path)
        except Exception as e:
            raise Exception(f"CSV to Excel conversion failed: {e}")
    
    def txt_to_pdf(self, txt_file: str, output_path: str) -> str:
        """Convert TXT to PDF (mobile-optimized)"""
        if not self.is_available:
            raise NotImplementedError("Conversion tools not available on mobile")
        
        try:
            from tools.convert_tools import ConvertTools
            desktop_tools = ConvertTools()
            return desktop_tools.txt_to_pdf(txt_file, output_path)
        except Exception as e:
            raise Exception(f"TXT to PDF conversion failed: {e}")

class MobileSystemTools:
    """Mobile-compatible system tools"""
    
    def __init__(self):
        self.is_available = self._check_availability()
    
    def _check_availability(self) -> bool:
        """Check if system tools are available on mobile"""
        try:
            import hashlib
            return True
        except ImportError:
            return False
    
    def generate_md5(self, file_path: str) -> str:
        """Generate MD5 hash (mobile-optimized)"""
        if not self.is_available:
            raise NotImplementedError("System tools not available on mobile")
        
        try:
            from tools.system_tools import SystemTools
            desktop_tools = SystemTools()
            return desktop_tools.generate_md5(file_path)
        except Exception as e:
            raise Exception(f"MD5 generation failed: {e}")
    
    def generate_sha256(self, file_path: str) -> str:
        """Generate SHA256 hash (mobile-optimized)"""
        if not self.is_available:
            raise NotImplementedError("System tools not available on mobile")
        
        try:
            from tools.system_tools import SystemTools
            desktop_tools = SystemTools()
            return desktop_tools.generate_sha256(file_path)
        except Exception as e:
            raise Exception(f"SHA256 generation failed: {e}")
    
    def encrypt_file(self, file_path: str, password: str, output_path: Optional[str] = None) -> str:
        """Encrypt file (mobile-optimized)"""
        if not self.is_available:
            raise NotImplementedError("System tools not available on mobile")
        
        try:
            from tools.system_tools import SystemTools
            desktop_tools = SystemTools()
            return desktop_tools.encrypt_file(file_path, password, output_path)
        except Exception as e:
            raise Exception(f"File encryption failed: {e}")
    
    def decrypt_file(self, encrypted_file_path: str, password: str, output_path: Optional[str] = None) -> str:
        """Decrypt file (mobile-optimized)"""
        if not self.is_available:
            raise NotImplementedError("System tools not available on mobile")
        
        try:
            from tools.system_tools import SystemTools
            desktop_tools = SystemTools()
            return desktop_tools.decrypt_file(encrypted_file_path, password, output_path)
        except Exception as e:
            raise Exception(f"File decryption failed: {e}")
    
    def generate_secure_password(self, length: int = 16) -> str:
        """Generate secure password (mobile-optimized)"""
        if not self.is_available:
            raise NotImplementedError("System tools not available on mobile")
        
        try:
            from tools.system_tools import SystemTools
            desktop_tools = SystemTools()
            return desktop_tools.generate_secure_password(length)
        except Exception as e:
            raise Exception(f"Password generation failed: {e}")
    
    def get_file_info(self, file_path: str) -> dict:
        """Get file information (mobile-optimized)"""
        if not self.is_available:
            raise NotImplementedError("System tools not available on mobile")
        
        try:
            from tools.system_tools import SystemTools
            desktop_tools = SystemTools()
            return desktop_tools.get_file_info(file_path)
        except Exception as e:
            raise Exception(f"Get file info failed: {e}")

class MobileNetTools:
    """Mobile-compatible network tools"""
    
    def __init__(self):
        self.is_available = self._check_availability()
    
    def _check_availability(self) -> bool:
        """Check if network tools are available on mobile"""
        try:
            import requests
            import speedtest
            return True
        except ImportError:
            return False
    
    def download_youtube_thumbnail(self, youtube_url: str, output_path: Optional[str] = None) -> str:
        """Download YouTube thumbnail (mobile-optimized)"""
        if not self.is_available:
            raise NotImplementedError("Network tools not available on mobile")
        
        try:
            from tools.net_tools import NetTools
            desktop_tools = NetTools()
            return desktop_tools.download_youtube_thumbnail(youtube_url, output_path)
        except Exception as e:
            raise Exception(f"YouTube thumbnail download failed: {e}")
    
    def shorten_url_tinyurl(self, long_url: str) -> str:
        """Shorten URL using TinyURL (mobile-optimized)"""
        if not self.is_available:
            raise NotImplementedError("Network tools not available on mobile")
        
        try:
            from tools.net_tools import NetTools
            desktop_tools = NetTools()
            return desktop_tools.shorten_url_tinyurl(long_url)
        except Exception as e:
            raise Exception(f"URL shortening failed: {e}")
    
    def test_internet_speed(self) -> dict:
        """Test internet speed (mobile-optimized)"""
        if not self.is_available:
            raise NotImplementedError("Network tools not available on mobile")
        
        try:
            from tools.net_tools import NetTools
            desktop_tools = NetTools()
            return desktop_tools.test_internet_speed()
        except Exception as e:
            raise Exception(f"Speed test failed: {e}")
    
    def get_public_ip(self) -> str:
        """Get public IP address (mobile-optimized)"""
        if not self.is_available:
            raise NotImplementedError("Network tools not available on mobile")
        
        try:
            from tools.net_tools import NetTools
            desktop_tools = NetTools()
            return desktop_tools.get_public_ip()
        except Exception as e:
            raise Exception(f"Get public IP failed: {e}")
    
    def check_website_status(self, url: str) -> dict:
        """Check website status (mobile-optimized)"""
        if not self.is_available:
            raise NotImplementedError("Network tools not available on mobile")
        
        try:
            from tools.net_tools import NetTools
            desktop_tools = NetTools()
            return desktop_tools.check_website_status(url)
        except Exception as e:
            raise Exception(f"Website status check failed: {e}")

# Mobile-specific utilities
class MobileUtils:
    """Mobile-specific utility functions"""
    
    @staticmethod
    def get_app_storage() -> str:
        """Get app storage directory for mobile"""
        try:
            # Android
            from android.storage import primary_external_storage_path
            return primary_external_storage_path()
        except ImportError:
            try:
                # iOS or other
                import os
                return os.path.expanduser("~/Documents")
            except:
                return os.path.expanduser("~")
    
    @staticmethod
    def get_temp_dir() -> str:
        """Get temporary directory for mobile"""
        return tempfile.gettempdir()
    
    @staticmethod
    def is_android() -> bool:
        """Check if running on Android"""
        try:
            import android
            return True
        except ImportError:
            return False
    
    @staticmethod
    def is_ios() -> bool:
        """Check if running on iOS"""
        try:
            import platform
            return platform.system() == "Darwin" and hasattr(sys, 'getandroidapilevel') == False
        except:
            return False
    
    @staticmethod
    def get_platform() -> str:
        """Get current platform"""
        if MobileUtils.is_android():
            return "android"
        elif MobileUtils.is_ios():
            return "ios"
        else:
            return "unknown"
    
    @staticmethod
    def show_progress(title: str = "İşlem", message: str = "Lütfen bekleyin..."):
        """Show progress indicator (platform-specific)"""
        # This would be implemented with platform-specific UI
        pass
    
    @staticmethod
    def hide_progress():
        """Hide progress indicator"""
        # This would be implemented with platform-specific UI
        pass
    
    @staticmethod
    def show_toast(message: str, duration: int = 2):
        """Show toast message (platform-specific)"""
        # This would be implemented with platform-specific UI
        pass
    
    @staticmethod
    def show_notification(title: str, message: str):
        """Show notification (platform-specific)"""
        try:
            # Android
            from plyer import notification
            notification.notify(title=title, message=message)
        except:
            # Fallback to toast
            MobileUtils.show_toast(f"{title}: {message}")
    
    @staticmethod
    def request_permissions():
        """Request necessary permissions on mobile"""
        try:
            # Android
            from android.permissions import request_permissions, Permission
            permissions = [
                Permission.WRITE_EXTERNAL_STORAGE,
                Permission.READ_EXTERNAL_STORAGE,
                Permission.INTERNET,
                Permission.CAMERA
            ]
            request_permissions(permissions)
        except:
            pass  # Permissions not available on this platform