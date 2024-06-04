# Network Anomaly Detection

## Описание проекта

Этот проект разработан для захвата сетевых пакетов в реальном времени и анализа данных для выявления сетевых аномалий, таких как сканирование портов. Приложение также может эмулировать сетевые аномалии для тестирования функций обнаружения.

## Структура проекта

- network_anomaly_detection/
  - README.md
  - requirements.txt
  - main.py
  - capture/
    - __init__.py
    - capture_packets.py
  - analysis/
    - __init__.py
    - detect_anomalies.py
  - emulation/
    - __init__.py
    - emulate_scanning.py
  - utils/
    - __init__.py
    - logger.py

## Установка

1. Клонируйте репозиторий:
   ```sh
   git clone https://github.com/G4linov/ITMO-net
   cd network_anomaly_detection

2. Создайте виртуальное окружение и активируйте его:
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # Для Windows: venv\Scripts\activate

3. Установите зависимости:
   ```sh
   pip install -r requirements.txt

## Запуск проекта

1. Запустите основной скрипт:
   ```sh
   sudo python main.py  # Для Unix-подобных систем, для Windows запустите с правами администратора
Этот скрипт запускает захват пакетов в одном потоке и эмулирует сканирование портов в другом.

## Компоненты

### Захват пакетов

Захват сетевых пакетов осуществляется с использованием библиотеки scapy. Пакеты анализируются в реальном времени для выявления аномалий.

Файл: `capture/capture_packets.py`

### Анализ данных

Анализ данных для выявления сетевых аномалий, таких как сканирование  портов, выполняется по установленным правилам. Правило обнаружения  основано на количестве попыток подключения к различным портам за  определенный промежуток времени.  

Файл: `analysis/detect_anomalies.py`

### Эмуляция сетевых аномалий

Эмуляция сетевых аномалий позволяет тестировать функции обнаружения аномалий. В этом проекте реализована функция эмуляции сканирования портов.

Файл: `emulation/emulate_scanning.py`

## Пример использования

Основной скрипт main.py запускает захват пакетов и эмуляцию  сканирования портов. Пример кода:  

```python
from capture.capture_packets import start_packet_capture
from emulation.emulate_scanning import emulate_port_scanning
import threading
import time

if __name__ == "__main__":
    # Запуск захвата пакетов в отдельном потоке
    capture_thread = threading.Thread(target=start_packet_capture)
    capture_thread.start()

    # Пауза, чтобы захват пакетов успел начаться
    time.sleep(5)

    # Эмуляция сканирования портов
    target_ip = "192.168.1.1"  # Замените на IP-адрес цели
    start_port = 1
    end_port = 100
    emulate_port_scanning(target_ip, start_port, end_port)
    
    # Остановка захвата через некоторое время
    time.sleep(10)
    print("Завершаем захват пакетов...")
    capture_thread.join()
```