import pygame
import os
import sys
import random
from menu import *
from render import *

R = render()

# for testing
if __name__ == "__main__":
    class Game:
        def __init__(self):
            pygame.init()
            self.screen = pygame.display.set_mode((800, 600))
            self.clock = pygame.time.Clock()

        def draw_text(self, text, size, x, y, center=True):
            # utility function to draw text at a given location
            # TODO: move font matching to beginning of file (don't repeat)
            font_name = pygame.font.match_font('arial')
            font = pygame.font.Font(font_name, size)
            text_surface = font.render(text, True, (255, 255, 255))
            text_rect = text_surface.get_rect()
            if center:
                text_rect.midtop = (x, y)
            else:
                text_rect.topleft = (x, y)
            return self.screen.blit(text_surface, text_rect)

    g = Game()
    font = pygame.font.match_font("Ubuntu Mono")
    # standard list of options and customized labels
    items = {"play": "Play", "opt": "Options", "quit": "Quit"}
    menu = GameMenu(g, "POKEMON", ["Play", "Options", "Quit"], font=font, font_size=40)
    menu.run()
    print("starting game")



res = 2
playerg = 'FW'
def choiceMenu(object):
    global res
    if object == 'display':
        return (400 * res, 300 * res)
    ''' 안쓰는것같은데 나중에 만져보자
    if object == 'retrato':
        if res == 1:
            return (100, 67)
        if res == 2:
            return (199, 135)
        if res == 3:
            return (298, 203)
    if object == 'mostrarret1':
        if res == 1:
            return 140
        if res == 2:
            return 217
        if res == 3:
            return 412
    if object == 'mostrarret2':
        if res == 1:
            return 110
        if res == 2:
            return 219
        if res == 3:
            return 328
    '''
    if object == 'enemy_ground':     # 싸울 때 상대가 서 있는 발판
        if res == 1:
            return (225, 55)
        if res == 2:
            return (262, 64)
        if res == 3:
            return (423, 104)
            return (423, 104)   # 얘는 왜 두 번 써있을까
    if object == 'myground': # 싸울 때 내 캐릭터가 서 있는 발판
        if res == 1:
            return (250, 30)
        if res == 2:
            return (418, 49)
        if res == 3:
            return (700, 80)
    '''얘도 안쓰는것같음
    if object == 'principal1':
        if res == 1:
            return (250, 30)
        if res == 2:
            return (height // 2)
        if res == 3:
            return (700, 80)
    '''


APP_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0]))  # Folder origin
main_background = pygame.image.load("fundo_batalha.png")      # 주인공 선택할 때 배경 -> Hufs Pygame Pokemon 문구 추가
pygame.mixer.init()
os.chdir(APP_FOLDER+'/Sons')
pygame.mixer.music.load('main_music.mp3')       # intro 배경음악
pygame.init()
beep = pygame.mixer.Sound('beep.wav')       # 캐릭터 고를 때 삑삑 소리나게
os.chdir(APP_FOLDER)
font = pygame.font.Font('gamefont.ttf', 40)     # 폰트 설정
font2 = pygame.font.Font('gamefont.ttf', 15)
sec = 50
size = width, height = choiceMenu('display')  # 스크린 설정
factor_size = 3
display = pygame.display.set_mode(size)
pygame.display.set_caption("HUFS ICE POKEMON")      # 상단바 설정, 바로 아래 코드는 상단바 아이콘
icon_window = pygame.image.load('icon.png')
pygame.display.set_icon(icon_window)
os.chdir(APP_FOLDER + "/pkmns")
os.chdir(APP_FOLDER + '/animacoes')
barra_branca = pygame.image.load('ponto_branco.png')
barra = pygame.image.load('barra.png')
os.chdir(APP_FOLDER)
barra = pygame.transform.scale(barra, size)
barra_branca = pygame.transform.scale(barra_branca, (25 * factor_size, 2 * factor_size))
defeated_enemy = 0     # 트레이너 몇 명 깼는지 세기
allowPass = False     # 트레이너 다 깨지 못하면 지나갈 수 없음
text_box = pygame.image.load('text_box.png')        # 대화상자 만들기
text_box = pygame.transform.scale(text_box, (width * res, height * res))
display_select_pokemon = pygame.image.load('tela_sel_pokemon.png')     # 싸움 시 포켓몬 선택할 수 있는 창 -> 선택하고 나서 이후에 아무것도 못하니까 처리하기
os.chdir(APP_FOLDER + "/pkmns")

# 포켓몬 정보들 - 사진, 이름, 타입, 기술...                                                                                                                                                                                                                           ]
ids = [["1b.png", "1bw.png", 'VENUSAUR', 'Grass', 'Poisson', ['Solar Beam', 'Leaf Storm', 'Earthquake', 'Energy Ball'], 11200, 11200],  #이상해꽃(Venusaur) / Grass / Poisson / Solar Beam / Leaf Storm / Earthquake / Energy Ball
       ["2b.png", "2bw.png", 'CHARIZARD', 'Fire', 'Fight', ['Flame Radiation', 'Circle of Fire', 'Inferno', 'Earthquake'], 200, 200],  #리자몽(Charizard) / Fire / Fight / Flame Radiation / Circle of Fire / Inferno / Earthquake
       ["3b.png", "3bw.png", 'BLASTOISE','Water', 'None', ['Aqua Jet', 'Bubble Beam', 'Bite', 'Earthquake'], 200, 200],           #거북왕(Blastoise)  / Water / None / Aqua Jet / Bubble Beam / Bite / Earthquake
       ["4b.png", "4bw.png", 'PIKACHU', 'Electric', 'None', ['Assault', 'Thunder', 'Thunderbolt', 'Bolt Strike'], 200, 200],  #피카츄(Pikachu) / Electric / None / Assault / Thunder / Thunderbolt / Bolt Strike /
       ["5b.png", "5bw.png", 'NIDOQUEEN', 'Poisson', 'Ground', ['Poissonous', 'Bite', 'Earthquake', 'Scratch'], 200, 200],         #니드퀸(Nidoqueen) / Poisson / Ground / Poissonous/ Bite / Earthquake /Scratch
       ["6b.png", "6bw.png", 'NIDOKING', 'Poisson', 'Ground', ['Poissonous', 'Bite', 'Earthquake', 'Scratch'],200, 200],             #니드킹(Nidoking) / Poisson / Ground / Poissonous/ Bite / Earthquake /Scratch
       ["7b.png", "7bw.png", 'ARCANINE', 'Fire', 'None', ['Flame Radiation', 'Inferno', 'Bite', 'Assault'], 200, 200],                #윈디(Arcanine) / Fire / None / Flame Radiation / Inferno / Bite /  Assault
       ["8b.png","8bw.png", 'MACHAMP', 'Fight', 'None', ['Low Blow', 'Earthquake', 'Hyper Beam', 'Collapse'], 200, 200],       #괴력몬(Machamp) / Fight / None / Low Blow / Earthquake / Hyper Beam / Collapse
       ["9b.png", "9bw.png", 'GASTLY','Ghost', 'Poisson', ['Haunt', 'Bite', 'Scratch', 'Nightmare'], 200, 200],            #고오스(Gastly) / Ghost / Poisson / Haunt / Bite / Nightmare / Dark Sphere
       ["10b.png", "10bw.png", 'GENGAR', 'Ghost', 'Poisson', ['Poissonous', 'Bite', 'Scratch', 'Nightmare'], 200, 200],        #팬텀(Gengar) / Ghost / Poisson / Poissonous / Bite / scratch /  nightmare
       ["11b.png", "11bw.png", 'ELECTABUZZ', 'Electric','None', ['Thunder', 'Quick Assault', 'Bolt Strike', 'Lightning Sphere'], 200, 200],  #에레브(Electabuzz) /  Electric / None / Thunder / Quick Assault / Bolt Strike / Lightning Sphere
       ["12b.png", "12bw.png", 'SNORLAX', 'Normal', 'None', ['Assault', 'Scratch', 'Bite', 'Earthquake'], 200, 200]]                 # 잠만보(Snorlax) / Normal / None  / Assault / Scratch / Bite / Earthquake
