import pygame

#tlačítko class
class button():
    def __init__(self, x, y, image, scale): #Dostane všechny proměnné
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale), int(height*scale))) #můj obrázek = peoměná obrázek (jako nevidíš to?)
        self.rect = self.image.get_rect() # udělá obdélník z můj obrázek
        self.rect.topleft = (x, y) #nastaví roh obdélníku na x, y
        self.clicked = False
    def draw(self, surface): #funkce pro "namalování" sama sebe používá se x.button.draw() a pak u button instance se doplní proměnné
        surface.blit(self.image, (self.rect.x, self.rect.y)) #"Nakreslí" tlačíko
        action = False #neudělal akci
        pos_mouse = pygame.mouse.get_pos() #ukládá pozici myši
        if self.rect.collidepoint(pos_mouse):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: #Když je zmáčknutá myš poprvé
                self.clicked = True #Zastaví další zmáčknutí
                action = True #udělal akci
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        return action #Vyhodí pokdu tlačítko udělalo akci, nebo ne 