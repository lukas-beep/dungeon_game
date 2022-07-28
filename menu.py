import pygame
from PIL import Image


class Menu:
    def __init__(self, screen):
        pygame.init()
        self.screen = screen
        self.WIDTH, self.HEIGHT = screen.get_size()
        self.load_buttons()
        self.draw_buttons()

    def pilImageToSurface(self, pilImage):
        return pygame.image.fromstring(
            pilImage.tobytes(), pilImage.size, pilImage.mode
        ).convert()

    def load_buttons(self):
        image = Image.open("buttons.png")
        w, h = image.size

        start_buttons = image.crop((0, 0, 40, 31))
        start_button = start_buttons.crop((0, 0, 40, 15))
        start_button_hovered = start_buttons.crop((0, 15, 40, 31))
        self.start_button = Button(
            [
                pygame.transform.scale2x(
                    pygame.transform.scale2x(
                        self.pilImageToSurface(start_button_hovered)
                    )
                ),
                pygame.transform.scale2x(
                    pygame.transform.scale2x(
                        self.pilImageToSurface(start_button)
                    )
                ),
            ], (self.WIDTH // 2 - 20 * 2 * 2, (self.HEIGHT // 2 - 15 * 2 * 2) - 50)
        )

    def draw_buttons(self):
        self.screen.blit(
            self.start_button.imgs[0],
            (self.start_button.rect.x, self.start_button.rect.y),
        )

    def chosse_button(self):
        clock = pygame.time.Clock()
        pygame.display.update()
        while 1:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print("lol")
                    if event.button == 1:
                        print("lllllll")
                        if self.start_button.rect.collidepoint(pos):
                            print("start")
                            return self.start_button

                # for card in self.player.hero.hand:
                #     h = card.hoverd
                #     card.hoverd = card.rect.collidepoint(pos)
                #     if not( card.hoverd == h) and not card.hoverd and not card.draging:
                #         redraw = True


class Button:
    def __init__(self, imgs, pos):
        self.imgs = imgs
        self.hover = False
        self.rect = self.imgs[0].get_rect()
        self.rect.x, self.rect.y = pos


class StartButton(Button):
    def __init__(self, imgs):
        super().__init__(imgs)

    def func(self, screen):
        pass  # TODO: start game


# INFO: make a class for the buttons
# FIXME: center the buttons
# TODO: do hover func
# TODO: can click on buttons
