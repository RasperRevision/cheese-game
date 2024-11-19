import pygame

pygame.init()
screen=pygame.display.set_mode((1280,720))
clock=pygame.time.Clock()
run=True
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run=False
  key=pygame.key.get_pressed()
  if key[pygame.K_q]:
    screen.fill("black")
  pygame.display.flip()
  clock.tick(60)
pygame.quit()
