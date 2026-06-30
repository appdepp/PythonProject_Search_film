# Film Search

Console application for searching films in a Sakila-style MySQL database.

## Features

- Search films by title
- Search films by genre and year
- Log user queries into a separate database
- Show top frequent queries

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create `.env` from `.env.example` and fill local database credentials:

```bash
cp .env.example .env
```

Run:

```bash
python main.py
```

## Security

Do not commit `.env`, logs, database passwords, or Telegram bot tokens.
