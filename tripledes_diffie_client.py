import socket
import random
from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad
import hashlib

def generate_private_key(p):
    return random.randint(2, p - 2)

def generate_public_key(private_key, g, p):
    return pow(g, private_key, p)

def calculate_shared_secret(other_public, private_key, p):
    return pow(other_public, private_key, p)

def tripledes_diffie_client():
    p = 23
    g = 5

    a = generate_private_key(p)
    A = generate_public_key(a, g, p)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 7000))
    print("TripleDES Diffie Client: Bağlantı sağlandı!")

    # Açık anahtar A'yı gönder
    client_socket.send(str(A).encode())
    print(f"Açık anahtar (A) gönderildi: {A}")

    # Bob’un açık anahtarını al
    B = int(client_socket.recv(1024).decode())
    print(f"Bob’un açık anahtarı (B) alındı: {B}")

    # Ortak gizli anahtar K
    K = calculate_shared_secret(B, a, p)
    print(f"Ortak gizli anahtar K: {K}")

    # TripleDES anahtarını üret (K → 24 byte)
    KEY = hashlib.sha256(str(K).encode()).digest()[:24]

    # Kullanıcıdan mesaj al ve şifrele
    message = input("Gönderilecek mesaj: ").encode()
    cipher = DES3.new(KEY, DES3.MODE_ECB)
    ciphertext = cipher.encrypt(pad(message, DES3.block_size))

    # Şifreli mesajı gönder
    client_socket.send(ciphertext)
    print("Şifreli mesaj gönderildi!")

    client_socket.close()

if __name__ == "__main__":
    tripledes_diffie_client()
