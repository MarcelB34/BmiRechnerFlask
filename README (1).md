# 🧮 BMI Rechner App

Eine webbasierte BMI-Rechner-Anwendung mit lokalem Messverlauf, gebaut mit Python (Flask) und modernem Dark-Mode-Design.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.x-lightgrey?logo=flask&logoColor=white)
![Status](https://img.shields.io/badge/Status-Live-brightgreen)
![Lizenz](https://img.shields.io/badge/Lizenz-MIT-orange)

---

## 📸 Screenshot

![BMI Rechner Screenshot](screenshot.png)

---

## ✨ Features

- **BMI-Berechnung** aus Gewicht (kg) und Körpergröße (cm)
- **Farbkodierte Auswertung** in 5 Kategorien (Untergewicht bis Adipositas Grad III)
- **Lokaler Messverlauf** — die letzten 5 Messungen werden im Browser gespeichert (localStorage)
- **Verlauf löschen** per Knopfdruck mit Bestätigungsdialog
- **Eingabevalidierung** mit benutzerfreundlicher Fehlermeldung
- **Responsives Dark-Mode-Design** — funktioniert auf Desktop und Mobilgeräten

---

## 🛠️ Tech Stack

| Komponente | Technologie |
|---|---|
| Backend | Python / Flask |
| Templating | Jinja2 |
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Datenspeicherung | Browser localStorage |
| Deployment | Nginx + Docker (Strato Server) |

---

## 🚀 Lokale Installation

```bash
# Repository klonen
git clone https://github.com/DEIN-USERNAME/bmi-rechner.git
cd bmi-rechner

# Abhängigkeiten installieren
pip install -r requirements.txt

# App starten
python main.py
```

Anschließend im Browser öffnen: `http://127.0.0.1:5000`

---

## 📁 Projektstruktur

```
bmi-rechner/
│
├── main.py                 # Flask-App & BMI-Logik
├── requirements.txt        # Python-Abhängigkeiten
├── templates/
│   └── index.html          # Jinja2-Template mit JavaScript
└── static/
    └── style.css           # Dark-Mode Stylesheet
```

---

## 📊 BMI-Kategorien

| BMI | Kategorie |
|---|---|
| < 18,5 | ⚠️ Untergewicht |
| 18,5 – 24,9 | ✅ Normalgewicht |
| 25,0 – 29,9 | ⚠️ Übergewicht |
| 30,0 – 34,9 | 🔴 Adipositas Grad I |
| 35,0 – 39,9 | 🔴 Adipositas Grad II |
| ≥ 40,0 | 🔴 Adipositas Grad III |

---

## 🌐 Live Demo

> Coming soon — wird auf [kaiserlabs-ai.de](https://kaiserlabs-ai.de) deployed.

---

## 📦 requirements.txt

```
flask
```

---

## 👤 Autor

**Marcel Bialas**  
[kaiserlabs-ai.de](https://kaiserlabs-ai.de) · 2026  
Pflegefachkraft im Übergang zum Python-Entwickler — Portfolio in Aufbau.

---

## 📄 Lizenz

Dieses Projekt steht unter der [MIT Lizenz](LICENSE).
