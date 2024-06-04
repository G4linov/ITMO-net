from scapy.all import sniff
from analysis.detect_anomalies import detect_port_scanning

def packet_callback(packet):
    detect_port_scanning(packet)

def start_packet_capture():
    print("Начинаем захват пакетов...")
    sniff(prn=packet_callback, store=False)
