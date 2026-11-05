<h1 align="center">🎮 Modular DQN AI Game</h1>
<h3 align="center">An Autonomous Reinforcement Learning Agent Powered by PyTorch</h3>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" />
  <img src="https://img.shields.io/badge/Pygame-1081C2?style=for-the-badge&logo=pygame&logoColor=white" />
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge" />
</p>

---

### 🌟 About The Project
This project is an implementation of an autonomous Deep Reinforcement Learning agent trained to play and master a dynamic arcade game. The agent utilizes a **Dueling Deep Q-Network (Dueling DQN)** architecture built with **PyTorch** to make real-time decisions, avoiding obstacles and optimizing its score dynamically.

---

### 🎥 Gameplay Demo
<p align="center">
  <img src="./Modular DQN AI.gif" alt="DQN Agent Gameplay" width="600"/>
</p>

---

### 🛠️ Project Structure
The project is built with a clean, modular architecture:
- **`main.py`** — The entry point to run and initialize the game and training loop.
- **`game.py`** — Core game logic, state management, and reward system.
- **`qplayer.py`** — The reinforcement learning agent, handling exploration/exploitation, policy, and memory replay.
- **`model.py`** — Neural network architecture definitions using **PyTorch (Dueling DQN)**.
- **`tile.py`** — Handles obstacles and environment entities.

---

### ⚙️ Tech Stack
- **Language:** Python
- **Deep Learning:** PyTorch
- **Environment / Graphics:** Pygame
- **Math & Utilities:** NumPy

---

### 🚀 Getting Started

To run this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Yahya-Alrabayah/Modular-DQN-AI-Game.git](https://github.com/Yahya-Alrabayah/Modular-DQN-AI-Game.git)
cd Modular-DQN-AI-Game
