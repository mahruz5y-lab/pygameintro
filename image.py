import pygame
pygame.init()
a, b = 500, 500
display_surface = pygame.display.set_mode((a,b))
pygame.display.set_caption('Adding background image')
background_image = pygame.transform.scale(pygame.image.load('cat.jpeg').convert(),(500,500))
mouse_image = pygame.transform.scale(pygame.image.load('mouse.jpg').convert_alpha(),(200,200))
mouse_rectangle = mouse_image.get_rect(center = (a//2, b//2 - 30))
text = pygame.font.Font(None, 36).render('Hello tom and jerry',True, pygame.Color('black'))
text_rect = text.get_rect(center=(a//2, b//2 + 110))
def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        display_surface.blit(background_image,(0,0))
        display_surface.blit(mouse_image,mouse_rectangle)
        display_surface.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
if __name__ == '__main__':
    game_loop()
        

