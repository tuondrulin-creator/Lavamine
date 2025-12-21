#Importování knihoven
import pygame
import button
import os
import sys
import random #Pro lehké náhodné změny čísel u countru peněz, aby vypadal lépe
# ===Funkce===
def sound_play(sound): #zkrátí potřebu pro psaní celého příkazu
    pygame.mixer.Sound.play(sound)
def resource_path(relative_path): #Přemění absolutní cesty na relativní
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, relative_path)
#Počítadla📊
def peníze_counter(x, y):
    if peníze > 500 and not peníze == 9999:
        counter_img = counter_font.render (f"$Prachy: {int(peníze + random.randint(1,2))}", True, [40, 120, 10])
    else:
        counter_img = counter_font.render (f"$Prachy: {int(peníze)}", True, [40, 120, 10])   
    screen.blit(counter_img, (x, y))
def kamení_counter(x, y):
    counter_img = counter_font.render (f"Kamení: {int(kamení)}", True, [60, 60, 60])
    screen.blit(counter_img, (x, y))
def krystaly_counter(x, y):
    counter_img = counter_font.render (f"Krystaly: {int(krystaly)}", True, [200, 150, 170])
    screen.blit(counter_img, (x, y))
def show_counters(fontX, penízeY, kameníY, krystalyY):
    peníze_counter(fontX, penízeY)
    kamení_counter(fontX, kameníY)
    krystaly_counter(fontX, krystalyY)
def version_show(version_img):
    screen.blit(version_img, (0, 700))

# ===pygamesetup===
pygame.init()
pygame.mixer.init()
pygame.font.init()
icon = pygame.image.load(resource_path("assets/Lavamine_icon.png"))
pygame.display.set_icon(icon)
pygame.display.set_caption("Lavamine v0.5") #TODO: updatovat verze Lavamine při update
screen = pygame.display.set_mode((1280, 720))
#verze hry
version_font = pygame.font.Font("freesansbold.ttf", 20) 
version_img = version_font.render ("v 0.5.2dev 21.12.2025", True, [255, 100, 100]) #TODO: updatovat verzi a datum vydání verze
#načtení zvuků
click = pygame.mixer.Sound(resource_path("sound\click.ogg"))
click_logo = pygame.mixer.Sound(resource_path("sound/fnaf-freddys-nose-sound.ogg"))
explosion = pygame.mixer.Sound(resource_path("sound/fnaf-freddys-nose-sound.ogg")) #TODO: najít zvuk pro tohle a taky přidat kód do tlačítka pro zvuky
error = pygame.mixer.Sound(resource_path("sound\error.ogg"))
build = pygame.mixer.Sound(resource_path("sound\postavit.ogg"))
tower_build = pygame.mixer.Sound(resource_path("sound/tower.ogg"))
#nic_zvuk = pygame.mixer.Sound(resource_path("sound/nic.ogg"))
# ===načíst tlačítka===
start_img = pygame.image.load(resource_path("assets\Start_button.png")).convert_alpha()
exit_img = pygame.image.load(resource_path("assets\Exit_button.png")).convert_alpha()
settings_img = pygame.image.load(resource_path("assets\Settings_button.png")).convert_alpha()
background_img = pygame.image.load(resource_path("assets\Lavamine_back.png")).convert_alpha()
research_background_img = pygame.image.load(resource_path("assets\Research_back.png")).convert_alpha()
research_img = pygame.image.load(resource_path("assets\Vyzkum.png")).convert_alpha()
tutorial_img = pygame.image.load(resource_path("assets\Tutorial.png")).convert_alpha()
menu_img = pygame.image.load(resource_path("assets\Menu.png")).convert_alpha()
back_img = pygame.image.load(resource_path("assets\Back.png")).convert_alpha()
Lvl1_research_img = pygame.image.load(resource_path("assets\Lvl1.png")).convert_alpha()
sound_img = pygame.image.load(resource_path("assets\Sound_on.png")).convert_alpha()
crystalrsch_img = pygame.image.load(resource_path("assets\Crystal_upgrade.png")).convert_alpha()
tower_research_img = pygame.image.load(resource_path("assets\Tower_upgrade.png")).convert_alpha()
mining_upgrade_img = pygame.image.load(resource_path("assets/Mining_upgrade.png")).convert_alpha()
gamelogo_img = pygame.image.load(resource_path("assets\Lavamine_icon_high.png")).convert_alpha()
lavamine_img = pygame.image.load(resource_path("assets\Lavamine.png")).convert_alpha()
stonemine_img = pygame.image.load(resource_path("assets\Stonemine.png")).convert_alpha()
crystalmine_img = pygame.image.load(resource_path("assets\Crystalmine.png")).convert_alpha()

