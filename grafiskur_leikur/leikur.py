import pygame
import time
import random

pygame.init()

######## LITIR ########
white = (255,255,255)
black = (0,0,0)
grey = (220,220,220)
red = (220,20,60)

######## SKJÁR ########
display_breidd = 800
display_haed = 600
gameDisplay = pygame.display.set_mode((display_breidd,display_haed))
pygame.display.set_caption('Haraldur Pottur og félagar í háska')

######## MYNDIR ########
harryImage = pygame.image.load('harry.png')
harryImage2 = pygame.image.load('harrylitill.png')
harry_breidd = 96
harry_haed = 128
hermioneImage = pygame.image.load('hermione.png')
hermioneImage2 = pygame.image.load('hermionelitil.png')
ginnyImage = pygame.image.load('ginny.png')
ginnyImage2 = pygame.image.load('ginnylitil.png')
dumbledoreImage = pygame.image.load('dumbledore.jpg')
ronImage = pygame.image.load('ron.png')
ronImage2 = pygame.image.load('ronlitill.png')
vitsugaImage = pygame.image.load('vitsugalitil.png')
voldemortImage = pygame.image.load('voldemort.png')
bakgrunnurGameIntro = pygame.image.load('kastali1.jpg')
bakgrunnurGameLevel1 = pygame.image.load('level1.jpg')
bakgrunnurGameLevel2 = pygame.image.load('himinn.jpg')
bakgrunnurGameLevel2 = pygame.transform.scale(bakgrunnurGameLevel2,(display_breidd,display_haed))
bakgrunnurGameLevel3 = pygame.image.load('level3.jpg')
bakgrunnurGameLevel3b = pygame.image.load('level3b.png')
bakgrunnurGameLevel3Win = pygame.image.load('level3Win.jpg')
bakgrunnurGamelevel4 = pygame.image.load('level4.jpg')
bakgrunnurGameDone = pygame.image.load('done.jpg')
lykill = pygame.image.load('lykill.png')
lykill_x = 25
lykill_y = 22

######## ANNAÐ ########
clock = pygame.time.Clock()
font = pygame.font.Font('Raleway.ttf', 30)

######## LEVELS ########
def leikurIntro():
    intro1 = True
    while intro1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(bakgrunnurGameIntro, (0,0))
        messageDisplayIntro('Haraldur Pottur og felagar i haska')
        takkar("Hefja Leik",337,450,150,75,white,grey,'StartLevel1')
        pygame.display.update()
        clock.tick(10)

def level1Intro():
    intro2 = True
    while intro2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bakgrunnurGameIntro, (0,0))
        messageDisplayLevel('Velkomin/nn í leikinn svaðilfari!',9)
        messageDisplayLevel('Við erum staðsett í Diagon Alley', 4.5)
        messageDisplayLevel('Vilt þú velja persónu?', 3)
        takkar("Já!",150,450,150,75,white,grey,'StartLevel1B')
        takkar("Nei",550,450,150,75,white,grey,'quit')
        pygame.display.update()
        clock.tick(10)

def level1():
    level1 = True
    while level1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bakgrunnurGameLevel1, (0,0))
        messageDisplayLevel('Velkomin/nn í búningaherbergið!',9)
        messageDisplayLevel('Vilt þú vera töframaður eða norn?',4.5)
        takkar("Norn",150,350,165,75,white,grey,'norn')
        takkar("Töframaður",550,350,165,75,white,grey,'toframadur')
        pygame.display.update()
        clock.tick(10)

def level1NORN():
    norn = True
    while norn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bakgrunnurGameLevel1, (0,0))
        messageDisplayLevel('Hvaða norn villt þú vera?',9)
        gameDisplay.blit(hermioneImage,(135,160))
        gameDisplay.blit(ginnyImage,(535,160))
        takkar("Hermína",150,450,165,75,white,grey,'hermione')
        takkar("Guðrún",550,450,165,75,white,grey,'ginny')
        pygame.display.update()
        clock.tick(10)

