import socket
from datetime import datetime

print(f"=========================================")
print(f"🛡️  SULTAN'S CYBERSECURITY PORT SCANNER v3.0 🛡️")
print(f"=========================================")

target_host = input("🔗 Скандайтын сайтты енгізіңіз (мысалы, google.com): ")

print(f"\n⏳ Скандеу уақыты: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"🔍 {target_host} порттары тексерілуде (1-100 аралығы)...")
print(f"-----------------------------------------")

try:
    
    for port in range(1, 101):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.3) 
        
        result = s.connect_ex((target_host, port))
        

        if result == 0:
            print(f"🔓 Порт {port}: АШЫҚ (Open)  <-- ҚАУІП ПЕН ОСАЛДЫҚ БОЛУЫ МҮМКІН!")
            
        s.close()

except KeyboardInterrupt:
    print("\n🛑 Скандеу пайдаланушы тарапынан тоқтатылды.")
except socket.gaierror:
    print("\n❌ Сайттың адресі қате. IP мекенжайын анықтау мүмкін емес.")
except socket.error:
    print("\n❌ Серверге қосылу мүмкін болмады.")

print(f"-----------------------------------------")
print("✅ Скандеу сәтті аяқталды!")
print(f"=========================================")