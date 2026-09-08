'''class Object:
    def __init__(self,x, y):
# to-do list object
    todo_img = pygame.image.load("media/todoliste.png").convert_alpha()
todo_img = pygame.transform.scale (todo_img,(175,175))

todo_x = 200
todo_y = 500

#rectangle to recognize the target
todo_rect = pygame.Rect(todo_x,todo_y, 175,175)

# clicking target to score -> source: https://www.youtube.com/watch?v=RvzYnh49Ntg
font = pygame.font.SysFont('Arial', 15, 'bold')
score = 0
WHITE = (255, 255, 255)

status = True
while (status):

  # iterate over the list of Event objects
  # that was returned by pygame.event.get() method.
    for i in pygame.event.get():

        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if i.type == pygame.QUIT:
            status = False

        if i.type == pygame.MOUSEBUTTONDOWN:
            if todo_rect.collidepoint(i.pos):
                score += 1

    # draw background & to-do list
    scrn.blit(imp,(0,0))
    scrn.blit(todo_img,(todo_x,todo_y))

    score_text = font.render(f"Score: {score}", True, WHITE)
    scrn.blit(score_text, (10,10))


# paint screen one time
    pygame.display.flip()

# deactivates the pygame library
pygame.quit()

if __name__ == "__main__":
    main()
'''