import socket
import random
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import hashlib

def generate_private_key(p):
    return random.randint(2, p - 2)

def generate_public_key(private_key, g, p):
    return pow(g, private_key, p)

def calculate_shared_secret(other_public, private_key, p):
    return pow(other_public, private_key, p)

def aes_diffie_server():
    p = 23
    g = 5

    b = generate_private_key(p)
    B = generate_public_key(b, g, p)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('0.0.0.0', 6000))
    server_socket.listen(1)
    print("AES Diffie Server: Bağlantı bekleniyor...")

    conn, addr = server_socket.accept()
    print(f"Bağlantı kabul edildi: {addr}")

    # Alice'in açık anahtarını al
    A = int(conn.recv(1024).decode())
    print(f"Alice'in açık anahtarı (A): {A}")

    # Bob’un açık anahtarını gönder
    conn.send(str(B).encode())
    print(f"Açık anahtar (B) gönderildi: {B}")

    # Ortak gizli anahtar K
    K = calculate_shared_secret(A, b, p)
    print(f"Ortak gizli anahtar K: {K}")

    # AES anahtarını üret (K → 16 byte)
    KEY = hashlib.sha256(str(K).encode()).digest()[:16]

    # Şifreli mesajı al ve çöz
    ciphertext = conn.recv(1024)
    cipher = AES.new(KEY, AES.MODE_ECB)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    print(f"Gelen mesaj (çözüldü): {plaintext.decode()}")

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    aes_diffie_server()
