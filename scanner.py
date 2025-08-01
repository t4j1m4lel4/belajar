import socket
import threading

target = input("Masukkan IP target: ")
print(f"\n🚀 Scanning target: {target}\n")

# Fungsi untuk scan port tertentu
def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown"
            print(f"[+] Port {port} terbuka ({service})")
        s.close()
    except:
        pass

# Scan menggunakan multithreading
for port in range(20, 1025):  # port 20-1024
    thread = threading.Thread(target=scan_port, args=(port,))
    thread.start()
