import socket
import hashlib

def hash_receiver():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('0.0.0.0', 8000))
    server_socket.listen(1)
    print("Hash Receiver: Bağlantı bekleniyor...")

    conn, addr = server_socket.accept()
    print(f"Bağlantı kabul edildi: {addr}")

    # M, S ve H'yi sırayla al
    # message = conn.recv(1024).decode()
    # salt = conn.recv(1024).decode()
    # received_hash = conn.recv(1024).decode()
    
    data = conn.recv(1024).decode()
    message, salt, received_hash = data.split("|||")

    print(f"Gelen mesaj (M): {message}")
    print(f"Gelen salt (S): {salt}")
    print(f"Gelen hash (H): {received_hash}")

    # H' hesapla
    calculated_hash = hashlib.sha256((message + salt).encode()).hexdigest()

    print(f"Hesaplanan hash (H'): {calculated_hash}")

    if received_hash == calculated_hash:
        print("✅ Mesaj doğrulandı: H == H'")
    else:
        print("❌ Mesaj doğrulanamadı: H ≠ H'")

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    hash_receiver()
