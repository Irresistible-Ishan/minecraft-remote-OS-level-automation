# minecraft-remote-OS-level-automation

A small experimental project that explores **controlling a locally running Minecraft client using OS-level keyboard and mouse automation**, with optional remote triggering via Discord or ssh.

This is a **learning and experimentation project**, not a finished product or a production ready bot.

---

## What this project is about

- Sending real keyboard and mouse inputs to Minecraft
- Triggering those inputs locally or remotely (via Discord)
- Automating simple, repetitive in-game actions
- Observing how Minecraft responds to precise input timing

The goal was mainly to **learn through experimentation** rather than build something polished.

---

## Research & observations

While building this, I manually tested and noted things like:

- Approximate mining times for different tools  
  (e.g. stone vs diamond pickaxe)
- Mouse movement required to rotate the camera  
  (~600 pixels ≈ 90° turn)
- How small timing changes affect movement consistency
- What information can be inferred from screenshots (HUD, F3 screen)

These observations are directly reflected in the delays and values used in the scripts.

---

## What it can do

- Walk, jump, crouch, and turn
- Mine and interact with blocks
- Execute simple scripted movement sequences
- Take screenshots for basic visual feedback
- Accept commands through Discord or local hotkeys
- with very well thought out mining steps which includes how bot should turn , stop , and move at every process of mining a 3d stucture or mountain.

---

## 📁 Repository Structure

├── discord/
│ ├── discord_remote_v1.py # Early Discord-controlled movement
│ └── discord_automation_v2.py # Scriptable remote automation
├── local/
│ └── local_automation.py # Hotkey-driven local automation
├── experiments/
│ └── mcpi_test.py # Deprecated experimental approach
├── README.md
├── LICENSE


## Technical Approach

- **No game mods**
- **No memory access**
- **No internal APIs**

Only:
- OS-level input simulation
- Visual feedback via screenshots
- Timed delays based on observed mechanics

This makes the automation fragile by design and that fragility is part of the research.

---

## Dependencies

- Python 3.9+
- Minecraft Java Edition (must be the active window)

### Python libraries

- pip install pyautogui pydirectinput discord pillow keyboard

### Important note

- This project controls your real keyboard and mouse
- Minecraft must be focused while it runs
- Running it while other applications are active may cause unintended input
- Intended only for learning and experimentation

### Author: Ishan Mani Singh - CODE7X