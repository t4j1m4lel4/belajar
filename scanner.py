import socket

target = input("Masukkan IP target: ")
for port in range(20, 81):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    if s.connect_ex((target, port)) == 0:
        print(f"[+] Port {port} terbuka")
    s.close()
