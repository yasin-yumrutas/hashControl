📌 Ödevin 1. Kısmı: Diffie-Hellman Anahtar Değişimi
Hocanın istediklerine göre kontrol listemiz:
Gereksinim	Durum	Açıklama
Alice ve Bob rolleri	✅	Alice → istemci, Bob → sunucu
Bob önce çalıştırılmalı	✅	Kodda doğru sıralama
generate_private_key() fonksiyonu	✅	Alice & Bob için ayrı gizli değer üretimi
generate_public_key() fonksiyonu	✅	g^a mod p ve g^b mod p hesaplanıyor
calculate_shared_secret() fonksiyonu	✅	Alice: B^a mod p, Bob: A^b mod p
Aynı K değeri çıkması	✅	Testte Alice & Bob aynı K'yi üretti (örnek: 14)
Dosya isimleri hocaya uygun	✅	alice_diffie_hellman.py ve bob_diffie_hellman.py







Alice mesajı (M) ve bir sayı (S) birleştirip hash’liyor:
H = hash(M + S)

Sonra Bob’a M, S, H gönderiliyor.

Bob da kendi tarafında H' = hash(M + S) hesaplıyor.

Eğer H == H' → Mesaj doğrulanmıştır.