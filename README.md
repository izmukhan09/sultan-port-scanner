# 🛡️ Cybersecurity Port Scanner (v3.0)

A lightweight and efficient network infrastructure security tool built with Python. It automates the process of scanning hosts to discover open ports and analyze potential network vulnerabilities.

## 🚀 Features
* **Automated Port Scanning:** Scans multiple ports sequentially using Python's `range()` function.
* **Smart UI:** Filters out closed ports and highlights open entry points that might require protection.
* **Robust Error Handling:** Features advanced `try-except` blocks to handle system interrupts (`KeyboardInterrupt`), invalid hostnames (`gaierror`), and connection drops (`error`).
* **Performance Optimized:** Uses custom connection timeouts to ensure rapid scanning execution.

## 🛠️ Technologies Used
* **Language:** Python 3.x
* **Core Libraries:** `socket`, `datetime`
* **Concepts:** Networking, TCP/IP Protocols, Exception Handling, Automation

## 💻 How To Run
1. Clone this repository.
2. Run the script using terminal:
   ```bash
   python scanner.py
