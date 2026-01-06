# 🌍 GeoConsent (still under Development) 

A **consent-based location verification tool** designed for Termux users.  
GeoConsent allows you to generate a secure link that lets another user **voluntarily share their GPS location** via browser permission.

> ⚠️ This project strictly follows ethical and legal standards.  
> Location access occurs **only after explicit user consent**.

---

## ✨ Features

- 🔗 Generate unique location-sharing links
- 📍 Browser-based GPS capture (no app install)
- 🔐 Explicit consent before sharing
- 💻 Termux-compatible CLI
- 🌐 Simple Flask backend
- 🗺 Google Maps link generation
- 🧩 Easy to extend (Telegram bot, live tracking, etc.)

---

## 🧠 How It Works

1. You generate a unique link using the CLI
2. You send the link to the other person
3. They open it in a browser
4. Browser asks for GPS permission
5. Location is sent to your backend
6. You receive the location in Termux

---

## 🛠 Tech Stack

- **Backend:** Python (Flask)
- **Frontend:** HTML + JavaScript
- **CLI:** Python
- **Platform:** Termux / Linux
- **GPS:** Browser Geolocation API

---

## 🚀 Installation (Termux)

```bash
pkg update -y
pkg install git python cloudflared -y
pip install flask
cd geoconsent 
chmod +x start.sh
./start.sh
