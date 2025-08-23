# python_project

## Projects
1. **Contact Manager (SQLite, CLI)** — Add/Update/Delete/Search contacts and export to CSV. Persists data in `contacts.db`.
2. **Password Manager (Tkinter + Encryption)** — Encrypted password vault using `cryptography.Fernet` and SQLite.
3. **Live Currency Converter (Tkinter + API)** — Real-time FX using `exchangerate.host` API.

## How to Run
- Install Python 3.9+
- (Recommended) Create a virtual environment
- Install requirements:
  ```bash
  pip install cryptography requests
  ```
- Run apps:
  ```bash
  # Contact Manager (CLI)
  python contact_manager_sqlite.py

  # Password Manager (GUI)
  python password_manager_gui.py

  # Currency Converter (GUI; needs internet)
  python live_currency_converter.py
  ```

## Notes
- The Password Manager generates a local `key.key`. Keep it safe. Losing it means you cannot decrypt saved passwords.
- The Currency Converter fetches **live rates**; ensure you have internet access when running it.
- These are educational/reference implementations. For production use, add master password, better key management, and input validation.
