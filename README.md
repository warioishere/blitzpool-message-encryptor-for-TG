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