def level1TOFRAMADUR():
    toframadur = True
    while toframadur:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bakgrunnurGameLevel1, (0,0))
        messageDisplayLevel('Hvaða töframaður villt þú vera?',9)
        gameDisplay.blit(harryImage,(135,160))
        gameDisplay.blit(ronImage,(535,160))
        takkar("Haraldur",150,450,165,75,white,grey,'harry')
        takkar("Rúnar",550,450,165,75,white,grey,'ron')
        pygame.display.update()
        clock.tick(10)

def level2Intro():
    intro3 = True
    while intro3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bakgrunnurGameIntro, (0,0))
        messageDisplayLevel('Þú ert á Quidditch æfingu fljúgjandi um loftin',9)
        messageDisplayLevel('blá þegar þú sérð að vitsugur eru að elta þig!',5.5)
        messageDisplayLevel('Þú hefur 20 sekúndur til að fljúga strax aftur',3.9)
        messageDisplayLevel('niður á völlinn áður en vitsugurnar ná þér, notaðu',3.1)
        messageDisplayLevel('örvatakanna til að hreyfa þig til hægri eða vinstri.',2.5)
        messageDisplayLevel('Passaðu að detta ekki af kústinum!',2.1)
        takkar("Byrja!",150,450,150,75,white,grey,'StartLevel2')
        takkar("Hætta",550,450,150,75,white,grey,'quit')
        pygame.display.update()
        clock.tick(10)

def level2():
    #upphafsstaður á persónunni
    x = (display_breidd*0.45)
    y = (display_haed*0.7)
    x_change = 0
    #Timer MUNA AÐ BREYTA TÍMANUM
    counter, teljari = 20, '20'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.Font('Raleway.ttf', 30)

    #Stærðin og hreyfing á vitsugum
    vitsuga_startx = random.randrange(0,display_breidd)
    vitsuga_starty = -600
    vitsuga_speed = 12
    vitsugahaed = 64
    vitsugabreidd = 72
    #Lykkjan sem keyrir leikinn
    level2 = False
    while not level2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.USEREVENT:
                counter -=1
                teljari = str(counter).rjust(3) if counter > 0 else level2WIN()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -3
                elif event.key == pygame.K_RIGHT:
                    x_change = 3
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        x += x_change
        #Teikna allt á skjáinn
        gameDisplay.blit(bakgrunnurGameLevel2, (0,0))
        gameDisplay.blit(font.render(teljari, True, (0, 0, 0)), (30, 40))
        vitsuga(vitsuga_startx, vitsuga_starty, vitsugabreidd, vitsugahaed)
        vitsuga_starty += vitsuga_speed
        personaMynd(x,y)
        #Þegar Harry klessir á endann á skjánum
        if x > display_breidd-harry_breidd or x < 0:
            crashBoundary()
        #Hreyfingin á vitsugunum
        if vitsuga_starty > display_haed:
            vitsuga_starty = 0 - vitsugahaed
            vitsuga_startx = random.randrange(0,display_breidd)
        #Þegar Harry klessir á vitsugu
        if y < vitsuga_starty+vitsugahaed:
            if x > vitsuga_startx and x < vitsuga_startx + vitsugabreidd or x + harry_breidd > vitsuga_startx and x + harry_breidd < vitsuga_startx + vitsugabreidd:
                crash()
        pygame.display.update()
        clock.tick(60)

def level2WIN():
    level2W = True
    while level2W:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(bakgrunnurGameIntro, (0,0))
        messageDisplayLevel('Hjúkk! Þú náðir niður á völlinn án þess',9)
        messageDisplayLevel('að vitsugurnar náðu þér!',5.5)
        pygame.display.update()
        #ATH er hægt að nota ehv annað????
        pygame.time.wait(5000)
        level3Intro()

def level3Intro():
    intro4 = True
    while intro4:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bakgrunnurGameIntro, (0,0))
        messageDisplayLevel('Ó nei! Eftir að hafa kíkt á klukkuna áttar þú',9)
        messageDisplayLevel('þig á að þú ert orðin alltof seinn í lokapróf.',5.5)
        messageDisplayLevel('Þú þarft að svara öllum spurningum á prófinu ',3.9)
        messageDisplayLevel('rétt, annars ertu fallinn!',3.1)
        takkar("Byrja á prófinu!",150,450,210,75,white,grey,'StartLevel3')
        takkar("Hætta",460,450,210,75,white,grey,'quit')
        pygame.display.update()
        clock.tick(10)

