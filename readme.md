# 📡 NetWatch – Dashboard de supervision réseau

NetWatch est un mini-dashboard de **monitoring réseau** développé en Python.  
Il scanne automatiquement votre réseau local avec `nmap` et affiche les appareils connectés via une interface web simple et interactive (Flask + HTML/JS).  

---

## ✨ Fonctionnalités
- 🔎 Scan automatique du réseau local (LAN / Wi-Fi)  
- 🖥️ Détection des appareils connectés (IP, nom, état)  
- ⚡ Interface web interactive avec Flask  
- 🚨 Alerte en cas de nouveaux appareils détectés  
- 📊 Historique des scans sauvegardé en JSON  

---

## 🛠️ Technologies utilisées
- **Python 3**  
- **Flask** (framework web)  
- **python-nmap** (wrapper de Nmap)  
- **HTML / JavaScript** (interface web)  
- **Linux (Ubuntu)** pour l’environnement d’exécution  

---

## 🚀 Installation et exécution

### 1. Cloner le projet
```bash
git clone https://github.com/yohannmbonguembappe/netwatch.git
cd netwatch
2. Créer un environnement virtuel
python3 -m venv .venv
source .venv/bin/activate

3. Installer les dépendances
pip install flask python-nmap

4. Lancer le serveur
python app.py

5 Accéder au dashboard
Localhost : http://127.0.0.1:5000

Réseau local : http://<votre-IP-local>:5000

##Aperçu
![Capture de Netwatch] (screen.png)
