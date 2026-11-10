import pygame as pg
import random
from tile import Tile
from qplayer import QPlayer

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = screen.get_size()
        self.player = QPlayer(self.width, self.height)
        self.tiles = []
        self.spawn_time = 0
        self.score = 0
        self.high_score = 0
        self.font = pg.font.SysFont("Arial", 18, bold=True)

    def update(self):
        state = self.player.get_state(self.tiles, self.height)
        action = self.player.choose_action(state)
        self.player.move(action)
        
        # Dynamic Difficulty Calculation
        current_speed = 4.0 + (self.high_score / 15.0)
        spawn_delay = max(450, 850 - (self.high_score * 4))

        if pg.time.get_ticks() - self.spawn_time > spawn_delay:
            self.tiles.append(Tile(self.width, random.randint(0, 3), current_speed))
            self.spawn_time = pg.time.get_ticks()

        reward, done = 0.05, False
        p_rect = self.player.get_hitbox()
        for t in self.tiles[:]:
            t.move()
            if t.get_hitbox().colliderect(p_rect):
                reward, done = -30, True
            elif t.y > self.height:
                self.tiles.remove(t)
                self.score += 1
                reward = 10

        next_state = self.player.get_state(self.tiles, self.height)
        self.player.memory.append((state, action, reward, next_state, done))
        self.player.train_step()

        if done:
            self.player.episodes += 1
            self.high_score = max(self.score, self.high_score)
            self.score = 0
            self.tiles = []
            self.player.column = random.randint(0, 3)

        # Rendering
        for t in self.tiles: 
            t.show(self.screen)
        self.player.show(self.screen)
        
        # Call UI with current speed
        self.draw_ui(current_speed)

    def draw_ui(self, speed):
        # Create text surfaces
        score_text = self.font.render(f"Score: {self.score}", True, (30, 30, 30))
        best_text = self.font.render(f"Best: {self.high_score}", True, (0, 100, 255))
        speed_text = self.font.render(f"Speed: {speed:.1f}", True, (200, 0, 0))
        
        # Draw text to screen at specific coordinates
        self.screen.blit(score_text, (20, 20))
        self.screen.blit(best_text, (20, 45))
        self.screen.blit(speed_text, (20, 70))