# Python Toolbox - Universal Edition

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20Mac%20%7C%20Android-blue)

## 🌟 Özellikler

### 🚀 Çoklu Platform Desteği
- ✅ **Railway Backend** - FastAPI ile cloud deployment
- ✅ **Windows EXE** - PyInstaller ile standalone executable
- ✅ **Android APK** - Kivy/KivyMD ile mobil uygulama
- ✅ **Linux/Mac** - PySide6 ile desktop uygulama

### 📱 Platformlar
| Platform | Arayüz | Deploy | Durum |
|----------|--------|--------|-------|
| Railway | FastAPI API | Cloud | ✅ Ready |
| Windows | PySide6 GUI | EXE | ✅ Ready |
| Linux | PySide6 GUI | Python | ✅ Ready |
| MacOS | PySide6 GUI | Python | ✅ Ready |
| Android | KivyMD GUI | APK | ✅ Ready |

---

## 🎯 Kullanım Şekilleri

### 1. Railway Backend (Cloud)
```bash
# Deploy to Railway
railway up
# or
python main.py backend
```

### 2. Desktop Application (Windows/Linux/Mac)
```bash
# Run with Python
python main.py desktop

# or Build EXE (Windows)
python scripts/build_all.py exe
```

### 3. Android Mobile App
```bash
# Build APK
python scripts/build_android.py

# or Run with Kivy (testing)
python main.py android
```

---

## 🛠️ Kurulum

### Gerekli Sistem Gereksinimleri
- Python 3.8 veya üzeri
- Platforma özel gereksinimler:
  - **Windows**: Visual C++ Build Tools
  - **Linux**: build-essential, python3-dev
  - **Mac**: Xcode Command Line Tools
  - **Android**: Java 8+, Android SDK

### Universal Kurulum
```bash
# 1. Projeyi klonlayın
git clone https://github.com/yourusername/python_toolbox.git
cd python_toolbox

# 2. Universal dependencies yükle
pip install -r requirements-universal.txt

# 3. Platforma özel kurulum
# Windows için:
pip install PySide6 pyinstaller

# Android build için:
pip install buildozer cython

# Backend için:
pip install fastapi uvicorn
```

### Platforma Özel Kurulum

#### Windows (EXE Build)
```bash
pip install PySide6 pyinstaller
python scripts/build_all.py exe
# dist/PythonToolbox.exe oluşur
```

#### Android (APK Build)
```bash
# Java 8+ yüklü olmalı
# Android SDK ve NDK buildozer tarafından indirilecek
python scripts/build_android.py
# mobile/buildozer/bin/*.apk oluşur
```

#### Railway Deploy
```bash
# Railway CLI yükle
npm install -g @railway/cli

# Login ve deploy
railway login
railway init
railway up
```

---

## 🚀 Kullanım

### Universal Launcher
```bash
# Otomatik platform tespiti
python main.py

# Manuel mod seçimi
python main.py desktop    # PySide6 GUI
python main.py android    # KivyMD GUI
python main.py backend    # FastAPI API
python main.py help       # Yardım
```

### Environment Variables
```bash
# Backend için
export PORT=8000
export PYTHONPATH=/path/to/project

# Android build için
export ANDROID_HOME=/path/to/android-sdk
export JAVA_HOME=/path/to/java
```

---

## 📱 Platform Özellikleri

### Railway Backend
- ✅ FastAPI REST API
- ✅ Health checks
- ✅ License management
- ✅ API key generation
- ✅ Auto-scaling
- ✅ PostgreSQL support

### Desktop (Windows/Linux/Mac)
- ✅ Modern PySide6 GUI
- ✅ Drag & drop support
- ✅ System tray integration
- ✅ File dialogs
- ✅ Multi-window support
- ✅ Native notifications

### Android Mobile
- ✅ KivyMD Material Design
- ✅ Touch-optimized interface
- ✅ File picker integration
- ✅ Share functionality
- ✅ Offline mode
- ✅ Push notifications (future)

---

## 🔧 Araçlar (Tüm Platformlarda)

### PDF Araçları
- ✅ PDF Birleştirme
- ✅ PDF Ayırma
- ✅ PDF → JPG Dönüştürme
- ✅ JPG → PDF Dönüştürme
- ✅ PDF Sıkıştırma
- ✅ Filigran Ekleme

### QR & Barkod Araçları
- ✅ QR Kod Üretme
- ✅ QR Kod Okuma
- ✅ WiFi QR Kodu
- ✅ Barkod Üretme
- ✅ Toplu QR Üretme

