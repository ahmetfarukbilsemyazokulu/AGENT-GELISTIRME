import json
import datetime

# --- YETENEKLER (TOOLS) ---
def arac_saat_ver():
    """Şu anki saati ve tarihi döndüren bir tool."""
    return f"📅 Güncel Tarih ve Saat: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

def arac_merhaba_de(isim):
    """Kullanıcıya özel selamlama yapan bir tool."""
    return f"👋 Merhaba {isim}! AGENT-GELISTIRME sistemine hoş geldin."

def arac_metin_analiz(metin):
    """Metin içindeki kelime ve karakter sayısını hesaplayan yeni bir tool."""
    kelime_sayisi = len(metin.split())
    karakter_sayisi = len(metin)
    return f"📊 Metin Analizi -> Kelime: {kelime_sayisi}, Karakter: {karakter_sayisi}"

# --- AJAN / CHATBOT YÖNETİCİSİ ---
def yapay_zeka_ajani(komut):
    print(f"🤖 Ajan komutu aldı: {komut}")
    
    # Basit bir niyet (intent) ve tool eşleme mekanizması
    if "saat" in komut.lower():
        return arac_saat_ver()
    elif "merhaba" in komut.lower():
        return arac_merhaba_de("Ahmet Faruk")
    elif "analiz et" in komut.lower():
        # Örnek metin analizi
        ornek_metin = "GitHub altyapısıyla maliyetsiz yapay zeka ajanları geliştiriyoruz."
        return arac_metin_analiz(ornek_metin)
    else:
        return f"💡 Mesajınız alındı: '{komut}'. Bu komut için henüz bir 'tool' tanımlanmadı, dilediğimiz gibi yeni bir fonksiyon ekleyebiliriz!"

# Test Çalıştırması
if __name__ == "__main__":
    print(yapay_zeka_ajani("Saat kaç?"))
    print(yapay_zeka_ajani("Merhaba ajan!"))
    print(yapay_zeka_ajani("Bu metni analiz et"))
