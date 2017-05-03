import pygame
import time

COLORS = [
    (0,0,0),
    (0,0,128),
    (0,128,0),
    (0,128,128),
    (128,0,0),
    (128,0,128),
    (128,128,0),
    (192,192,192),
    (128,128,128),
    (0,0,255),
    (0,255,0),
    (0,255,255),
    (255,0,0),
    (255,0,255),
    (255,255,0),
    (255,255,255)
]

class ConFont:
    def __init__(self):
        self.font = pygame.image.load('font.png')

        self.width = self.font.get_width() // 16
        self.height= self.font.get_height()// 16

        self.fonts = []
        self.font.set_colorkey((255,255,255),pygame.RLEACCEL)
        for color in COLORS:
            new = pygame.Surface(self.font.get_size())
            new.set_colorkey((0,32,0),pygame.RLEACCEL)
            new.fill(color)
            new.blit(self.font,(0,0))
            self.fonts.append(new)

    def __getitem__(self,(color,index)):
        x_index = index % 16
        y_index = index // 16

        return self.fonts[color].subsurface((x_index*self.width,y_index*self.height,self.width,self.height))

class TextConsole:
    def __init__(self,screen,font):
        self.screen = screen
        self.font = font

        self.width = self.screen.get_width() // self.font.width
        self.height= self.screen.get_height() // self.font.height

        self.cursor_x = 0
        self.cursor_y = 0
        self.fg = 7
        self.bg = 0

    def printf(self,text):
        for character in text:
            if character == '\n':
                self.do_newline()
            elif character == chr(9):
                self.cursor_x -= 1
            else:
                pygame.draw.rect(self.screen,COLORS[self.bg],
                    (self.cursor_x*self.font.width,
                     self.cursor_y*self.font.height,
                     self.font.width,
                     self.font.height)
                )
                self.screen.blit(self.font[self.fg,ord(character)],
                    (self.cursor_x*self.font.width,
                    self.cursor_y*self.font.height
                ))
                self.cursor_x += 1
                if self.cursor_x > self.width:
                    self.do_newlone()
        pygame.display.update()

    def do_newline(self):
        self.cursor_y += 1
        self.cursor_x = 0
        if self.cursor_y == self.height:
            self.cursor_y -= 1
            self.screen.blit(self.screen.copy(),(0,-self.font.height))

    def set_color(self,bg,fg):
        self.bg = bg
        self.fg = fg

    def getline(self,rep = lambda n:n):
        pygame.key.set_repeat(500,50)
        entry = ''
        cursor = False
        while True:
            c2 = (time.time() % 1) >= 0.5
            if c2 != cursor:
                cursor = not cursor
                if cursor:
                    self.printf(chr(22))
                else:
                    self.printf(chr(9)+' '+chr(9))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    raise SystemExit
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if cursor: self.printf(chr(9)+' '+chr(9))
                        self.printf('\n')
                        return entry
                    elif event.key == pygame.K_BACKSPACE:
                        if entry:
                            entry = entry[:-1]
                            if cursor: self.printf(chr(9)+' '+chr(9))
                            self.printf(chr(9)+' '+chr(9))
                            if cursor: self.printf(chr(22))
                    else:
                        if str(event.unicode):
                            entry += str(event.unicode)
                            if cursor: self.printf(chr(9)+' '+chr(9))
                            self.printf(rep(str(event.unicode)))
                            if cursor: self.printf(chr(22))

    def yesno(self,prompt):
        while True:
            self.printf(prompt)
            l = self.getline()
            if l.lower().startswith('y'): return True
            if l.lower().startswith('n'): return False
            self.printf('Please answer yes or no.\n')