### Görsel Araçları
- ✅ Görsel Dönüştürme
- ✅ Yeniden Boyutlandırma
- ✅ Filigran Ekleme
- ✅ Optimize Etme

### Dosya Dönüştürücüler
- ✅ Excel ↔ JSON
- ✅ CSV → Excel
- ✅ TXT → PDF
- ✅ Word → PDF

### Sistem Araçları
- ✅ Hash Hesaplama
- ✅ Dosya Şifreleme
- ✅ ZIP İşlemleri
- ✅ Secure Password

### İnternet Araçları
- ✅ YouTube Thumbnail
- ✅ URL Kısaltma
- ✅ Hız Testi
- ✅ IP Görüntüleme

---

## 📁 Proje Yapısı

```
python_toolbox/
├── main.py                 # Universal launcher
├── app.py                  # Desktop application
├── requirements-universal.txt  # All platform dependencies
├── README-UNIVERSAL.md     # This file
├── 
├── tools/                  # Core tools (all platforms)
│   ├── pdf_tools.py
│   ├── qr_tools.py
│   ├── image_tools.py
│   ├── convert_tools.py
│   ├── system_tools.py
│   └── net_tools.py
│
├── platforms/              # Platform-specific tools
│   └── mobile_tools.py     # Mobile-optimized tools
│
├── ui/                     # Desktop GUI
│   └── main_window.py
│
├── mobile/                 # Android app
│   ├── src/
│   │   └── main_app.py
│   └── buildozer/
│       └── buildozer.spec
│
├── api/                    # Backend API
│   └── main.py
│
├── components/             # Shared components
│   └── license_manager.py
│
└── scripts/                # Build scripts
    ├── build_all.py
    └── build_android.py
```

---

## 🏗️ Build Sistemi

### Tek Komutla Hepsini Build Et
```bash
python scripts/build_all.py all
```

### Ayrı Ayrı Build
```bash
# Backend test
python scripts/build_all.py backend

# Desktop test
python scripts/build_all.py desktop

# Android APK
python scripts/build_android.py

# Windows EXE
python scripts/build_all.py exe
```

### Build Özellikleri
- ✅ Otomatik platform tespiti
- ✅ Dependency kontrolü
- ✅ Hata raporlama
- ✅ Progress tracking
- ✅ Cross-platform uyumluluk

---

## 🔐 Lisans Sistemi

### Tüm Platformlarda
- ✅ Free/Pro versiyon desteği
- ✅ Offline lisans doğrulama
- ✅ Online API doğrulama
- ✅ JSON lisans dosyası
- ✅ Usage tracking

### Free vs Pro
| Özellik | Free | Pro |
|---------|------|-----|
| PDF Limit | 5 dosya | Sınırsız |
| Batch Limit | 10 dosya | Sınırsız |
| Pro Araçlar | ❌ | ✅ |
| Öncelikli Destek | ❌ | ✅ |

---

## 🌐 API Kullanımı

### Health Check
```bash
curl https://your-app.up.railway.app/health
```

### License Generation
```bash
curl -X POST https://your-app.up.railway.app/generate-license \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","name":"John Doe"}'
```

### API Endpoints
- `GET /` - Root endpoint
- `GET /health` - Health check
- `POST /generate-license` - License oluştur
- `POST /verify-license` - License doğrula
- `POST /generate-api-key` - API key oluştur
- `GET /stats` - İstatistikler

---

## 📱 Mobile Özellikleri

### Android Uygulama
- ✅ Material Design 3
- ✅ Touch-optimized interface
- ✅ File picker integration
- ✅ Progress indicators
- ✅ Toast notifications
- ✅ Dialog system
- ✅ File manager
- ✅ Storage permissions
- ✅ Network operations
- ✅ Offline mode

### Mobile-Specific Tools
- ✅ QR Code Scanner (camera)
- ✅ Image Gallery Picker
- ✅ File Sharing
- ✅ Download Manager
- ✅ Storage Manager

---

## 🚀 Hızlı Başlangıç

### 1. Railway Deploy (5 dk)
```bash
# Railway'e bağla ve deploy et
railway login
railway init
railway up
```

### 2. Windows EXE (10 dk)
```bash
python scripts/build_all.py exe
# dist/PythonToolbox.exe
```

### 3. Android APK (30 dk)
```bash
python scripts/build_android.py
# mobile/buildozer/bin/*.apk
```