'''우선은 12마리만 사용
       ["13b.png", "13bw.png", 'DRAGONITE', 'DRAGÃO', 'Fly', ['HIPER CHOQUE DO TROVÃO', 'LANÇA-CHAMAS', 'Earthquake', 'ESFERA DE ENERGIA'], 200, 200],
       ["14b.png", "14bw.png", 'MEGANIUM', 'GRAMA', 'None',['Solar Beam', 'Leaf Storm', 'INVESTIDA', 'BOLHA VENENOSA'], 200, 200],
       ["15b.png", "15bw.png", 'TYPHLOSION', 'FOGO', 'None', ['INFERNO', 'CÍRCULO DE FOGO', 'INVESTIDA', 'Earthquake'], 200, 200],
       ["16b.png", "16bw.png", 'FERALIGATR', 'ÁGUA', 'None', ['MORDIDA', 'BOLHAS', 'MORDIDA', 'Earthquake'], 200, 200],
       ["17b.png", "17bw.png", 'CROBAT', 'Fly','Poisson', ['ARRANHAR', 'Leaf Storm', 'Earthquake', 'ESFERA DE ENERGIA'],200, 200],
       ["18b.png", "18bw.png", 'ESPEON', 'PSIQUÍCO', 'None', ['CONFUSÃO', 'GOLPE PSIQUÍCO', 'ESFERA DE ENERGIA', 'GOLPE ESTRELADO'], 200, 200],
       ["19b.png", "19bw.png", 'UMBREON', 'TREVAS', 'None', ['ATORMENTAR', 'PESADELO', 'ESFERA NEGRA', 'DEVORADOR DE SONHOS'], 200, 200],
       ["20b.png", "20bw.png", 'STEELIX', 'Iron', 'TERRA', ['TERREMOTO', 'INVESTIDA', 'MORDIDA', 'DESABAMENTO'],200,200],
       ["21b.png", "21bw.png", 'HOUNDOOM', 'FOGO','TREVAS', ['PESADELO', 'LANÇA-CHAMAS', 'TERREMOTO', 'ESFERA DE ENERGIA'],200,200],
       ["22b.png", "22bw.png", 'TYRANITAR', 'PEDRA','TREVAS', ['MORDIDA', 'HIPER RAIO', 'DESABAMENTO', 'TERREMOTO'],200,200],
       ["23b.png", "23bw.png", 'SCEPTILE', 'GRAMA', 'None',['ARRANHAR', 'Solar Beam', 'MORDIDA', 'TERREMOTO'],200,200],
       ["24b.png", "24bw.png", 'BLAZIKEN', 'FOGO', 'LUTADOR', ['HIPER RAIO', 'LABAREDA', 'BICADA', 'INFERNO'],200,200],
       ["25b.png", "25bw.png", 'SWAMPERT', 'ÁGUA','TERRA', ['JATO D\'ÁGUA', 'BOLHAS', 'TERREMOTO', 'MORDIDA'],200,200],
       ["26b.png", "26bw.png", 'GARDEVOIR', 'PSIQUÍCO', 'Fairy', ['CONFUSÃO', 'GOLPE PSIQUÍCO', 'ESFERA DE ENERGIA', 'TERREMOTO'],200,200],
       ["27b.png", "27bw.png", 'AGGRON', 'Iron','PEDRA', ['DESABAMENTO', 'ATAQUE RÁPIDO', 'HIPER RAIO', 'TERREMOTO'],200,200],
       ["28b.png", "28bw.png", 'FLYGON', 'TERRA','DRAGÃO', ['GOLPE AÉREO', 'HIPER RAIO', 'GARRAS DE DRAGÃO', 'TERREMOTO'],200,200],
       ["29b.png", "29bw.png", 'MILOTIC', 'ÁGUA','None', ['NEVASCA', 'JATO D\'ÁGUA', 'CABEÇADA', 'QUEDA LIVRE'], 200,200],
       ["30b.png", "30bw.png", 'SALAMENCE', 'DRAGÃO', 'Fly', ['MORDIDA', 'GOLPE AÉREO', 'CABEÇADA', 'TERREMOTO'],200,200],
       ["31b.png", "31bw.png", 'LATIOS', 'DRAGÃO','PSIQUÍCO', ['GOLPE AÉREO', 'CABEÇADA', 'GOLPE PSIQUÍCO', 'HIPER RAIO'],200,200],
       ["32b.png", "32bw.png", 'TORTERRA', 'GRAMA', 'TERRA', ['TERREMOTO', 'Leaf Storm', 'ABSORVER', 'TERREMOTO'], 200,200],
       ["33b.png", "33bw.png", 'INFERNAPE', 'FOGO','LUTADOR', ['SOCO DE FOGO', 'LABAREDA', 'INFERNO', 'GOLPE BAIXO'], 200,200],
       ["34b.png", "34bw.png", 'EMPOLEON', 'ÁGUA', 'Iron', ['BOLHAS', 'JATO D\'ÁGUA', 'BICADA', 'GARRA DE METAL'],200,200],
       ["35b.png", "35bw.png", 'LUXRAY', 'ELÉTRICO','None', ['INVESTIDA TROVÃO', 'TROVÃO SELVAGEM', 'MORDIDA', 'MORDIDA RELÂMPAGO'],200,200],
       ["36b.png", "36bw.png", 'RAMPARDOS', 'PEDRA','None', ['CABEÇADA', 'BOLHA VENENOSA', 'DESABAMENTO', 'TERREMOTO'],200,200],
       ["37b.png", "37bw.png", 'PACHIRISU', 'ELÉTRICO','None', ['ATAQUE RÁPIDO', 'INVESTIDA RELÂMPAGO', 'RAIO', 'CHOQUE DO TROVÃO'],200,200],
       ["38b.png", "38bw.png", 'GASTRODON', 'ÁGUA', 'TERRA', ['BOLHA VENENOSA', 'JATO D\'ÁGUA', 'ATAQUE RÁPIDO', 'TERREMOTO'],200,200],
       ["39b.png", "39bw.png", 'GARCHOMP', 'DRAGÃO', 'TERRA', ['GARRAS DE DRAGÃO', 'DESABAMENTO', 'HIPER RAIO', 'TERREMOTO'],200,200],
       ["40b.png", "40bw.png", 'LUCARIO', 'LUTADOR','Iron',['ESFERA DE ENERGIA', 'DESABAMENTO', 'GOLPE KARATE', 'GOLPE BAIXO'],200,200],
       ["41b.png", "41bw.png", 'GLISCOR', 'TERRA', 'Fly', ['CORTE CRUZADO', 'MORDIDA', 'INVESTIDA AÉREA', 'ATAQUE RÁPIDO'],200,200],
       ["42b.png", "42bw.png", 'LEAFEON', 'GRAMA','None', ['Leaf Storm', 'ABSORVER', 'ESFERA DE ENERGIA', 'ARRANHAR'],200,200],
       ["43b.png", "43bw.png", 'GLACEON', 'GELO', 'None',['MORDIDA GLACIAL', 'NEVASCA', 'RAIO DE GELO', 'INVESTIDA'],200,200],
       ["44b.png", "44bw.png", 'PORYGON-Z ', 'NORMAL','None', ['CHOQUE DO TROVÃO', 'INVESTIDA', 'ESFERA DE ENERGIA', 'TERREMOTO'],200,200],
       ["45b.png", "45bw.png", 'GALLADE','PSIQUÍCO', 'LUTADOR', ['CORTE CRUZADO', 'ATAQUE RÁPIDO', 'LANÇA-CHAMAS', 'TERREMOTO'],200,200]]
'''

# 상대와 나의 포켓몬 타입에 따라 주고 받는 데미지 설정
def damage_amount(pokemon_type, enemy_type, tipo2i, teste):
    if teste == False:
        m1 = damage_amount(pokemon_type, tipo2i, enemy_type, True)
        pokemon_type = get_type_txt(pokemon_type)       # 기술에 따라 타입 리턴
    m1 = 1
    m = 1
    if enemy_type != 'None': ######################## 바꿈
        if pokemon_type == enemy_type and pokemon_type != 'Dragon' and pokemon_type != 'Ghost':
            m = 1
        elif pokemon_type == enemy_type and pokemon_type == 'Dragon':
            m = 2
        elif pokemon_type == 'Water' and (enemy_type == 'Dragon' or enemy_type == 'Grass'):
            m = 0.5
        elif pokemon_type == 'Water' and (enemy_type == 'Fire' or enemy_type == 'Rock' or enemy_type == 'Ground'):
            m = 2
        elif pokemon_type == 'Dragon' and (enemy_type == 'Dragon' or enemy_type == 'Grass'):
            m = 0.5
        elif pokemon_type == 'Water' and (enemy_type == 'Fire' or enemy_type == 'Rock' or enemy_type == 'Ground'):
            m = 2
        elif pokemon_type == 'Fight' and (enemy_type == 'Normal' or enemy_type == 'Rock' or enemy_type == 'Iron' or enemy_type == 'Ice' or enemy_type == 'Dark'):
            m = 2
        elif pokemon_type == 'Fight' and (enemy_type == 'Fly' or enemy_type == 'Poisson' or enemy_type == 'Fairy' or enemy_type == 'Esper'):
            m = 0.5
        elif pokemon_type == 'Fight' and (enemy_type == 'Ghost'):
            m = 0
        elif pokemon_type == 'Fly' and (enemy_type == 'Fight' or enemy_type == 'Grass'):
            m = 2
        elif pokemon_type == 'Fly' and (enemy_type == 'Rock' or enemy_type == 'Iron' or enemy_type == 'Electric'):
            m = 0.5
        elif pokemon_type == 'Poisson' and (enemy_type == 'Poisson' or enemy_type == 'Ground' or enemy_type == 'Rock' or enemy_type == 'Ghost'):
            m = 0.5
        elif pokemon_type == 'Poisson' and (enemy_type == 'Iron'):
            m = 0
        elif pokemon_type == 'Poisson' and (enemy_type == 'Grass' or enemy_type == 'Fairy'):
            m = 2
        elif pokemon_type == 'Ground' and (enemy_type == 'Fly'):
            m = 0.5
        elif pokemon_type == 'Ground' and (enemy_type == 'Poisson' or enemy_type == 'Rock' or enemy_type == 'Iron' or enemy_type == 'Fire' or enemy_type == 'Electric'):
            m = 2
        elif pokemon_type == 'Ground' and (enemy_type == 'Fly'):
            m = 0
        elif pokemon_type == 'Ghost' and (enemy_type == pokemon_type or enemy_type == 'Esper'):
            m = 2
        elif pokemon_type == 'Ghost' and enemy_type == 'Normal':
            m = 0
        elif pokemon_type == 'Ghost' and enemy_type == 'Dark':
            m = 0.5
        elif pokemon_type == 'Iron' and (enemy_type == 'Rock' or enemy_type == 'Ice' or enemy_type == 'Fairy'):
            m = 2
        elif pokemon_type == 'Iron' and (enemy_type == 'Fire' or enemy_type == 'Water' or enemy_type == 'Electric'):
            m = 0.5
        elif pokemon_type == 'Fire' and (enemy_type == 'Rock' or enemy_type == 'Water' or enemy_type == 'Dragon'):
            m = 0.5
        elif pokemon_type == 'Fire' and (enemy_type == 'Grass' or enemy_type == 'Ice' or enemy_type == 'Iron'):
            m = 2
        elif pokemon_type == 'Grass' and (enemy_type == 'Fly' or enemy_type == 'Poisson' or enemy_type == 'Iron' or enemy_type == 'Fire' or enemy_type == 'Dragon'):
            m = 0.5
        elif pokemon_type == 'Grass' and (enemy_type == 'Ground' or enemy_type == 'Rock' or enemy_type == 'Water'):
            m = 2
        elif pokemon_type == 'Electric' and (enemy_type == 'Fly' or enemy_type == 'Water'):
            m = 2
        elif pokemon_type == 'Electric' and (enemy_type == 'Ground' or enemy_type == 'Rock'):
            m = 0
        elif pokemon_type == 'Electric' and (enemy_type == 'Grass' or enemy_type == 'Dragon'):
            m = 0.5
        elif pokemon_type == 'Esper' and (enemy_type == 'Fight' or enemy_type == 'Poisson'):
            m = 2
        elif pokemon_type == 'Esper' and enemy_type == 'Dark':
            m = 0
        elif pokemon_type == 'Esper' and enemy_type == 'Iron':
            m = 0.5
        elif pokemon_type == 'Ice' and (enemy_type == 'Fly' or enemy_type == 'Ground' or enemy_type == 'Grass' or enemy_type == 'Dragon'):
            m = 2
        elif pokemon_type == 'Ice' and (enemy_type == 'Fire' or enemy_type == 'Iron' or enemy_type == 'Water'):
            m = 0.5
        else:
            m = 1
    elif enemy_type == 'None':
        m = 1
    return m * m1

icons = []      # 캐릭터 12마리 선택할 수 있게 사진 넣어두는 리스트

# 트레이너 별 포켓몬 정보 모음
pkmn_astro = [[pygame.image.load("13f1.png"), pygame.image.load("13f2.png"), 'DRAGONITE', 'Dragon',
               'Fly', ['Hyper Beam', 'Flame Radiation', 'Earthquake', 'Energy Ball'], 200, 200],
              [pygame.image.load("43f1.png"), pygame.image.load("43f2.png"), 'GLACEON', 'Ice',
               'None',['Glacial Bite', 'Blizzard', 'Ice Beam', 'Assault'],200,200],
              [pygame.image.load("40f1.png"), pygame.image.load("40f2.png"), 'LUCARIO', 'Fight',
               'Iron',['Energy Ball', 'Collapse', 'Karate Blow', 'Low Blow'],200,200]]

