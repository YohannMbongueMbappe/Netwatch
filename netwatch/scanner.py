# scanner.py
import nmap
import json
from pathlib import Path
from datetime import datetime

CACHE = Path("devices.json")

def scan(network="192.168.1.0/24"):
    nm = nmap.PortScanner()
    nm.scan(hosts=network, arguments="-sn")  # découverte d'hôtes rapide

    devices = []
    for host in nm.all_hosts():
        state = nm[host].state()
        hostname = nm[host].hostname() or ""
        devices.append({"ip": host, "hostname": hostname, "state": state})

    snapshot = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "devices": sorted(devices, key=lambda d: d["ip"])
    }
    CACHE.write_text(json.dumps(snapshot, indent=2))
    return snapshot

def load_last():
    if CACHE.exists():
        return json.loads(CACHE.read_text())
    return {"timestamp": None, "devices": []}
