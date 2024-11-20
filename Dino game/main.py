import pygame
import random
import os

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Game")

BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background.png")), (WIDTH, HEIGHT))
WHITE = (255, 255, 255)

# Load images
dino_img = pygame.image.load(os.path.join("assets", "Dino.png"))
cactus_images = [
    pygame.image.load(os.path.join("assets", "cac1.png")),
    pygame.image.load(os.path.join("assets", "cac2.png")),
    pygame.image.load(os.path.join("assets", "cac3.png"))
]

for i in range(len(cactus_images)):
    cactus_images[i] = pygame.transform.scale(cactus_images[i], (40, 80))


def main():
    global score
    run = True
    FPS = 30
    score = 0
    main_font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 60)
    dino_x = 50
    dino_y = HEIGHT - 150
    is_jumping = False
    jump_count = 10
    cacti = []
    font = pygame.font.Font(None, 36)

    clock = pygame.time.Clock()

    lost = False
    last_cactus_x = WIDTH  

    MIN_CACTUS_DISTANCE = 300  

    def redraw_window():
        win.blit(BG, (0, 0))
        win.blit(dino_img, (dino_x, dino_y))
        for cactus in cacti:
            win.blit(cactus_images[cactus[2]], (cactus[0], cactus[1]))
        score_text = font.render(f"Score: {score}", True, WHITE)
        win.blit(score_text, (10, 10))

        if lost:
            lost_label = lost_font.render("You Lost!!", 1, (255, 255, 255))
            kills_label = main_font.render(f"Score: {score}", 1, (255, 255, 255))
            win.blit(lost_label, (WIDTH / 2 - lost_label.get_width() / 2, 350))
            win.blit(kills_label, (WIDTH / 2 - kills_label.get_width() / 2, 415))

        pygame.display.update()

    while run:
        clock.tick(FPS)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        # Jumping logic
        if not is_jumping:
            if keys[pygame.K_SPACE]:
                is_jumping = True
        else:
            if jump_count >= -10:
                neg = 1
                if jump_count < 0:
                    neg = -1
                dino_y -= (jump_count ** 2) * 0.5 * neg
                jump_count -= 1
            else:
                is_jumping = False
                jump_count = 10

        
        if len(cacti) == 0 or cacti[-1][0] < WIDTH - MIN_CACTUS_DISTANCE:
            if random.randint(1, 50) == 1:  
                cactus_type = random.randint(0, len(cactus_images) - 1)
                cacti.append([WIDTH, HEIGHT - 150, cactus_type])
                last_cactus_x = WIDTH 

        
        for cactus in cacti:
            cactus[0] -= 10  
            if cactus[0] < 0:
                cacti.remove(cactus)
                score += 1

        
            if (dino_x < cactus[0] + 20) and (dino_x + 40 > cactus[0]) and (dino_y + 40 > cactus[1]):
                lost = True

        redraw_window()

        if lost:
            pygame.time.delay(2000)
            run = False



def main_menu():
    title_font = pygame.font.SysFont("comicsans", 60)
    run = True
    while run:
        win.blit(BG, (0, 0))
        title_label = title_font.render("Press the mouse to begin...", 1, (255, 255, 255))
        win.blit(title_label, (WIDTH / 2 - title_label.get_width() / 2, 350))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
    pygame.quit()


main_menu()
