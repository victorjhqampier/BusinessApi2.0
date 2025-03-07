# Business API - BIAN Capability - API LED  

A Go-based web server designed to deliver lightweight and efficient endpoints for various applications. Developed with extensibility and scalability in mind, this project utilizes FastAPI.

---

## Copyright

© 2025 Arify Labs

This code is licensed under the **GNU Affero General Public License (AGPL), version 3.0 or later**.  
You are free to use, modify, and distribute this code, but any changes or improvements must be contributed back to the original project and shared under the same license.

For more details about the license, visit:  
[https://www.gnu.org/licenses/agpl-3.0.html](https://www.gnu.org/licenses/agpl-3.0.html)

---

## Features

- Lightweight and modular structure.
- Easily extensible for adding new endpoints.
- Powered by FastAPI
- Built-in support for JSON-based responses.

---

## How to Run

1. Run Command - Go to src/
   ```bash
    cd src/
    python -m venv env
    Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser
    env/Scripts/activate.ps1
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    uvicorn Presentation.app:app --reload

1. Or Run
   ```bash
   .\start.ps1
