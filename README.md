# cloud-mini-project
It is cloud mini project to learn about Redis app → Nginx proxy → Prometheus metrics → Grafana dashboards

Sctrucuter would be somewhat like this

cloud-mini-project/
├── README.md
├── requirements.txt        # Python dependencies
├── src/                    # Application source code
│   ├── __init__.py
│   └── app.py              # Example entry point
├── configs/                # Config files for Nginx, Prometheus, Grafana
│   ├── nginx.conf
│   ├── prometheus.yml
│   └── grafana-dashboard.json
├── scripts/                # Helper scripts (setup, run, monitoring)
│   └── seed_redis.py
├── tests/                  # Unit tests
│   └── test_app.py
└── docker/                 # Dockerfiles for each service
    ├── Dockerfile.app
    ├── Dockerfile.redis
    └── Dockerfile.nginx


Great move! Setting up a Python virtual environment will give you a clean workspace for your **cloud-mini-project**. Here’s a step-by-step guide you can follow on your Kali Linux system:

---

## 🔧 Steps to Create a Virtual Environment

1. **Check Python installation**
   ```bash
   python3 --version
   ```
   Make sure you have Python 3 installed (most likely you do on Kali).

2. **Install venv (if missing)**
   ```bash
   sudo apt update
   sudo apt install python3-venv -y
   ```

3. **Create a virtual environment inside your project**
   Navigate to your project folder:
   ```bash
   cd ~/Documents/CloudProject/cloud-mini-project
   ```
   Then create the environment:
   ```bash
   python3 -m venv .venv
   ```

   This will create a `.venv` directory inside your project.

4. **Activate the virtual environment**
   ```bash
   source .venv/bin/activate
   ```
   Your shell prompt should now show `(.venv)` at the beginning, meaning you’re inside the environment.

5. **Select Python interpreter in VS Code (if you’re using it)**
   - Open VS Code in your project folder:  
     ```bash
     code .
     ```
   - Press **Ctrl+Shift+P** → type **Python: Select Interpreter**.
   - Choose the one pointing to `cloud-mini-project/.venv/bin/python`.

6. **Install dependencies**
   If you later add a `requirements.txt`, you can install everything with:
   ```bash
   pip install -r requirements.txt
   ```

---

## ⚡ Quick Tip
Keep each project in its own virtual environment. That way, you can experiment with Redis clients, Prometheus exporters, or Flask/Django apps without messing up your system Python.

---

Would you like me to also show you how to **structure your project repo** (e.g., `src/`, `tests/`, `requirements.txt`) so it’s ready for adding Redis, Nginx configs, and monitoring scripts? That way your cloud-mini-project won’t just be a README—it’ll be a proper playground.

