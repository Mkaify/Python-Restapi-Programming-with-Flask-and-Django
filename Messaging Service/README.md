# Messaging Service

A small **Nameko** example: a **message service** (RPC + Redis) and a **web server** (HTTP) that talk over the broker. It’s the “microservices” piece of the repo—different from the Flask and Django apps.

## You’ll need

- Python 3.10+  
- **Redis** running (default URL in config: `redis://localhost:6379/0`)  
- **RabbitMQ** running (default AMQP: `pyamqp://guest:guest@localhost`)  
- `pip install -r requirements.txt`

## Quick start

1. Start **Redis** and **RabbitMQ** on your machine (defaults above).  
2. Install and activate a venv, then:

   ```bash
   cd "Messaging Service"
   pip install -r requirements.txt
   nameko run --config config.yaml temp_messenger.service
   ```

3. Open **http://127.0.0.1:8000/** (see `WEB_SERVER_ADDRESS` in `config.yaml`).

## Config

`config.yaml` sets **AMQP_URI**, **REDIS_URL**, and the web bind address. Change URLs there if your broker or Redis use different hosts or ports.

## Tests

With the venv active:

```bash
pytest
```

(Integration tests may expect services or fakes—check `tests/` if something fails without Redis/RabbitMQ.)

## Why it feels heavier

Unlike Flask or Django in this repo, this project **depends on running infrastructure** (message broker + Redis). That’s normal for Nameko; it’s not broken, just a different shape of app.