def level3():
    level3 = True
    while level3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bakgrunnurGameLevel3, (0,0))
        messageDisplayLevel('Þú mætir í kennslustofuna og',9)
        messageDisplayLevel('sérð 4 bunka af prófum á kennara-',5.5)
        messageDisplayLevel('borðinu. Veldu eitt próf til',3.9)
        messageDisplayLevel('að reyna við.',3.1)
        takkar("Próf 1",88,350,90,120,white,grey,'1')
        takkar("Próf 2",266,350,90,120,white,grey,'2')
        takkar("Próf 3",444,350,90,120,white,grey,'3')
        takkar("Próf 4",622,350,90,120,white,grey,'4')
        pygame.display.update()
        clock.tick(10)

def level3HP():
    level3HP = True
    while level3HP:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bakgrunnurGameLevel3, (0,0))
        messageDisplayLevel('Þú hefur valið próf sem hentar',9)
        messageDisplayLevel('vel fyrir Harald.',5.5)
        takkar("Hefja Próf",150,400,225,75,white,grey,'HP1')
        takkar("Velja annað próf",475,400,225,75,white,grey,'StartLevel3')
        pygame.display.update()
        clock.tick(10)

def level3HG():
    level3HG = True
    while level3HG:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bakgrunnurGameLevel3, (0,0))
        messageDisplayLevel('Þú hefur valið próf sem hentar',9)
        messageDisplayLevel('vel fyrir Hermínu.',5.5)
        takkar("Hefja Próf",150,400,225,75,white,grey,'HG1')
        takkar("Velja annað próf",475,400,225,75,white,grey,'StartLevel3')
        pygame.display.update()
        clock.tick(10)

def level3RV():
    level3RV = True
    while level3RV:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bakgrunnurGameLevel3, (0,0))
        messageDisplayLevel('Þú hefur valið próf sem hentar',9)
        messageDisplayLevel('vel fyrir Rúnar.',5.5)
        takkar("Hefja Próf",150,400,225,75,white,grey,'RV1')
        takkar("Velja annað próf",475,400,225,75,white,grey,'StartLevel3')
        pygame.display.update()
        clock.tick(10)

def level3GV():
    level3GV = True
    while level3GV:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bakgrunnurGameLevel3, (0,0))
        messageDisplayLevel('Þú hefur valið próf sem hentar',9)
        messageDisplayLevel('vel fyrir Guðrúnu.',5.5)
        takkar("Hefja Próf",150,400,225,75,white,grey,'GV1')
        takkar("Velja annað próf",475,400,225,75,white,grey,'StartLevel3')
        pygame.display.update()
        clock.tick(10)

def level3Win():
    level3HG = True
    while level3HG:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bakgrunnurGameLevel3Win, (0,0))
        messageDisplayLevel3('Til hamingju! þú stóðst lokaprófið!!',2.5)
        messageDisplayLevel3('Þú hefur útskrifast úr Hogwartsskóla',2.2)
        pygame.display.update()
        pygame.time.wait(5000)
        level4Intro()

def level4Intro():
    intro5 = True
    while intro5:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bakgrunnurGameIntro, (0,0))
        messageDisplayLevel('Þú labbar út úr lokaprófinu að harðlæstum',9)
        messageDisplayLevel('útidyrum að Hogwartsskóla.',5.5)
        messageDisplayLevel('Bjargaðu sumrinu með því að safna 15 lyklum',3.9)
        messageDisplayLevel('áður en tíminn rennur út!',3.1)
        messageDisplayLevel('Notaðu örvatakkana til að hreyfa þig', 2.5)
        takkar("Byrja á prófinu!",150,450,210,75,white,grey,'StartLevel4')
        takkar("Hætta",460,450,210,75,white,grey,'quit')
        pygame.display.update()
        clock.tick(10)

