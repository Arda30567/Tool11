#!/usr/bin/env python3
"""
Python Toolbox - Universal Launcher
Railway + Windows EXE + Android APK Destekli
"""

import sys
import os
import platform
from pathlib import Path

def get_platform():
    """Çalışan platformu tespit et"""
    if hasattr(sys, 'getandroidapilevel'):
        return 'android'
    elif platform.system() == 'Windows':
        return 'windows'
    elif platform.system() == 'Linux':
        return 'linux'
    elif platform.system() == 'Darwin':
        return 'macos'
    else:
        return 'unknown'

def launch_desktop():
    """Desktop (Windows/Linux/Mac) uygulamasını başlat"""
    try:
        from PySide6.QtWidgets import QApplication
        from PySide6.QtCore import Qt
        from ui.main_window import MainWindow
        
        app = QApplication(sys.argv)
        app.setApplicationName("Python Toolbox")
        app.setApplicationVersion("2.0.0")
        app.setOrganizationName("Python Toolbox")
        app.setAttribute(Qt.AA_EnableHighDpiScaling)
        app.setAttribute(Qt.AA_UseHighDpiPixmaps)
        
        window = MainWindow()
        window.show()
        
        return app.exec()
        
    except ImportError as e:
        print(f"PySide6 import hatası: {e}")
        print("PySide6 yüklemek için: pip install PySide6")
        return 1

def launch_android():
    """Android uygulamasını başlat"""
    try:
        from kivy.lang import Builder
        from kivymd.app import MDApp
        from mobile.src.main_app import PythonToolboxApp
        
        app = PythonToolboxApp()
        return app.run()
        
    except ImportError as e:
        print(f"Kivy import hatası: {e}")
        print("Kivy yüklemek için: pip install kivy kivymd")
        return 1

def launch_backend():
    """Backend API'yi başlat"""
    try:
        import uvicorn
        from api.main import app
        
        print("Python Toolbox Backend API başlatılıyor...")
        print("Port: 8000")
        print("URL: http://localhost:8000")
        print("Health: http://localhost:8000/health")
        
        uvicorn.run(
            app,
            host="0.0.0.0",
            port=8000,
            reload=True,
            log_level="info"
        )
        
    except ImportError as e:
        print(f"FastAPI/uvicorn import hatası: {e}")
        print("Yüklemek için: pip install fastapi uvicorn")
        return 1

def show_help():
    """Yardım mesajını göster"""
    print("""
Python Toolbox - Universal Launcher v2.0.0

Kullanım:
  python main.py [MOD]

Modlar:
  desktop     - Masaüstü uygulamasını başlat (PySide6)
  android     - Android uygulamasını başlat (Kivy)
  backend     - Backend API'yi başlat (FastAPI)
  help        - Bu yardım mesajını göster

Otomatik Tespit:
  Windows/Linux/Mac - Desktop modu
  Android           - Android modu
  Railway/Heroku    - Backend modu

Örnekler:
  python main.py desktop
  python main.py android
  python main.py backend
  python main.py help

Notlar:
  - Masaüstü için: PySide6 gerekli
  - Android için: Kivy, KivyMD gerekli
  - Backend için: FastAPI, uvicorn gerekli
    """)

def main():
    """Ana launcher fonksiyonu"""
    
    # Komut satırı argümanlarını al
    if len(sys.argv) > 1:
        mode = sys.argv[1].lower()
    else:
        # Otomatik mod tespiti
        current_platform = get_platform()
        
        if current_platform == 'android':
            mode = 'android'
        elif current_platform == 'windows':
            mode = 'desktop'
        elif 'RAILWAY' in os.environ or 'DYNO' in os.environ:
            # Railway veya Heroku ortamı
            mode = 'backend'
        elif os.environ.get('PORT'):
            # Cloud platform (Railway, Render, vb.)
            mode = 'backend'
        else:
            # Varsayılan desktop
            mode = 'desktop'
    
    # Moda göre başlat
    if mode == 'desktop':
        print("Python Toolbox Desktop modu başlatılıyor...")
        sys.exit(launch_desktop())
        
    elif mode == 'android':
        print("Python Toolbox Android modu başlatılıyor...")
        sys.exit(launch_android())
        
    elif mode == 'backend':
        print("Python Toolbox Backend modu başlatılıyor...")
        sys.exit(launch_backend())
        
    elif mode == 'help':
        show_help()
        sys.exit(0)
        
    else:
        print(f"Bilinmeyen mod: {mode}")
        print("Yardım için: python main.py help")
        sys.exit(1)

if __name__ == "__main__":
    main()