pkmn_clara = [[pygame.image.load("26f1.png"), pygame.image.load("26f2.png"), 'GARDEVOIR', 'Esper',
               'Fairy', ['Confuse', 'Psychic Blow', 'Energy Ball', 'Earthquake'],200,200],
              [pygame.image.load("43f1.png"), pygame.image.load("43f2.png"), 'GLACEON', 'Ice',
               'None',['Glacial Bite', 'Blizzard', 'Ice Beam', 'Assault'],200,200],
              [pygame.image.load("10f1.png"), pygame.image.load("10f2.png"), 'GENGAR', 'Ghost',
               'Poisson', ['Poissonous', 'Bite', 'Scratch', 'Nightmare'], 200, 200]]

pkmn_ale = [[pygame.image.load("41f1.png"), pygame.image.load("41f2.png"), 'GLISCOR', 'Ground', 'Fly', ['Cut Across', 'Bite', 'Somersault', 'Quick Assault'],200,200],
              [pygame.image.load("43f1.png"), pygame.image.load("43f2.png"), 'GLACEON', 'Ice', 'None',['Glacial Bite', 'Blizzard', 'Ice Beam', 'Assault'],200,200],
              [pygame.image.load("40f1.png"), pygame.image.load("40f2.png"), 'LUCARIO', 'Fight','Iron',['Energy Ball', 'Collapse', 'Karate Blow', 'Low Blow'],200,200]]

pkmn_luciana = [[pygame.image.load("35f1.png"), pygame.image.load("35f2.png"), 'LUXRAY', 'Electric','None', ['Bolttacker', 'Thunder Storm', 'Bite', 'Thunder Bite'],200,200],
              [pygame.image.load("26f1.png"), pygame.image.load("26f2.png"), 'GARDEVOIR', 'Esper', 'Fairy', ['Confuse', 'Psychic Blow', 'Energy Ball', 'Earthquake'],200,200],
              [pygame.image.load("12f1.png"), pygame.image.load("12f2.png"), 'SNORLAX', 'Normal', 'None', ['Assault', 'Scratch', 'Bite', 'Earthquake'], 200, 200]]

# 우선은 12마리만 두는 거로
for i in range(1, 13):
    icons.append(pygame.image.load(str(i) + 'icon.png'))
#  FIM
os.chdir(APP_FOLDER + "/Sprites")
npc_icon = pygame.image.load('npcicon.png')     # 느낌표 뜨면서 대결 신청하러 갈 때 그 느낌표 사진
hp = [pygame.image.load('hp_high.png'), pygame.image.load('hp_med.png'), pygame.image.load('hp_low.png')]       # 피가 얼마나 남았냐에 따른 색상 차이
enemy_ground = pygame.image.load('baseinimiga.png')
enemy_ground = pygame.transform.scale(enemy_ground, (choiceMenu('enemy_ground')))
myground = pygame.image.load('basealiada.png')
myground = pygame.transform.scale(myground, (choiceMenu('myground')))

# 트레이너 npc 사진 모음
astro = ['Astro', 421, 367, pygame.image.load('Looking_Left_Astro.png'), pygame.image.load('Walking_Left_1_Astro.png'),
         pygame.image.load('Walking_Left_2_Astro.png'), pygame.image.load('astro_retrato.png'),
         pygame.image.load('astro_corpo1.png'), pygame.image.load('astro_corpo2.png'), pygame.image.load('astro_corpo3.png')]

clara = ['Clara', 421, 190, pygame.image.load('Looking_Left_Clara.png'), pygame.image.load('Walking_Left_1_Clara.png'),
         pygame.image.load('Walking_Left_2_Clara.png'), pygame.image.load('clara_retrato.png'),
         pygame.image.load('clara_corpo1.png'), pygame.image.load('clara_corpo2.png'),
         pygame.image.load('clara_corpo3.png')]

luciana = ['Luciana', 421, 131, pygame.image.load('Looking_Left_Luciana.png'),
           pygame.image.load('Walking_Left_1_Luciana.png'),pygame.image.load('Walking_Left_2_Luciana.png'),
           pygame.image.load('luciana_retrato.png'), pygame.image.load('luciana_corpo1.png'),
           pygame.image.load('luciana_corpo2.png'), pygame.image.load('luciana_corpo3.png')]

ale = ['Ale', 421, 264, pygame.image.load('Looking_Left_Ale.png'), pygame.image.load('Walking_Left_1_Ale.png'),
       pygame.image.load('Walking_Left_2_Ale.png'), pygame.image.load('ale_retrato.png'),
       pygame.image.load('ale_corpo1.png'), pygame.image.load('ale_corpo2.png'), pygame.image.load('ale_corpo3.png')]

# 트레이너랑 싸울 때
def NPCchallenge(npc):
    global display, clock, enemy_ground, myground, main_background, mode
    lines = ['YOU WILL NOT BE ABLE TO GO THERE', 'BETTER SAY GOODBYE FOR YOUR NOTE!', 'I WILL NOT BE REPULSED', 'I ALMOST DYED BY DOING THAT ONE'] # 시합 시작할때 나오는 대사
    num = 0
    for i in range(7, 10):
        clock.tick(5)
        posm = posx, posy = pygame.mouse.get_pos()
        display.blit(main_background, (0,0))
        display.blit(enemy_ground, (495, 134))
        display.blit(myground, (3, 354))
        os.chdir(APP_FOLDER + "/Sprites")
        y = launchpkb[0]
        x = npc[i]
        x = pygame.transform.scale(x, (200, 200))
        y = pygame.transform.scale(y, (200, 200))
        display.blit(x, (522, 0))
        display.blit(y, (150, 200))
        pygame.display.update()
    show_lines('{}: {}'.format(npc[0], lines[(random.randrange(0, len(lines)))]))      # 대사 랜덤으로 내보내기
    for i in range(522, 800, 5):
        clock.tick(100)
        x = npc[9]
        if i - 522 < 50: num = 1
        elif i - 522 < 100: num = 2
        elif i - 522 < 190: num = 3
        else: num = 4
        y = launchpkb[num]
        x = pygame.transform.scale(x, (200, 200))
        y = pygame.transform.scale(y, (200, 200))
        display.blit(main_background, (0, 0))
        display.blit(enemy_ground, (495, 134))
        display.blit(myground, (3, 354))
        display.blit(x, (i, 0))
        display.blit(y, (150 - (i - 522), 200))
        pygame.display.flip()

os.chdir(APP_FOLDER)
barratime = pygame.image.load('seu_time.png')       # 함께 할 포켓몬 6마리 고르는 6개 박스 사진 넣기
os.chdir(APP_FOLDER + "/animacao1")  # sprites 폴더에 들어갑시다
xD = []
xD2 = []
clock = pygame.time.Clock()

# 애니메이션 효과 주려고 사진 연속으로 타다닥
for i in range(30, 83):
    c = pygame.image.load('00' + str(i) + '.png')
    c = (pygame.transform.scale(c, size))
    xD.append(c)
for i in range(83, 92):
    c = pygame.image.load('00' + str(i) + '.png')
    c = (pygame.transform.scale(c, size))
    xD2.append(c)

# 애니메이션 효과
transition_effect = []
os.chdir(APP_FOLDER + "/Sons")
sonstransition_effect = [pygame.mixer.Sound('golpe_karate.wav')]
os.chdir(APP_FOLDER + "/animacoes/ataques/golpe_karate")
transition_effect2 = []
for i in range(6, 10):
    x = pygame.image.load("000" + str(i) + '.png')
    x = pygame.transform.scale(x, (800, 600))
    transition_effect2.append(x)
for i in range(10, 58):
    x = pygame.image.load("00" + str(i) + '.png')
    x = pygame.transform.scale(x, (800, 600))
    transition_effect2.append(x)
transition_effect.append(transition_effect2)
del transition_effect2
os.chdir(APP_FOLDER)


def golpe_karate():
    global display, transition_effect, fundo, sonstransition_effect, clock
    sonstransition_effect[0].play()
    for i in range(len(transition_effect[0])):
        display.blit(fundo, (0, 0))
        display.blit(transition_effect[0][i], (0, 0))
        pygame.display.flip()
        clock.tick(25)
fightingNPC = ''

# 각 트레이너 깰 때마다 다음 트레이너 만날 수 있게 짜기
def meet_NPC():
    global allowPass, x, y, player, APP_FOLDER, display, mode, fightingNPC, NPCposition
    posx, posy = pygame.mouse.get_pos()
    if y >= 364 and y<= 370 and defeated_enemy == 0:      # Astro Trainer 만나게하기
        allowPass = False
        y = 367
        NPCposition[1] = player, (x, y)
        os.chdir(APP_FOLDER + "/Sprites")
        player = pygame.image.load("Looking_"+ pos +"_" + playerg + ".png")
        for i in NPCposition:
            display.blit(i[0], (i[1]))
        display.blit(npc_icon, (429, 356))
        pygame.display.flip()
        pygame.time.wait(350)
        mode = 'ready'
        fightingNPC = 'astro'
    elif y >= 262 and y<= 268 and defeated_enemy == 1:    # Ale Trainer 만나게하기
        allowPass = False
        y = 265
        NPCposition[1] = player, (x, y)
        os.chdir(APP_FOLDER + "/Sprites")
        player = pygame.image.load("Looking_"+ pos +"_" + playerg + ".png")
        for i in NPCposition:
            display.blit(i[0], (i[1]))
        display.blit(npc_icon, (429, 254))
        pygame.display.flip()
        pygame.time.wait(350)
        mode = 'ready'
        fightingNPC = 'ale'
    elif y >= 186 and y<= 193  and defeated_enemy == 2:       # Clara Trainer 만나게 하기
        allowPass = False
        y = 190
        NPCposition[1] = player, (x, y)
        os.chdir(APP_FOLDER + "/Sprites")
        player = pygame.image.load("Looking_"+ pos +"_" + playerg + ".png")
        for i in NPCposition:
            display.blit(i[0], (i[1]))
        display.blit(npc_icon, (429, 180))
        pygame.display.flip()
        pygame.time.wait(350)
        mode = 'ready'
        fightingNPC = 'clara'
    elif y >= 126 and y<= 134  and defeated_enemy == 3:       # Luciana Trainer 만나게 하기
        allowPass = False
        y = 131
        NPCposition[1] = player, (x, y)
        os.chdir(APP_FOLDER + "/Sprites")
        player = pygame.image.load("Looking_"+ pos +"_" + playerg + ".png")
        for i in NPCposition:
            display.blit(i[0], (i[1]))
        display.blit(npc_icon, (429, 121))
        pygame.display.flip()
        pygame.time.wait(350)
        mode = 'ready'
        fightingNPC = 'luciana'