def level4():
    tonlist()
    x = 300
    y = 300
    x_change = 0
    y_change = 0
    counter, teljari = 30, '30'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    stig = 0
    winner = 15

    randLykill_x = random.randrange(0, display_breidd-lykill_x)
    randLykill_y = random.randrange(0, display_haed-lykill_y)
    level4 = False
    while not level4:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #Teljari
            if event.type == pygame.USEREVENT:
                counter -=1
                teljari = str(counter).rjust(3) if counter > 0 else crashBoundary2()
            # hreyfir persónu til hliðar, upp og niður
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -10
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = 10
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = - 10
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = 10
                    x_change = 0

        x += x_change
        y += y_change

        #Þegar persóna klessir á endann á skjánum
        if x > display_breidd-harry_breidd or x < 0:
            crashBoundary2()
        if y > display_haed-harry_haed or y < 0:
            crashBoundary2()

        #Þegar persóna nær lykli

        #gameDisplay.blit(bakgrunnurGamelevel4, (0,0))
        gameDisplay.fill(white)
        personaMynd(x,y)
        gameDisplay.blit(lykill,(randLykill_x,randLykill_y))
        gameDisplay.blit(font.render(teljari, True, (0, 0, 0)), (30, 40))
        stigafjoldi(stig)
        pygame.display.update()
        if x > randLykill_x and x < randLykill_x + lykill_x or x + harry_breidd > randLykill_x and x + harry_breidd < randLykill_x + lykill_x:
            stig += 1
            randLykill_x = random.randrange(0, display_breidd-lykill_x)
            randLykill_y = random.randrange(0, display_haed-lykill_y)
        if stig == winner:
            level4WIN()
        clock.tick(20)

def level4WIN():
    level4Win = True
    while level4Win:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bakgrunnurGameDone, (0,0))
        messageDisplayIntro('Gledilegt sumar!')
        pygame.display.update()
        pygame.time.wait(5000)
        pygame.quit()
        quit()




######## ANNAÐ ########
def tonlist():
    pygame.mixer.music.load('hplag.wav')
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.mixer.music.play(-1)

def win():
    pygame.mixer.music.load('win.wav')
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.mixer.music.play()

def wrong():
    pygame.mixer.music.load('wrong.wav')
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.mixer.music.play()

def laugh():
    pygame.mixer.music.load('EvilLaugh.wav')
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.mixer.music.play()

def klapp():
    pygame.mixer.music.load('klapp.wav')
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.mixer.music.play()

def stigafjoldi(stig):
    stigTexti = font.render("Stig: "+str(stig), True, black)
    gameDisplay.blit(stigTexti,[0,0])

def hermione():
    hermione = True
    while hermione:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(grey)
        gameDisplay.blit(hermioneImage,(298,300))
        messageDisplayLevel('Þú hefur valið bráðkláran mugga sem má líkja við',9)
        messageDisplayLevel('gangandi orðabók. Þegar kemur að erfiðum',5.5)
        messageDisplayLevel('tímum er ávallt hægt að stóla á visku hennar',3.9)
        messageDisplayLevel('til þess að sigrast á öllum áskorunum.',3.1)
        pygame.display.update()
        pygame.time.wait(10000)
        level2Intro()

def ginny():
    ginny = True
    while ginny:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(grey)
        gameDisplay.blit(ginnyImage,(298,300))
        messageDisplayLevel('Þú hefur valið einn úr Vilmundarættinni!',9)
        messageDisplayLevel('Guðrún er kraftmikil og öflug galdrakona sem',5.5)
        messageDisplayLevel('ræður við erfiða galdra og er ein af bestu',3.9)
        messageDisplayLevel('"Quidditch" spilurum Hogwarts.',3.1)
        pygame.display.update()
        pygame.time.wait(10000)
        level2Intro()

def ron():
    ron = True
    while ron:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(grey)
        gameDisplay.blit(ronImage,(298,300))
        messageDisplayLevel('Þú kemur frá stórri galdraætt sem er hvað',9)
        messageDisplayLevel('þekktust fyrir sitt eldrauða hár. Alltaf er hægt',5.5)
        messageDisplayLevel('að treysta á skopskyn og hæfileika þína að',3.9)
        messageDisplayLevel('hugsa út fyrir kassann í erfiðum aðstæðum.',3.1)
        pygame.display.update()
        pygame.time.wait(10000)
        level2Intro()

