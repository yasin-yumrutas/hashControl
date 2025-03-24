import socket
import random

def generate_private_key():
    # 1 < b < p-1 olacak şekilde private key üret
    p = 23
    return random.randint(2, p - 2)

def generate_public_key(private_key, g, p):
    return pow(g, private_key, p)

def calculate_shared_secret(other_public, private_key, p):
    return pow(other_public, private_key, p)

def bob_server():
    p = 23  # Ortak asal sayı
    g = 5   # Ortak kök (primitive root)

    print("Bob: Sunucu başlatılıyor...")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind(('0.0.0.0', 5000))
    server_socket.listen(1)
    print("Bob: Bağlantı bekleniyor...")

    conn, addr = server_socket.accept()
    print(f"Bob: Bağlantı kabul edildi: {addr}")

    # Alice'in açık anahtarını al
    alice_public = int(conn.recv(1024).decode())
    print(f"Bob: Alice'in açık anahtarı (A) alındı: {alice_public}")

    # Bob’un gizli anahtarı ve açık anahtarını üret
    b = generate_private_key()
    B = generate_public_key(b, g, p)

    # Bob’un açık anahtarını Alice’e gönder
    conn.send(str(B).encode())
    print(f"Bob: Açık anahtar (B) gönderildi: {B}")

    # Ortak gizli anahtar K'yı hesapla
    shared_secret = calculate_shared_secret(alice_public, b, p)
    print(f"Bob: Hesaplanan ortak gizli anahtar (K): {shared_secret}")

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    bob_server()
