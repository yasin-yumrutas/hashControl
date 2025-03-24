import socket
import hashlib
import random

def hash_sender():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 8000))
    print("Hash Sender: Bağlantı sağlandı!")

    # Mesaj al
    message = input("Gönderilecek mesaj (M): ")

    # Rastgele bir sayı üret (salt S)
    salt = str(random.randint(1000, 9999))

    # Hash hesapla: H = hash(M + S)
    combined = message + salt
    hash_value = hashlib.sha256(combined.encode()).hexdigest()

    # M, S ve H'yi sırayla gönder
    # client_socket.send(message.encode())
    # client_socket.send(salt.encode())
    # client_socket.send(hash_value.encode())

    data = f"{message}|||{salt}|||{hash_value}"
    client_socket.send(data.encode())

    print(f"Gönderildi:\n- Mesaj (M): {message}\n- Salt (S): {salt}\n- Hash (H): {hash_value}")

    client_socket.close()

if __name__ == "__main__":
    hash_sender()
