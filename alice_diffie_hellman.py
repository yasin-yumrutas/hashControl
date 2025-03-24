import socket
import random

def generate_private_key():
    # 1 < a < p-1 olacak şekilde private key üret
    p = 23
    return random.randint(2, p - 2)

def generate_public_key(private_key, g, p):
    return pow(g, private_key, p)

def calculate_shared_secret(other_public, private_key, p):
    return pow(other_public, private_key, p)

def alice_client():
    p = 23  # Ortak asal sayı
    g = 5   # Ortak kök (primitive root)

    # Alice’in gizli ve açık anahtarını üret
    a = generate_private_key()
    A = generate_public_key(a, g, p)

    print("Alice: Bob'a bağlanılıyor...")
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 5000))

    # Açık anahtar A'yı Bob'a gönder
    client_socket.send(str(A).encode())
    print(f"Alice: Açık anahtar (A) gönderildi: {A}")

    # Bob’un açık anahtarını al
    bob_public = int(client_socket.recv(1024).decode())
    print(f"Alice: Bob’un açık anahtarı (B) alındı: {bob_public}")

    # Ortak gizli anahtar K'yı hesapla
    shared_secret = calculate_shared_secret(bob_public, a, p)
    print(f"Alice: Hesaplanan ortak gizli anahtar (K): {shared_secret}")

    client_socket.close()

if __name__ == "__main__":
    alice_client()