tower_img = pygame.image.load(resource_path("assets\TOWER.png")).convert_alpha()
#button instance
gamelogo = button.button(560, 130, gamelogo_img, 1)

start_button = button.button( 100, 140, start_img, 1) #použije tlačítko class pro udělání tlačítka 
exit_button = button.button( 800, 140, exit_img, 1)
settings_button = button.button( 440, 400, settings_img, 1)
background = button.button ( 0, 0, background_img, 1) #pozadí pro hlavní hru
research_background = button.button ( 0, 0, research_background_img, 1) #pozadí pro research obrazovku
tutorial_background = button.button ( 0, 0, tutorial_img, 1) #Pozadí pro tutorial
research_button = button.button( 993, 540, research_img, 0.8)
menu_button = button.button( 1082, 0, menu_img, 0.55)
back_button = button.button( 0, 0, back_img, 0.8)
sound_button = button.button( 250, 50, sound_img, 0.8)

lavamine = button.button(516, 350, lavamine_img, 1)
lavamine1 = button.button(1050, 320, lavamine_img, 1)
lavamine2 = button.button(765, 15, lavamine_img, 1)

stone_mine = button.button(300, 350, stonemine_img, 1)
stone_mine1 = button.button(300, 535, stonemine_img, 1)

crystal_mine = button.button(10, 112, crystalmine_img, 1)
crystal_mine1 = button.button(760, 360, crystalmine_img, 1)

tower = button.button(520, 68, tower_img, 1.2)

lvl1_research_button = button.button(360, 20, Lvl1_research_img, 0.9)
crystalrsch_button = button. button(360, 260, crystalrsch_img, 0.9 )
tower_research_button = button.button(360, 500, tower_research_img, 0.9)
mining_upgrade_button = button.button(760, 20, mining_upgrade_img, 0.9)
# ===počítadlo===
counter_font = pygame.font.Font("freesansbold.ttf", 36) #použije font pro počítadlo, kdyžtak se dá stáhnout a hodit do assets jiný font
fontX = 8
peníze_fontY = 430
kamení_fontY = 530
krystaly_fontY = 630
# ===proměnné===
#proměnné pro hru
peníze = 150
kamení = 0
krystaly = 0

lavamine_level = 0
lavamine1_level = 0
lavamine2_level = 0

stonemine_level = 0
stonemine1_level = 0

crystalmine_level = 0
crystalmine1_level = 0

tower_čekání = 0
čekání_counter = 0

lvl1_research = False
crystalrsch = False
tower_research = False
mining_upgrade = False

ending_screen = False
self_clicked_tutorial = True
played_tutorial = False
clicked_zvuk = 0
zvuk = "on"
fps = 20 #framerate
clock = pygame.time.Clock() #definuje hodiny

# definování proměn pro obrazovku
hlavní_hra = False
nastavení = False
research_screen = False
tutorial_screen = False

