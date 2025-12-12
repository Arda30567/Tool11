#!/usr/bin/env python3
"""
Python Toolbox - Android APK Build Script
Buildozer kullanarak Android APK oluşturur
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def check_buildozer():
    """Buildozer'ın yüklü olup olmadığını kontrol et"""
    try:
        result = subprocess.run(['buildozer', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✓ Buildozer yüklü: {result.stdout.strip()}")
            return True
        else:
            print("✗ Buildozer bulunamadı")
            return False
    except FileNotFoundError:
        print("✗ Buildozer bulunamadı")
        return False

def install_buildozer():
    """Buildozer'ı yükle"""
    print("Buildozer yükleniyor...")
    
    # Buildozer'ı yükle
    commands = [
        [sys.executable, '-m', 'pip', 'install', 'buildozer'],
        [sys.executable, '-m', 'pip', 'install', 'cython']
    ]
    
    for cmd in commands:
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode != 0:
                print(f"✗ Hata: {' '.join(cmd)}")
                print(f"Hata: {result.stderr}")
                return False
        except Exception as e:
            print(f"✗ Komut çalıştırılırken hata: {e}")
            return False
    
    print("✓ Buildozer yüklendi")
    return True

def check_android_sdk():
    """Android SDK'nın yüklü olup olmadığını kontrol et"""
    android_home = os.environ.get('ANDROID_HOME') or os.environ.get('ANDROID_SDK_ROOT')
    
    if android_home and os.path.exists(android_home):
        print(f"✓ Android SDK bulundu: {android_home}")
        return True
    else:
        print("✗ Android SDK bulunamadı")
        print("Lütfen Android SDK'yı yükleyin veya ANDROID_HOME ortam değişkenini ayarlayın")
        return False

def setup_environment():
    """Gerekli ortam değişkenlerini ayarla"""
    print("Ortam değişkenleri kontrol ediliyor...")
    
    # Android SDK için
    if not os.environ.get('ANDROID_HOME') and not os.environ.get('ANDROID_SDK_ROOT'):
        print("⚠ ANDROID_HOME veya ANDROID_SDK_ROOT ayarlanmamış")
        print("Buildozer Android SDK'yı otomatik indirecek")
    
    # Java için
    java_home = os.environ.get('JAVA_HOME')
    if java_home:
        print(f"✓ JAVA_HOME: {java_home}")
    else:
        print("⚠ JAVA_HOME ayarlanmamış")
        print("Java 8 veya üzeri gereklidir")
    
    return True

def build_apk():
    """APK oluştur"""
    print("\n" + "="*60)
    print("Python Toolbox Android APK Build")
    print("="*60)
    
    # Proje klasörü
    project_root = Path(__file__).parent.parent
    mobile_dir = project_root / "mobile"
    
    if not mobile_dir.exists():
        print("✗ Mobile klasörü bulunamadı")
        return False
    
    # Buildozer spec dosyasını kontrol et
    spec_file = mobile_dir / "buildozer.spec"
    if not spec_file.exists():
        print("✗ buildozer.spec dosyası bulunamadı")
        return False
    
    # Mobile/src klasörünü kontrol et
    src_dir = mobile_dir / "src"
    if not src_dir.exists():
        print("✗ mobile/src klasörü bulunamadı")
        return False
    
    # main_app.py dosyasını kontrol et
    main_app = src_dir / "main_app.py"
    if not main_app.exists():
        print("✗ main_app.py dosyası bulunamadı")
        return False
    
    print("✓ Gerekli dosyalar kontrol edildi")
    
    # Buildozer klasörünü oluştur
    buildozer_dir = mobile_dir / "buildozer"
    buildozer_dir.mkdir(exist_ok=True)
    
    # Spec dosyasını kopyala
    spec_target = buildozer_dir / "buildozer.spec"
    if not spec_target.exists():
        shutil.copy2(spec_file, spec_target)
    
    # src klasörünü buildozer klasörüne kopyala
    src_target = buildozer_dir / "src"
    if src_target.exists():
        shutil.rmtree(src_target)
    shutil.copytree(src_dir, src_target)
    
    # Kivy/KivyMD yükle
    print("\nKivy ve KivyMD yükleniyor...")
    kivy_install = [
        [sys.executable, '-m', 'pip', 'install', 'kivy==2.2.1'],
        [sys.executable, '-m', 'pip', 'install', 'kivymd==1.1.1'],
        [sys.executable, '-m', 'pip', 'install', 'Pillow==10.0.0'],
        [sys.executable, '-m', 'pip', 'install', 'qrcode==7.4.2'],
        [sys.executable, '-m', 'pip', 'install', 'requests==2.31.0'],
        [sys.executable, '-m', 'pip', 'install', 'speedtest-cli==2.1.3']
    ]
    
    for cmd in kivy_install:
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode != 0:
                print(f"✗ Hata: {' '.join(cmd)}")
                print(result.stderr)
                return False
        except Exception as e:
            print(f"✗ Komut çalıştırılırken hata: {e}")
            return False
    
    print("✓ Kivy ve bağımlılıkları yüklendi")
    
    # Buildozer init (ilk kez)
    print("\nBuildozer init yapılıyor...")
    os.chdir(str(buildozer_dir))
    
    try:
        result = subprocess.run(['buildozer', 'init'], capture_output=True, text=True)
        if result.returncode != 0:
            print("✗ Buildozer init başarısız")
            print(result.stderr)
    except Exception as e:
        print(f"✗ Buildozer init hatası: {e}")
    
    # APK build
    print("\nAPK build işlemi başlatılıyor...")
    print("⚠ Bu işlem 10-30 dakika sürebilir")
    print("⚠ İlk build'de Android SDK ve NDK indirilecek (2-3 GB)")
    
    try:
        # Debug build
        result = subprocess.run(['buildozer', '-v', 'android', 'debug'], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("\n✓ APK build başarılı!")
            
            # APK dosyasını kontrol et
            bin_dir = buildozer_dir / "bin"
            if bin_dir.exists():
                apk_files = list(bin_dir.glob("*.apk"))
                if apk_files:
                    apk_file = apk_files[0]
                    print(f"✓ APK dosyası: {apk_file}")
                    print(f"  Boyut: {apk_file.stat().st_size / (1024*1024):.1f} MB")
                    
                    # APK'yi ana dist klasörüne kopyala
                    dist_apk = project_root / "dist" / f"PythonToolbox-Android-{apk_file.name}"
                    dist_apk.parent.mkdir(exist_ok=True)
                    shutil.copy2(apk_file, dist_apk)
                    print(f"✓ APK kopyalandı: {dist_apk}")
                    
                    return True
                else:
                    print("✗ APK dosyası bulunamadı")
                    return False
            else:
                print("✗ Bin klasörü bulunamadı")
                return False
        else:
            print("\n✗ APK build başarısız")
            print("Hata detayları:")
            print(result.stderr[-1000:])  # Son 1000 karakteri göster
            return False
            
    except KeyboardInterrupt:
        print("\n⚠ Build işlemi kullanıcı tarafından iptal edildi")
        return False
    except Exception as e:
        print(f"\n✗ Build hatası: {e}")
        return False

def main():
    """Ana fonksiyon"""
    print("Python Toolbox Android APK Build Script")
    print("="*50)
    
    # 1. Buildozer kontrolü
    print("\n1. Buildozer kontrol ediliyor...")
    if not check_buildozer():
        if not install_buildozer():
            print("✗ Buildozer yüklenemedi, işlem durduruldu")
            return False
    
    # 2. Android SDK kontrolü
    print("\n2. Android SDK kontrol ediliyor...")
    if not check_android_sdk():
        print("⚠ Android SDK bulunamadı ama buildozer otomatik indirecek")
    
    # 3. Ortam değişkenleri
    print("\n3. Ortam değişkenleri kontrol ediliyor...")
    if not setup_environment():
        print("✗ Ortam değişkenleri ayarlanamadı")
        return False
    
    # 4. APK build
    print("\n4. APK build işlemi...")
    if build_apk():
        print("\n" + "="*60)
        print("✓ Android APK build başarılı!")
        print("="*60)
        print("\nSonraki adımlar:")
        print("1. APK dosyasını Android cihazınıza yükleyin")
        print("2. Bilinmeyen kaynaklardan uygulama yüklemeye izin verin")
        print("3. Uygulamayı çalıştırın ve test edin")
        print("\nNot: İlk çalıştırmada bazı araçlar çalışmayabilir.")
        print("Mobil versiyon sınırlı özellikler içerir.")
        return True
    else:
        print("\n" + "="*60)
        print("✗ Android APK build başarısız!")
        print("="*60)
        print("\nSorun giderme:")
        print("1. Java 8+ yüklü olduğundan emin olun")
        print("2. İnternet bağlantınızın olduğundan emin olun")
        print("3. Buildozer dokümantasyonunu kontrol edin")
        print("4. Hata mesajlarını inceleyin")
        return False

if __name__ == "__main__":
    main()