### 4. Desktop Test (1 dk)
```bash
python main.py desktop
```

---

## 🔧 Geliştirme

### Platform Ekleme
```python
# main.py'ye yeni platform ekle
def launch_new_platform():
    # Platform-specific code
    pass
```

### Tool Ekleme
```python
# tools klasörüne yeni araç ekle
# platforms/mobile_tools.py'ye mobile versiyon ekle
```

### Build Script Ekleme
```python
# scripts klasörüne yeni build scripti ekle
# build_all.py'ye entegre et
```

---

## 📊 İstatistikler

### Kod İstatistikleri
- **6 Ana Kategori**
- **30+ Profesyonel Araç**
- **3 Platform Desteği**
- **5000+ Satır Kod**
- **100% Python**

### Platform Kapsama Alanı
- ✅ Railway (Cloud)
- ✅ Windows (EXE)
- ✅ Linux (Python)
- ✅ MacOS (Python)
- ✅ Android (APK)
- ⏳ iOS (Future)

---

## 🛠️ Teknik Detayler

### Backend Stack
- **Framework**: FastAPI
- **Server**: Uvicorn
- **Database**: SQLite (expandable to PostgreSQL)
- **Authentication**: JWT tokens
- **Deployment**: Railway/Heroku/Render

### Desktop Stack
- **GUI**: PySide6 (Qt6)
- **Styling**: QSS/Custom themes
- **Icons**: Material Design Icons
- **Packaging**: PyInstaller

### Mobile Stack
- **Framework**: Kivy
- **UI**: KivyMD (Material Design)
- **Navigation**: NavigationRail
- **Packaging**: Buildozer

### Shared Stack
- **Core**: Python 3.8+
- **Tools**: 30+ modules
- **Licensing**: Custom system
- **Logging**: Python logging
- **Testing**: pytest (future)

---

## 🐛 Sorun Giderme

### Common Issues

#### Buildozer Android Build Fails
```bash
# Java kontrol
java -version

# Android SDK kontrol
echo $ANDROID_HOME

# Buildozer reset
buildozer android clean
buildozer android debug
```

#### PyInstaller EXE Fails
```bash
# Dependencies kontrol
pip list

# Hidden imports ekle
# build.spec dosyasını düzenle
```

#### PySide6 Import Error
```bash
# PySide6 yükle
pip install PySide6

# Qt plugins kontrol
# QT_QPA_PLATFORM_PLUGIN_PATH kontrol et
```

#### Kivy Import Error
```bash
# Kivy yükle
pip install kivy kivymd

# OpenGL kontrol
# KIVY_GL_BACKEND ayarla
```

---

## 📞 Destek

### Yardım Kanalları
1. **GitHub Issues** - Bug reports & feature requests
2. **Documentation** - README ve DEPLOY dosyaları
3. **Build Logs** - scripts/build_all.py test çıktıları
4. **Community** - Python toplulukları

### Debug Bilgisi
```bash
# System info
python --version
pip list
platform.platform()

# Build info
python scripts/build_all.py test
```

---

## 🔄 Güncelleme

### Versiyon Yönetimi
- **Major**: API değişiklikleri
- **Minor**: Yeni özellikler
- **Patch**: Bug fixes

### Güncelleme Süreci
1. Yeni versiyon tag'le
2. Tüm platformlarda test et
3. Release notes hazırla
4. Deploy et

---

## 📝 Lisans

MIT License - Detaylar için LICENSE dosyasına bakın.

---

## 🤝 Katkıda Bulunma

1. Fork yap
2. Feature branch oluştur
3. Tüm platformlarda test et
4. Pull request gönder

---

## 🙏 Teşekkürler

- **Kivy Team** - Mobile framework
- **Qt Company** - Desktop framework
- **FastAPI Team** - Web framework
- **Python Community** - Core language
- **Open Source Contributors** - All libraries

---

## 📞 İletişim

- **GitHub**: [python_toolbox](https://github.com/yourusername/python_toolbox)
- **Issues**: [GitHub Issues](https://github.com/yourusername/python_toolbox/issues)
- **Email**: support@pythontoolbox.com

---

**Made with ❤️ for the Python Community**

[⭐ Star on GitHub](https://github.com/yourusername/python_toolbox) | 
[📱 Download APK](https://github.com/yourusername/python_toolbox/releases) | 
[💻 Download EXE](https://github.com/yourusername/python_toolbox/releases)