def harry():
    harry = True
    while harry:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(grey)
        gameDisplay.blit(harryImage,(298,300))
        messageDisplayLevel('Hinn útvaldi! þú hefur ekki átt sjö dagana sæla.',9)
        messageDisplayLevel('Þú hefur barist við sjálfan Lávarð Valdimar og',5.5)
        messageDisplayLevel('býrð því að mikilli reynslu. Sjálfur ertu fljótur',3.9)
        messageDisplayLevel('á fótum og ræður við galdra sem fáir jafnaldrar',3.1)
        messageDisplayLevel('þínir þora að kljást við.',2.5)
        pygame.display.update()
        pygame.time.wait(10000)
        level2Intro()

def crashBoundary():
    crashB = True
    while crashB:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bakgrunnurGameLevel2, (0,0))
        messageDisplayLevel('Ó nei! þú dast af kústinum!',9)
        messageDisplayLevel('Vilt þú reyna aftur?',5.5)
        takkar("Já!",150,450,165,75,white,grey,'StartLevel2')
        takkar("Nei",550,450,165,75,white,grey,'quit')
        pygame.display.update()
        clock.tick(10)

def crashBoundary2():
    crashB = True
    while crashB:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bakgrunnurGamelevel4, (0,0))
        messageDisplayLevel('Ó nei! Þú náðir ekki öllum lyklunum í tæka tíð ',3.9)
        messageDisplayLevel('Vilt þú reyna aftur?',3.1)
        takkar("Já!",150,450,165,75,white,grey,'StartLevel4')
        takkar("Nei",550,450,165,75,white,grey,'quit')
        pygame.display.update()
        clock.tick(10)

def crash():
    crash = True
    while crash:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bakgrunnurGameLevel2, (0,0))
        messageDisplayLevel('Ó nei! Vitsuga náði þér!',9)
        messageDisplayLevel('Vilt þú reyna aftur?',5.5)
        takkar("Já!",150,450,165,75,white,grey,'StartLevel2')
        takkar("Nei",550,450,165,75,white,grey,'quit')
        pygame.display.update()
        clock.tick(10)

def vitsuga(vitsugax, vitsugay,vitsuga_breidd,vitsuga_haed):
    gameDisplay.blit(vitsugaImage,(vitsugax, vitsugay,vitsuga_breidd,vitsuga_haed))

def personaMynd(x,y):
        gameDisplay.blit(harryImage2,(x,y))

def rangt():
    laugh()
    rangt = True
    while rangt:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bakgrunnurGameLevel3, (0,0))
        gameDisplay.blit(voldemortImage,(330,160))
        messageDisplayLevel('Nú ert þú í klófestiu Lávarðs Valdimars',9)
        messageDisplayLevel('og ert hér með gerður brottrækur úr Hogwarts',5.5)
        takkar("Byrja aftur",150,450,225,75,white,grey,'StartLevel3')
        takkar("Hætta",475,450,225,75,white,grey,'quit')
        pygame.display.update()
        clock.tick(10)

def HP1():
    level3HP1 = True
    while level3HP1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bakgrunnurGameLevel3b, (0,0))
        messageDisplayLevel('Hvað heitir mamma Haralds Potts?',9)
        takkar("Claudia",150,150,225,75,white,grey,'rangt')
        takkar("Lily",150,250,225,75,white,grey,'HP2')
        takkar("Petunia",150,350,225,75,white,grey,'rangt')
        takkar("Molly",150,450,225,75,white,grey,'rangt')
        pygame.display.update()
        clock.tick(10)

def HP2():
    level3HP2 = True
    while level3HP2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bakgrunnurGameLevel3b, (0,0))
        messageDisplayLevel('Hver sótti Harald á 11 ára afmælisdag hans?',9)
        takkar("Albus Dumbledore",150,150,250,75,white,grey,'rangt')
        takkar("Gilderoy Lockhart",150,250,250,75,white,grey,'rangt')
        takkar("Rubeus Hagrid",150,350,250,75,white,grey,'HP3')
        takkar("Arthur Weasley",150,450,250,75,white,grey,'rangt')
        pygame.display.update()
        clock.tick(10)

