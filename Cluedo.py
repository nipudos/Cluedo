# coding : utf-8

import pygame
from pygame.locals import *
from random import *

nomJoueur1=input("Quel est le nom du premier joueur ? ")
nomJoueur2=input("Celui du deuxième joueur ? ")
nomJoueur3=input("Et enfin celui du troisième ? ")

while nomJoueur1=="":
    nomJoueur1=input("Veuilliez rentrer un nom pour le joueur 1.")
while nomJoueur2=="":
    nomJoueur2=input("Veuilliez rentrer un nom pour le joueur 2.")
while nomJoueur3=="":
    nomJoueur3=input("Veuilliez rentrer un nom pour le joueur 3.")

pygame.init()

# Personnalisation de la fenêtre
longueurCase=36
largeurCase=36
fenetre=pygame.display.set_mode((22*longueurCase+550,23*largeurCase))
pygame.display.set_caption("Cluedo")
icone=pygame.image.load("icone.png")
pygame.display.set_icon(icone)

perso1=pygame.image.load("pion1.png").convert_alpha()
perso2=pygame.image.load("pion2.png").convert_alpha()
perso_3=pygame.image.load("pion3.png").convert_alpha()
fondNoir=pygame.image.load("fond.png").convert()
fondNoir2=pygame.image.load("fond2.png").convert()
plateauJeu=pygame.image.load("plateauJeu.png").convert()
boutonJouer=pygame.image.load("boutonJouer.png").convert()

# On définit les positions de départ des trois joueurs
posX_J1=20
posY_J1=18
posX_J2=1
posY_J2=14
posX_J3=13
posY_J3=1

# On définit notre plateau suivant l'image plateauJeu en utilisant des 0 pour les bords, des 3 pour les pièces, des 1 pour les couloirs, des 10 pour les portes, des 6 pour la pièce centrale et enfin des 2,8 et 15 pour les différentes positions de départ des joueurs
plateau=[22*[0],[0,3,3,3,3,3,1,1,1,1,3,3,3,15,1,1,3,3,3,3,3,0],[0,3,3,3,3,3,1,1,3,3,3,3,3,3,1,1,3,3,3,3,3,0],[0,3,3,3,3,3,1,1,3,3,3,3,3,3,1,1,10,3,3,3,3,0],[0,3,3,3,3,3,1,1,3,3,3,3,3,3,1,1,1,3,3,3,3,0],[0,3,3,3,3,10,1,1,10,3,3,3,3,10,1,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,1,3,3,3,3,3,3,1,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,1,3,10,3,3,10,3,1,1,1,1,1,1,1,0],[0,3,3,3,3,1,1,1,1,1,1,1,1,1,1,1,3,3,3,3,3,0],[0,3,3,3,3,3,3,3,3,1,1,1,1,1,1,1,10,3,3,3,3,0],[0,3,3,3,3,3,3,3,10,1,1,6,6,6,1,1,3,3,3,3,3,0],[0,3,3,3,3,3,3,3,3,1,1,6,6,6,1,1,3,3,3,3,3,0],[0,3,3,3,3,3,3,3,10,1,1,6,6,6,1,1,3,3,3,3,3,0],[0,3,3,3,3,3,3,1,1,1,1,6,6,6,1,1,1,1,1,1,1,0],[0,8,1,1,1,1,1,1,1,1,1,1,1,1,1,3,3,10,3,3,3,0],[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,10,3,3,3,3,3,0],[0,1,1,1,1,1,1,1,1,1,3,10,3,1,1,3,3,3,3,3,3,0],[0,3,3,3,3,3,3,10,1,1,3,3,3,1,1,1,1,1,1,1,1,0],[0,3,3,3,3,3,3,3,1,1,3,3,3,1,1,1,1,1,1,1,2,0],[0,3,3,3,3,3,3,3,1,1,3,3,3,1,10,3,3,3,3,3,3,0],[0,3,3,3,3,3,3,3,1,1,3,3,3,1,3,3,3,3,3,3,3,0],[0,3,3,3,3,3,3,3,1,1,3,3,3,1,3,3,3,3,3,3,3,0],22*[0]]

# On définit les différentes cartes
listeArmes=["Matraque","Chandelier","Revolver","Poignard","Clé anglaise","Corde"]
listePieces=["Cuisine","Rédac","Réunion","Bureau des développeurs","Salle de bain","Salle de tournage","Couloir","Régie commerciale","Salle de dej'"]
listeCoupables=["Colonel Moutarde","Mademoiselle Rose","Monsieur Olive","Madame Pervanche","Professeur Violet","Madame Leblanc"]

# On tire au sort une arme, un coupable et une pièce qui formeront la bonne hypothèse
resArme=choice(listeArmes)
resPiece=choice(listePieces)
resCoupable=choice(listeCoupables)
resHypothese=[resArme,resCoupable,resPiece]

# On retire les cartes choisies des listes
listeArmes.remove(resArme)
listeCoupables.remove(resCoupable)
listePieces.remove(resPiece)

