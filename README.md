## English (German see below)

🔒 Purpose

This tool lets you encrypt confidential messages (e.g., Bitcoin addresses) so that only the BlitzPool server (https://blitzpool.yourdevice.ch/#/) can decrypt them. Even Telegram does not know the contents.

The tool works fully offline, uses public-key encryption (RSA, 4096 bits), and is easy to use on all operating systems.
🖥️ For macOS & Linux (Python Version)
📦 Requirements

    Python 3.x installed

    The cryptography package installed:

pip3 install cryptography

▶️ Usage

    Open a terminal

    Navigate to the folder where encrypt-message.py is located

    Start the tool:

python3 encrypt-message.py

    Enter your miner BTC address, e.g.:

bc1q123xxx

    Send the output of the program including /subscribe to the bot. You should then be logged in.

🪟 For Windows (EXE Version)

The Windows version works the same as the Python tool but does not require any Python installation. You can run it directly by double-clicking or using the terminal.
▶️ Usage

    Open a terminal or double-click blitzpool-message-encryptor.exe

    Enter your miner BTC address, e.g.:

bc1q123xxx

    Send the output of the program including /subscribe to the bot. You should then be logged in.

🛡️ Security

    Encryption is based on RSA-4096 with OAEP padding (SHA-256)

    The public key is embedded in the tool

    No connection to any server is established

    Everything runs locally on your machine

## German

### 🔒 Zweck

Mit diesem Tool kannst du vertrauliche Nachrichten (z. B. Bitcoin-Adressen) so verschlüsseln, dass nur der BlitzPool Server (https://blitzpool.yourdevice.ch/#/) sie entschlüsseln kann. Selbst Telegram kennt den Inhalt nicht.

Das Tool funktioniert vollständig offline, nutzt Public-Key-Verschlüsselung (RSA, 4096 Bit) und ist auf allen Betriebssystemen einfach zu bedienen.

---

## 🖥️ Für macOS & Linux (Python-Version)

### 📦 Voraussetzungen

- Python 3.x ist installiert
- Das Paket cryptography ist installiert:

```
pip3 install cryptography
```

### ▶️ Anwendung

1. Öffne ein Terminal
2. Wechsle in den Ordner, in dem sich die Datei encrypt-message.py befindet
3. Starte das Tool:

```
python3 encrypt-message.py
```

1. Gib deine Miner BTC Adresse ein ein, z. B.:

```
bc1q123xxx
```
2. Sende den Output des Programms inklusive /subscribe an den Bot, anschliessend solltest du eingeloggt sein.

## 🪟 Für Windows (EXE-Version)

Die Windows-Version funktioniert wie das Python-Tool, benötigt aber keine Python-Installation. Du kannst sie direkt per Doppelklick oder im Terminal ausführen.

### ▶️ Anwendung

1. Öffne ein Terminal oder doppelklicke die Datei blitzpool-message-encryptor.exe
2. Gib deine Miner BTC Adresse ein ein, z. B.:

```
bc1q123xxx
```
2. Sende den Output des Programms inklusive /subscribe an den Bot, anschliessend solltest du eingeloggt sein.

## 🛡️ Sicherheit

- Die Verschlüsselung basiert auf RSA-4096 mit OAEP Padding (SHA-256)
- Der Public Key ist fest im Tool eingebettet
- Es wird keine Verbindung zu irgendeinem Server hergestellt
- Alles läuft lokal auf deinem Rechner
