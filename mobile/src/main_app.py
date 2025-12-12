"""
Python Toolbox - Android App
KivyMD ile modern Android arayüzü
"""

from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineListItem, TwoLineListItem
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.progressbar import MDProgressBar
from kivymd.uix.card import MDCard
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivy.properties import StringProperty, BooleanProperty
from kivy.clock import Clock
import threading
import os

# Import tools (mobile-compatible versions)
from platforms.mobile_tools import MobilePDFTools, MobileQRTools, MobileImageTools
from platforms.mobile_tools import MobileConvertTools, MobileSystemTools, MobileNetTools

KV = '''
<MainScreen>:
    MDBoxLayout:
        orientation: 'vertical'
        
        MDTopAppBar:
            title: "Python Toolbox"
            elevation: 10
            
        MDNavigationRail:
            MDNavigationRailItem:
                text: "PDF"
                icon: "file-pdf-box"
                on_release: app.show_pdf_tools()
                
            MDNavigationRailItem:
                text: "QR/Barkod"
                icon: "qrcode"
                on_release: app.show_qr_tools()
                
            MDNavigationRailItem:
                text: "Görsel"
                icon: "image"
                on_release: app.show_image_tools()
                
            MDNavigationRailItem:
                text: "Dönüştürücü"
                icon: "file-replace"
                on_release: app.show_convert_tools()
                
            MDNavigationRailItem:
                text: "Sistem"
                icon: "tools"
                on_release: app.show_system_tools()
                
            MDNavigationRailItem:
                text: "İnternet"
                icon: "web"
                on_release: app.show_net_tools()
        
        MDScreenManager:
            id: screen_manager
            
            MDScreen:
                name: "pdf_screen"
                MDBoxLayout:
                    orientation: 'vertical'
                    padding: 20
                    spacing: 20
                    
                    MDLabel:
                        text: "PDF Araçları"
                        halign: "center"
                        font_style: "H5"
                        
                    MDGridLayout:
                        cols: 2
                        spacing: 20
                        adaptive_height: True
                        
                        MDCard:
                            orientation: "vertical"
                            padding: 15
                            size_hint_y: None
                            height: 150
                            
                            MDLabel:
                                text: "PDF Birleştir"
                                halign: "center"
                                font_style: "H6"
                                
                            MDIconButton:
                                icon: "file-pdf-box"
                                pos_hint: {"center_x": .5}
                                on_release: app.pdf_merge_dialog()
                                
                        MDCard:
                            orientation: "vertical"
                            padding: 15
                            size_hint_y: None
                            height: 150
                            
                            MDLabel:
                                text: "PDF Ayır"
                                halign: "center"
                                font_style: "H6"
                                
                            MDIconButton:
                                icon: "file-pdf-box"
                                pos_hint: {"center_x": .5}
                                on_release: app.pdf_split_dialog()
                                
            MDScreen:
                name: "qr_screen"
                MDBoxLayout:
                    orientation: 'vertical'
                    padding: 20
                    spacing: 20
                    
                    MDLabel:
                        text: "QR & Barkod Araçları"
                        halign: "center"
                        font_style: "H5"
                        
                    MDTextField:
                        id: qr_input
                        hint_text: "Metin, URL veya veri girin..."
                        mode: "rectangle"
                        
                    MDBoxLayout:
                        orientation: 'horizontal'
                        spacing: 20
                        size_hint_y: None
                        height: 50
                        
                        MDRaisedButton:
                            text: "QR Oluştur"
                            on_release: app.generate_qr()
                            
                        MDRaisedButton:
                            text: "QR Oku"
                            on_release: app.read_qr()
                            
            MDScreen:
                name: "image_screen"
                MDBoxLayout:
                    orientation: 'vertical'
                    padding: 20
                    spacing: 20
                    
                    MDLabel:
                        text: "Görsel Araçları"
                        halign: "center"
                        font_style: "H5"
                        
                    MDGridLayout:
                        cols: 2
                        spacing: 20
                        adaptive_height: True
                        
                        MDCard:
                            orientation: "vertical"
                            padding: 15
                            size_hint_y: None
                            height: 150
                            
                            MDLabel:
                                text: "Görsel Dönüştür"
                                halign: "center"
                                font_style: "H6"
                                
                            MDIconButton:
                                icon: "image"
                                pos_hint: {"center_x": .5}
                                on_release: app.image_convert_dialog()
                                
                        MDCard:
                            orientation: "vertical"
                            padding: 15
                            size_hint_y: None
                            height: 150
                            
                            MDLabel:
                                text: "Yeniden Boyutlandır"
                                halign: "center"
                                font_style: "H6"
                                
                            MDIconButton:
                                icon: "resize"
                                pos_hint: {"center_x": .5}
                                on_release: app.image_resize_dialog()
                                
            MDScreen:
                name: "convert_screen"
                MDBoxLayout:
                    orientation: 'vertical'
                    padding: 20
                    spacing: 20
                    
                    MDLabel:
                        text: "Dosya Dönüştürücü"
                        halign: "center"
                        font_style: "H5"
                        
                    MDList:
                        TwoLineListItem:
                            text: "Excel → JSON"
                            secondary_text: "Excel dosyasını JSON formatına dönüştür"
                            on_release: app.convert_excel_to_json()
                            
                        TwoLineListItem:
                            text: "JSON → Excel"
                            secondary_text: "JSON dosyasını Excel formatına dönüştür"
                            on_release: app.convert_json_to_excel()
                            
                        TwoLineListItem:
                            text: "TXT → PDF"
                            secondary_text: "Metin dosyasını PDF formatına dönüştür"
                            on_release: app.convert_txt_to_pdf()
                            
            MDScreen:
                name: "system_screen"
                MDBoxLayout:
                    orientation: 'vertical'
                    padding: 20
                    spacing: 20
                    
                    MDLabel:
                        text: "Sistem Araçları"
                        halign: "center"
                        font_style: "H5"
                        
                    MDList:
                        TwoLineListItem:
                            text: "Hash Hesapla"
                            secondary_text: "MD5, SHA256 hash değerlerini hesapla"
                            on_release: app.calculate_hash_dialog()
                            
                        TwoLineListItem:
                            text: "Dosya Şifrele"
                            secondary_text: "AES şifreleme ile dosyayı koru"
                            on_release: app.encrypt_file_dialog()
                            
            MDScreen:
                name: "net_screen"
                MDBoxLayout:
                    orientation: 'vertical'
                    padding: 20
                    spacing: 20
                    
                    MDLabel:
                        text: "İnternet Araçları"
                        halign: "center"
                        font_style: "H5"
                        
                    MDList:
                        TwoLineListItem:
                            text: "YouTube Thumbnail"
                            secondary_text: "YouTube videosunun thumbnail'ını indir"
                            on_release: app.youtube_thumbnail_dialog()
                            
                        TwoLineListItem:
                            text: "İnternet Hız Testi"
                            secondary_text: "İnternet bağlantı hızını test et"
                            on_release: app.speed_test()
                            
                        TwoLineListItem:
                            text: "IP Adresim"
                            secondary_text: "Genel IP adresini görüntüle"
                            on_release: app.show_my_ip()
'''

class PythonToolboxApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Python Toolbox"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        
        # Initialize tools
        self.pdf_tools = MobilePDFTools()
        self.qr_tools = MobileQRTools()
        self.image_tools = MobileImageTools()
        self.convert_tools = MobileConvertTools()
        self.system_tools = MobileSystemTools()
        self.net_tools = MobileNetTools()
        
        # File manager
        self.file_manager = MDFileManager(
            exit_manager=self.exit_file_manager,
            select_path=self.select_file_path
        )
        
        self.selected_file = None
        self.dialog = None

    def build(self):
        return Builder.load_string(KV)

    def show_pdf_tools(self):
        self.root.ids.screen_manager.current = "pdf_screen"

    def show_qr_tools(self):
        self.root.ids.screen_manager.current = "qr_screen"

    def show_image_tools(self):
        self.root.ids.screen_manager.current = "image_screen"

    def show_convert_tools(self):
        self.root.ids.screen_manager.current = "convert_screen"

    def show_system_tools(self):
        self.root.ids.screen_manager.current = "system_screen"

    def show_net_tools(self):
        self.root.ids.screen_manager.current = "net_screen"

    def pdf_merge_dialog(self):
        self.show_dialog(
            title="PDF Birleştir",
            text="Henüz mobil versiyonda aktif değil",
            buttons=[
                MDFlatButton(text="Tamam", on_release=self.close_dialog)
            ]
        )

    def pdf_split_dialog(self):
        self.show_dialog(
            title="PDF Ayır",
            text="Henüz mobil versiyonda aktif değil",
            buttons=[
                MDFlatButton(text="Tamam", on_release=self.close_dialog)
            ]
        )

    def generate_qr(self):
        text = self.root.ids.qr_input.text
        if not text:
            self.show_snackbar("Lütfen bir metin girin")
            return
        
        try:
            # QR kod oluştur
            output_path = os.path.join(self.get_app_storage(), "qr_code.png")
            self.qr_tools.generate_qr(text, output_path)
            self.show_snackbar(f"QR kod oluşturuldu: {output_path}")
        except Exception as e:
            self.show_snackbar(f"Hata: {str(e)}")

    def read_qr(self):
        self.file_manager.show(self.get_app_storage())
        self.file_manager_mode = "qr_read"

    def image_convert_dialog(self):
        self.show_dialog(
            title="Görsel Dönüştür",
            text="Henüz mobil versiyonda aktif değil",
            buttons=[
                MDFlatButton(text="Tamam", on_release=self.close_dialog)
            ]
        )

    def image_resize_dialog(self):
        self.show_dialog(
            title="Yeniden Boyutlandır",
            text="Henüz mobil versiyonda aktif değil",
            buttons=[
                MDFlatButton(text="Tamam", on_release=self.close_dialog)
            ]
        )

    def convert_excel_to_json(self):
        self.show_dialog(
            title="Excel → JSON",
            text="Henüz mobil versiyonda aktif değil",
            buttons=[
                MDFlatButton(text="Tamam", on_release=self.close_dialog)
            ]
        )

    def convert_json_to_excel(self):
        self.show_dialog(
            title="JSON → Excel",
            text="Henüz mobil versiyonda aktif değil",
            buttons=[
                MDFlatButton(text="Tamam", on_release=self.close_dialog)
            ]
        )

    def convert_txt_to_pdf(self):
        self.show_dialog(
            title="TXT → PDF",
            text="Henüz mobil versiyonda aktif değil",
            buttons=[
                MDFlatButton(text="Tamam", on_release=self.close_dialog)
            ]
        )

    def calculate_hash_dialog(self):
        self.show_dialog(
            title="Hash Hesapla",
            text="Henüz mobil versiyonda aktif değil",
            buttons=[
                MDFlatButton(text="Tamam", on_release=self.close_dialog)
            ]
        )

    def encrypt_file_dialog(self):
        self.show_dialog(
            title="Dosya Şifrele",
            text="Henüz mobil versiyonda aktif değil",
            buttons=[
                MDFlatButton(text="Tamam", on_release=self.close_dialog)
            ]
        )

    def youtube_thumbnail_dialog(self):
        self.show_dialog(
            title="YouTube Thumbnail",
            text="Henüz mobil versiyonda aktif değil",
            buttons=[
                MDFlatButton(text="Tamam", on_release=self.close_dialog)
            ]
        )

    def speed_test(self):
        def test_speed():
            try:
                result = self.net_tools.test_internet_speed()
                Clock.schedule_once(lambda dt: self.show_dialog(
                    title="Hız Testi Sonucu",
                    text=f"İndirme: {result['download_mbps']} Mbps\nYükleme: {result['upload_mbps']} Mbps\nPing: {result['ping_ms']} ms",
                    buttons=[
                        MDFlatButton(text="Tamam", on_release=self.close_dialog)
                    ]
                ))
            except Exception as e:
                Clock.schedule_once(lambda dt: self.show_snackbar(f"Hata: {str(e)}"))
        
        threading.Thread(target=test_speed).start()

    def show_my_ip(self):
        def get_ip():
            try:
                ip = self.net_tools.get_public_ip()
                Clock.schedule_once(lambda dt: self.show_dialog(
                    title="IP Adresiniz",
                    text=f"Genel IP: {ip}",
                    buttons=[
                        MDFlatButton(text="Tamam", on_release=self.close_dialog)
                    ]
                ))
            except Exception as e:
                Clock.schedule_once(lambda dt: self.show_snackbar(f"Hata: {str(e)}"))
        
        threading.Thread(target=get_ip).start()

    def get_app_storage(self):
        """Android depolama yolunu al"""
        try:
            from android.storage import primary_external_storage_path
            return primary_external_storage_path()
        except:
            return os.path.expanduser("~")

    def show_dialog(self, title, text, buttons):
        """Dialog göster"""
        if not self.dialog:
            self.dialog = MDDialog(
                title=title,
                text=text,
                buttons=buttons
            )
        else:
            self.dialog.title = title
            self.dialog.text = text
            self.dialog.buttons = buttons
        
        self.dialog.open()

    def close_dialog(self, *args):
        """Dialog kapat"""
        if self.dialog:
            self.dialog.dismiss()

    def show_snackbar(self, text):
        """Snackbar göster"""
        Snackbar(
            text=text,
            duration=2
        ).open()

    def exit_file_manager(self, *args):
        """File manager kapat"""
        self.file_manager.close()

    def select_file_path(self, path):
        """Dosya seçildiğinde çağrılır"""
        self.selected_file = path
        self.file_manager.close()
        
        if hasattr(self, 'file_manager_mode') and self.file_manager_mode == "qr_read":
            self.read_qr_from_file(path)

    def read_qr_from_file(self, image_path):
        """QR kodu dosyadan oku"""
        try:
            result = self.qr_tools.read_qr(image_path)
            if result:
                text = "\\n".join([r['data'] for r in result])
                self.show_dialog(
                    title="QR Kod İçeriği",
                    text=text,
                    buttons=[
                        MDFlatButton(text="Tamam", on_release=self.close_dialog)
                    ]
                )
            else:
                self.show_snackbar("QR kod bulunamadı")
        except Exception as e:
            self.show_snackbar(f"Hata: {str(e)}")

if __name__ == "__main__":
    PythonToolboxApp().run()