def HP3():
    level3HP3 = True
    while level3HP3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bakgrunnurGameLevel3b, (0,0))
        messageDisplayLevel('Hver er guðfaðir Haralds?',9)
        takkar("Albus Dumbledore",150,150,240,75,white,grey,'rangt')
        takkar("Arthur Weasley",150,250,240,75,white,grey,'rangt')
        takkar("Lucius Malfoy",150,350,240,75,white,grey,'rangt')
        takkar("Sirius Black",150,450,240,75,white,grey,'HP4')
        pygame.display.update()
        clock.tick(10)

def HP4():
    level3HP4 = True
    while level3HP4:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bakgrunnurGameLevel3b, (0,0))
        messageDisplayLevel('Hvaða stöðu spilar Haraldur í Quidditch?',9)
        takkar("Gæslumaður (Keeper)",150,150,310,75,white,grey,'rangt')
        takkar("Leitari (Seeker)",150,250,310,75,white,grey,'level3WIN')
        takkar("Varnarmaður (Beater)",150,350,310,75,white,grey,'rangt')
        takkar("Sóknarmaður (Chaser)",150,450,310,75,white,grey,'rangt')
        pygame.display.update()
        clock.tick(10)

def HG1():
    level3HG1 = True
    while level3HG1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bakgrunnurGameLevel3b, (0,0))
        messageDisplayLevel('Við hvað starfa foreldrar',9)
        messageDisplayLevel('Hermínu?',5.5)
        takkar("Verkfræðingar",150,150,225,75,white,grey,'rangt')
        takkar("Lögfræðingar",150,250,225,75,white,grey,'rangt')
        takkar("Kennarar",150,350,225,75,white,grey,'rangt')
        takkar("Tannlæknar",150,450,225,75,white,grey,'HG2')
        pygame.display.update()
        clock.tick(10)

def HG2():
    level3HG2 = True
    while level3HG2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bakgrunnurGameLevel3b, (0,0))
        messageDisplayLevel('Hvaða vera ræðst á Hermínu á ',9)
        messageDisplayLevel('stelpuklósettinu fyrsta árið í Hogwarts?',5.5)
        takkar("Draugur",150,150,250,75,white,grey,'rangt')
        takkar("Mús",150,250,250,75,white,grey,'rangt')
        takkar("Tröll",150,350,250,75,white,grey,'HG3')
        takkar("Hippogriff",150,450,250,75,white,grey,'rangt')
        pygame.display.update()
        clock.tick(10)

def HG3():
    level3HG3 = True
    while level3HG3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bakgrunnurGameLevel3b, (0,0))
        messageDisplayLevel('Hver fer með Hermínu á jólaballið?',9)
        takkar("Victor Krum",150,150,240,75,white,grey,'HG4')
        takkar("Neville Longbottom",150,250,240,75,white,grey,'rangt')
        takkar("Ron Weasley",150,350,240,75,white,grey,'rangt')
        takkar("Draco Malfoy",150,450,240,75,white,grey,'rangt')
        pygame.display.update()
        clock.tick(10)

def HG4():
    level3HG4 = True
    while level3HG4:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bakgrunnurGameLevel3b, (0,0))
        messageDisplayLevel('Hvern slær Hermína í andlitið?',9)
        takkar("Victor Krum",150,150,310,75,white,grey,'rangt')
        takkar("Neville Longbottom",150,250,310,75,white,grey,'rangt')
        takkar("Ron Weasley",150,350,310,75,white,grey,'rangt')
        takkar("Draco Malfoy",150,450,310,75,white,grey,'level3WIN')
        pygame.display.update()
        clock.tick(10)

def RV1():
    level3RV1 = True
    while level3RV1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bakgrunnurGameLevel3b, (0,0))
        messageDisplayLevel('Hvað heitir rottan hans Rúnars?',9)
        takkar("Frankie",150,150,225,75,white,grey,'rangt')
        takkar("Scabbers",150,250,225,75,white,grey,'RV2')
        takkar("Oscar",150,350,225,75,white,grey,'rangt')
        takkar("Dobbie",150,450,225,75,white,grey,'rangt')
        pygame.display.update()
        clock.tick(10)