# 느낌표 뜨면 NPC 애들 걸어오고 배틀 신청하는 파트
def approachingNPC(npc):
    global astro, clara, ale, luciana, display, x, y, clock, display, passage_line, player, mode, APP_FOLDER
    if npc == 'astro':
        for i in range(astro[1], x+20, -2):
            NPCposition = [[passage_line, (0, 0)], [player, (x, y)], [astro[3], (astro[1], astro[2])],
                         [ale[3], (ale[1], ale[2])], [luciana[3], (luciana[1], luciana[2])],
                         [clara[3], (clara[1], clara[2])]]
            astro[1] = i
            astro[3], astro[4] = astro[4], astro[3]
            display.fill((0,0,0))
            for i1 in NPCposition:
                display.blit(i1[0], i1[1])
            pygame.display.flip()
            clock.tick(15)
        os.chdir(APP_FOLDER + '/Sprites')
        astro[3] = pygame.image.load('Looking_Left_Astro.png')
        os.chdir(APP_FOLDER)
        show_lines('Astro: Let\'s battle!')   ###대사 바꿈
        mode = 'battlefield'
    if npc == 'ale':
        for i in range(ale[1], x + 20, -2):
            NPCposition = [[passage_line, (0, 0)], [player, (x, y)], [ale[3], (ale[1], ale[2])],
                             [luciana[3], (luciana[1], luciana[2])],
                             [clara[3], (clara[1], clara[2])]]
            ale[1] = i
            ale[3], ale[4] = ale[4], ale[3]
            display.fill((0, 0, 0))
            for i1 in NPCposition:
                display.blit(i1[0], i1[1])
            pygame.display.flip()
            clock.tick(15)
        os.chdir(APP_FOLDER + '/Sprites')
        ale[3] = pygame.image.load('Looking_Left_Ale.png')
        os.chdir(APP_FOLDER)
        show_lines('Ale: My Pokemon will defeat you.!')
        mode = 'battlefield'
    if npc == 'clara':
        for i in range(clara[1], x + 20, -2):
            NPCposition = [[passage_line, (0, 0)], [player, (x, y)], [luciana[3], (luciana[1], luciana[2])], [clara[3], (clara[1], clara[2])]]
            clara[1] = i
            clara[3], clara[4] = clara[4], clara[3]
            display.fill((0, 0, 0))
            for i1 in NPCposition:
                display.blit(i1[0], i1[1])
            pygame.display.flip()
            clock.tick(15)
        os.chdir(APP_FOLDER + '/Sprites')
        clara[3] = pygame.image.load('Looking_Left_Clara.png')
        os.chdir(APP_FOLDER)
        show_lines('Clara: You will not get out of here!')
        mode = 'battlefield'
    if npc == 'luciana':
        for i in range(luciana[1], x + 20, -2):
            NPCposition = [[passage_line, (0, 0)], [player, (x, y)], [luciana[3], (luciana[1], luciana[2])],]
            luciana[1] = i
            luciana[3], luciana[4] = luciana[4], luciana[3]
            display.fill((0, 0, 0))
            for i1 in NPCposition:
                display.blit(i1[0], i1[1])
            pygame.display.flip()
            clock.tick(15)
        os.chdir(APP_FOLDER + '/Sprites')
        luciana[3] = pygame.image.load('Looking_Left_Luciana.png')
        os.chdir(APP_FOLDER)
        show_lines('Luciana: There\'s no way I can lose it here.')
        mode = 'battlefield'


# 걷는 이미지, 달리는 이미지 각각 넣어두고 연속으로 보이게 할 것
walkleft = []
walkup = []
walkdown = []
walkright = []
runleft = []
runup = []
rundown = []
runright = []
launchpkb = []

# 캐릭터 고른 것 설정
os.chdir(APP_FOLDER)
os.chdir(APP_FOLDER + "/Sprites")
player = pygame.image.load("Looking_Down_" + playerg + ".png")  # Carregar imagem do personagem
turn = 1  # Which step did the character give?
pos = 'Down'  # What is the last position the character has walked
os.chdir(APP_FOLDER)  # Back to source folder
personagem_coordenadas = x, y = 50, 50  # Character coordinates
fundo = pygame.image.load("fundo_batalha.png")  # Fundo
os.chdir(APP_FOLDER + '/pkmns')
pk1 = pygame.image.load('1b.png')
os.chdir(APP_FOLDER)
myteam = []
keyboard_image = pygame.image.load('tela nome.png')      # 키보드 사진
tech_image = pygame.image.load('tela_sel.png')


