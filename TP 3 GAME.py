#Jialun Cao
import pygame


pygame.init()
LARGEUR, HAUTEUR = 1024, 768 # taille Largeur/Hauteur de fenêtre
ECRAN = pygame.display.set_mode((LARGEUR,HAUTEUR)) # affichage de la fenêtre
pygame.display.set_caption("Accueil") # affiche le titre de la fenêtre
ECRAN.fill(((139, 0, 0))) # coloriser l'arrière-plan (RVB), car par défaut aucune couleur.
LANCEMENT = True

#Texte
Couleur_texte = (0,0,0)
#Titre
Font_Nom_Du_Jeu = pygame.font.Font("Jacquard12.ttf", 70)   
Jeu_title = Font_Nom_Du_Jeu.render("Does Not Commute", True, Couleur_texte)
#Mode de jeu
Font_mode_du_jeu = pygame.font.Font("Jacquard12.ttf", 45)
TXT_Record_Mondial = Font_mode_du_jeu.render("Record Mondial", True, Couleur_texte)
TXT_Solo = Font_mode_du_jeu.render("Solo", True, Couleur_texte)
TXT_Face_a_Face = Font_mode_du_jeu.render("Face à Face", True, Couleur_texte)

#Valeur pour les modes de jeu
Choix_game_mode = 1 #1 pour Record mondial, 2 pour solo et 3 pour Face à face

Nb_joystick = pygame.joystick.get_count()#Detecter le nombre de joystick

if Nb_joystick == 0:#Anonce du message s'il y en a pas
    print("Attention, No controler connected")
else:#Sinon on connect le joystick
    Main_joystick = pygame.joystick.Joystick(0)
    Main_joystick.init()

Choix_bouge = False #Variable pour que le joystick ne saute pas les choix


while LANCEMENT: # boucle de contrôle des évènements et de l’arrêt 
    for event in pygame.event.get(): # pour tous les évènements qui seront obtenus
        if event.type == pygame.QUIT: # constante QUIT afin de quitter correctement l'application,
           LANCEMENT = False
    
        #Mettre le crochet jaune sur le mode de jeu choisit
        if Choix_game_mode == 1:
            Selected_CoordY = 330
        elif Choix_game_mode == 2:
            Selected_CoordY = 455
        elif Choix_game_mode == 3:
            Selected_CoordY = 580

        #Effacer le crochet jaune
        pygame.draw.rect(ECRAN, (139, 0, 0), (267, 330, 490, 115), 10) 
        pygame.draw.rect(ECRAN, (139, 0, 0), (267, 455, 490, 115), 10)
        pygame.draw.rect(ECRAN, (139, 0, 0), (267, 580, 490, 115), 10)
        #Crochet jaune de choix autour le choix du jeu
        pygame.draw.rect(ECRAN, (255, 255, 0), (267, Selected_CoordY, 490, 115), 10)

        #Dessiner les rectangles du mode de jeu
        Rect_RM= pygame.draw.rect(ECRAN, (255, 165, 0), (287, 350, 450, 75))
        Rect_Solo= pygame.draw.rect(ECRAN, (255, 165, 0), (287, 475, 450, 75))
        Rect_FaF= pygame.draw.rect(ECRAN, (255, 165, 0), (287, 600, 450, 75))

        #dessin noir du cote
        pygame.draw.rect(ECRAN, (0, 0, 0), (0, 0, 256, 768))
        pygame.draw.rect(ECRAN, (0, 0, 0), (768, 0, 256, 768))
        #Afficher les textes
        ECRAN.blit(TXT_Record_Mondial, ((LARGEUR-TXT_Record_Mondial.get_width())//2,350+(Rect_RM.height-TXT_Record_Mondial.get_height())//2))
        ECRAN.blit(TXT_Solo, ((LARGEUR-TXT_Solo.get_width())//2,475+(Rect_Solo.height-TXT_Solo.get_height())//2) )
        ECRAN.blit(TXT_Face_a_Face, ((LARGEUR-TXT_Face_a_Face.get_width())//2,600+(Rect_FaF.height-TXT_Face_a_Face.get_height())//2))
        ECRAN.blit(Jeu_title, (260,100))
        
        
        if event.type == pygame.JOYAXISMOTION:#Detection du motion du joystick
            Pos_Y_joy = Main_joystick.get_axis(1)#On a seulement besoin du position Y du joystick

            if Pos_Y_joy >=0.5 and Choix_game_mode <3 and Choix_bouge == False: #Quand on bouge le joystick vers le bas
                Choix_game_mode +=1
                Choix_bouge = True

            if Pos_Y_joy <=-0.5 and Choix_game_mode >1 and Choix_bouge == False: #Quand on bouge le joystick vers le haut
                Choix_game_mode -=1
                Choix_bouge = True

            if Pos_Y_joy < 0.5 and Pos_Y_joy > -0.5:#Reset la variable Choix_bouge pour continuer de descendre ou remonter
                Choix_bouge = False

        if event.type == pygame.JOYBUTTONDOWN: #Detection d'appuie du bouton
            if Main_joystick.get_button(0):#Changer ce bouton pour celui du start (Its just a test on my side)
                if Choix_game_mode == 1: #Si c'est le premier choix choisit
                    pygame.draw.rect(ECRAN, (255, 207, 105), (287, 350, 450, 75))#Changer le couleur du rectangle choix
                    #Remettre le texte
                    ECRAN.blit(TXT_Record_Mondial, ((LARGEUR-TXT_Record_Mondial.get_width())//2,350+(Rect_RM.height-TXT_Record_Mondial.get_height())//2))
                    #Command here
                if Choix_game_mode == 2:
                    pygame.draw.rect(ECRAN, (255, 207, 105), (287, 475, 450, 75))
                    ECRAN.blit(TXT_Solo, ((LARGEUR-TXT_Solo.get_width())//2,475+(Rect_Solo.height-TXT_Solo.get_height())//2) )
                    #Command here
                if Choix_game_mode == 3:
                    pygame.draw.rect(ECRAN, (255, 207, 105), (287, 600, 450, 75))
                    ECRAN.blit(TXT_Face_a_Face, ((LARGEUR-TXT_Face_a_Face.get_width())//2,600+(Rect_FaF.height-TXT_Face_a_Face.get_height())//2))
                    #Command here

        pygame.display.flip() # mise à jour de l’écran, pour chaque évènement ou nouveaux


pygame.quit()