def RV2():
    level3RV2 = True
    while level3RV2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bakgrunnurGameLevel3b, (0,0))
        messageDisplayLevel('Hvaða stöðu spilar Rúnar í ',9)
        messageDisplayLevel('Quidditch?',5.5)
        takkar("Gæslumaður (Kepper)",150,150,250,75,white,grey,'RV3')
        takkar("Leitari (Seeker)",150,250,250,75,white,grey,'rangt')
        takkar("Varnarmaður (Beater)",150,350,250,75,white,grey,'rangt')
        takkar("Sóknarmaður (Chaser)",150,450,250,75,white,grey,'rangt')
        pygame.display.update()
        clock.tick(10)

def RV3():
    level3RV3 = True
    while level3RV3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bakgrunnurGameLevel3b, (0,0))
        messageDisplayLevel('Hvaða dýr hræðist Rúnar mest?',9)
        takkar("Dreka",150,150,240,75,white,grey,'rangt')
        takkar("Könguló",150,250,240,75,white,grey,'RV4')
        takkar("Hippogriff",150,350,240,75,white,grey,'rangt')
        takkar("Mýs",150,450,240,75,white,grey,'rangt')
        pygame.display.update()
        clock.tick(10)

def RV4():
    level3RV4 = True
    while level3RV4:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bakgrunnurGameLevel3b, (0,0))
        messageDisplayLevel('Hverju safnar Rúnar?',9)
        takkar("Súkkulaðifroskum",150,150,310,75,white,grey,'level3WIN')
        takkar("Bertie Bott's baunum",150,250,310,75,white,grey,'rangt')
        takkar("Frímerkjum",150,350,310,75,white,grey,'rangt')
        takkar("Quidditch spilum",150,450,310,75,white,grey,'rangt')
        pygame.display.update()
        clock.tick(10)

def GV1():
    level3GV1 = True
    while level3GV1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bakgrunnurGameLevel3b, (0,0))
        messageDisplayLevel('Hvað á Guðrún marga bræður',9)
        takkar("1",150,150,310,75,white,grey,'rangt')
        takkar("2",150,250,310,75,white,grey,'rangt')
        takkar("5",150,350,310,75,white,grey,'rangt')
        takkar("6",150,450,310,75,white,grey,'GV2')
        pygame.display.update()
        clock.tick(10)

def GV2():
    level3GV2 = True
    while level3GV2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bakgrunnurGameLevel3b, (0,0))
        messageDisplayLevel('Hvaða stöðu spilar Guðrún í Quidditch?',9)
        takkar("Gæslumaður (Keeper)",150,150,310,75,white,grey,'rangt')
        takkar("Leitari (Seeker)",150,250,310,75,white,grey,'rangt')
        takkar("Varnarmaður (Beater)",150,350,310,75,white,grey,'rangt')
        takkar("Sóknarmaður (Chaser)",150,450,310,75,white,grey,'GV3')
        pygame.display.update()
        clock.tick(10)

def GV3():
    level3GV3 = True
    while level3GV3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bakgrunnurGameLevel3b, (0,0))
        messageDisplayLevel('Hvaða herbergi opnar Guðrún í Hogwarts?',9)
        takkar("Room of Requirement",150,150,310,75,white,grey,'rangt')
        takkar("Trophy Room",150,250,310,75,white,grey,'rangt')
        takkar("Shrieking Shack",150,350,310,75,white,grey,'rangt')
        takkar("Chamber of Secret",150,450,310,75,white,grey,'GV4')
        pygame.display.update()
        clock.tick(10)

def GV4():
    level3GV4 = True
    while level3GV4:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bakgrunnurGameLevel3b, (0,0))
        messageDisplayLevel('Hvað heitir gæludýr Guðrúnar',9)
        takkar("Scabbers",150,150,310,75,white,grey,'rangt')
        takkar("Crookshanks",150,250,310,75,white,grey,'rangt')
        takkar("Arnold",150,350,310,75,white,grey,'level3WIN')
        takkar("Bob",150,450,310,75,white,grey,'rangt')
        pygame.display.update()
        clock.tick(10)