# 애니메이션 전환
def animation_transition(sprite):
    global barra, display, clock, barra_branca, xD, xD2
    sprite = pygame.transform.scale(sprite, (199, 135))
    for i in range(0, 20):
        clock.tick(12)
        display.blit(barra, (0, 0))
        display.blit(barra_branca, (100 + i, height // 2))
        display.blit(barra_branca, (76 + i, height // 2 - 25 * 2))
        display.blit(barra_branca, (500 - i, height // 2 - 20 * 2))
        display.blit(barra_branca, (300 + i, height // 2 - 25 * 2))
        display.blit(barra_branca, (450 + i, height // 2))
        display.blit(barra_branca, (280 + i, height // 2 - 40 * 2))
        display.blit(barra_branca, (265 + i, height // 2))
        display.blit(sprite, ((width // 2 - 50 * res)+i, 219))
        pygame.display.flip()

###사진 display
def pic(sprite):
    global display, clock, xD, xD2
    sprite = pygame.transform.scale(sprite, (800, 600))
    for i in range(0, 20):
        clock.tick(12)
        display.blit(sprite, (0,0))
        pygame.display.flip()




# fim
text_box = pygame.transform.scale(text_box, (800, 600))

# 대사 나오는 것
def show_lines(text):
    showing_text = []
    if len(text) >= 50:
        text = text.split()
        text_pass = ''
        for i in text:
            if (len(text_pass) + len(i)) <= 50:
                text_pass += i + ' '
            else:
                showing_text.append(text_pass)
                text_pass = i + ' '
    else:
        showing_text.append(text)
    update_text(showing_text)

# 대사 따라라락
def update_text(showing_text):
    global display, text_box, telaatual, clock
    last = ''
    top = False
    for count in range(len(showing_text)):
        for i in range(len(showing_text[count])):
            last = font.render(showing_text[count-1], True, [0, 0, 0])
            text = font.render(showing_text[count][0:i+1], True, [0, 0, 0])
            display.blit(text_box, (0, 0))
            if not(top):
                display.blit(text, (35, 475))
                pygame.display.update((0, 452, 800, 148))
            if top:
                display.blit(last, (35, 475))
                display.blit(text, (35, 520))
                pygame.display.update((0, 452, 800, 148))
            clock.tick(60)
        if not(top):
            top = True
        else:
            top = False
    clock.tick(2)


# 캐릭터 통로 안에서만 다닐 수 있게 제한 + 속도 조절
def andar():  # Função para andar
    global turn, pos, x, y, APP_FOLDER, player, display, clock
    if x >= 405:
        x = 405
    if x <= 324:
        x = 324
    if y >= 575:
        y = 575
    turn += 1
    turn %= 4
    clocks = 15

    # 방향키 누르면 움직이기
    if keys[pygame.K_RIGHT] and keys[pygame.K_LSHIFT] == 0:
        x += 2
        player = walkright[turn]
        clock.tick(clocks)
        pos = 'Right'
    elif keys[pygame.K_LEFT] and keys[pygame.K_LSHIFT] == 0:
        x -= 2
        player = walkleft[turn]
        clock.tick(clocks)
        pos = 'Left'
    elif keys[pygame.K_DOWN] and keys[pygame.K_LSHIFT] == 0:
        player = walkdown[turn]
        y += 2
        clock.tick(clocks)
        pos = 'Down'
    elif keys[pygame.K_UP] and keys[pygame.K_LSHIFT] == 0:
        player = walkup[turn]
        y -= 2
        clock.tick(clocks)
        pos = 'Up'

    # shift 누르면 달리기
    elif keys[pygame.K_RIGHT] and keys[pygame.K_LSHIFT] == 1:
        player = runright[turn]
        x += 2 * factor_size
        clock.tick(clocks)
        pos = 'Right'
    elif keys[pygame.K_LEFT] and keys[pygame.K_LSHIFT] == 1:
        player = runleft[turn]
        x -= 2 * factor_size
        clock.tick(clocks)
        pos = 'Left'
    elif keys[pygame.K_DOWN] and keys[pygame.K_LSHIFT] == 1:
        player = rundown[turn]
        y += 2 * factor_size
        clock.tick(clocks)
        pos = 'Down'
    elif keys[pygame.K_UP] and keys[pygame.K_LSHIFT] == 1:
        player = runup[turn]
        y -= 2 * factor_size
        clock.tick(clocks)
        pos = 'Up'
    else:
        os.chdir(APP_FOLDER + "/Sprites")
        player = pygame.image.load('Looking_' + pos + '_' + playerg + '.png')
        os.chdir(APP_FOLDER)

# 시작할 때 이름 정하기
playername = ''
def inputName():
    global display, playername, clock
    caps = False
    if keys[pygame.K_CAPSLOCK] and not(caps):
        caps = True
    elif keys[pygame.K_CAPSLOCK] and caps == True:
        caps = False
    clock.tick(10)
    if keys[pygame.K_a] and not(caps):
        playername += 'a'
    elif keys[pygame.K_a] and caps:
        playername += 'A'
    elif keys[pygame.K_b] and not(caps):
        playername += 'b'
    elif keys[pygame.K_b] and caps:
        playername += 'B'
    elif keys[pygame.K_c] and not(caps):
        playername += 'c'
    elif keys[pygame.K_c] and caps:
        playername += 'C'
    elif keys[pygame.K_d] and not(caps):
        playername += 'd'
    elif keys[pygame.K_d] and caps:
        playername += 'D'
    elif keys[pygame.K_e] and not(caps):
        playername += 'e'
    elif keys[pygame.K_e] and caps:
        playername += 'E'
    elif keys[pygame.K_f] and not(caps):
        playername += 'f'
    elif keys[pygame.K_f] and caps:
        playername += 'F'
    elif keys[pygame.K_g] and not(caps):
        playername += 'g'
    elif keys[pygame.K_g] and caps:
        playername += 'G'
    elif keys[pygame.K_h] and not(caps):
        playername += 'h'
    elif keys[pygame.K_d] and caps:
        playername += 'H'
    elif keys[pygame.K_i] and not(caps):
        playername += 'i'
    elif keys[pygame.K_i] and caps:
        playername += 'I'
    elif keys[pygame.K_j] and not(caps):
        playername += 'j'
    elif keys[pygame.K_j] and caps:
        playername += 'J'
    elif keys[pygame.K_k] and not(caps):
        playername += 'k'
    elif keys[pygame.K_k] and caps:
        playername += 'K'
    elif keys[pygame.K_l] and not(caps):
        playername += 'l'
    elif keys[pygame.K_l] and caps:
        playername += 'L'
    elif keys[pygame.K_m] and not(caps):
        playername += 'm'
    elif keys[pygame.K_m] and caps:
        playername += 'M'
    elif keys[pygame.K_n] and not(caps):
        playername += 'n'
    elif keys[pygame.K_n] and caps:
        playername += 'N'
    elif keys[pygame.K_o] and not(caps):
        playername += 'o'
    elif keys[pygame.K_o] and caps:
        playername += 'O'
    elif keys[pygame.K_p] and not(caps):
        playername += 'p'
    elif keys[pygame.K_p] and caps:
        playername += 'P'
    elif keys[pygame.K_q] and not(caps):
        playername += 'q'
    elif keys[pygame.K_q] and caps:
        playername += 'Q'
    elif keys[pygame.K_r] and not(caps):
        playername += 'r'
    elif keys[pygame.K_r] and caps:
        playername += 'R'
    elif keys[pygame.K_s] and not(caps):
        playername += 's'
    elif keys[pygame.K_s] and caps:
        playername += 'S'
    elif keys[pygame.K_t] and not(caps):
        playername += 't'
    elif keys[pygame.K_t] and caps:
        playername += 'T'
    elif keys[pygame.K_u] and not(caps):
        playername += 'u'
    elif keys[pygame.K_u] and caps:
        playername += 'U'
    elif keys[pygame.K_v] and not(caps):
        playername += 'v'
    elif keys[pygame.K_v] and caps:
        playername += 'V'
    elif keys[pygame.K_w] and not(caps):
        playername += 'w'
    elif keys[pygame.K_w] and caps:
        playername += 'W'
    elif keys[pygame.K_x] and not(caps):
        playername += 'x'
    elif keys[pygame.K_u] and caps:
        playername += 'X'
    elif keys[pygame.K_y] and not(caps):
        playername += 'y'
    elif keys[pygame.K_y] and caps:
        playername += 'Y'
    elif keys[pygame.K_z] and not(caps):
        playername += 'z'
    elif keys[pygame.K_z] and caps:
        playername += 'Z'
    elif keys[pygame.K_BACKSPACE]:
        playername = playername[:len(playername)-1]

    return 0


pokemon_array = []
for i in range(1, 13):
    each_pokemon = [icons[i - 1], i * 60, 200]
    pokemon_array.append(each_pokemon)

''' 포켓몬 줄여서 여기 우선 주석처리
for i in range(10, 19):
    each_pokemon = [icons[i - 1], (i - 9) * 60, 250]
    pokemon_array.append(each_pokemon)
for i in range(19, 28):
    each_pokemon = [icons[i - 1], (i - 18) * 60, 300]
    pokemon_array.append(each_pokemon)
for i in range(28, 37):
    each_pokemon = [icons[i - 1], (i - 27) * 60, 350]
    pokemon_array.append(each_pokemon)
for i in range(37, 46):
    each_pokemon = [icons[i - 1], (i - 36) * 60, 400]
    pokemon_array.append(each_pokemon)
    '''

id = 0
pikachu_background = pygame.image.load('fundo_box.png')
pikachu_background = pygame.transform.scale(pikachu_background, (800, 600))

# 포켓몬 선택시 보여주기
def show_icons():
    global icons, display, pokemon_array, id, pikachu_background, barratime, clock
    display.blit(pikachu_background, (0, 0))
    rect_id = pokemon_array[id][0].get_rect(topleft=(pokemon_array[id][1], pokemon_array[id][2]))
    clock.tick(15)
    display.blit(pokemon_array[id][0], (pokemon_array[id][1], pokemon_array[id][2] - 10))
    pygame.display.update(rect_id)
    display.blit(pikachu_background, (0, 0))
    for i in range(len(pokemon_array)):
        display.blit(pokemon_array[i][0], (pokemon_array[i][1], pokemon_array[i][2]))
    clock.tick(15)
    display.blit(barratime, (0, 0))
    pygame.display.flip()

# 싸우다 선택 후 기술 선택 창에서 각 기술 별로 id가 있는데 방향키 움직일때마다 기술 id 움직여줘서 선택할 때 해당되는 기술 쓰기 & 선택하려고 움직일 때마다 삑삑 소리 & 제한시간 20초
def choose_attack():
    global clock, techID, keys, myteam, mode
    clock.tick(20)
    if keys[pygame.K_RIGHT]:
        techID += 1
        beep.play()
    elif keys[pygame.K_LEFT]:
        techID -= 1
        beep.play()
    elif keys[pygame.K_DOWN]:
        techID += 2
        beep.play()
    elif keys[pygame.K_UP]:
        techID -= 2
        beep.play()
    elif keys[pygame.K_SPACE]:
        my_attack(myteam[0][5][techID])
        show_lines('{} use {}'.format(myteam[0][2], myteam[0][5][techID]))
        pygame.time.wait(200)
        if get_enemy()[0][6] > 0:
            attackOfEnemy()
        mode = 'select_menu'
    techID %= 4

# 선택한 포켓몬 우리팀으로 데려오기
def get_pokemon(id):
    x = []
    for i in id:
        x.append(i)
    return x


# 포켓몬 선택 시 위치별로 id 달라짐
def select_pokemon_id():
    global keys, id, ids, myteam, beep
    if keys[pygame.K_RIGHT]:
        id += 1
        beep.play()
    elif keys[pygame.K_LEFT]:
        id -= 1
        beep.play()
    elif keys[pygame.K_DOWN]:
        id += 12
        beep.play()
    elif keys[pygame.K_UP]:
        id -= 12
        beep.play()
    elif keys[pygame.K_SPACE]:
        myteam.append(get_pokemon(ids[id]))       # 스페이스 누르면 해당 포켓몬 내 팀으로 데려오기
    clock.tick(25)
    id = id % 12

select_icon = pygame.image.load('seleciona.png')


# 싸울 때 메뉴 선택 창
def select_menu():
    global keys, id, beep, mode
    if keys[pygame.K_RIGHT]:
        id += 1
        beep.play()
    elif keys[pygame.K_LEFT]:
        id -= 1
        beep.play()
    elif keys[pygame.K_DOWN]:
        id += 2
        beep.play()
    elif keys[pygame.K_UP]:
        id -= 2
        beep.play()
    elif keys[pygame.K_SPACE]:
        if id == 0:
            mode = 'select_tech'
        if id == 1:
            mode = 'select_menu'
        if id == 2:
            mode = 'select_pokemon'
    pygame.time.wait(80)
    clock.tick(15)
    id = id % 3


def blit_seleciona():
    global mode, id, select_icon, techID
    posm = posx, posy = pygame.mouse.get_pos()
    posb = 0
    if mode == 'select_menu':
        if id == 0:
            posb = (388, 409)
        elif id == 1:
            posb = (62,512)
        elif id == 2:
            posb = (721, 512)
    if mode == 'select_tech':
        if techID == 0:
            posb = (105, 394)
        elif techID == 1:
            posb = (348, 394)
        elif techID == 2:
            posb = (105, 488)
        elif techID == 3:
            posb = (348, 488)
    return posb

# 방향키로 움직여서 캐릭터 id 받기
def choose_character():
    global keys, id
    if keys[pygame.K_RIGHT]:
        id += 1
    elif keys[pygame.K_LEFT]:
        id -= 1
    #elif keys[pygame.K_DOWN]:
    #    id += 2
    #elif keys[pygame.K_UP]:
    #    id -= 2
    elif keys[pygame.K_SPACE]:
        select_gender(id)
    id %= 2
    show_character_choice()

# 포켓몬 별 아이콘 id 리턴
def get_icon(txt):
    a = ''
    txt = str(txt)
    for i in txt:
        if i.isnumeric(): a += i
    return int(a)-1

# 포켓몬 우리팀에 하나씩 늘어날 때마다 이름이랑 아이콘 뜨도록 창 설정
def this_is_myteam():
    global display, icons, myteam, ids, barratime
    xpos, ypos = pygame.mouse.get_pos()
    if len(myteam) == 1:
        x = get_icon(myteam[0][0])
        display.blit(icons[x], (20, 20))
        name = font2.render(myteam[0][2], True, [255,255,255])
        display.blit(name, (75, 19))
    if len(myteam) == 2:
        x = get_icon(myteam[0][0])
        display.blit(icons[x], (20, 20))
        name = font2.render(myteam[0][2], True, [255,255,255])
        display.blit(name, (75, 19))
        x = get_icon(myteam[1][0])
        display.blit(icons[x], (342, 20))
        name = font2.render(myteam[1][2], True, [255,255,255])
        display.blit(name, (397, 19))
    if len(myteam) == 3:
        x = get_icon(myteam[0][0])
        display.blit(icons[x], (20, 20))
        name = font2.render(myteam[0][2], True, [255,255,255])
        display.blit(name, (75, 19))
        x = get_icon(myteam[1][0])
        display.blit(icons[x], (342, 20))
        name = font2.render(myteam[1][2], True, [255,255,255])
        display.blit(name, (397, 19))
        x = get_icon(myteam[2][0])
        display.blit(icons[x], (667, 20))
        name = font2.render(myteam[2][2], True, [255,255,255])
        display.blit(name, (722, 19))
    if len(myteam) == 4:
        x = get_icon(myteam[0][0])
        display.blit(icons[x], (20, 20))
        name = font2.render(myteam[0][2], True, [255,255,255])
        display.blit(name, (75, 19))
        x = get_icon(myteam[1][0])
        display.blit(icons[x], (342, 20))
        name = font2.render(myteam[1][2], True, [255,255,255])
        display.blit(name, (397, 19))
        x = get_icon(myteam[2][0])
        display.blit(icons[x], (667, 20))
        name = font2.render(myteam[2][2], True, [255,255,255])
        display.blit(name, (722, 19))
        x = get_icon(myteam[3][0])
        display.blit(icons[x], (20, 78))
        name = font2.render(myteam[3][2], True, [255, 255, 255])
        display.blit(name, (75, 73))
    if len(myteam) == 5:
        x = get_icon(myteam[0][0])
        display.blit(icons[x], (20, 20))
        name = font2.render(myteam[0][2], True, [255, 255, 255])
        display.blit(name, (75, 19))
        x = get_icon(myteam[1][0])
        display.blit(icons[x], (342, 20))
        name = font2.render(myteam[1][2], True, [255, 255, 255])
        display.blit(name, (397, 19))
        x = get_icon(myteam[2][0])
        display.blit(icons[x], (667, 20))
        name = font2.render(myteam[2][2], True, [255, 255, 255])
        display.blit(name, (722, 19))
        x = get_icon(myteam[3][0])
        display.blit(icons[x], (20, 78))
        name = font2.render(myteam[3][2], True, [255, 255, 255])
        display.blit(name, (75, 73))
        x = get_icon(myteam[4][0])
        display.blit(icons[x], (342, 78))
        name = font2.render(myteam[4][2], True, [255, 255, 255])
        display.blit(name, (397, 73))
    if len(myteam) == 6:
        x = get_icon(myteam[0][0])
        display.blit(icons[x], (20, 20))
        name = font2.render(myteam[0][2], True, [255, 255, 255])
        display.blit(name, (75, 19))
        x = get_icon(myteam[1][0])
        display.blit(icons[x], (342, 20))
        name = font2.render(myteam[1][2], True, [255, 255, 255])
        display.blit(name, (397, 19))
        x = get_icon(myteam[2][0])
        display.blit(icons[x], (667, 20))
        name = font2.render(myteam[2][2], True, [255, 255, 255])
        display.blit(name, (722, 19))
        x = get_icon(myteam[3][0])
        display.blit(icons[x], (20, 78))
        name = font2.render(myteam[3][2], True, [255, 255, 255])
        display.blit(name, (75, 73))
        x = get_icon(myteam[4][0])
        display.blit(icons[x], (342, 78))
        name = font2.render(myteam[4][2], True, [255, 255, 255])
        display.blit(name, (397, 73))
        x = get_icon(myteam[5][0])
        display.blit(icons[x], (667, 78))
        name = font2.render(myteam[5][2], True, [255, 255, 255])
        display.blit(name, (722, 73))

# 포켓몬 아이콘 다 뜨고 그에 맞게 id 함께 설정
def select_pokemon():
    global display, icons, id
    select_pokemon_id()
    show_icons()


os.chdir(APP_FOLDER + '/Sprites')
character = [pygame.image.load('Principal_FW.png'), pygame.image.load('Principal_MB.png')]

# 포켓몬 선택시에 뿌옇게 되는 거 연속적 이미지로 리스트에 넣기 -> 활용은 안한듯
selboxes = []
for i in range(1, 5):
    selboxes.append(pygame.image.load('box_sel{}.png'.format(i)))

# 캐릭터 선택시 선택한 캐릭터 밝게, 아닌 캐릭터 어둡게
characteraux = []
for i in range(len(character)):
    copy = character[i]
    copy.fill((100, 100, 100), special_flags=pygame.BLEND_RGB_SUB)
    characteraux.append(copy)
character = [pygame.image.load('Principal_FW.png'), pygame.image.load('Principal_MB.png')]
os.chdir(APP_FOLDER)

# 바꿀 포켓몬의 인덱스별로 포켓몬 정보 넘겨주기
select_pokemon_index = 0
def to_change_pokemon():
    global select_pokemon_index, selboxes, display_select_pokemon
    if select_pokemon_index == 0:
        x = [[display_select_pokemon, (0,0)], [selboxes[2], (177,143)], [selboxes[0], (443, 150)], [selboxes[0], (176, 258)],
             [selboxes[0], (443, 258)], [selboxes[0], (174, 374)], [selboxes[0], (443, 374)]]
    elif select_pokemon_index == 1:
        x = [[display_select_pokemon, (0, 0)], [selboxes[3], (173, 148)], [selboxes[1], (443, 144)],
             [selboxes[0], (176, 258)], [selboxes[0], (443, 258)], [selboxes[0], (174, 374)], [selboxes[0], (443, 374)]]
    elif select_pokemon_index == 2:
        x = [[display_select_pokemon, (0, 0)], [selboxes[3], (173, 148)], [selboxes[0], (443, 150)],
             [selboxes[1], (176, 252)], [selboxes[0], (443, 258)], [selboxes[0], (174, 374)], [selboxes[0], (443, 374)]]
    elif select_pokemon_index == 3:
        x = [[display_select_pokemon, (0, 0)], [selboxes[3], (173, 148)], [selboxes[0], (443, 150)],
             [selboxes[0], (176, 258)], [selboxes[1], (443, 252)], [selboxes[0], (174, 374)], [selboxes[0], (443, 374)]]
    elif select_pokemon_index == 4:
        x = [[display_select_pokemon, (0, 0)], [selboxes[3], (173, 148)], [selboxes[0], (443, 150)],
             [selboxes[0], (176, 258)], [selboxes[0], (443, 258)], [selboxes[1], (174, 370)], [selboxes[0], (443, 374)]]
    elif select_pokemon_index == 5:
        x = [[display_select_pokemon, (0, 0)], [selboxes[3], (173, 148)], [selboxes[0], (443, 150)],
             [selboxes[0], (176, 258)], [selboxes[0], (443, 258)], [selboxes[0], (174, 374)], [selboxes[1], (443, 370)]]
    return x

# mode와 그 mode의 몇 번째 아이콘이냐에 따라 아이콘의 위치 리턴하기
def icon_position(i, mode):
    x = 0
    if mode == 'icon':
        if i == 0: x = (215, 171)
        elif i == 1: x = (476, 176)
        elif i == 2: x = (215, 280)
        elif i == 3: x = (476, 283)
        elif i == 4: x = (217, 397)
        elif i == 5: x = (483, 398)
    elif mode == 'name':
        if i == 0: x = (297, 162)
        elif i == 1: x = (572, 164)
        elif i == 2: x = (297, 273)
        elif i == 3: x = (572, 273)
        elif i == 4: x = (297, 388)
        elif i == 5: x = (572, 388)
    elif mode == 'hp1':
        if i == 0: x = (303, 201)
        elif i == 1: x = (571, 205)
        elif i == 2: x = (303, 312)
        elif i == 3: x = (571, 312)
        elif i == 4: x = (303, 428)
        elif i == 5: x = (571, 428)
    elif mode == 'hp2':
        if i == 0: x = (303+35, 201)
        elif i == 1: x = (571+35, 205)
        elif i == 2: x = (303+35, 312)
        elif i == 3: x = (571+35, 312)
        elif i == 4: x = (303+35, 428)
        elif i == 5: x = (571+35, 428)
    return x

# 포켓몬 바꾸면 화면에 나오는 포켓몬 정보 바꿔주기
def change_pokemon():
    global display_select_pokemon, selboxes, select_pokemon_index, clock
    global icons, myteam
    x1 = []
    posm = pygame.mouse.get_pos()
    names = []
    hp1 = []
    hp2 = []
    for i in range(len(myteam)):
        aux = [icons[get_icon(myteam[i][0])], icon_position(i, 'icon')]
        x1.append(aux)
        aux2 = [font2.render(myteam[i][2], True, [255, 255, 255]), icon_position(i, 'name')]
        names.append(aux2)
        aux3 = [font2.render(str(myteam[i][6]), True, [255, 255, 255]), icon_position(i, 'hp1')]
        hp1.append(aux3)
        aux4 = [font2.render(str(myteam[i][7]), True, [255, 255, 255]), icon_position(i, 'hp2')]
        hp2.append(aux4)
    x = to_change_pokemon()
    x = x[0:len(myteam)+1]
    x = x + x1 + names + hp1 + hp2
    return x

# 포켓몬 바꾸러 들어가서 키보드 움직이면 index 바뀌고 space 누르면 바로 적의 공격 턴으로 넘어감
def change_pokemon_2():
    global select_pokemon_index, myteam, clock, beep, current_pokemon, mode, spritestimen
    if keys[pygame.K_UP]:
        select_pokemon_index -= 2
        beep.play()
    elif keys[pygame.K_DOWN]:
        select_pokemon_index += 2
        beep.play()
    elif keys[pygame.K_RIGHT]:
        select_pokemon_index += 1
        beep.play()
    elif keys[pygame.K_LEFT]:
        select_pokemon_index -= 1
        beep.play()
    elif keys[pygame.K_SPACE]:
        mode = 'enemy\'s_attack'
        myteam[0], myteam[select_pokemon_index] = myteam[select_pokemon_index], myteam[0]       # 맨 처음 애랑 고른 애랑 인덱스 바꿔주기
        spritestimen[0], spritestimen[select_pokemon_index] = spritestimen[select_pokemon_index], spritestimen[0]   # 이미지도 바꿔줘야 함
        current_pokemon = myteam[0]     # 맨 처음으로 옮겨 놓은 (아까 고른) 포켓몬이 화면에 나와 있는 포켓몬
    select_pokemon_index %= len(myteam)
    clock.tick(8)

# 키보드 움직일 때마다 캐릭터 선택 화면 (밝기 차이)
def show_character_choice():
    global id, display, character, fundo, characteraux
    display.blit(fundo, (0, 0))
    if id == 0:
        display.blit(character[0], (200, 200))
        display.blit(characteraux[1], (400, 200))
    elif id == 1:
        display.blit(characteraux[0], (200, 200))
        display.blit(character[1], (400, 200))
    pygame.time.wait(60)
    pygame.display.flip()

# 캐릭터 성별 정해줌
def select_gender(id):
    global playerg, did_select_character
    if id == 0:
        playerg = 'FW'
    elif id == 1:
        playerg = 'MB'
    did_select_character = True     # 캐릭터 골랐다

# 이름 입력하라는 창
def show_name():
    global display, playername, font
    pygame.time.wait(40)
    posm = posx, posy = pygame.mouse.get_pos()
    textoa = "Input your name."  ######################################바꿈
    textoa = font.render(textoa, True, [0, 0, 0])
    display.blit(textoa, (94, 188))
    playernamea = font.render(playername, True, [0, 0, 0])
    display.blit(playernamea, (215, 79))
    font3 = pygame.font.Font('gamefont.ttf', 25)
    display.blit((font3.render('Decided', True, [0,0,0])), (638, 208))
    display.blit((font3.render('Delete', True, [0, 0, 0])), (521, 208))
    pygame.display.flip()

# 상대편이랑 내 캐릭터 체력 아이콘
tela_ataque = pygame.image.load('tela ataque.png')
os.chdir(APP_FOLDER + '/Sprites')
my_hp = pygame.image.load('barra_aliado.png')
enemy_hp = pygame.image.load('barra_inimigo.png')
os.chdir(APP_FOLDER)

# 기술 별로 타입인덱스 부여. 그 타입인덱스를 타입박스에 넣으면 해당 타입 리턴
def get_type(tech):
    global typeboxes    # 포켓몬 기술 속성
    if tech == 'Solar Beam' or tech == 'Leaf Storm':
        type_index = 8
    if tech == 'Scratch' or tech == 'Hyper Beam' or tech == 'Bite' or tech == 'Quick Assault'  or tech == 'Assault':
        type_index = 3
    if tech == 'Earthquake':
        type_index = 0
    if tech == 'Karate Blow' or tech == 'Low Blow' or tech == 'Cut Across':
        type_index = 1
    if tech == 'Aqua Jet' or tech == 'Bubble Beam':
        type_index = 2
    if tech == 'Glacial Bite' or tech == 'Ice Beam' or tech == 'Blizzard':
        type_index = 4
    if tech ==  'Inferno' or tech == 'Flame Radiation' or tech == 'Circle of Fire':
        type_index = 6
    if tech == 'Thunder' or tech == 'Thunderbolt' or tech == 'Bolt Strike' or tech == 'Lightning Sphere' or tech == 'Bolttacker' or tech == 'Thunder Bite' or tech == 'Thunder Storm':
        type_index = 9
    if tech == 'Haunt' or tech == 'Nightmare' or tech == 'Dark Sphere':
        type_index = 11
    if tech == 'Energy Ball' or tech == 'Confuse' or tech == 'Psychic Blow':
        type_index = 12
    if tech == 'Poissonous':
        type_index = 13
    if tech == 'Somersault':
        type_index = 14
    if tech == 'Collapse':
        type_index = 15
    return typeboxes[type_index]


# 위와 같은데 이거는 직접 기술을 넣어서 타입 리턴
def get_type_txt(tech):
    if tech == 'Solar Beam' or tech == 'Leaf Storm':
        type = 'Grass'
    if tech == 'Scratch' or tech == 'Hyper Beam' or tech == 'Bite' or tech == 'Quick Assault' or tech == 'Assault':
        type = 'Normal'
    if tech == 'Earthquake':
        type = 'Ground'
    if tech == 'Karate Blow' or tech == 'Low Blow' or tech == 'Cut Across':
        type = 'Fight'
    if tech == 'Aqua Jet' or tech == 'Bubble Beam':
        type = 'Water'
    if tech == 'Glacial Bite' or tech == 'Ice Beam' or tech == 'Blizzard':
        type = 'Ice'
    if tech == 'SOCO DE FOGO' or tech == 'Inferno' or tech == 'LABAREDA' or tech == 'Flame Radiation' or tech == 'Circle of Fire':
        type = 'Fire'
    if tech == 'Thunder' or tech == 'Thunderbolt' or tech == 'Bolt Strike' or tech == 'Lightning Sphere' or tech == 'Bolttacker' or tech == 'Thunder Bite' or tech == 'Thunder Storm':
        type = 'Electric'
    if tech == 'Haunt' or tech == 'Nightmare' or tech == 'Dark Sphere':
        type = 'Dark'
    if tech == 'Energy Ball' or tech == 'Confuse' or tech == 'Psychic Blow':
        type = 'Esper'
    if tech == 'Poissonous':
        type = 'Poisson'
    if tech == 'Somersault':
        type = 'Fly'
    if tech == 'Collapse':
        type = 'Rock'
    return type

# damage_amount 계산해서 기술별로 상대에게 얼마나 효과있는지 리턴
def how_effective(pokemon_type, enemy_type, tipo21, teste):
    x = damage_amount(pokemon_type, enemy_type, tipo21, teste)
    if x == 1:
        effect = '      Effective'
    elif x>= 2:
        effect = 'SUPER Effective'
    elif x == 0.5:
        effect = 'Less Effective'
    elif x == 0:
        effect = '   NOT Effective'
    return effect

# 텍스트 가운데 정렬
def centralizar(text):
    while len(text) < 19:
        text = ' ' + text + ' '
    return text

typeboxes = []

# 움직이게 보이는 것들 이미지 가져오기
def get_from_sprites():
    global walkdown, walkleft, walkright, walkup, rundown, runleft, runright, runup, playerg, APP_FOLDER, launchpkb, typeboxes
    os.chdir(APP_FOLDER + '/Sprites')
    # 달리는 이미지 연속으로 보이게
    for i in range(1, 3):
        runup.append(pygame.image.load('Run_Up_0_{}.png'.format(playerg)))
        runup.append(pygame.image.load('Run_Up_{}_{}.png'.format(i, playerg)))
        runleft.append(pygame.image.load('Run_Left_0_{}.png'.format(playerg)))
        runleft.append(pygame.image.load('Run_Left_{}_{}.png'.format(i, playerg)))
        rundown.append(pygame.image.load('Run_Down_0_{}.png'.format(playerg)))
        rundown.append(pygame.image.load('Run_Down_{}_{}.png'.format(i, playerg)))
        runright.append(pygame.image.load('Run_Right_0_{}.png'.format(playerg)))
        runright.append(pygame.image.load('Run_Right_{}_{}.png'.format(i, playerg)))
    # 걷는 이미지 연속으로 보이게
    for i in range(1, 3):
        walkup.append(pygame.image.load('Looking_Up_{}.png'.format(playerg)))
        walkup.append(pygame.image.load('Walking_Up_{}_{}.png'.format(i, playerg)))
        walkleft.append(pygame.image.load('Looking_Left_{}.png'.format(playerg)))
        walkleft.append(pygame.image.load('Walking_Left_{}_{}.png'.format(i, playerg)))
        walkdown.append(pygame.image.load('Looking_Down_{}.png'.format(playerg)))
        walkdown.append(pygame.image.load('Walking_Down_{}_{}.png'.format(i, playerg)))
        walkright.append(pygame.image.load('Looking_Right_{}.png'.format(playerg)))
        walkright.append(pygame.image.load('Walking_Right_{}_{}.png'.format(i, playerg)))
    # 몬스터볼 던지는 모션
    for i in range(1, 6):
        launchpkb.append(pygame.image.load('pk{}{}.png'.format(i, playerg)))
    # 타입 박스 리스트에 추가해두기
    for i in range(1, 17):
        typeboxes.append(pygame.image.load('type_box{}.png'.format(i)))
    os.chdir(APP_FOLDER)

passage_line = pygame.image.load('principalfundo.png')
mode = "game"
pygame.mixer.music.play()
turn = 0


techID = 0

def show_character():
    global turn, clock, display, walkdown
    turn += 1
    turn %= 4
    posm = posx, posy = pygame.mouse.get_pos()
    player = walkdown[turn]
    player = pygame.transform.scale(player, (68, 68))
    display.blit(player, (91, 57))

# 상대편 hp 줄게 하기
def my_attack(pokemon):
    global myteam, pkmn_luciana, pkmn_astro, pkmn_clara, pkmn_ale, playername, mode
    if fightingNPC == 'astro':
        m = damage_amount(pokemon, pkmn_astro[0][3], pkmn_astro[0][4] ,False)
        pkmn_astro[0][6] -= 50*m
    if fightingNPC == 'ale':
        m = damage_amount(pokemon, pkmn_ale[0][3], pkmn_ale[0][4] ,False)
        pkmn_ale[0][6] -= 50*m
    if fightingNPC == 'clara':
        m = damage_amount(pokemon, pkmn_clara[0][3], pkmn_clara[0][4] ,False)
        pkmn_clara[0][6] -= 50*m
    if fightingNPC == 'luciana':
        m = damage_amount(pokemon, pkmn_luciana[0][3], pkmn_luciana[0][4] ,False)
        pkmn_luciana[0][6] -= 50*m
    mode = 'select_menu'

# 기술 인덱스별로 타입 리턴한 거 보여주기
def blit_ataques(ataque):
    a = get_type(ataque)
    a = pygame.transform.scale(a, (int(124*1.5), int(55*1.5)))
    return a

# 누구랑 싸우냐에 따라 그 이름 리턴
def get_enemy2():
    global fightingNPC, astro, ale, luciana, clara
    if fightingNPC == 'astro':
        return astro
    if fightingNPC == 'ale':
        return ale
    if fightingNPC == 'clara':
        return clara
    if fightingNPC == 'luciana':
        return luciana

# 누구랑 싸우냐에 따라 그 트레이너의 포켓몬들 리턴
def get_enemy():
    global pkmn_astro, pkmn_clara, fightingNPC, pkmn_luciana, pkmn_ale
    if fightingNPC == 'astro':
        return pkmn_astro
    if fightingNPC == 'ale':
        return pkmn_ale
    if fightingNPC == 'clara':
        return pkmn_clara
    if fightingNPC == 'luciana':
        return pkmn_luciana

# 대결할 때 나오는 멘트들, 포켓몬 죽었을 때 등등....
def battle_situation():
    global pkmn_ale, pkmn_luciana, pkmn_clara, pkmn_astro, myteam, mode, NPCposition, defeated_enemy, APP_FOLDER, playername, spritestimen
    global current_pokemon, mainloop2, clock
    end = pygame.image.load('ending.png')
    win = pygame.image.load('win.gif')
    winall = pygame.image.load('winall.jpg')
    if current_pokemon[6] <= 0:
        show_lines('{} was defeated'.format(myteam[0][2]))
        clock.tick(7)
        show_lines('{}: Oh, no!'.format(playername))
        if len(myteam) >= 2:
            show_lines('{}: Go {}'.format(playername, myteam[1][2]))
        else:   # 내 포켓몬 모두 죽으면 끝
            show_lines('{}: Damn it, I lost it!'.format(playername))
            endActive = True
            while endActive:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameActive = False
                display.blit(end, (0, 0))
                mouse = pygame.mouse.get_pressed()
                if mouse[0]:
                    endActive = False
                pygame.display.update()
        del myteam[0]
        del spritestimen[0]
    if len(myteam) <= 0:
        mainloop2 = False
    if fightingNPC == 'astro':
        if pkmn_astro[0][6] <= 0:
            if len(pkmn_astro) > 1:
                show_lines('Astro: oh no! {} come back'.format(pkmn_astro[0][2]))
                if len(pkmn_astro) >= 2:
                    show_lines('Astro: Finish him {}!'.format(pkmn_astro[1][2]))
                del pkmn_astro[0]
            else:
                show_lines('Astro: DAMN IT! You can go! ')
                clock.tick(8)
                show_lines('Astro: But do not think you\'ll get far!')
                mode = 'game'
                pic(win)
                del NPCposition[2]
                os.chdir(APP_FOLDER + '/Sons')
                pygame.mixer.music.load('main_music.mp3')
                pygame.init()
                pygame.mixer.music.play()
                os.chdir(APP_FOLDER)
                defeated_enemy += 1       # Astro 이기면 ale랑 싸우게 +1 해주기
    if fightingNPC == 'ale':
        if pkmn_ale[0][6] <= 0:
            if len(pkmn_ale) > 1:
                show_lines('Ale: oh no! {} come back.'.format(pkmn_ale[0][2], pkmn_ale[1][2]))
                clock.tick(10)
                if len(pkmn_ale) >= 2:
                    show_lines('Ale: Go {}!'.format(pkmn_ale[1][2]))
                del pkmn_ale[0]
            else:
                show_lines('Ale: You will not get very far.')
                mode = 'game'
                pic(win)
                os.chdir(APP_FOLDER + '/Sons')
                pygame.mixer.music.load('main_music.mp3')
                pygame.init()
                pygame.mixer.music.play()
                os.chdir(APP_FOLDER)
                del NPCposition[2]
                defeated_enemy += 1   # ale 이기면 다음 clara 만나게 +1
    if fightingNPC == 'clara':
        if pkmn_clara[0][6] <= 0:
            if len(pkmn_clara) > 1:
                show_lines('Clara: Oh, no! {} come back, end it {}! I need to get through!'.format(pkmn_clara[0][2], pkmn_clara[1][2]))
                del pkmn_clara[0]
            else:
                show_lines('Clara: DAMN IT! You can pass, but do not think it will end!')
                mode = 'game'
                pic(win)
                os.chdir(APP_FOLDER + '/Sons')
                pygame.mixer.music.load('main_music.mp3')
                pygame.init()
                pygame.mixer.music.play()
                os.chdir(APP_FOLDER)
                del NPCposition[2]
                defeated_enemy += 1   # clara 이기면 luciana 만나게 하기
    if fightingNPC == 'luciana':
        if pkmn_luciana[0][6] <= 0:
            if len(pkmn_luciana) > 1:
                show_lines('Luciana: Oh, no! {} come back, end it {}! I need to go!'.format(pkmn_luciana[0][2], pkmn_luciana[1][2]))
                del pkmn_luciana[0]
            else:
                show_lines('Luciana: DAMN IT! You can go, but do not think you\'re going to get there!')
                mode = 'game'
                pic(winall)
                os.chdir(APP_FOLDER + '/Sons')
                pygame.mixer.music.load('main_music.mp3')
                pygame.init()
                pygame.mixer.music.play()
                os.chdir(APP_FOLDER)
                del NPCposition[2]
                defeated_enemy += 1

# 상대편 공격
def attackOfEnemy():
    global pkmn_astro, pkmn_luciana, pkmn_clara, pkmn_ale, myteam, current_pokemon
    x = random.randrange(0,4)
    if defeated_enemy == 0:
        c = pkmn_astro[0][5][x]
        show_lines('{} use {}'.format(pkmn_astro[0][2], pkmn_astro[0][5][x]))
        c = damage_amount(c, current_pokemon[0][3], current_pokemon[0][4], False)
        current_pokemon[6] -= 50 * c
    if defeated_enemy == 1:
        c = pkmn_ale[0][5][x]
        show_lines('{} use {}'.format(pkmn_ale[0][2], pkmn_ale[0][5][x]))
        c = damage_amount(c, myteam[0][3], myteam[0][4], False)
        current_pokemon[6] -= 50 * c
    if defeated_enemy == 2:
        c = pkmn_clara[0][5][x]
        show_lines('{} use {}'.format(pkmn_clara[0][2], pkmn_clara[0][5][x]))
        c = damage_amount(c, myteam[0][3], myteam[0][4], False)
        current_pokemon[6] -= 50 * c
    if defeated_enemy == 3:
        c = pkmn_luciana[0][5][x]
        show_lines('{} use {}'.format(pkmn_luciana[0][2], pkmn_luciana[0][5][x]))
        c = damage_amount(c, myteam[0][3], myteam[0][4], False)
        current_pokemon[6] -= 50 * c


def get_hp_bar(type):
    global myteam, pkmn_ale, pkmn_astro, pkmn_clara, pkmn_luciana, hpa, fightingNPC
    if type == 'aliado':
        x = int((myteam[0][6] / myteam[0][7]) * 100)
    else:
        if fightingNPC == 'astro':
            x = int((pkmn_astro[0][6] / pkmn_astro[0][7]) * 100)
        if fightingNPC == 'ale':
            x = int((pkmn_ale[0][6] / pkmn_ale[0][7]) * 100)
        if fightingNPC == 'clara':
            x = int((pkmn_clara[0][6] / pkmn_clara[0][7]) * 100)
        if fightingNPC == 'luciana':
            x = int((pkmn_luciana[0][6] / pkmn_luciana[0][7]) * 100)
    if x > 70:
        hpa = pygame.transform.scale(hp[0], (int(x * 0.84), 11))
    if x <= 70:
        hpa = pygame.transform.scale(hp[1], (int(x * 0.84), 11))
    if x <= 30:
        hpa = pygame.transform.scale(hp[2], (int(x * 0.84), 11))
    if x <= 0:
        hpa = pygame.transform.scale(hp[2], (0, 11))
    return hpa

clock = pygame.time.Clock()
turn = 0
hpa = pygame.transform.scale(hp[0], (84, 11))
playerg = ''
did_input_name = False
did_select_character = False

# 캐릭터 고를 때까지 캐릭터 화면 뜨기

introActive = True
intro = pygame.image.load('intro.jpg')

R.Act(introActive,intro)


while did_select_character == False:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_q]:
            pygame.quit()
            sys.exit()
    display.blit(fundo, (0, 0))  # Mostrar o fundoq
    choose_character()
    pygame.display.flip()
    clock.tick(25)
get_from_sprites()

# 이름 정할 때까지 키보드 화면 뜨기
while did_input_name == False:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_q]:
            pygame.quit()
            sys.exit()
    if keys[pygame.K_RETURN]:
        did_input_name = True
    display.blit(keyboard_image, (0,0))
    inputName()
    show_character()
    show_name()

id = 0

# 포켓몬 6마리 고를 때까지 포켓몬 고르는 창 뜨기
while len(myteam) != 6:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # or keys[pygame.K_q]:
            pygame.quit()
            sys.exit()
    select_pokemon()
    this_is_myteam()
    pygame.display.flip()

# escolheu_time = False

allowPass = True
id = 0
fightingNPC = 'astro'
os.chdir(APP_FOLDER + '/pkmns')
spritestimen = []
spritestimew = []

for i in range(6):
    auxa = pygame.image.load(myteam[i][1])
    auxa = pygame.transform.scale(auxa, (82*5, 82*5))
    spritestimew.append(x)
    auxa = pygame.image.load(myteam[i][0])
    auxa = pygame.transform.scale(auxa, (82*5, 82*5))
    spritestimen.append(pygame.image.load(myteam[i][0]))
os.chdir(APP_FOLDER)
y = 800
mainloop2 = True
x = 400

# 주인공한테 느낌표 뜨면서 다가올 때 이미지   각 트레이너 자리에서 주인공 자리까지 걸어오기
NPCposition = [[passage_line, (0, 0)], [player, (x, y)], [astro[3], (astro[1], astro[2])],
                 [ale[3], (ale[1], ale[2])],
                 [clara[3], (clara[1], clara[2])], [luciana[3], (luciana[1], luciana[2])]]

# 게임 전반적인 모드 포함해서 게임 돌아가는데 안꺼지도록
while mainloop2:
    NPCposition[1] = [player, (x, y)]
    posm = posx, posy = pygame.mouse.get_pos()
    telabatalha = [[main_background, (0,0)], [tela_ataque, (0,0)], [my_hp, (596, 302)], [enemy_hp, (0, 54)],
                   [myground, (3, 354)], [enemy_ground, (495, 134)], [get_hp_bar('aliado'), (700, 335)],
                   [select_icon, blit_seleciona()], [get_hp_bar(''), (84, 94)],
                   [pygame.transform.scale2x(spritestimen[0]), (146, 238)],[pygame.transform.scale2x(get_enemy()[0][0]), (564, 20)],
                   [font2.render(str(myteam[0][2]), True, [0, 0, 0]), (714, 313)],[font2.render(str(get_enemy()[0][2]), True, [0,0,0]), (93, 71)],
                   [pygame.transform.scale2x(get_enemy()[0][0]), (564, 20)],
                   [font2.render(str(myteam[0][6]), True, [0,0,0]), (721, 345)],
                   [font2.render(str(myteam[0][7]), True, [0,0,0]), (756, 345)]]
    keys = pygame.key.get_pressed()
    display.fill((0,0,0))
    display.blit(passage_line, (0, 0))  # 배경 나타나기
    if len(myteam) == 0:
        break
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_q]:
            pygame.quit()
            sys.exit()
    if allowPass: andar()
    if mode == 'game':
        allowPass = True
        meet_NPC()
        telaatual = NPCposition
    elif mode == 'ready':
        approachingNPC(fightingNPC)
        telaatual = NPCposition
    elif mode == 'battlefield':
        os.chdir(APP_FOLDER + '/Sons')
        pygame.mixer.music.load('batalha.mp3')
        pygame.init()
        pygame.mixer.music.play()
        os.chdir(APP_FOLDER)
        mode = 'select_menu'
        animation_transition(get_enemy2()[6])
        NPCchallenge(get_enemy2())      # Trainer 리턴
    elif mode == 'select_menu':
        os.chdir(APP_FOLDER)
        tela_ataque = pygame.image.load('tela ataque.png')
        telaatual = telabatalha
        select_menu()
    elif mode == 'select_tech':
        if keys[pygame.K_ESCAPE]:
            mode = 'select_menu'
        pkmni_atual = get_enemy()  # 각 트레이너별로 자기 포켓몬 리턴
        tela_ataque = pygame.image.load('tela_sel.png')
        how_effective_txt = how_effective(myteam[0][5][techID], pkmni_atual[0][3], pkmni_atual[0][4], False)
        how_effective_txt = font.render(how_effective_txt, True, [0, 0, 0])
        telaescolha = [[main_background, (0, 0)], [tela_ataque, (0, 0)], [my_hp, (596, 302)],
                       [enemy_hp, (0, 54)], [myground, (3, 354)], [enemy_ground, (495, 134)],
                       [get_hp_bar('aliado'), (700, 335)],
                       [blit_ataques(myteam[0][5][0]), (25, 412)],
                       [font2.render(centralizar(myteam[0][5][0]), True, [0, 0, 0]), (71, 434)],
                       [blit_ataques(myteam[0][5][1]), (264, 411)],
                       [font2.render(centralizar(myteam[0][5][1]), True, [0, 0, 0]), (308, 434)],
                       [blit_ataques(myteam[0][5][2]), (25, 502)],
                       [font2.render((centralizar(myteam[0][5][2])), True, [0, 0, 0]), (73, 529)],
                       [blit_ataques(myteam[0][5][3]), (264, 502)],
                       [font2.render(centralizar(myteam[0][5][3]), True, [0, 0, 0]), (308, 529)],
                       [select_icon, blit_seleciona()], [how_effective_txt, (592, 404)],
                       [pygame.transform.scale2x(get_enemy()[0][0]), (564, 20)],
                       [font2.render(str(myteam[0][6]), True, [0,0,0]), (721, 345)],
                       [font2.render(str(myteam[0][7]), True, [0,0,0]), (756, 345)],
                       [font2.render(str(myteam[0][2]), True, [0, 0, 0]), (714, 313)],
                       [pygame.transform.scale2x(spritestimen[0]), (146, 238)], [get_hp_bar(''), (84, 94)],
                       [font2.render(str(get_enemy()[0][2]), True, [0,0,0]), (93, 71)]]
        current_pokemon = myteam[0]
        telaatual = telaescolha
        choose_attack()
        blit_seleciona()
        battle_situation()
    elif mode == 'select_pokemon':
        telaatual = change_pokemon()
        change_pokemon_2()
    elif mode == 'enemy\'s_attack':
        attackOfEnemy()
        mode = 'select_menu'
    for i in telaatual:
        display.blit(i[0], i[1])
    pygame.display.flip()