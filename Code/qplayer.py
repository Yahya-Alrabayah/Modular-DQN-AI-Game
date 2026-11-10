import torch
import torch.optim as optim
import numpy as np
import random
import pygame as pg
from collections import deque
from model import DuelingDQN

class QPlayer:
    def __init__(self, screen_width, screen_height):
        self.num_columns = 4
        self.width = screen_width // self.num_columns
        self.size = 36
        self.column = 1
        self.y = screen_height - self.size - 50
        self.state_size = 4 
        self.action_size = 3 
        self.model = DuelingDQN(self.state_size, self.action_size)
        self.target_model = DuelingDQN(self.state_size, self.action_size)
        self.target_model.load_state_dict(self.model.state_dict())
        self.optimizer = optim.Adam(self.model.parameters(), lr=0.0005)
        self.memory = deque(maxlen=10000)
        self.gamma, self.epsilon, self.epsilon_decay = 0.99, 1.0, 0.9994 
        self.epsilon_min, self.tau, self.episodes = 0.02, 0.01, 0

    def soft_update(self):
        for target_param, local_param in zip(self.target_model.parameters(), self.model.parameters()):
            target_param.data.copy_(self.tau * local_param.data + (1.0 - self.tau) * target_param.data)

    def get_state(self, tiles, screen_height):
        if not tiles: return np.array([self.column/3, 0.0, 1.0, 0.5], dtype=np.float32)
        upcoming = sorted([t for t in tiles if t.y < self.y + self.size], key=lambda t: abs(self.y - t.y))
        t1 = upcoming[0] if upcoming else None
        t2 = upcoming[1] if len(upcoming) > 1 else t1
        if not t1: return np.array([self.column/3, 0.0, 1.0, 0.5], dtype=np.float32)
        return np.array([self.column/3, t1.column/3, (self.y - t1.y)/screen_height, t2.column/3 if t2 else 0.0], dtype=np.float32)

    def choose_action(self, state):
        if random.random() < self.epsilon: return random.randint(0, 2)
        state_t = torch.FloatTensor(state).unsqueeze(0)
        with torch.no_grad(): return torch.argmax(self.model(state_t)).item()

    def train_step(self):
        if len(self.memory) < 128: return
        batch = random.sample(self.memory, 128)
        s, a, r, sn, d = zip(*batch)
        s_t, sn_t = torch.FloatTensor(np.array(s)), torch.FloatTensor(np.array(sn))
        a_t, r_t, d_t = torch.LongTensor(a), torch.FloatTensor(r), torch.FloatTensor(d)
        curr_q = self.model(s_t).gather(1, a_t.unsqueeze(1)).squeeze(1)
        next_q = self.target_model(sn_t).max(1)[0]
        targets = r_t + (1 - d_t) * self.gamma * next_q
        loss = torch.nn.MSELoss()(curr_q, targets.detach())
        self.optimizer.zero_grad(); loss.backward(); self.optimizer.step()
        self.soft_update()
        if self.epsilon > self.epsilon_min: self.epsilon *= self.epsilon_decay

    def move(self, action):
        if action == 0 and self.column > 0: self.column -= 1
        elif action == 2 and self.column < self.num_columns - 1: self.column += 1

    def show(self, screen):
        x = self.column * self.width + (self.width - self.size) // 2
        pg.draw.rect(screen, (255, 60, 60), (x, self.y, self.size, self.size))

    def get_hitbox(self):
        x = self.column * self.width + (self.width - self.size) // 2
        return pg.Rect(x, self.y, self.size, self.size)