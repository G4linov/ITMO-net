from scapy.all import IP, TCP, send

def emulate_port_scanning(target_ip, start_port, end_port):
    print(f"Эмуляция сканирования портов для {target_ip}...")
    for port in range(start_port, end_port + 1):
        packet = IP(dst=target_ip)/TCP(dport=port)
        send(packet, verbose=0)
        print(f"Отправлен пакет на {target_ip}:{port}")
