import time
import os

def lembrete():
    os.system("""
    osascript -e 'display notification "Hora de beber água!" with title "Já bebeu água hoje?"'
    """)

while True:
    lembrete()
    time.sleep(3600)  # 1 hora

