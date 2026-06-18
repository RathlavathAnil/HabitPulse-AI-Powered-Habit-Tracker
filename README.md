# HabitPulse

An AI-powered habit tracker and productivity coach built with Python and Ollama (Llama 3.2). HabitPulse combines local habit management with an on-device AI coach that provides personalized productivity suggestions — no cloud dependency, no API keys.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [Skills Demonstrated](#skills-demonstrated)
- [Resume Bullets](#resume-bullets)
- [Improvement Suggestions](#improvement-suggestions)
- [License](#license)

---

## Overview

HabitPulse is a command-line productivity application that helps users build and track habits while receiving AI-generated coaching. The AI coach runs entirely on-device via Ollama, making it privacy-first and internet-independent. Habit data is persisted locally in JSON, keeping the stack simple and portable.

This project demonstrates practical applications of local LLM integration, clean Python architecture, and persistent data management — skills directly relevant to backend, AI/ML, and full-stack engineering roles.

---

## Features

| Feature | Description |
|---|---|
| Add Habits | Create named habits with optional frequency and category |
| Track Progress | Log daily completions and update streak counters |
| Completion Analytics | View per-habit completion percentages over any time window |
| Delete Habits | Remove habits and their history cleanly from local storage |
| Persistent Storage | All data stored in structured JSON with no external database dependency |
| AI Coach | On-device LLM (Llama 3.2 via Ollama) generates personalized productivity suggestions |
| Context-Aware Advice | AI coach reads current habit data to provide habit-specific, not generic, feedback |

---

## Architecture

```
User Input (CLI)
       |
       v
  CLI Handler (main.py)
       |
  _____|_____
 |           |
 v           v
Habit      AI Coach
Manager    Module
(CRUD)     (Ollama Client)
 |           |
 v           v
JSON       Llama 3.2
Storage    (Local Model)
```

**Data flow:**

1. The user interacts through a CLI menu.
2. The `HabitManager` handles all CRUD operations, reading and writing to `habits.json`.
3. When coaching is requested, the `AICoach` module reads the current habit state, constructs a context-aware prompt, and queries the local Ollama instance.
4. Ollama runs Llama 3.2 locally and returns a streaming or complete response.
5. The response is formatted and displayed to the user.

The AI coach module is intentionally decoupled from the habit manager, making it straightforward to swap the underlying model or upgrade to a different Ollama-supported LLM without touching habit logic.

---

## Project Structure

```
habitpulse/
├── main.py                 # Entry point and CLI menu loop
├── habit_manager.py        # Habit CRUD operations and analytics
├── ai_coach.py             # Ollama integration and prompt construction
├── storage.py              # JSON read/write abstraction
├── utils.py                # Date helpers and formatting utilities
├── data/
│   └── habits.json         # Local persistent storage (auto-created)
├── tests/
│   ├── test_habit_manager.py
│   └── test_storage.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.10+ |
| LLM Runtime | Ollama |
| Model | Llama 3.2 (3B, runs on CPU) |
| Storage | JSON (file-based) |
| CLI | Python standard library (`argparse` / `input`) |
| Testing | `pytest` |

---

## Getting Started

### Prerequisites

- Python 3.10 or higher
- [Ollama](https://ollama.com) installed and running locally

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/habitpulse.git
cd habitpulse
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate       # macOS/Linux
venv\Scripts\activate          # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Pull the Llama 3.2 model via Ollama

```bash
ollama pull llama3.2
```

### 5. Run the application

```bash
python main.py
```

---

## Usage

### Adding a habit

```
> python main.py

1. Add Habit
2. Update Progress
3. View Habits
4. Get AI Coaching
5. Delete Habit
6. Exit

Choose an option: 1
Habit name: Morning Run
Frequency (daily/weekly): daily
Habit "Morning Run" added successfully.
```

### Viewing progress

```
Choose an option: 3

Habit             | Streak | Completion
------------------|--------|------------
Morning Run       |  5 days|  71.4%
Read for 30 mins  |  2 days|  42.8%
Drink 2L Water    |  7 days|  100.0%
```

### Getting AI coaching

```
Choose an option: 4

Analyzing your habits...

AI Coach:
Your "Morning Run" completion has dropped below 75% this week. 
Consider anchoring it to an existing routine — placing your 
running shoes next to your bed the night before reduces 
decision fatigue in the morning. Your water intake habit 
is at 100%; apply the same environmental design principle 
to your other habits.
```

---

## Roadmap

- [ ] `rich` library integration for improved terminal UI
- [ ] Habit streaks with milestone notifications
- [ ] Weekly summary report (exported to Markdown or PDF)
- [ ] Config file support for custom Ollama model selection
- [ ] REST API layer (FastAPI) to support a future web or mobile frontend
- [ ] SQLite migration path from JSON for larger datasets

---

## Skills Demonstrated

- **Python OOP** — Modular class design with separation of concerns across manager, storage, and AI layers
- **Local LLM Integration** — Programmatic use of Ollama's Python client for on-device inference
- **Prompt Engineering** — Context-aware prompt construction using live application data
- **File I/O and Data Persistence** — Structured JSON storage with error handling and schema validation
- **CLI Application Design** — User-facing menu loop with input validation
- **Software Architecture** — Decoupled modules enabling component-level testability and future extensibility
- **Testing** — Unit tests with `pytest` for core logic modules

---

## Resume Bullets

> Copy-paste ready. Optimized for ATS keyword matching in software engineering and AI/ML roles.

- Built an AI-powered habit tracking CLI application in Python integrating Ollama (Llama 3.2) for on-device LLM inference, demonstrating practical experience with local large language model deployment and prompt engineering
- Designed a modular architecture separating habit management, AI coaching, and data persistence layers, enabling independent unit testing and reducing inter-component coupling
- Implemented context-aware productivity coaching by dynamically constructing prompts from real-time habit data, producing personalized suggestions without relying on external APIs or cloud services
- Developed persistent data storage using structured JSON with a clean read/write abstraction layer, supporting full CRUD operations and habit analytics including streaks and completion percentages

---

## Improvement Suggestions

These additions increase project quality and recruiter impact without significantly increasing complexity:

**1. Add a `rich`-based UI (1–2 hours)**
Replace `print()` statements with the `rich` library for colored tables, progress bars, and formatted panels. Immediately makes the project look production-grade in screenshots.

**2. Write unit tests with `pytest` (2–3 hours)**
Cover `habit_manager.py` and `storage.py`. A `tests/` directory with passing tests signals engineering maturity to technical reviewers.

**3. Add a `config.yaml` file (1 hour)**
Let users configure the Ollama model name, data path, and default habit frequency from a config file instead of hardcoding values. Demonstrates configuration management awareness.

**4. Create a `--export` flag (2 hours)**
Add a CLI flag that exports a weekly summary to a Markdown file. Gives the project a tangible output artifact useful in demos.

**5. Add a `Makefile` (30 minutes)**
Provide `make run`, `make test`, and `make clean` targets. Common in professional Python projects and appreciated by reviewers cloning your repo.

**6. Record a short demo GIF (30 minutes)**
Use `asciinema` or `terminalizer` to record a 30-second demo and embed it in the README. The single highest-ROI improvement for recruiter appeal.

---

## License

MIT License. See [LICENSE](LICENSE) for details.
