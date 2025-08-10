# puchai-bunk-buddy

An MCP server for Puch AI with **Live Attendance Tracker** & **Bunk Forecaster** — calculate safe bunk days and keep your attendance above target.

1. **Live Attendance Tracker** — Reads your attendance data from a CSV file and shows subject-wise percentages, safe bunks left, and projections if you miss upcoming classes.  
2. **Bunk Forecaster** — Calculates exactly how many classes you can safely bunk (or how many you must attend) to maintain a target percentage.

---

## 🚀 Features
- **Subject-wise attendance tracking**
- **Safe bunk calculation** — stay above your target %
- **Future attendance projection** — see the effect of bunking days ahead
- **CSV-based data** — simple to update without editing code
- **Fully integrated MCP tools** — connect directly to Puch AI via WhatsApp

---

## 🛠 Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/puchai-bunk-buddy.git
cd puchai-bunk-buddy
```

### 2. Create and activate a virtual environment
```bash
uv venv
source .venv/bin/activate
```

### 3. Install dependencies
```bash
uv sync
```

### 4. Configure environment variables  
Copy the example file:
```bash
cp .env.example .env
```

Edit `.env` and set:
```ini
AUTH_TOKEN=your_secret_token_here
MY_NUMBER=919876543210
```

### 5. Prepare your attendance CSV  
Update `attendance.csv` in the project root:
```csv
Subject,Total_Classes,Attended_Classes
CS302,40,32
PPD 401,38,28
C424,30,25
CS399,42,31
CS301,35,27
```

---

## ▶️ Running the Server
```bash
python mcp_starter.py
```
You should see:
```text
🚀 Starting MCP server on http://0.0.0.0:8086
```

---

## 🌐 Connecting to Puch AI

1. Start an **ngrok** tunnel:
```bash
ngrok http 8086
```
2. Get the HTTPS URL from ngrok.  
3. Open WhatsApp and send to Puch AI:
```text
/mcp connect https://your-ngrok-url/mcp your_secret_token_here
```

---

## 📌 Example Commands in Puch AI

**Get all subjects with bunk forecast for 2 days:**
```bash
/mcp attendance_forecaster bunk_days=2
```

**Get only CS302 data:**
```bash
/mcp attendance_forecaster subject=CS302 bunk_days=1
```

**Calculate safe bunks if you attended 80 out of 100 classes:**
```bash
/mcp bunk_calculator total_classes=100 attended_classes=80 required_percent=75
```

---

## 💡 Future Improvements
- Real-time attendance sync from Google Sheets
- Graph-based projections using `matplotlib`
- Web dashboard for easier data updates

---

## 📜 License
This project is licensed under the MIT License.

---

**#BuildWithPuch 🚀**