# On distribue les cartes restantes aux joueurs
piocheJ1=[]
piocheJ2=[]
piocheJ3=[]
liste_pioche=listeArmes+listeCoupables+listePieces
for i in range(len(liste_pioche)//3):
    tirage=choice(liste_pioche)
    piocheJ1.append(tirage)
    liste_pioche.remove(tirage)
    tirage=choice(liste_pioche)
    piocheJ2.append(tirage)
    liste_pioche.remove(tirage)
    tirage=choice(liste_pioche)
    piocheJ3.append(tirage)
    liste_pioche.remove(tirage)

cartesTrouvJ1=[]
cartesTrouvJ2=[]
cartesTrouvJ3=[]

tourJoueur=0
nmbreCoups=0

blue=(255,255,255) # Variable qui correspond à la couleur du texte qui s'affiche, à la base bleu puis nous avons finalement opté pour le blanc mais nous avons laissé le nom blue à cause du nombre de fois où on utilise cette variable, cela aurait pris trop de temps à tout changer
arial=pygame.font.SysFont("arial",23) # On définit les deux polices que l'on va utiliser
arial2=pygame.font.SysFont("arial",33)

txtHypothese=arial.render("Cliquez ici pour faire une hypothèse", False, blue)
txtHypotheseFinale=arial.render("Cliquez ici pour faire votre hypothèse finale", False, blue)

txtPioche=arial.render("Cliquez ici pour afficher vos cartes", False, blue)
txtPioche2=arial.render("(Seul vous pouvez regarder !)", False, blue)

txtJ1=arial.render("{} : pour vous déplacer, utilisez les flèches directionelles.".format(nomJoueur1), False, blue)
txtJ2=arial.render("{} : pour vous déplacer, utilisez les touches ZQSD.".format(nomJoueur2), False, blue)
txtJ3=arial.render("{} : pour vous déplacer, utilisez le pavé numérique 8456.".format(nomJoueur3), False, blue)

txtmoutarde=arial.render("Colonel Moutarde", False, blue)
txtrose=arial.render("Mademoiselle Rose", False, blue)
txtolive=arial.render("Monsieur Olive", False, blue)
txtpervanche=arial.render("Madame Pervanche", False, blue)
txtviolet=arial.render("Professeur Violet", False, blue)
txtleblanc=arial.render("Madame Leblanc", False, blue)

txtcuisine=arial.render("Cuisine", False, blue)
txtreunion=arial.render("Réunion", False, blue)
txtredac=arial.render("Rédac", False, blue)
txtbureau=arial.render("Bureau des développeurs", False, blue)
txtsdb=arial.render("Salle de bain", False, blue)
txtsdt=arial.render("Salle de tournage", False, blue)
txtcouloir=arial.render("Couloir", False, blue)
txtregie=arial.render("Régie commerciale", False, blue)
txtsdd=arial.render("Salle de dej'", False, blue)

txtmatraque=arial.render("Matraque", False, blue)
txtchandelier=arial.render("Chandelier", False, blue)
txtrevolver=arial.render("Revolver", False, blue)
txtpoignard=arial.render("Poignard", False, blue)
txtcle=arial.render("Clé anglaise", False, blue)
txtcorde=arial.render("Corde", False, blue)

txtnomJoueur1=arial.render(nomJoueur1, False, blue)
txtnomJoueur2=arial.render(nomJoueur2, False, blue)
txtnomJoueur3=arial.render(nomJoueur3, False, blue)

txtsuspects=arial.render("Suspects", False, blue)
txtarmes=arial.render("Armes", False, blue)
txtjoueurs=arial.render("Joueurs", False, blue)
txtpieces=arial.render("Pièces", False, blue)

txtcartes_pioche=arial.render("Vos cartes", False, blue)
txtcartes_trouvees=arial.render("Cartes découvertes", False, blue)

txtvalidation=arial.render("Cliquez ici pour la reformuler", False, blue)
txtjoueur_suivant=arial.render("Pressez la touche Entrée pour passer au joueur suivant", False, blue)

# On définit toutes les hypothèses qui s'activeront au fur et à mesure du code
condHypothese=False
condArme=False
condCoupable=False
condJoueur=False
condTest=False
condAffichCarte=False
condDesaffichCarte=False
condHypothese2=False
condHypotheseFinale=False
condHypotheseFinale2=False

elimJ1=False
elimJ2=False
elimJ3=False

imgAccueil=pygame.image.load("accueil.jpg").convert()

# On définit les variables qui serviront à accueillir l'hypothèse du joueur
condarme=""
condpiece=""
condcoupable=""
condjoueur=""
condcomplete=""
mauvaise_pioche=""

# On définit une musique
musique=pygame.mixer.Sound("musiqueCluedo.ogg")

# Affiche dans la console la bonne hypothèse pour pouvoir tester le jeu plus rapidement, à mettre en commentaire pour faire une vraie partie
print(resHypothese)

continuerJeu=True
accesJeu=False

while continuerJeu==True:
    if accesJeu==False:
        fenetre.blit(imgAccueil,[-125,14])
        fenetre.blit(boutonJouer,[600,400])
    if accesJeu==True:
        fenetre.blit(plateauJeu,[2,3]) #Pour aligner les cases de l'image avec les cases du vrai plateau en dessous
        for j in range(23):
            for i in range(22):
                if plateau[j][i]==2 or plateau[j][i]==5:
                    fenetre.blit(perso1,(i*36,j*36))
                if plateau[j][i]==8 or plateau[j][i]==11:
                    fenetre.blit(perso2,(i*36,j*36))
                if plateau[j][i]==15 or plateau[j][i]==14:
                    fenetre.blit(perso_3,(i*36,j*36))

    for event in pygame.event.get():
        if event.type == QUIT:
            continuerJeu = False

        elif event.type==KEYDOWN:
            if nmbreCoups!=0 and condHypothese2==False:
                condHypothese=False
                condHypothese2=False
                condHypotheseFinale=False
                condHypotheseFinale2=False
                condArme=False
                condCoupable=False
                condJoueur=False
                condTest=False
                condAffichCarte=False
                condDesaffichCarte=False
                txtPioche=arial.render("Cliquez ici pour afficher vos cartes", False, blue)
                txtPioche2=arial.render("(Seul vous pouvez regarder !)", False, blue)

                if tourJoueur==1:
                    if event.key==K_RIGHT:
                        if plateau[posY_J1][posX_J1+1]==1:
                            fenetre.blit(fondNoir,(22*longueurCase,0))
                            if plateau[posY_J1][posX_J1]==2:
                                plateau[posY_J1][posX_J1]=1
                            elif plateau[posY_J1][posX_J1]==5:
                                plateau[posY_J1][posX_J1]=10
                            plateau[posY_J1][posX_J1+1]=2
                            posX_J1+=1
                            nmbreCoups=nmbreCoups-1
                            if nmbreCoups==0:
                                fenetre.blit(txtjoueur_suivant,(22*longueurCase,350))
                        elif plateau[posY_J1][posX_J1+1]==10:
                            fenetre.blit(fondNoir,(22*longueurCase,0))
                            plateau[posY_J1][posX_J1]=1
                            plateau[posY_J1][posX_J1+1]=5
                            fenetre.blit(txtHypothese,[22*longueurCase,160])
                            posX_J1+=1
                            condHypothese=True
                            condHypothese2=True
                            nmbreCoups=nmbreCoups-1
                            if nmbreCoups==0:
                                fenetre.blit(txtjoueur_suivant,(22*longueurCase,350))
                        elif plateau[posY_J1][posX_J1+1]==6:
                            fenetre.blit(fondNoir,(22*longueurCase,0))
                            plateau[posY_J1][posX_J1]=1
                            posX_J1+=1
                            nmbreCoups=nmbreCoups-1
                            if nmbreCoups==0:
                                fenetre.blit(txtjoueur_suivant,(22*longueurCase,350))
                            condHypotheseFinale=True
                            fenetre.blit(txtHypotheseFinale,[22*longueurCase,160])
                            condHypotheseFinale2=True


                    elif event.key==K_LEFT:
                        if plateau[posY_J1][posX_J1-1]==1:
                            fenetre.blit(fondNoir,(22*longueurCase,0))
                            if plateau[posY_J1][posX_J1]==2:
                                plateau[posY_J1][posX_J1]=1
                            elif plateau[posY_J1][posX_J1]==5:
                                plateau[posY_J1][posX_J1]=10
                            plateau[posY_J1][posX_J1-1]=2
                            posX_J1-=1
                            nmbreCoups=nmbreCoups-1
                            if nmbreCoups==0:
                                fenetre.blit(txtjoueur_suivant,(22*longueurCase,350))
                        elif plateau[posY_J1][posX_J1-1]==10:
                            fenetre.blit(fondNoir,(22*longueurCase,0))
                            plateau[posY_J1][posX_J1]=1
                            plateau[posY_J1][posX_J1-1]=5
                            fenetre.blit(txtHypothese,[22*longueurCase,160])
                            posX_J1-=1
                            condHypothese=True
                            condHypothese2=True
                            nmbreCoups=nmbreCoups-1
                            if nmbreCoups==0:
                                fenetre.blit(txtjoueur_suivant,(22*longueurCase,350))
                        elif plateau[posY_J1][posX_J1-1]==6:
                            fenetre.blit(fondNoir,(22*longueurCase,0))
                            plateau[posY_J1][posX_J1]=1
                            posX_J1-=1
                            nmbreCoups=nmbreCoups-1
                            if nmbreCoups==0:
                                fenetre.blit(txtjoueur_suivant,(22*longueurCase,350))
                            condHypotheseFinale=True
                            fenetre.blit(txtHypotheseFinale,[22*longueurCase,160])
                            condHypotheseFinale2=True

                    elif event.key==K_DOWN:
                        if plateau[posY_J1+1][posX_J1]==1:
                            fenetre.blit(fondNoir,(22*longueurCase,0))
                            if plateau[posY_J1][posX_J1]==2:
                                plateau[posY_J1][posX_J1]=1
                            elif plateau[posY_J1][posX_J1]==5:
                                plateau[posY_J1][posX_J1]=10
                            plateau[posY_J1+1][posX_J1]=2
                            posY_J1+=1
                            nmbreCoups=nmbreCoups-1
                            if nmbreCoups==0:
                                fenetre.blit(txtjoueur_suivant,(22*longueurCase,350))
                        elif plateau[posY_J1+1][posX_J1]==10:
                            fenetre.blit(fondNoir,(22*longueurCase,0))
                            plateau[posY_J1][posX_J1]=1
                            plateau[posY_J1+1][posX_J1]=5
                            fenetre.blit(txtHypothese,[22*longueurCase,160])
                            posY_J1+=1
                            condHypothese=True
                            condHypothese2=True
                            nmbreCoups=nmbreCoups-1
                            if nmbreCoups==0:
                                fenetre.blit(txtjoueur_suivant,(22*longueurCase,350))
                        elif plateau[posY_J1+1][posX_J1]==6:
                            fenetre.blit(fondNoir,(22*longueurCase,0))
                            plateau[posY_J1][posX_J1]=1
                            posY_J1+=1
                            nmbreCoups=nmbreCoups-1
                            if nmbreCoups==0:
                                fenetre.blit(txtjoueur_suivant,(22*longueurCase,350))
                            condHypotheseFinale=True
                            fenetre.blit(txtHypotheseFinale,[22*longueurCase,160])
                            condHypotheseFinale2=True

                    elif event.key==K_UP:
                        if plateau[posY_J1-1][posX_J1]==1:
                            fenetre.blit(fondNoir,(22*longueurCase,0))
                            if plateau[posY_J1][posX_J1]==2:
                                plateau[posY_J1][posX_J1]=1
                            elif plateau[posY_J1][posX_J1]==5:
                                plateau[posY_J1][posX_J1]=10
                            plateau[posY_J1-1][posX_J1]=2
                            posY_J1-=1
                            nmbreCoups=nmbreCoups-1
                            if nmbreCoups==0:
                                fenetre.blit(txtjoueur_suivant,(22*longueurCase,350))
                        elif plateau[posY_J1-1][posX_J1]==10:
                            fenetre.blit(fondNoir,(22*longueurCase,0))
                            plateau[posY_J1][posX_J1]=1
                            plateau[posY_J1-1][posX_J1]=5
                            fenetre.blit(txtHypothese,[22*longueurCase,160])
                            posY_J1-=1
                            condHypothese=True
                            condHypothese2=True
                            nmbreCoups=nmbreCoups-1
                            if nmbreCoups==0:
                                fenetre.blit(txtjoueur_suivant,(22*longueurCase,350))
                        elif plateau[posY_J1-1][posX_J1]==6:
                            fenetre.blit(fondNoir,(22*longueurCase,0))
                            plateau[posY_J1][posX_J1]=1
                            posY_J1-=1
                            nmbreCoups=nmbreCoups-1
                            if nmbreCoups==0:
                                fenetre.blit(txtjoueur_suivant,(22*longueurCase,350))
                            condHypotheseFinale=True
                            fenetre.blit(txtHypotheseFinale,[22*longueurCase,160])
                            condHypotheseFinale2=True

                if tourJoueur==2:
                    if event.key==K_d:
                        if plateau[posY_J2][posX_J2+1]==1:
                            fenetre.blit(fondNoir,(22*longueurCase,0))
                            if plateau[posY_J2][posX_J2]==8:
                                plateau[posY_J2][posX_J2]=1
                            elif plateau[posY_J2][posX_J2]==11:
                                plateau[posY_J2][posX_J2]=10
                            plateau[posY_J2][posX_J2+1]=8
                            posX_J2+=1
                            nmbreCoups=nmbreCoups-1
                            if nmbreCoups==0:
                                fenetre.blit(txtjoueur_suivant,(22*longueurCase,350))
                        elif plateau[posY_J2][posX_J2+1]==10:
                            fenetre.blit(fondNoir,(22*longueurCase,0))
                            plateau[posY_J2][posX_J2]=1
                            plateau[posY_J2][posX_J2+1]=11
                            fenetre.blit(txtHypothese,[22*longueurCase,160])
                            posX_J2+=1
                            condHypothese=True
                            condHypothese2=True
                            nmbreCoups=nmbreCoups-1
                            if nmbreCoups==0:
                                fenetre.blit(txtjoueur_suivant,(22*longueurCase,350))
                        elif plateau[posY_J2][posX_J2+1]==6:
                            fenetre.blit(fondNoir,(22*longueurCase,0))
                            plateau[posY_J2][posX_J2]=1
                            posX_J2+=1
                            nmbreCoups=nmbreCoups-1
                            if nmbreCoups==0:
                                fenetre.blit(txtjoueur_suivant,(22*longueurCase,350))
                            condHypotheseFinale=True
                            fenetre.blit(txtHypotheseFinale,[22*longueurCase,160])
                            condHypotheseFinale2=True

                    elif event.key==K_a:
                        if plateau[posY_J2][posX_J2-1]==1:
                            fenetre.blit(fondNoir,(22*longueurCase,0))
                            if plateau[posY_J2][posX_J2]==8:
                                plateau[posY_J2][posX_J2]=1
                            elif plateau[posY_J2][posX_J2]==11:
                                plateau[posY_J2][posX_J2]=10
                            plateau[posY_J2][posX_J2-1]=8
                            posX_J2-=1
                            nmbreCoups=nmbreCoups-1
                            if nmbreCoups==0:
                                fenetre.blit(txtjoueur_suivant,(22*longueurCase,350))
                        elif plateau[posY_J2][posX_J2-1]==10:
                            fenetre.blit(fondNoir,(22*longueurCase,0))
                            plateau[posY_J2][posX_J2]=1
                            plateau[posY_J2][posX_J2-1]=11
                            fenetre.blit(txtHypothese,[22*longueurCase,160])
                            posX_J2-=1
                            condHypothese=True
                            condHypothese2=True
                            nmbreCoups=nmbreCoups-1
                            if nmbreCoups==0:
                                fenetre.blit(txtjoueur_suivant,(22*longueurCase,350))
                        elif plateau[posY_J2][posX_J2-1]==6:
                            fenetre.blit(fondNoir,(22*longueurCase,0))
                            plateau[posY_J2][posX_J2]=1
                            posX_J2-=1
                            nmbreCoups=nmbreCoups-1
                            if nmbreCoups==0:
                                fenetre.blit(txtjoueur_suivant,(22*longueurCase,350))
                            condHypotheseFinale=True
                            fenetre.blit(txtHypotheseFinale,[22*longueurCase,160])
                            condHypotheseFinale2=True

                    elif event.key==K_s:
                        if plateau[posY_J2+1][posX_J2]==1:
                            fenetre.blit(fondNoir,(22*longueurCase,0))
                            if plateau[posY_J2][posX_J2]==8:
                                plateau[posY_J2][posX_J2]=1
                            elif plateau[posY_J2][posX_J2]==11:
                                plateau[posY_J2][posX_J2]=10
                            plateau[posY_J2+1][posX_J2]=8
                            posY_J2+=1
                            nmbreCoups=nmbreCoups-1
                            if nmbreCoups==0:
                                fenetre.blit(txtjoueur_suivant,(22*longueurCase,350))
                        elif plateau[posY_J2+1][posX_J2]==10:
                            fenetre.blit(fondNoir,(22*longueurCase,0))
                            plateau[posY_J2][posX_J2]=1
                            plateau[posY_J2+1][posX_J2]=11
                            fenetre.blit(txtHypothese,[22*longueurCase,160])
                            posY_J2+=1
                            condHypothese=True
                            condHypothese2=True
                            nmbreCoups=nmbreCoups-1
                            if nmbreCoups==0:
                                fenetre.blit(txtjoueur_suivant,(22*longueurCase,350))
                        elif plateau[posY_J2+1][posX_J2]==6:
                            fenetre.blit(fondNoir,(22*longueurCase,0))
                            plateau[posY_J2][posX_J2]=1
                            posY_J2+=1
                            nmbreCoups=nmbreCoups-1
                            if nmbreCoups==0:
                                fenetre.blit(txtjoueur_suivant,(22*longueurCase,350))
                            condHypotheseFinale=True
                            fenetre.blit(txtHypotheseFinale,[22*longueurCase,160])
                            condHypotheseFinale2=True

                    elif event.key==K_w:
                        if plateau[posY_J2-1][posX_J2]==1:
                            fenetre.blit(fondNoir,(22*longueurCase,0))
                            if plateau[posY_J2][posX_J2]==8:
                                plateau[posY_J2][posX_J2]=1
                            elif plateau[posY_J2][posX_J2]==11:
                                plateau[posY_J2][posX_J2]=10
                            plateau[posY_J2-1][posX_J2]=8
                            posY_J2-=1
                            nmbreCoups=nmbreCoups-1
                            if nmbreCoups==0:
                                fenetre.blit(txtjoueur_suivant,(22*longueurCase,350))
                        elif plateau[posY_J2-1][posX_J2]==10:
                            fenetre.blit(fondNoir,(22*longueurCase,0))
                            plateau[posY_J2][posX_J2]=1
                            plateau[posY_J2-1][posX_J2]=11
                            fenetre.blit(txtHypothese,[22*longueurCase,160])
                            posY_J2-=1
                            condHypothese=True
                            condHypothese2=True
                            nmbreCoups=nmbreCoups-1
                            if nmbreCoups==0:
                                fenetre.blit(txtjoueur_suivant,(22*longueurCase,350))
                        elif plateau[posY_J2-1][posX_J2]==6:
                            fenetre.blit(fondNoir,(22*longueurCase,0))
                            plateau[posY_J2][posX_J2]=1
                            posY_J2-=1
                            nmbreCoups=nmbreCoups-1
                            if nmbreCoups==0:
                                fenetre.blit(txtjoueur_suivant,(22*longueurCase,350))
                            condHypotheseFinale=True
                            fenetre.blit(txtHypotheseFinale,[22*longueurCase,160])
                            condHypotheseFinale2=True

                if tourJoueur==3:
                    if event.key==K_KP6:
                        if plateau[posY_J3][posX_J3+1]==1:
                            fenetre.blit(fondNoir,(22*longueurCase,0))
                            if plateau[posY_J3][posX_J3]==15:
                                plateau[posY_J3][posX_J3]=1
                            elif plateau[posY_J3][posX_J3]==14:
                                plateau[posY_J3][posX_J3]=10
                            plateau[posY_J3][posX_J3+1]=15
                            posX_J3+=1
                            nmbreCoups=nmbreCoups-1
                            if nmbreCoups==0:
                                fenetre.blit(txtjoueur_suivant,(22*longueurCase,350))
                        elif plateau[posY_J3][posX_J3+1]==10:
                            fenetre.blit(fondNoir,(22*longueurCase,0))
                            plateau[posY_J3][posX_J3]=1
                            plateau[posY_J3][posX_J3+1]=14
                            fenetre.blit(txtHypothese,[22*longueurCase,160])
                            posX_J3+=1
                            condHypothese=True
                            condHypothese2=True
                            nmbreCoups=nmbreCoups-1
                            if nmbreCoups==0:
                                fenetre.blit(txtjoueur_suivant,(22*longueurCase,350))
                        elif plateau[posY_J3][posX_J3+1]==6:
                            fenetre.blit(fondNoir,(22*longueurCase,0))
                            plateau[posY_J3][posX_J3]=1
                            posX_J3+=1
                            nmbreCoups=nmbreCoups-1
                            if nmbreCoups==0:
                                fenetre.blit(txtjoueur_suivant,(22*longueurCase,350))
                            condHypotheseFinale=True
                            fenetre.blit(txtHypotheseFinale,[22*longueurCase,160])
                            condHypotheseFinale2=True

                    elif event.key==K_KP4:
                        if plateau[posY_J3][posX_J3-1]==1:
                            fenetre.blit(fondNoir,(22*longueurCase,0))
                            if plateau[posY_J3][posX_J3]==15:
                                plateau[posY_J3][posX_J3]=1
                            elif plateau[posY_J3][posX_J3]==14:
                                plateau[posY_J3][posX_J3]=10
                            plateau[posY_J3][posX_J3-1]=15
                            posX_J3-=1
                            nmbreCoups=nmbreCoups-1
                            if nmbreCoups==0:
                                fenetre.blit(txtjoueur_suivant,(22*longueurCase,350))
                        elif plateau[posY_J3][posX_J3-1]==10:
                            fenetre.blit(fondNoir,(22*longueurCase,0))
                            plateau[posY_J3][posX_J3]=1
                            plateau[posY_J3][posX_J3-1]=14
                            fenetre.blit(txtHypothese,[22*longueurCase,160])
                            posX_J3-=1
                            condHypothese=True
                            condHypothese2=True
                            nmbreCoups=nmbreCoups-1
                            if nmbreCoups==0:
                                fenetre.blit(txtjoueur_suivant,(22*longueurCase,350))
                        elif plateau[posY_J3][posX_J3-1]==6:
                            fenetre.blit(fondNoir,(22*longueurCase,0))
                            plateau[posY_J3][posX_J3]=1
                            posX_J3-=1
                            nmbreCoups=nmbreCoups-1
                            if nmbreCoups==0:
                                fenetre.blit(txtjoueur_suivant,(22*longueurCase,350))
                            condHypotheseFinale=True
                            fenetre.blit(txtHypotheseFinale,[22*longueurCase,160])
                            condHypotheseFinale2=True

                    elif event.key==K_KP5:
                        if plateau[posY_J3+1][posX_J3]==1:
                            fenetre.blit(fondNoir,(22*longueurCase,0))
                            if plateau[posY_J3][posX_J3]==15:
                                plateau[posY_J3][posX_J3]=1
                            elif plateau[posY_J3][posX_J3]==14:
                                plateau[posY_J3][posX_J3]=10
                            plateau[posY_J3+1][posX_J3]=15
                            posY_J3+=1
                            nmbreCoups=nmbreCoups-1
                            if nmbreCoups==0:
                                fenetre.blit(txtjoueur_suivant,(22*longueurCase,350))
                        elif plateau[posY_J3+1][posX_J3]==10:
                            fenetre.blit(fondNoir,(22*longueurCase,0))
                            plateau[posY_J3][posX_J3]=1
                            plateau[posY_J3+1][posX_J3]=14
                            fenetre.blit(txtHypothese,[22*longueurCase,160])
                            posY_J3+=1
                            condHypothese=True
                            condHypothese2=True
                            nmbreCoups=nmbreCoups-1
                            if nmbreCoups==0:
                                fenetre.blit(txtjoueur_suivant,(22*longueurCase,350))
                        elif plateau[posY_J3+1][posX_J3]==6:
                            fenetre.blit(fondNoir,(22*longueurCase,0))
                            plateau[posY_J3][posX_J3]=1
                            posY_J3+=1
                            nmbreCoups=nmbreCoups-1
                            if nmbreCoups==0:
                                fenetre.blit(txtjoueur_suivant,(22*longueurCase,350))
                            condHypotheseFinale=True
                            fenetre.blit(txtHypotheseFinale,[22*longueurCase,160])
                            condHypotheseFinale2=True

                    elif event.key==K_KP8:
                        if plateau[posY_J3-1][posX_J3]==1:
                            fenetre.blit(fondNoir,(22*longueurCase,0))
                            if plateau[posY_J3][posX_J3]==15:
                                plateau[posY_J3][posX_J3]=1
                            elif plateau[posY_J3][posX_J3]==14:
                                plateau[posY_J3][posX_J3]=10
                            plateau[posY_J3-1][posX_J3]=15
                            posY_J3-=1
                            nmbreCoups=nmbreCoups-1
                            if nmbreCoups==0:
                                fenetre.blit(txtjoueur_suivant,(22*longueurCase,350))
                        elif plateau[posY_J3-1][posX_J3]==10:
                            fenetre.blit(fondNoir,(22*longueurCase,0))
                            plateau[posY_J3][posX_J3]=1
                            plateau[posY_J3-1][posX_J3]=14
                            fenetre.blit(txtHypothese,[22*longueurCase,160])
                            posY_J3-=1
                            condHypothese=True
                            condHypothese2=True
                            nmbreCoups=nmbreCoups-1
                            if nmbreCoups==0:
                                fenetre.blit(txtjoueur_suivant,(22*longueurCase,350))
                        elif plateau[posY_J3-1][posX_J3]==6:
                            fenetre.blit(fondNoir,(22*longueurCase,0))
                            plateau[posY_J3][posX_J3]=1
                            posY_J3-=1
                            nmbreCoups=nmbreCoups-1
                            if nmbreCoups==0:
                                fenetre.blit(txtjoueur_suivant,(22*longueurCase,350))
                            condHypotheseFinale=True
                            fenetre.blit(txtHypotheseFinale,[22*longueurCase,160])
                            condHypotheseFinale2=True

            if event.key==K_RETURN:
                condarme=""
                condcoupable=""
                condjoueur=""
                condpiece=""
                condcomplete=""
                condHypothese2=False
                mauvaise_pioche=""
                fenetre.blit(fondNoir,(22*longueurCase,0))
                de_1=randint(1,6)
                de_2=randint(1,6)
                nmbreCoups=de_1+de_2
                tourJoueur=tourJoueur+1
                if tourJoueur>3:
                    tourJoueur=tourJoueur-3
                if elimJ1==True and tourJoueur==1:
                    tourJoueur+=1
                if elimJ2==True and tourJoueur==2:
                    tourJoueur+=1
                if elimJ3==True and tourJoueur==3:
                    tourJoueur+=1

            elif event.key==K_h:
                fenetre.blit(fondNoir,(22*longueurCase,0))

            elif event.key==K_ESCAPE:
                continuerJeu=False
                accesJeu=False

        elif event.type == MOUSEBUTTONUP:
            if event.button==1:
                if accesJeu==False:
                    if 500<event.pos[0]<800:
                        if 300<event.pos[1]<605:
                            musique.play()
                            accesJeu=True
                            condarme=""
                            condcoupable=""
                            condjoueur=""
                            condpiece=""
                            condcomplete=""
                            condHypothese2=False
                            mauvaise_pioche=""
                            fenetre.blit(fondNoir2,(0,0))
                            de_1=randint(1,6)
                            de_2=randint(1,6)
                            nmbreCoups=de_1+de_2
                            tourJoueur=1
                            if tourJoueur>3:
                                tourJoueur=tourJoueur-3
                            if elimJ1==True and tourJoueur==1:
                                tourJoueur+=1
                            if elimJ2==True and tourJoueur==2:
                                tourJoueur+=1
                            if elimJ3==True and tourJoueur==3:
                                tourJoueur+=1

                if condHypothese==False:
                    if 22*longueurCase<event.pos[0]<1100:
                        if 545<event.pos[1]<605:
                            if tourJoueur==1:
                                fenetre.blit(fondNoir,(22*longueurCase,0))
                                txtPioche=arial.render("Pressez la touche 'H' pour masquer vos cartes", False, blue)
                                txtPioche2=arial.render("", False, blue)
                                fenetre.blit(txtcartes_pioche,[22*longueurCase,320])
                                fenetre.blit(txtcartes_trouvees,[1010,320])
                                for i in range(6):
                                    txtaffichage_pioche=arial.render("{}".format(piocheJ1[i]), False, blue)
                                    fenetre.blit(txtaffichage_pioche,[22*longueurCase,350+i*25])
                                for i in range(len(cartesTrouvJ1)):
                                    txtaffichage_cartes_trouvees=arial.render("{}".format(cartesTrouvJ1[i]), False, blue)
                                    fenetre.blit(txtaffichage_cartes_trouvees,[1010,350+i*25])
                            if tourJoueur==2:
                                fenetre.blit(fondNoir,(22*longueurCase,0))
                                txtPioche=arial.render("Pressez la touche 'H' pour masquer vos cartes", False, blue)
                                txtPioche2=arial.render("", False, blue)
                                fenetre.blit(txtcartes_pioche,[22*longueurCase,320])
                                fenetre.blit(txtcartes_trouvees,[1010,320])
                                for i in range(6):
                                    txtaffichage_pioche=arial.render("{}".format(piocheJ2[i]), False, blue)
                                    fenetre.blit(txtaffichage_pioche,[22*longueurCase,350+i*25])
                                for i in range(len(cartesTrouvJ2)):
                                    txtaffichage_cartes_trouvees=arial.render("{}".format(cartesTrouvJ2[i]), False, blue)
                                    fenetre.blit(txtaffichage_cartes_trouvees,[1010,350+i*25])
                            if tourJoueur==3:
                                fenetre.blit(fondNoir,(22*longueurCase,0))
                                txtPioche=arial.render("Pressez la touche 'H' pour masquer vos cartes", False, blue)
                                txtPioche2=arial.render("", False, blue)
                                fenetre.blit(txtcartes_pioche,[22*longueurCase,320])
                                fenetre.blit(txtcartes_trouvees,[1010,320])
                                for i in range(6):
                                    txtaffichage_pioche=arial.render("{}".format(piocheJ3[i]), False, blue)
                                    fenetre.blit(txtaffichage_pioche,[22*longueurCase,350+i*25])
                                for i in range(len(cartesTrouvJ3)):
                                    txtaffichage_cartes_trouvees=arial.render("{}".format(cartesTrouvJ3[i]), False, blue)
                                    fenetre.blit(txtaffichage_cartes_trouvees,[1010,350+i*25])


                if condHypothese==True:
                    condHypotheseFinale=False
                    if 22*longueurCase<event.pos[0]<22*longueurCase+500:
                        if 155<event.pos[1]<185:
                            condHypothese=False
                            condArme=True
                            condCoupable=True
                            condTest=True
                            fenetre.blit(fondNoir,(22*longueurCase,0))
                            fenetre.blit(txtsuspects,[22*longueurCase,210])
                            fenetre.blit(txtarmes,[1010,210])
                            fenetre.blit(txtchandelier,[1010,250])
                            fenetre.blit(txtcorde,[1010,280])
                            fenetre.blit(txtcle,[1010,310])
                            fenetre.blit(txtmatraque,[1010,340])
                            fenetre.blit(txtpoignard,[1010,370])
                            fenetre.blit(txtrevolver,[1010,400])
                            fenetre.blit(txtleblanc,[22*longueurCase,250])
                            fenetre.blit(txtmoutarde,[22*longueurCase,280])
                            fenetre.blit(txtolive,[22*longueurCase,310])
                            fenetre.blit(txtviolet,[22*longueurCase,340])
                            fenetre.blit(txtrose,[22*longueurCase,370])
                            fenetre.blit(txtpervanche,[22*longueurCase,400])
                            if condHypotheseFinale2==False:
                                condJoueur=True
                                fenetre.blit(txtjoueurs,[1170,210])
                                if tourJoueur==1:
                                    fenetre.blit(txtnomJoueur2,[1170,310])
                                    fenetre.blit(txtnomJoueur3,[1170,340])
                                if tourJoueur==2:
                                    fenetre.blit(txtnomJoueur1,[1170,310])
                                    fenetre.blit(txtnomJoueur3,[1170,340])
                                if tourJoueur==3:
                                    fenetre.blit(txtnomJoueur1,[1170,310])
                                    fenetre.blit(txtnomJoueur2,[1170,340])
                            if condHypotheseFinale2==True:
                                cond_piece=True
                                fenetre.blit(txtpieces,[1170,210])
                                fenetre.blit(txtredac,[1170,250])
                                fenetre.blit(txtcuisine,[1170,280])
                                fenetre.blit(txtsdb,[1170,310])
                                fenetre.blit(txtsdt,[1170,460])
                                fenetre.blit(txtsdd,[1170,400])
                                fenetre.blit(txtregie,[1170,340])
                                fenetre.blit(txtcouloir,[1170,370])
                                fenetre.blit(txtbureau,[1170,430])
                                fenetre.blit(txtreunion,[1170,490])


                if condArme==True:
                    if 1000<event.pos[0]<1140:
                        if 245<event.pos[1]<274:
                            condarme="Chandelier"
                        if 275<event.pos[1]<304:
                            condarme="Corde"
                        if 305<event.pos[1]<334:
                            condarme="Clé anglaise"
                        if 335<event.pos[1]<364:
                            condarme="Matraque"
                        if 365<event.pos[1]<394:
                            condarme="Poignard"
                        if 395<event.pos[1]<424:
                            condarme="Revolver"
                        if 245<event.pos[1]<424:
                            condArme=False

                if condCoupable==True:
                    if 22*longueurCase<event.pos[0]<950:
                        if 245<event.pos[1]<274:
                            condcoupable="Madame Leblanc"
                        if 275<event.pos[1]<304:
                            condcoupable="Colonel Moutarde"
                        if 305<event.pos[1]<334:
                            condcoupable="Monsieur Olive"
                        if 335<event.pos[1]<364:
                            condcoupable="Professeur Violet"
                        if 365<event.pos[1]<394:
                            condcoupable="Mademoiselle Rose"
                        if 395<event.pos[1]<424:
                            condcoupable="Madame Pervanche"
                        if 245<event.pos[1]<424:
                            condCoupable=False

                if condJoueur==True:
                    if 1170<event.pos[0]<1250:
                        if 306<event.pos[1]<335:
                            if tourJoueur==1:
                                condjoueur=nomJoueur2
                            else:
                                condjoueur=nomJoueur1
                        if 336<event.pos[1]<365:
                            if tourJoueur==3:
                                condjoueur=nomJoueur2
                            else:
                                condjoueur=nomJoueur3
                        if 306<event.pos[1]<365:
                            condJoueur=False

                if condHypotheseFinale2==False:
                    if tourJoueur==1:
                        if posX_J1==5 and posY_J1==5:
                            condpiece="Cuisine"
                        if posX_J1==8 and posY_J1==5:
                            condpiece="Rédac"
                        if posX_J1==13 and posY_J1==5:
                            condpiece="Rédac"
                        if posX_J1==9 and posY_J1==7:
                            condpiece="Rédac"
                        if posX_J1==12 and posY_J1==7:
                            condpiece="Rédac"
                        if posX_J1==16 and posY_J1==3:
                            condpiece="Salle de bain"
                        if posX_J1==16 and posY_J1==9:
                            condpiece="Réunion"
                        if posX_J1==17 and posY_J1==14:
                            condpiece="Bureau des développeurs"
                        if posX_J1==15 and posY_J1==15:
                            condpiece="Bureau des développeurs"
                        if posX_J1==14 and posY_J1==19:
                            condpiece="Salle de tournage"
                        if posX_J1==11 and posY_J1==16:
                            condpiece="Couloir"
                        if posX_J1==7 and posY_J1==17:
                            condpiece="Régie commerciale"
                        if posX_J1==8 and posY_J1==10:
                            condpiece="Salle de dej'"
                        if posX_J1==8 and posY_J1==12:
                            condpiece="Salle de dej'"

                    if tourJoueur==2:
                        if posX_J2==5 and posY_J2==5:
                            condpiece="Cuisine"
                        if posX_J2==8 and posY_J2==5:
                            condpiece="Rédac"
                        if posX_J2==13 and posY_J2==5:
                            condpiece="Rédac"
                        if posX_J2==9 and posY_J2==7:
                            condpiece="Rédac"
                        if posX_J2==12 and posY_J2==7:
                            condpiece="Rédac"
                        if posX_J2==16 and posY_J2==3:
                            condpiece="Salle de bain"
                        if posX_J2==16 and posY_J2==9:
                            condpiece="Réunion"
                        if posX_J2==17 and posY_J2==14:
                            condpiece="Bureau des développeurs"
                        if posX_J2==15 and posY_J2==15:
                            condpiece="Bureau des développeurs"
                        if posX_J2==14 and posY_J2==19:
                            condpiece="Salle de tournage"
                        if posX_J2==11 and posY_J2==16:
                            condpiece="Couloir"
                        if posX_J2==7 and posY_J2==17:
                            condpiece="Régie commerciale"
                        if posX_J2==8 and posY_J2==10:
                            condpiece="Salle de dej'"
                        if posX_J2==8 and posY_J2==12:
                            condpiece="Salle de dej'"

                    if tourJoueur==3:
                        if posX_J1==5 and posY_J1==5:
                            condpiece="Cuisine"
                        if posX_J3==8 and posY_J3==5:
                            condpiece="Rédac"
                        if posX_J3==13 and posY_J3==5:
                            condpiece="Rédac"
                        if posX_J3==9 and posY_J3==7:
                            condpiece="Rédac"
                        if posX_J3==12 and posY_J3==7:
                            condpiece="Rédac"
                        if posX_J3==16 and posY_J3==3:
                            condpiece="Salle de bain"
                        if posX_J3==16 and posY_J3==9:
                            condpiece="Réunion"
                        if posX_J3==17 and posY_J3==14:
                            condpiece="Bureau des développeurs"
                        if posX_J3==15 and posY_J3==15:
                            condpiece="Bureau des développeurs"
                        if posX_J3==14 and posY_J3==19:
                            condpiece="Salle de tournage"
                        if posX_J3==11 and posY_J3==16:
                            condpiece="Couloir"
                        if posX_J3==7 and posY_J3==17:
                            condpiece="Régie commerciale"
                        if posX_J3==8 and posY_J3==10:
                            condpiece="Salle de dej'"
                        if posX_J3==8 and posY_J3==12:
                            condpiece="Salle de dej'"

                elif condHypotheseFinale2==True and condpiece=="":
                    if 1170<event.pos[0]<1300:
                        if 245<event.pos[1]<274:
                            condpiece="Rédac"
                        if 275<event.pos[1]<304:
                            condpiece="Cuisine"
                        if 305<event.pos[1]<334:
                            condpiece="Salle de bain"
                        if 335<event.pos[1]<364:
                            condpiece="Régie commerciale"
                        if 365<event.pos[1]<394:
                            condpiece="Couloir"
                        if 395<event.pos[1]<424:
                            condpiece="Salle de dej'"
                        if 425<event.pos[1]<454:
                            condpiece="Bureau des développeurs"
                        if 455<event.pos[1]<484:
                            condpiece="Salle de tournage"
                        if 485<event.pos[1]<514:
                            condpiece="Réunion"
                        if 245<event.pos[1]<514:
                            condjoueur="."
##                            condHypotheseFinale2=False

                txtresume_hypothese=arial.render(("Votre hypothèse est la suivante : le crime a été commis avec "), False, blue)
                txtresume_hypothese2=arial.render(("un(e) {}, par {}, dans le/la {}.".format(condarme,condcoupable,condpiece)), False, blue)
                txtresume_hypothese3=arial.render(("Vous demandez à vérifier auprès de {}.".format(condjoueur)), False, blue)
                txtresume_hypothese4=arial.render(("Confirmer ?        Oui             Non"), False, blue)

                if condarme!="" and condcoupable!="" and condjoueur!="" and condTest==True:
                    fenetre.blit(fondNoir,(22*longueurCase,0))
                    fenetre.blit(txtresume_hypothese,[22*longueurCase,280])
                    fenetre.blit(txtresume_hypothese2,[22*longueurCase,310])
                    if condHypotheseFinale2==False:
                        fenetre.blit(txtresume_hypothese3,[22*longueurCase,340])
                    fenetre.blit(txtresume_hypothese4,[22*longueurCase,370])
                    if 365<event.pos[1]<390:
                        if 920<event.pos[0]<960:
                            condTest=False
                            condcomplete=[condarme,condcoupable,condpiece]
                            if condHypotheseFinale2==True:
                                if condcomplete==resHypothese:
                                    fenetre.blit(fondNoir,[22*longueurCase,0])
                                    txtreussite=arial.render(("Félicitations, vous avez trouvé la bonne réponse !"), False, blue)
                                    txtreussite2=arial.render(("Pressez la touche Echap pour quitter le jeu"), False, blue)
                                    fenetre.blit(txtreussite,[22*longueurCase,400])
                                    fenetre.blit(txtreussite2,[22*longueurCase,430])
                                else:
                                    fenetre.blit(fondNoir,[22*longueurCase,0])
                                    txtechec=arial.render(("Ce n'est malheureusement pas la bonne réponse."), False, blue)
                                    txtechec2=arial.render(("Vous êtes donc éliminé du jeu."), False, blue)
                                    fenetre.blit(txtechec,[22*longueurCase,400])
                                    fenetre.blit(txtechec2,[22*longueurCase,430])
                                    fenetre.blit(txtjoueur_suivant,[22*longueurCase,500])
                                    if tourJoueur==1:
                                        elimJ1=True
                                    if tourJoueur==2:
                                        elimJ2=True
                                    if tourJoueur==3:
                                        elimJ3=True
                            if condHypotheseFinale2==False:
                                compteur=0
                                if condjoueur==nomJoueur1:
                                    for element in condcomplete:
                                        for i in range(len(piocheJ1)):
                                            if element==piocheJ1[i] and compteur==0:
                                                compteur=compteur+1
                                                mauvaise_pioche=element
                                    if mauvaise_pioche=="":
                                        txtmauvaise_pioche=arial.render(("Bonne nouvelle, {} ne possède aucune carte pouvant".format(condjoueur)), False, blue)
                                        txtmauvaise_pioche2=arial.render(("réfuter votre hypothèse."), False, blue)
                                        fenetre.blit(fondNoir,(22*longueurCase,0))
                                        fenetre.blit(txtmauvaise_pioche,[22*longueurCase,250])
                                        fenetre.blit(txtmauvaise_pioche2,[22*longueurCase,280])
                                        fenetre.blit(txtjoueur_suivant,(22*longueurCase,350))
                                    else:
                                        txtbonne_pioche=arial.render(("Malheureusement, {} possède une carte pouvant".format(condjoueur)), False, blue)
                                        txtbonne_pioche2=arial.render(("réfuter votre hypothèse."), False, blue)
                                        txtaffichage_carte=arial.render(("Cliquez ici pour l'afficher"), False, blue)
                                        txtaffichage_carte2=arial.render(("(Seul vous et {} pouvez regarder.)".format(condjoueur)), False, blue)
                                        fenetre.blit(fondNoir,(22*longueurCase,0))
                                        fenetre.blit(txtbonne_pioche,[22*longueurCase,250])
                                        fenetre.blit(txtbonne_pioche2,[22*longueurCase,280])
                                        fenetre.blit(txtaffichage_carte,[22*longueurCase,340])
                                        fenetre.blit(txtaffichage_carte2,[22*longueurCase,400])
                                        condAffichCarte=True
                                        if tourJoueur==2:
                                            cartesTrouvJ2.append(mauvaise_pioche)
                                        if tourJoueur==3:
                                            cartesTrouvJ3.append(mauvaise_pioche)

                                if condjoueur==nomJoueur2:
                                    for element in condcomplete:
                                        for i in range(len(piocheJ2)):
                                            if element==piocheJ2[i] and compteur==0:
                                                compteur=compteur+1
                                                mauvaise_pioche=element
                                    if mauvaise_pioche=="":
                                        txtmauvaise_pioche=arial.render(("Bonne nouvelle, {} ne possède aucune carte pouvant".format(condjoueur)), False, blue)
                                        txtmauvaise_pioche2=arial.render(("réfuter votre hypothèse."), False, blue)
                                        fenetre.blit(fondNoir,(22*longueurCase,0))
                                        fenetre.blit(txtmauvaise_pioche,[22*longueurCase,250])
                                        fenetre.blit(txtmauvaise_pioche2,[22*longueurCase,280])
                                        fenetre.blit(txtjoueur_suivant,(22*longueurCase,350))
                                    else:
                                        txtbonne_pioche=arial.render(("Malheureusement, {} possède une carte pouvant".format(condjoueur)), False, blue)
                                        txtbonne_pioche2=arial.render(("réfuter votre hypothèse."), False, blue)
                                        txtaffichage_carte=arial.render(("Cliquez ici pour l'afficher"), False, blue)
                                        txtaffichage_carte2=arial.render(("(Seul vous et {} pouvez regarder.)".format(condjoueur)), False, blue)
                                        fenetre.blit(fondNoir,(22*longueurCase,0))
                                        fenetre.blit(txtbonne_pioche,[22*longueurCase,250])
                                        fenetre.blit(txtbonne_pioche2,[22*longueurCase,280])
                                        fenetre.blit(txtaffichage_carte,[22*longueurCase,340])
                                        fenetre.blit(txtaffichage_carte2,[22*longueurCase,400])
                                        condAffichCarte=True
                                        if tourJoueur==1:
                                            cartesTrouvJ1.append(mauvaise_pioche)
                                        if tourJoueur==3:
                                            cartesTrouvJ3.append(mauvaise_pioche)

                                if condjoueur==nomJoueur3:
                                    for element in condcomplete:
                                        for i in range(len(piocheJ3)):
                                            if element==piocheJ3[i] and compteur==0:
                                                compteur=compteur+1
                                                mauvaise_pioche=element
                                    if mauvaise_pioche=="":
                                        txtmauvaise_pioche=arial.render(("Bonne nouvelle, {} ne possède aucune carte pouvant".format(condjoueur)), False, blue)
                                        txtmauvaise_pioche2=arial.render(("réfuter votre hypothèse."), False, blue)
                                        fenetre.blit(fondNoir,(22*longueurCase,0))
                                        fenetre.blit(txtmauvaise_pioche,[22*longueurCase,250])
                                        fenetre.blit(txtmauvaise_pioche2,[22*longueurCase,280])
                                        fenetre.blit(txtjoueur_suivant,(22*longueurCase,350))
                                    else:
                                        txtbonne_pioche=arial.render(("Malheureusement, {} possède une carte pouvant".format(condjoueur)), False, blue)
                                        txtbonne_pioche2=arial.render(("réfuter votre hypothèse."), False, blue)
                                        txtaffichage_carte=arial.render(("Cliquez ici pour l'afficher"), False, blue)
                                        txtaffichage_carte2=arial.render(("(Seul vous et {} pouvez regarder.)".format(condjoueur)), False, blue)
                                        fenetre.blit(fondNoir,(22*longueurCase,0))
                                        fenetre.blit(txtbonne_pioche,[22*longueurCase,250])
                                        fenetre.blit(txtbonne_pioche2,[22*longueurCase,280])
                                        fenetre.blit(txtaffichage_carte,[22*longueurCase,340])
                                        fenetre.blit(txtaffichage_carte2,[22*longueurCase,400])
                                        condAffichCarte=True
                                        if tourJoueur==2:
                                            cartesTrouvJ2.append(mauvaise_pioche)
                                        if tourJoueur==1:
                                            cartesTrouvJ1.append(mauvaise_pioche)

                        if 1020<event.pos[0]<1060:
                            condHypothese=True
                            condarme=""
                            condcoupable=""
                            if condHypotheseFinale2==False:
                                condjoueur=""
                            if condHypotheseFinale2==True:
                                condpiece=""
                                condjoueur=""
                            fenetre.blit(fondNoir,(22*longueurCase,0))
                            fenetre.blit(txtvalidation,[22*longueurCase,160])

                if condHypotheseFinale==True:
                    txtHypotheseFinale_validation=arial.render("Êtes-vous sûr ? Si celle ci est fausse, vous serez éliminé du jeu.", False, blue)
                    fenetre.blit(txtHypotheseFinale_validation,[22*longueurCase,120])
                    condHypothese=True

                if condAffichCarte==True:
                    if 22*longueurCase<event.pos[0]<1100:
                        if 335<event.pos[1]<365:
                            txtcarte=arial.render(("La carte est : {}".format(mauvaise_pioche)), False, blue)
                            fenetre.blit(fondNoir,(22*longueurCase,0))
                            fenetre.blit(txtcarte,[22*longueurCase,340])
                            condAffichCarte=False
                            txtdesaffichage=arial.render(("Cliquez ici pour masquer la carte"), False, blue)
                            fenetre.blit(txtdesaffichage,[22*longueurCase,400])
                            condDesaffichCarte=True

                if condDesaffichCarte==True:
                    if 22*longueurCase<event.pos[0]<1100:
                        if 395<event.pos[1]<424:
                            fenetre.blit(fondNoir,(22*longueurCase,0))
                            fenetre.blit(txtjoueur_suivant,(22*longueurCase,350))
                            condDesaffichCarte=False

    txtcoups_restants=arial.render(("{} coup(s) restant(s)".format(nmbreCoups)), False, blue)

    if accesJeu==True:
        if tourJoueur==1:
            fenetre.blit(txtJ1,[22*longueurCase,10])
            fenetre.blit(txtcoups_restants,[22*longueurCase,75])
            if condHypothese2==False and condHypotheseFinale2==False:
                fenetre.blit(txtPioche,[22*longueurCase,550])
                fenetre.blit(txtPioche2,[22*longueurCase,580])
        if tourJoueur==2:
            fenetre.blit(txtJ2,[22*longueurCase,10])
            fenetre.blit(txtcoups_restants,[22*longueurCase,75])
            if condHypothese2==False and condHypotheseFinale2==False:
                fenetre.blit(txtPioche,[22*longueurCase,550])
                fenetre.blit(txtPioche2,[22*longueurCase,580])
        if tourJoueur==3:
            fenetre.blit(txtJ3,[22*longueurCase,10])
            fenetre.blit(txtcoups_restants,[22*longueurCase,75])
            if condHypothese2==False and condHypotheseFinale2==False:
                fenetre.blit(txtPioche,[22*longueurCase,550])
                fenetre.blit(txtPioche2,[22*longueurCase,580])

    pygame.display.flip()
pygame.quit()