######## TEXTAR ########
def messageDisplayIntro(text):
    introtexti = pygame.font.Font('HPfont.ttf', 70)
    textSurf, textRect = textObjectsBlack(text, introtexti)
    textRect.center = ((display_breidd/2),(display_haed/2))
    gameDisplay.blit(textSurf, textRect)

def messageDisplayLevel(text,lina):
    introtexti = pygame.font.Font('Raleway.ttf', 35)
    textSurf, textRect = textObjectsBlack(text, introtexti)
    textRect.center = ((display_breidd/2),(display_haed/lina))
    gameDisplay.blit(textSurf, textRect)

def messageDisplayLevel3(text,lina):
    introtexti = pygame.font.Font('Raleway.ttf', 35)
    textSurf, textRect = textObjectsRed(text, introtexti)
    textRect.center = ((display_breidd/2),(display_haed/lina))
    gameDisplay.blit(textSurf, textRect)

def textObjectsBlack(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def textObjectsWhite(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def textObjectsRed(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()

######## TAKKAR ########
def takkar(text,x,y,breidd,haed,litur1,litur2,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #gera kassa gráa ef músin fer yfir kassana
    if x+breidd > mouse[0] > x and y+haed > mouse[1] > y:
        pygame.draw.rect(gameDisplay, litur2,(x,y,breidd,haed))
        if click[0] == 1 and action !=None:
            if action == "StartLevel1":
                level1Intro()
            elif action == "StartLevel1B":
                level1()
            elif action == "quit":
                pygame.quit()
                quit()
            elif action == "norn":
                level1NORN()
            elif action == "toframadur":
                level1TOFRAMADUR()
            elif action == "hermione":
                hermione()
            elif action == "ginny":
                ginny()
            elif action == "ron":
                ron()
            elif action == "harry":
                harry()
            elif action == "StartLevel2":
                time.sleep(1)
                level2()
            elif action == "StartLevel3":
                level3()
            elif action == "StartLevel4":
                level4()
            elif action == "level3WIN":
                klapp()
                level3Win()
            elif action == "rangt":
                wrong()
                time.sleep(1)
                rangt()
            elif action == "1":
                level3HP()
            elif action == "HP1":
                time.sleep(1)
                HP1()
            elif action == "HP2":
                win()
                time.sleep(1)
                HP2()
            elif action == "HP3":
                win()
                time.sleep(1)
                HP3()
            elif action == "HP4":
                win()
                time.sleep(1)
                HP4()
            elif action == "2":
                level3HG()
            elif action == "HG1":
                time.sleep(1)
                HG1()
            elif action == "HG2":
                win()
                time.sleep(1)
                HG2()
            elif action == "HG3":
                win()
                time.sleep(1)
                HG3()
            elif action == "HG4":
                win()
                time.sleep(1)
                HG4()
            elif action == "3":
                level3RV()
            elif action == "RV1":
                time.sleep(1)
                RV1()
            elif action == "RV2":
                win()
                time.sleep(1)
                RV2()
            elif action == "RV3":
                win()
                time.sleep(1)
                RV3()
            elif action == "RV4":
                win()
                time.sleep(1)
                RV4()
            elif action == "4":
                level3GV()
            elif action == "GV1":
                time.sleep(1)
                GV1()
            elif action == "GV2":
                win()
                time.sleep(1)
                GV2()
            elif action == "GV3":
                win()
                time.sleep(1)
                GV3()
            elif action == "GV4":
                win()
                time.sleep(1)
                GV4()

    else:
        pygame.draw.rect(gameDisplay, litur1,(x,y,breidd,haed))

    takkar = pygame.font.Font('Raleway.ttf', 30)
    textSurf, textRect = textObjectsBlack(text, takkar)
    textRect.center = ((x+(breidd/2)),(y+(haed/2)))
    gameDisplay.blit(textSurf, textRect)








tonlist()
leikurIntro()
