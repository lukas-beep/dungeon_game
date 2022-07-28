import pygame
from PIL import Image


class Menu:
    def __init__(self, screen):
        pygame.init()
        self.screen = screen
        self.WIDTH, self.HEIGHT = screen.get_size()
        self.buttons = []
        self.load_buttons()
        self.draw_buttons()
        

    def pilImageToSurface(self, pilImage):
        return pygame.image.fromstring(
            pilImage.tobytes(), pilImage.size, pilImage.mode
        ).convert()

    def load_buttons(self):
        image = Image.open("buttons.png")

        for i in range(0, 128, 39):
            _buttons = image.crop((i, 0, i + 39, 31))
            button = _buttons.crop((0, 0, 40, 15))
            button_hovered = _buttons.crop((0, 15, 40, 31))
            button_info = (
                [
                    pygame.transform.scale2x(
                        pygame.transform.scale2x(self.pilImageToSurface(button_hovered))
                    ),
                    pygame.transform.scale2x(
                        pygame.transform.scale2x(self.pilImageToSurface(button))
                    ),
                ],
                (self.WIDTH // 2 - 20 * 2 * 2, (self.HEIGHT // 2 - 15 * 2 * 2) - 50+(i*1.7)),
            )
            if i == 0:
                self.buttons.append(StartButton(*button_info))
            elif i == 39 * 1:
                self.buttons.append(MenuButton(*button_info))
            elif i == 39 * 2:
                self.buttons.append(QuitButton(*button_info))

    def draw_buttons(self):
        for button in self.buttons:
            self.screen.blit(
                button.imgs[0 if not button.hover else 1],
                (button.rect.x, button.rect.y),
            )

    def chosse_button(self):
        clock = pygame.time.Clock()
        pygame.display.update()
        redraw = False
        while 1:
            clock.tick(60)
            if redraw:
                self.draw_buttons()
                pygame.display.flip()
                redraw = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for button in self.buttons:
                            if button.rect.collidepoint(pos):
                                button.func()
                                return button

                for button in self.buttons:
                    h = button.hover
                    button.hover = button.rect.collidepoint(pos)
                    if not (button.hover == h):
                        redraw = True
                    

class Button:
    def __init__(self, imgs, pos):
        self.imgs = imgs
        self.hover = False
        self.rect = self.imgs[0].get_rect()
        self.rect.x, self.rect.y = pos


class StartButton(Button):
    def __init__(self, imgs, pos):
        super().__init__(imgs, pos)

    def func(self):
        pass  # TODO: start game


class QuitButton(Button):
    def __init__(self, imgs, pos):
        super().__init__(imgs, pos)

    def func(self):
        pygame.quit()
        quit()


class MenuButton(Button):
    def __init__(self, imgs, pos):
        super().__init__(imgs, pos)

    def func(self):
        pass  # TODO: do menu


# TODO: do hover func
