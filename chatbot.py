import json
import datetime

# --- YETENEKLER (TOOLS) ---
def arac_saat_ver():
    """Şu anki saati ve tarihi döndüren bir tool."""
    return f"📅 Güncel Tarih ve Saat: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

def arac_merhaba_de(isim):
    """Kullanıcıya özel selamlama yapan bir tool."""
    return f"👋 Merhaba {isim}! AGENT-GELISTIRME sistemine hoş geldin."

# --- AJAN / CHATBOT YÖNETİCİSİ ---
def yapay_zeka_ajani(komut):
    print(f"🤖 Ajan komutu aldı: {komut}")
    
    # Basit bir niyet (intent) ve tool eşleme mekanizması
    if "saat" in komut.lower():
        return arac_saat_ver()
    elif "merhaba" in komut.lower():
        return arac_merhaba_de("Ahmet Faruk")
    else:
        return f"💡 Mesajınız alındı: '{komut}'. Bu aşamada yeni bir 'tool' ekleyerek bunu geliştirebiliriz!"

# Test Çalıştırması
if __name__ == "__main__":
    print(yapay_zeka_ajani("Saat kaç?"))
    print(yapay_zeka_ajani("Merhaba ajan!"))
