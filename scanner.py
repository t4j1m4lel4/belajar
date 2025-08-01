import socket
import threading
import time

target = input("Masukkan IP target: ")
start_port = int(input("Port awal: "))
end_port = int(input("Port akhir: "))
mode = input("Mode (cepat/lambat): ").lower()

threads = []
open_ports = []

# Set delay sesuai mode
delay = 0.05 if mode == "cepat" else 0.2

print(f"\n🚀 Scanning {target} dari port {start_port} sampai {end_port}...\n")

# Fungsi scanning port
def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((target, port))
    if result == 0:
        try:
            service = socket.getservbyport(port)
        except:
            service = "Unknown"
        print(f"[+] Port {port} terbuka ({service})")
        open_ports.append((port, service))
    s.close()
    time.sleep(delay)

# Membuat thread untuk setiap port
for port in range(start_port, end_port + 1):
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

# Tunggu semua thread selesai
for t in threads:
    t.join()

# Simpan hasil ke file
with open("hasil_scan.txt", "w") as f:
    for port, service in open_ports:
        f.write(f"Port {port} terbuka ({service})\n")

print(f"\n✅ Scan selesai! Hasil disimpan di 'hasil_scan.txt'")
