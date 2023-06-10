from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
      
class ProductItem(BoxLayout):
    def __init__(self, product, **kwargs):
        super(ProductItem, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.spacing = 10

        self.product = product

        # Resim
        image = Image(source=product["resim"])
        self.add_widget(image)

        label_ozellik = Label(text=product["ozellik"])
        self.add_widget(label_ozellik)

        label_fiyat = Label(text="Fiyat: " + product["fiyat"] + " TL")
        self.add_widget(label_fiyat)

        label_kiralama = Label(text="Kiralama: " + product["kiralamafiyat"] + " TL")
        self.add_widget(label_kiralama)

        button_kirala = Button(text="Kirala", on_press=self.kirala_button_press)
        self.add_widget(button_kirala)

        button_satinal = Button(text="Satın Al", on_press=self.satinal_button_press)
        self.add_widget(button_satinal)

    def kirala_button_press(self, instance):
        kirala_popup = KiralamaPopup()
        kirala_popup.open()

    def satinal_button_press(self, instance):
        print("Satın Al Button Pressed")
        popup = Popup(title='Satın Alma İşlemi',
                      content=SatinalmaPopup(self.product),
                      size_hint=(None, None), size=(400, 400))
        popup.open()


class SatinalmaPopup(BoxLayout):
    def __init__(self, product, **kwargs):
        super(SatinalmaPopup, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10

        self.product = product

        self.label_ad_soyad = Label(text="Ad Soyad:")
        self.add_widget(self.label_ad_soyad)

        self.input_ad_soyad = TextInput()
        self.add_widget(self.input_ad_soyad)

        self.label_adres = Label(text="Adres:")
        self.add_widget(self.label_adres)

        self.input_adres = TextInput()
        self.add_widget(self.input_adres)

        self.label_odeme = Label(text="Nasıl ödeme yapacaksınız (kart mı nakit mi):")
        self.add_widget(self.label_odeme)

        self.button_nakit = Button(text="Nakit", on_press=self.nakit_button_press)
        self.add_widget(self.button_nakit)

        self.button_kart = Button(text="Kart", on_press=self.kart_button_press)
        self.add_widget(self.button_kart)

        self.button_onayla = Button(text="Onayla", on_press=self.onayla_button_press)
        self.add_widget(self.button_onayla)

    def nakit_button_press(self, instance):
        self.odeme_yontemi = "nakit"
        self.button_nakit.background_color = (0, 1, 0, 1)  # Yeşil renkli arka plan

        # Kart seçeneği için rengi sıfırla
        self.button_kart.background_color = (1, 1, 1, 1)  # Beyaz renkli arka plan

    def kart_button_press(self, instance):
        self.odeme_yontemi = "kart"
        self.button_kart.background_color = (0, 1, 0, 1)  # Yeşil renkli arka plan

        # Nakit seçeneği için rengi sıfırla
        self.button_nakit.background_color = (1, 1, 1, 1)  # Beyaz renkli arka plan

    def onayla_button_press(self, instance):
        ad_soyad = self.input_ad_soyad.text
        adres = self.input_adres.text
        odeme = self.odeme_yontemi

        print("Ad Soyad:", ad_soyad)
        print("Adres:", adres)
        print("Ödeme Yöntemi:", odeme)

        if odeme == "nakit":
            mesaj = "Ürününüz yola çıktı. Nakit olarak ödeme yapılacak."
        elif odeme == "kart":
            mesaj = "Ürününüzün yanında POS makinesi ile kuryemizde olacaktır."
        else:
            mesaj = "Geçersiz ödeme yöntemi."

        self.parent.parent.dismiss()  # Popup'ı kapat

        popup = Popup(title='Satın Alma İşlemi',
                      content=SatinalmaSonucPopup(mesaj),
                      size_hint=(None, None), size=(400, 200))
        popup.open()


class SatinalmaSonucPopup(BoxLayout):
    def __init__(self, mesaj, **kwargs):
        super(SatinalmaSonucPopup, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10

        self.label_mesaj = Label(text=mesaj)
        self.add_widget(self.label_mesaj)

        self.button_tamam = Button(text="Tamam", on_press=self.tamam_button_press)
        self.add_widget(self.button_tamam)

    def tamam_button_press(self, instance):
        self.parent.parent.dismiss()  # Popup'ı kapat
        print("Tercih ettiğiniz için teşekkür ederiz.")


class KiralamaPopup(Popup):
    def __init__(self, **kwargs):
        super(KiralamaPopup, self).__init__(**kwargs)
        self.title = "Kiralama İşlemi"
        self.size_hint = (None, None)
        self.size = (400, 400)

        layout = BoxLayout(orientation='vertical', spacing=10)

        self.label_ad_soyad = Label(text="Ad Soyad:")
        layout.add_widget(self.label_ad_soyad)

        self.input_ad_soyad = TextInput()
        layout.add_widget(self.input_ad_soyad)

        self.label_adres = Label(text="Adres:")
        layout.add_widget(self.label_adres)

        self.input_adres = TextInput()
        layout.add_widget(self.input_adres)

        self.label_odeme = Label(text="Nasıl ödeme yapacaksınız (kart mı nakit mi):")
        layout.add_widget(self.label_odeme)

        self.button_nakit = Button(text="Nakit", on_press=self.nakit_button_press)
        layout.add_widget(self.button_nakit)

        self.button_kart = Button(text="Kart", on_press=self.kart_button_press)
        layout.add_widget(self.button_kart)

        self.label_gun_sayisi = Label(text="Kaç gün kiralayacaksınız:")
        layout.add_widget(self.label_gun_sayisi)

        self.input_gun_sayisi = TextInput()
        layout.add_widget(self.input_gun_sayisi)

        self.button_onayla = Button(text="Onayla", on_press=self.onayla_button_press)
        layout.add_widget(self.button_onayla)

        self.content = layout

    def nakit_button_press(self, instance):
        self.odeme_yontemi = "nakit"
        self.button_nakit.background_color = (0, 1, 0, 1)  # Yeşil renkli arka plan

        # Kart seçeneği için rengi sıfırla
        self.button_kart.background_color = (1, 1, 1, 1)  # Beyaz renkli arka plan

    def kart_button_press(self, instance):
        self.odeme_yontemi = "kart"
        self.button_kart.background_color = (0, 1, 0, 1)  # Yeşil renkli arka plan

        # Nakit seçeneği için rengi sıfırla
        self.button_nakit.background_color = (1, 1, 1, 1)  # Beyaz renkli arka plan

    def onayla_button_press(self, instance):
        ad_soyad = self.input_ad_soyad.text
        adres = self.input_adres.text
        odeme = self.odeme_yontemi
        gun_sayisi = self.input_gun_sayisi.text

        print("Ad Soyad:", ad_soyad)
        print("Adres:", adres)
        print("Ödeme Yöntemi:", odeme)
        print("Gün Sayısı:", gun_sayisi)

        if odeme == "nakit":
            mesaj = "Ürününüz kiralama için hazırlandı. Nakit olarak ödeme yapılacak."
        elif odeme == "kart":
            mesaj = "Ürününüzün yanında POS makinesi ile kuryemizde olacaktır."
        else:
            mesaj = "Geçersiz ödeme yöntemi."

        self.dismiss()  # Popup'ı kapat

        popup = Popup(title='Kiralama İşlemi',
                      content=KiralamaSonucPopup(mesaj),
                      size_hint=(None, None), size=(400, 200))
        popup.open()


class KiralamaSonucPopup(BoxLayout):
    def __init__(self, mesaj, **kwargs):
        super(KiralamaSonucPopup, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10

        self.label_mesaj = Label(text=mesaj)
        self.add_widget(self.label_mesaj)

        self.button_tamam = Button(text="Tamam", on_press=self.tamam_button_press)
        self.add_widget(self.button_tamam)

    def tamam_button_press(self, instance):
        self.parent.parent.dismiss()  # Popup'ı kapat
        print("Tercih ettiğiniz için teşekkür ederiz.")


class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10)

        products = [
            {"ozellik": "PlayStation", "fiyat": "5000", "kiralamafiyat": "100", "resim": "playsation.jpeg"},
            {"ozellik": "Fön Makinesi", "fiyat": "3000", "kiralamafiyat": "80", "resim": "fön.jpeg"},
            {"ozellik": "Dyson Airwrap Saç", "fiyat": "14000", "kiralamafiyat": "200", "resim": "dyson_airwrrap.jpeg"},
            {"ozellik": "Macbook Pro", "fiyat": "30000", "kiralamafiyat": "300", "resim": "macbook.jpeg"},
            {"ozellik": "İphone 14 pro max(128gb)", "fiyat": "50000", "kiralamafiyat": "500", "resim": "iphone.jpeg"},
            {"ozellik": "Buharlı Ütü ", "fiyat": "1500", "kiralamafiyat": "150", "resim": "buharlı_ütü.jpeg"},
            {"ozellik": "İstasyonlu Robot Süpürge", "fiyat": "31000", "kiralamafiyat": "1000", "resim": "robo_süpürge.jpeg"},
            {"ozellik": "Airfry(6Lt)", "fiyat": "4000", "kiralamafiyat": "150", "resim": "airfryer.jpeg"},
            {"ozellik": "Ses Sistemi", "fiyat": "7000", "kiralamafiyat": "400", "resim": "ses_sistemi.jpeg"},
            {"ozellik": "Apple Watch", "fiyat": "10000", "kiralamafiyat": "300", "resim": "apple_watch.jpeg"},
            
        ]

        for product in products:
            product_item = ProductItem(product)
            layout.add_widget(product_item)

        return layout


if __name__ == "__main__":
    MyApp().run()
