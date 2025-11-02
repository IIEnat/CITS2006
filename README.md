# CITS2006 – Defensive Cybersecurity Projects

This repository contains all assessment tasks for **CITS2006: Defensive Cybersecurity**, split into separate folders.

---

## 🔹 AI-Powered IDS
Machine-learning intrusion detection system that classifies packets as **normal** or **anomalous** using a preprocessing + Random Forest pipeline.

**Run**
```bash
python IDS.py
```

**Output Metrics**
Accuracy, Precision, Recall, F1 Score + Confusion Matrix

Dataset: `big_dataset.csv` (~25K entries)

---

## 🔹 Real-Time IP Reputation Checker
Uses the **AbuseIPDB API** to check IP reputation in real-time via CLI.

**Setup**
```bash
pip install python-dotenv requests
echo "ABUSEIPDB_API_KEY=your_api_key_here" > .env
python ip_reputation_checker.py
```

---

## 🔹 CLI Login System (RBAC)
Terminal login menu demonstrating **Role-Based Access Control**.

**Roles**
| Role | Permissions |
|------|-------------|
| Admin | Manage users, shutdown |
| User | View own profile |
| Guest | Read-only |

**Run**
```bash
python cli_login_access_control.py
```

---

## 🔹 Data Masking Extension (SPM)
Extends the Secure Password Manager by **overriding** the view function to **mask email addresses** while keeping other features unchanged.

**Run**
```bash
python data_masking_extension.py
```

---

## 🔹 Morse Code Learning Game
Simple CLI game where users translate random letters into Morse Code.

**Run**
```bash
python Morse.py
```

---

## 🔹 Secure Password Manager (SPM)
Command-line password manager using **SQLAlchemy** + **Fernet encryption**, storing credentials securely in `passwords.db`.

**Setup**
```bash
pip install sqlalchemy python-dotenv cryptography
# generate key manually via Fernet.generate_key()
echo "SECRET_KEY=your_fernet_key" > .env
python password_manager.py
```

---
