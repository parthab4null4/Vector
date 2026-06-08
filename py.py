import pygame
import random
import sys

pygame.init()

# ---------------- SETTINGS ----------------
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Monster Battle")

font = pygame.font.SysFont("arial", 30)
small_font = pygame.font.SysFont("arial", 22)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (220, 0, 0)
BLUE = (50, 120, 255)
GRAY = (180, 180, 180)
DARK = (40, 40, 40)

clock = pygame.time.Clock()

# ---------------- GAME DATA ----------------
player_health = 100
monster_health = 100

message = "Battle Started!"

# ---------------- BUTTON CLASS ----------------
class Button:
    def __init__(self, x, y, w, h, text, color):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.color = color

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=10)
        pygame.draw.rect(screen, BLACK, self.rect, 3, border_radius=10)

        txt = small_font.render(self.text, True, BLACK)
        screen.blit(
            txt,
            (
                self.rect.centerx - txt.get_width() // 2,
                self.rect.centery - txt.get_height() // 2,
            ),
        )

    def clicked(self, pos):
        return self.rect.collidepoint(pos)

# ---------------- BUTTONS ----------------
attack_btn = Button(150, 500, 180, 60, "ATTACK", GREEN)
heal_btn = Button(360, 500, 180, 60, "HEAL", BLUE)
escape_btn = Button(570, 500, 180, 60, "ESCAPE", RED)

# ---------------- FUNCTIONS ----------------
def draw_health_bar(x, y, health):
    pygame.draw.rect(screen, RED, (x, y, 300, 30))
    pygame.draw.rect(screen, GREEN, (x, y, health * 3, 30))
    pygame.draw.rect(screen, BLACK, (x, y, 300, 30), 2)

def monster_attack():
    global player_health, message

    damage = random.randint(10, 25)
    player_health -= damage

    if player_health < 0:
        player_health = 0

    message = f"Monster hit you for {damage} damage!"

def player_attack():
    global monster_health, message

    damage = random.randint(10, 30)
    monster_health -= damage

    if monster_health < 0:
        monster_health = 0

    message = f"You hit monster for {damage} damage!"

    if monster_health > 0:
        monster_attack()

def player_heal():
    global player_health, message

    heal = random.randint(10, 20)
    player_health += heal

    if player_health > 100:
        player_health = 100

    message = f"You healed {heal} HP!"

    if monster_health > 0:
        monster_attack()

# ---------------- MAIN LOOP ----------------
running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if (
            event.type == pygame.MOUSEBUTTONDOWN
            and player_health > 0
            and monster_health > 0
        ):
            mouse = pygame.mouse.get_pos()

            if attack_btn.clicked(mouse):
                player_attack()

            elif heal_btn.clicked(mouse):
                player_heal()

            elif escape_btn.clicked(mouse):
                running = False

    # Background
    screen.fill((220, 235, 255))

    # Title
    title = font.render("MONSTER BATTLE", True, BLACK)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 20))

    # Player
    pygame.draw.rect(screen, BLUE, (100, 180, 150, 150), border_radius=20)
    player_text = font.render("PLAYER", True, BLACK)
    screen.blit(player_text, (115, 140))

    # Monster
    pygame.draw.rect(screen, RED, (650, 180, 150, 150), border_radius=20)
    monster_text = font.render("MONSTER", True, BLACK)
    screen.blit(monster_text, (650, 140))

    # VS Text
    vs = font.render("VS", True, BLACK)
    screen.blit(vs, (430, 220))

    # Health Bars
    draw_health_bar(50, 100, player_health)
    draw_health_bar(550, 100, monster_health)

    hp1 = small_font.render(f"HP: {player_health}/100", True, BLACK)
    hp2 = small_font.render(f"HP: {monster_health}/100", True, BLACK)

    screen.blit(hp1, (120, 70))
    screen.blit(hp2, (620, 70))

    # Buttons
    if player_health > 0 and monster_health > 0:
        attack_btn.draw()
        heal_btn.draw()
        escape_btn.draw()

    # Message Box
    pygame.draw.rect(screen, WHITE, (150, 390, 600, 70))
    pygame.draw.rect(screen, BLACK, (150, 390, 600, 70), 2)

    msg = small_font.render(message, True, BLACK)
    screen.blit(msg, (170, 415))

    # Game Over
    if monster_health <= 0:
        win = font.render("YOU WIN!", True, GREEN)
        screen.blit(win, (WIDTH // 2 - 80, 320))

    elif player_health <= 0:
        lose = font.render("MONSTER WINS!", True, RED)
        screen.blit(lose, (WIDTH // 2 - 120, 320))

    pygame.display.update()

pygame.quit()
sys.exit()