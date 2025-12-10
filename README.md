# Portfolio Asset Manager 🚀

![Python](https://img.shields.io/badge/Python-3.13%2B-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.124%2B-009688?logo=fastapi&logoColor=white)
![SQLModel](https://img.shields.io/badge/SQLModel-Database-green)
![uv](https://img.shields.io/badge/uv-Package_Manager-purple)

## 📋 Overview

**Portfolio Asset Manager** is a robust, high-performance backend API designed to securely manage personal investment portfolios. It solves the problem of tracking distributed assets by providing a centralized, secure ledger accessible via REST endpoints.

Unlike simple CRUD apps, this project focuses on **Engineering Maturity**: implementing strict Multi-Tenancy (users see only their data), industrial-grade security (JWT + Bcrypt), and a modern, scalable architecture.

## 🏗 Architecture

The system follows a modular **Clean Architecture** principle, ensuring separation of concerns:

1.  **Security Layer:** Handles JWT issuance (PyJWT), password hashing (Bcrypt), and request interception via Dependency Injection to ensure only authenticated access.
2.  **API Layer:** RESTful endpoints built with **FastAPI**, fully typed with Pydantic schemas for strict data validation.
3.  **Storage Layer:** Relational data persistance managed by **SQLModel**, utilizing Foreign Keys to enforce ownership relationships between Users and Assets.

## 🛠 Tech Stack

* **Language:** Python 3.13
* **Framework:** FastAPI (Async/Await)
* **Database:** SQLModel (SQLite for dev / PostgreSQL ready)
* **Package Manager:** uv (Next-gen Python tooling, replacing pip/poetry)
* **Security:** PyJWT (Token handling), Passlib/Bcrypt (Hashing)
* **Quality Assurance:** Ruff (Linter/Formatter)

## 🚀 How to Run

### Prerequisites
* **uv** installed (The modern Python package manager)
* Python 3.10+

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/portfolio-asset-manager.git](https://github.com/YOUR_USERNAME/portfolio-asset-manager.git)
    cd portfolio-asset-manager
    ```

2.  **Install dependencies (Lightning fast via uv):**
    ```bash
    uv sync
    ```

### Usage

1.  **Start the API Server:**
    ```bash
    uv run uvicorn src.asset_manager.main:app --reload
    ```

2.  **Explore the API:**
    Open your browser and navigate to the interactive Swagger UI:
    👉 **http://127.0.0.1:8000/docs**

    * **Step 1:** Create a user via `POST /api/v1/users/`
    * **Step 2:** Login via the **Authorize** button (or `POST /api/v1/token`)
    * **Step 3:** Manage assets via `POST` and `GET /api/v1/assets/`

## 💡 Challenges & Lessons Learned

During the development, I encountered a significant **Dependency Hell** issue involving `passlib` and newer versions of `bcrypt` (v4.0+), which caused the authentication system to crash silently.
* **Solution:** I learned how to use `uv` to strictly pin compatible library versions in `pyproject.toml`, ensuring a reproducible build environment.

Another challenge was strictly typing the **ORM Relationships**. Mapping Pydantic input models to SQLModel database entities required a deep understanding of how to unpack dictionaries (`**model_dump()`) while manually injecting secure fields like `owner_id` from the JWT token.