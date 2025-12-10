# Portfolio Asset Manager 💼
A backend API application for investment portfolio management, designed according to modern software engineering standards (2025).  
The project demonstrates the use of an advanced Python technology stack, modular architecture, and a focus on security and code quality.

## 🚀 Key Features
- 🔐 **Secure Authorization:** Full registration and login system based on **JWT (JSON Web Tokens)** with password hashing using Bcrypt.
- 🛡️ **Data Separation:** Application-level Multi-tenancy – users can access only their own assets.
- 💰 **Asset Management:** REST API endpoints for adding and viewing investments with automatic owner assignment.
- ⚡ **High Performance:** Asynchronous FastAPI (async/await).

## 🛠️ Tech Stack
- **Language:** Python 3.13+
- **Framework:** FastAPI 0.124+
- **ORM / Database:** SQLModel (Pydantic + SQLAlchemy)
- **Dependency Management:** uv (fast successor to pip/poetry)
- **Code Quality:** Ruff (linting + formatting)

## ⚙️ Installation and Setup

### 1. Prerequisites
Install **uv**:

**Windows (PowerShell):**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**macOS / Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Clone and Install
```bash
git clone https://github.com/your-username/portfolio-asset-manager.git
cd portfolio-asset-manager

uv sync
```

### 3. Run Development Server
```bash
uv run uvicorn src.asset_manager.main:app --reload
```

API docs (Swagger UI) will be available at:  
**http://127.0.0.1:8000/docs**

---

## 🧪 Development and Quality Assurance (QA)

### Code Formatting (Auto-fix)
```bash
uv run ruff format .
```

### Static Analysis (Linter)
```bash
uv run ruff check . --fix
```

### Tests
```bash
uv run pytest
```

---

## 📂 Project Structure
```
src/asset_manager/
├── api/
│   ├── v1/endpoints/   # Business logic for endpoints (users, assets, auth)
│   └── deps.py         # Dependencies (Dependency Injection)
├── core/               # Global config and security (hashing, JWT)
├── db/                 # Database models and session configuration
├── schemas/            # Pydantic schemas (DTOs)
└── main.py             # Application entry point
```

---

## 🔜 Roadmap
- [ ] Integration with external APIs (e.g., CoinGecko)
- [ ] Authorization endpoint tests
- [ ] Docker containerization
- [ ] Deployment to cloud (Render)

---

## 👤 Author
**Mikolaj Kopacz**
