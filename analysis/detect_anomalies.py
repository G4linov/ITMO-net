from scapy.all import IP, TCP
from collections import defaultdict
import time

port_scan_threshold = 10  # Порог количества подключений к разным портам за короткий период
connections = defaultdict(list)

def detect_port_scanning(packet):
    if packet.haslayer(TCP):
        ip = packet[IP].src
        port = packet[TCP].dport
        current_time = time.time()

        # Обновляем список портов, к которым было подключение
        connections[ip].append((port, current_time))

        # Оставляем только недавние соединения (например, за последние 60 секунд)
        connections[ip] = [(p, t) for p, t in connections[ip] if current_time - t < 60]

        # Проверяем количество уникальных портов
        unique_ports = len(set(p for p, t in connections[ip]))
        if unique_ports > port_scan_threshold:
            print(f"Обнаружено сканирование портов с IP {ip}")
