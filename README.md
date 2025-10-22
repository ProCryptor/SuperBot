# 🔷 Base Onchain Activity — by Finesse Labs × CF

Automation tool to simulate and maintain **onchain activity** in the **Base ecosystem**.  
Supports modular task routes, randomization, OKX integration, and Telegram alerts.

---

## ⚙️ Configuration

Main settings are in `config.py` and `tasks.py`.

### ⏱️ Timings & Retry Logic
- `PAUSE_BETWEEN_WALLETS` — Delay between wallets.
- `PAUSE_BETWEEN_MODULES` — Delay between modules.
- `RETRIES` — Retry attempts on failure.
- `PAUSE_BETWEEN_RETRIES` — Delay before retry.
- `WAIT_FOR_RECEIPT` — Wait for funds to arrive before next module.

### 🔑 Wallets & Proxies
- `wallets.txt` — List of private keys (`0x...`)
- `proxies.txt` — Proxies (`user:pass@host:port`)
- `MOBILE_PROXY` / `ROTATE_IP` — Proxy behavior.

### 📲 Notifications
- `TG_BOT_TOKEN` — Telegram bot token.
- `TG_USER_ID` — Your Telegram ID for logs.

---

## 🔷 Tasks & Routes

Defined in `tasks.py`.

- **TASKS** — Top-level list of tasks to run.  
- `[ ]` — One random choice from the list.  
- `( )` — All inside are executed in random order.  
- Single string — Executes directly.  
- `OKX_WITHDRAW` — Always executed first if present.  

### Examples:
```python
QUICK_BURST = [
    ['UNISWAP', 'MATCHA_SWAP', 'OKX_WITHDRAW']
]

TRADER_HUSTLE = [
    ["RANDOM_SWAPS"],
    (
        ['UNISWAP', 'BUNGEE_SWAP'],
        ['RUBYSCORE_VOTE'],
        ['WRAPPER_UNWRAPPER']
    ),
    ['SWAP_ALL_TO_ETH']
]

DEV_MARATHON = [
    ["CONTRACT_DEPLOY"],
    ["RANDOM_TXS"],
    (
        ['MATCHA_SWAP', 'OWLTO_SWAP', 'RELAY_SWAP'],
        ['RUBYSCORE_VOTE'],
        ['WRAPPER_UNWRAPPER']
    ),
    ['SWAP_ALL_TO_ETH']
]

CROSS_CHAIN_VOYAGE = [
    ["RANDOM_TXS"]
]
```

---

## 🔷 Available Modules

Configured in `config.py`:

- `UNISWAP`
- `MATCHA_SWAP`
- `BUNGEE_SWAP`
- `OWLTO_SWAP`
- `RELAY_SWAP`
- `RUBYSCORE_VOTE` (vote on [rubyscore.io](https://rubyscore.io/dashboard))
- `WRAPPER_UNWRAPPER` (wrap/unwrap ETH)
- `CONTRACT_DEPLOY`
- `RANDOM_TXS` / `RANDOM_SWAPS` / `RANDOM_DEXes` mode
- `SWAP_ALL_TO_ETH`
- `OKX_WITHDRAW`

### 🔷 Available Tokens -> 25+
---

## 📁 File Structure

- `wallets.txt` — EVM private keys
- `proxies.txt` — Proxies
- `tasks.py` — Task routes
- `config.py` — Module/global settings

---

## 🚀 Quickstart
0. Create venv:
   ```bash
   python -m venv menv
   source menv/bin/activate
   ```

1. Install deps:
   ```bash
   pip install -r requirements.txt
   ```

2. Run:
   ```bash
   python main.py
   ```

   Options:
   - **Generate new database** — Fresh DB init  
   - **Work with existing database** — Use saved DB  

---

## 🧠 About

Built with 🔷 by **Finesse Labs** × **CF**  
For builders, by builders.