run = True #spustí loop
# ===🛞Hlavní loop===
while run:
    clicked_zvuk = clicked_zvuk + 1 #Pro tlačítko nastavení zvuku, aby šlo zmáčknout pouze 1 za frame
    if clicked_zvuk > 6: #Aby zbetečně nepřetíkala tato proměnná
        clicked_zvuk = 6
    for event in pygame.event.get(): #Event handler
        if event.type == pygame.QUIT: #Když event, který dostane je event pro zavření
            print("❌event pg.quit zavřel hru")
            run = False #Zastaví loop
            pygame.display.quit() #vypne display modul
            pygame.mixer.quit() #vypne zvukový modul
            pygame.quit() #vypne pygame
            sys.exit() #Zavře vše pomocí systému

    # materiálový příděl ⬇️ 
    if lavamine_level == 1:
        peníze = peníze + 0.5
    if lavamine_level == 2:
        peníze = peníze + 0.5
        peníze = peníze + 0.25
    if lavamine1_level == 1:
        peníze = peníze + 0.5
    if lavamine1_level == 2:
        peníze = peníze +0.5
        peníze = peníze +0.25
    if lavamine2_level == 1:
        peníze = peníze + 0.5
    if lavamine2_level == 2:
        peníze = peníze +0.5
        peníze = peníze +0.25
    if mining_upgrade == True:
        peníze = peníze - 0.25
    if stonemine_level == 1:
        kamení = kamení + 0.5
        if mining_upgrade == True:
            kamení = kamení + 0.25
    if stonemine1_level == 1:
        kamení = kamení + 0.5 
        if mining_upgrade == True:
            kamení = kamení + 0.25
    if crystalmine_level == 1:
        krystaly = krystaly + 0.25
        if mining_upgrade == True:
            krystaly = krystaly + 0.25
    if crystalmine1_level == 1:
        krystaly = krystaly + 0.25
        if mining_upgrade == True:
            krystaly = krystaly + 0.25

    if peníze > 9999: #Zastaví maximální peníze, ať nepřeteče ten counter mimo obrazovku
        peníze = 9999 
    if kamení > 9999: #stejný důvod
        kamení = 9999
    if krystaly > 9999: #stejný důvod
        krystaly = 9999
    
    if tower_research == "čeká":
        tower_čekání = tower_čekání + 1
        if tower_čekání == 25:
            tower_research = "postavena"

    #renderovat hru tady⬇️
    screen.fill("orange")
    version_show(version_img)
    #toto zabrání aby hned po tutorialu si omylem něco zmáčknul
    if hlavní_hra == "čeká":
        čekání_counter = čekání_counter + 1
        if tutorial_background.draw(screen):
            print()
        if čekání_counter == 5:
            hlavní_hra = True
    # === tlačítka ===
    if hlavní_hra == False: #Pokud jsem v menu ukáže se
        if start_button.draw(screen): #pokud je true proměnná action, udělá věci
            print("🧩Tlačítko START zmáčknuto")
            sound_play(click)
            if played_tutorial == True: 
                hlavní_hra = True
            elif played_tutorial == False:
                hlavní_hra = "ostatní"
                tutorial_screen = True
                print("🧩START zahajuje tutorial 1/2")
            else:
                print("❌Tlačítko start neví co udělat")
            start_img = pygame.image.load(resource_path("assets\Start1.png")).convert_alpha()
            start_button = button.button( 100, 140, start_img, 1)
        if exit_button.draw(screen):
            print("🧩Tlačítko EXIT zmáčknuto")
            run = False
        if settings_button.draw(screen):
            print("🧩Tlačítko NASTAVENÍ zmáčknuto")
            sound_play(click)
            nastavení = True
            hlavní_hra = "ostatní"
        if gamelogo.draw(screen):
            print("🧩Tlačítko LOGO zmáčknuto")
            sound_play(click_logo)

    if hlavní_hra == True: # Pokud jsem v hlavní hře, ukáže se
        background.draw(screen)
        if research_button.draw(screen):
            print("🧩Tlačítko VÝZKUM zmáčknuto")
            research_screen = True #otevře menu výzkumu
            sound_play(click)
            hlavní_hra = ("ostatní") #zavře ostatní věci
        if menu_button.draw(screen):
            print("🧩Tlačítko MENU (Hlavní) zmáčknuto")
            sound_play(click)
            hlavní_hra = False #hodí zpět do hlavního menu
        # === Stavby ===
        if lavamine.draw(screen): #První Lavamine
            if lavamine_level == 0 and peníze > 149: #Pokud je level 1 a peníze jsou 150+
                sound_play(build)
                print("🛠️Lavamine postaven")
                peníze = peníze - 150 #odečte peníze a změní si sprite a dá se na lvl 1
                lavamine_img = pygame.image.load(resource_path("assets\Lavamine_1.png")).convert_alpha()
                lavamine = button.button(516, 350, lavamine_img, 1)
                lavamine_level = 1
            if lavamine_level == 1 and peníze > 299 and kamení > 99 and lvl1_research == True:
                sound_play(build)
                print("🛠️Lavamine upgrade na lvl 1")
                peníze = peníze - 300 #odečte peníze a kamení a změní si sprite a dá se na lvl 2
                kamení = kamení - 100
                lavamine_img = pygame.image.load(resource_path("assets\Lavamine_2.png")).convert_alpha()
                lavamine = button.button(516, 350, lavamine_img, 1)
                lavamine_level = 2 
        if lavamine1.draw(screen): #Druhý Lavamine
            if lavamine1_level == 0 and peníze > 149: #Pokud je level 1 a peníze jsou 150+
                sound_play(build)
                print("🛠️Lavamine1 postaven")
                peníze = peníze - 150 #odečte peníze a změní si sprite a dá se na lvl 1
                lavamine_img = pygame.image.load(resource_path("assets\Lavamine_1.png")).convert_alpha()
                lavamine1 = button.button(1050, 320, lavamine_img, 1)
                lavamine1_level = 1
            if lavamine1_level == 1 and peníze > 299 and kamení > 99 and lvl1_research == True:
                sound_play(build)
                print("🛠️Lavamine1 upgrade na lvl 1")
                peníze = peníze - 300 #odečte peníze a kamení a změní si sprite a dá se na lvl 2
                kamení = kamení - 100
                lavamine_img = pygame.image.load(resource_path("assets\Lavamine_2.png")).convert_alpha()
                lavamine1 = button.button(1050, 320, lavamine_img, 1)
                lavamine1_level = 2 
        if lavamine2.draw(screen): #Druhý Lavamine
            if lavamine2_level == 0 and peníze > 149: #Pokud je level 1 a peníze jsou 150+
                sound_play(build)
                print("🛠️Lavamine2 postaven")
                peníze = peníze - 150 #odečte peníze a změní si sprite a dá se na lvl 1
                lavamine_img = pygame.image.load(resource_path("assets\Lavamine_1.png")).convert_alpha()
                lavamine2 = button.button(765, 15, lavamine_img, 1)
                lavamine2_level = 1
            if lavamine2_level == 1 and peníze > 299 and kamení > 99 and lvl1_research == True:
                sound_play(build)
                print("🛠️Lavamine2 upgrade na lvl 1")
                peníze = peníze - 300 #odečte peníze a kamení a změní si sprite a dá se na lvl 2
                kamení = kamení - 100
                lavamine_img = pygame.image.load(resource_path("assets\Lavamine_2.png")).convert_alpha()
                lavamine2 = button.button(765, 15, lavamine_img, 1)
                lavamine2_level = 2 
        if crystalrsch == True:
            if crystal_mine.draw(screen):
                if crystalmine_level == 0 and peníze > 799 and kamení > 399 and crystalrsch == True:
                    sound_play(build)
                    print("🛠️Crystalmine postaven")
                    peníze = peníze - 800
                    kamení = kamení - 400
                    crystalmine_img = pygame.image.load(resource_path("assets\Crystalmine2.png")).convert_alpha()
                    crystal_mine = button.button(10, 112, crystalmine_img, 1)
                    crystalmine_level = 1
            if crystal_mine1.draw(screen):
                if crystalmine1_level == 0 and peníze > 799 and kamení > 399 and crystalrsch == True:
                    sound_play(build)
                    print("🛠️Crystalmine1 postaven")
                    peníze = peníze - 800
                    kamení = kamení - 400
                    crystalmine_img = pygame.image.load(resource_path("assets\Crystalmine1.png")).convert_alpha()
                    crystal_mine1 = button.button(760, 360, crystalmine_img, 1)
                    crystalmine1_level = 1

        if stone_mine.draw(screen):
            if stonemine_level == 0 and peníze > 199:
                sound_play(build)
                print("🛠️Stonemine postaven")
                peníze = peníze - 200
                stonemine_img = pygame.image.load(resource_path("assets\Stonemine_1.png")).convert_alpha()
                stone_mine = button.button(300, 350, stonemine_img, 1)
                stonemine_level = 1
        if stone_mine1.draw(screen):
            if stonemine1_level == 0 and peníze > 199:
                sound_play(build)
                print("🛠️Stonemine1 postaven")
                peníze = peníze - 200
                stonemine_img = pygame.image.load(resource_path("assets\Stonemine_1.png")).convert_alpha()
                stone_mine1 = button.button(300, 535, stonemine_img, 1)
                stonemine1_level = 1
        # ========VĚŽ========
        if tower_research == True or tower_research == "postavena":
            if tower.draw(screen):
                if peníze > 3499 and kamení > 1499 and krystaly > 799 and tower_research == True:
                    sound_play(tower_build)
                    print("😈VĚŽ POSTAVENA!")
                    peníze = peníze - 3500
                    kamení = kamení - 1500
                    krystaly = krystaly - 800
                    tower_research = "čeká"
                    tower_img = pygame.image.load(resource_path("assets\TOWER1.png")).convert_alpha()
                    tower = button.button(520, 68, tower_img, 1.2)
                if tower_research == "postavena":
                    sound_play(explosion)
                    print("🧩VĚŽ zahajuje ending")
                    hlavní_hra = "ostatní"
                    ending_screen = True
        #verze
        version_show(version_img)
        #Počítadla 📊
        show_counters(fontX, peníze_fontY, kamení_fontY, krystaly_fontY)
    #Ostatní menu
    if research_screen == True:
        research_background.draw(screen)
        if back_button.draw(screen):
            print("🧩Tlačítko ZPĚT (VÝZKUM) zmáčknuto")
            sound_play(click)
            research_screen = False #zavře research screen
            hlavní_hra = True #otevře hlavní hru
        if lvl1_research_button.draw(screen) and peníze > 499 and lvl1_research == False: 
            print("🧩Tlačítko LVL1 výzkum zmáčknuto")
            sound_play(click)
            lvl1_research = True #umožní stavět lvl1 budovy
            peníze = peníze - 500
            Lvl1_research_img = pygame.image.load(resource_path("assets\Lvl1_bought.png")).convert_alpha() #změní obrázek
            lvl1_research_button = button.button(360, 20, Lvl1_research_img, 0.9) #updatne svůj vzhled
        if crystalrsch_button.draw(screen) and peníze > 599 and kamení > 349 and crystalrsch == False: 
            print("🧩Tlačítko CRYSTAL výzkum zmáčknuto")
            sound_play(click)
            crystalrsch = True #umožní stavět krystalové budovy
            peníze = peníze - 600
            kamení = kamení - 350
            crystalrsch_img = pygame.image.load(resource_path("assets/Crystal_upgrade_bought.png")).convert_alpha() #změní obrázek
            crystalrsch_button = button.button(360, 260, crystalrsch_img, 0.9) #updatne svůj vzhled
        if tower_research_button.draw(screen) and peníze > 2499 and kamení > 799 and krystaly > 499 and tower_research == False: 
            print("🧩Tlačítko VĚŽ výzkum zmáčknuto")
            hlavní_hra = "čeká"
            sound_play(error)
            tower_research = True #umožní stavět VĚŽ
            peníze = peníze - 2500
            kamení = kamení - 800
            krystaly = krystaly - 500
            tower_research_img = pygame.image.load(resource_path("assets/Tower_upgrade_bought.png")).convert_alpha() #změní obrázek
            tower_research_button = button.button(360, 500, tower_research_img, 0.9)#updatne svůj vzhled
        if mining_upgrade_button.draw(screen) and peníze > 499 and kamení > 199 and krystaly > 99 and mining_upgrade == False: 
            print("🧩Tlačítko MINING výzkum zmáčknuto")
            sound_play(click)
            mining_upgrade = True #Na začátku kódu odebere peníze a přidá krystaly a kamení
            peníze = peníze - 500
            kamení = kamení - 200
            krystaly = krystaly - 100
            mining_upgrade_img = pygame.image.load(resource_path("assets/Mining_upgrade_bought.png")).convert_alpha() #změní obrázek
            mining_upgrade_button = button.button(760, 20, mining_upgrade_img, 0.9) #updatne svůj vzhled
        #verze
        version_show(version_img)  
        #Počítadla 📊
        show_counters(fontX, peníze_fontY, kamení_fontY, krystaly_fontY)

    if nastavení == True:
        if menu_button.draw(screen):
            print("🧩Tlačítko MENU (Nastavení) zmáčknuto")
            sound_play(click)
            hlavní_hra = False
            nastavení = False  
        if sound_button.draw(screen):
            print("🧩Tlačítko ZVUK zmáčknuto")
            if zvuk == "off" and clicked_zvuk > 3:
                zvuk = "on"
                click = pygame.mixer.Sound(resource_path("sound\click.ogg"))
                build = pygame.mixer.Sound(resource_path("sound\postavit.ogg"))
                tower_build = pygame.mixer.Sound(resource_path("sound/tower.ogg"))
                click_logo = pygame.mixer.Sound(resource_path("sound/fnaf-freddys-nose-sound.ogg"))
                error = pygame.mixer.Sound(resource_path("sound\error.ogg"))
                sound_play(click)
                sound_img = pygame.image.load(resource_path("assets\Sound_on.png")).convert_alpha()
                sound_button = button.button( 250, 50, sound_img, 0.8)
                print ("🔊Zvuk zapnut")
                clicked_zvuk = 0
            elif zvuk == "on" and clicked_zvuk > 3:
                zvuk = "off"
                click = pygame.mixer.Sound(resource_path("sound/nic.wav"))
                build = pygame.mixer.Sound(resource_path("sound/nic.wav"))
                tower_build = pygame.mixer.Sound(resource_path("sound/nic.wav"))
                click_logo = pygame.mixer.Sound(resource_path("sound/nic.wav"))
                error = pygame.mixer.Sound(resource_path("sound/nic.wav"))
                sound_img = pygame.image.load(resource_path("assets\Sound_off.png")).convert_alpha()
                sound_button = button.button( 250, 50, sound_img, 0.8)
                print("🔇Zvuk vypnut")
                clicked_zvuk = 0
    if tutorial_screen == True:
        if tutorial_background.draw(screen):
                if pygame.mouse.get_pressed()[0] == 1 and self_clicked_tutorial == False and played_tutorial == False: #zabraňuje tomu aby držení myši okamžitě přskočilo tutorial, myš musí být zmáčknuta znovu
                    self_clicked_tutorial = True #Zastaví další zmáčknutí
                    print("🧩TUTORIAL zmáčknut 2/2")
                    tutorial_img = pygame.image.load(resource_path("assets\Tutorial1.png")).convert_alpha()
                    tutorial_background = button.button ( 0, 0, tutorial_img, 1)
                    played_tutorial = True
                    self_clicked_tutorial = True
                elif pygame.mouse.get_pressed()[0] == 1 and self_clicked_tutorial == False and played_tutorial == True: #pokud je myš zmáčknuta po 2. tak se tohle spustí
                    print("🧩TUTORIAL zmáčknut (tutorial dokončen)")
                    hlavní_hra = "čeká"
                    tutorial_screen = False
                else:
                    self_clicked_tutorial = False #odklikne tlačítko, aby se mohlo znovu zmáčknout
        #Tutorial text
        if played_tutorial == False:
            tutorial_text1 = counter_font.render ("Ahoj, já jsem Helperbot 3!", True, [0, 0, 0]) #tady napsat text a barvu
            screen.blit(tutorial_text1, (25, 40)) #ukáže text
            tutorial_text2 = counter_font.render ("Mým cílem je ti pomoct s vytěžením všeho co tu je.", True, [0, 0, 0]) 
            screen.blit(tutorial_text2, (25, 90)) 
            tutorial_text3 = counter_font.render ("Tak pojď na to!", True, [0, 0, 0]) 
            screen.blit(tutorial_text3, (25, 140))
        else:
            tutorial_text4 = counter_font.render ("Je to velmi lehké, takže řeknu jenom začátek.", True, [0, 0, 0]) 
            screen.blit(tutorial_text4, (25, 40))
            tutorial_text5 = counter_font.render ("Toto je panel se zdroji, ukazuje kolik máte zdrojů.", True, [0, 0, 0]) 
            screen.blit(tutorial_text5, (10, 200))
            tutorial_text6 = counter_font.render ("Toto je Lavamine, postav ho pro více peněz.", True, [0, 0, 0]) 
            screen.blit(tutorial_text6, (470, 280))
            tutorial_text7 = counter_font.render ("To je vše, zbytek určitě zvládnete, tak čau!", True, [0, 0, 0]) 
            screen.blit(tutorial_text7, (500, 600))
    if ending_screen == True:
        ending_text1 = counter_font.render ("Ending je WIP, děkuji za hraní!", True, [0, 0, 0]) 
        screen.blit(ending_text1, (25, 40))

    pygame.display.update()
    clock.tick(fps)
print("❌Konec loopu")
pygame.display.quit() #vypne display modul
pygame.mixer.quit() #vypne zvukový modul
pygame.quit() #vypne pygame
sys.exit() #Zavře vše pomocí systému
