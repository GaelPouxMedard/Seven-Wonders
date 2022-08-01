bois = "bois"
pierre = "pierre"
argile = "argile"
fer = "fer"
tissu = "tissu"
verre = "verre"
parchemin = "parchemin"

argent = "argent"

base = [bois, pierre, argile, fer]
manufacture = [tissu, verre, parchemin]
ressources = [bois, pierre, argile, fer, tissu, verre, parchemin, argent]


marron = "marron"
gris = "gris"
jaune = "jaune"
vert = "vert"
rouge = "rouge"
bleu = "bleu"
violet = "violet"
couleurs = [marron, gris, jaune, vert, rouge, bleu, violet]

merveille = "merveille"
militaire = "militaire"
points = "points"
somme = "somme"
nom = "nom"
argent_score = "argent-score"
trait_score = "trait-score"
rond_score = "rond-score"
triangle_score = "triangle-score"
etoile_score = "etoile-score"

symbole_etoile = "etoile"
symbole_masque = "masque"
symbole_goutte = "goutte"
symbole_chameau = "chameau"
symbole_devanture = "devanture"
symbole_balance = "balance"
symbole_livre = "livre"
symbole_fer_a_cheval = "fer-à-cheval"
symbole_bol = "bol"
symbole_cible = "cible"
symbole_lampe = "lampe"
symbole_marteau = "marteau"
symbole_temple = "temple"
symbole_parchemin = "parchemin"
symbole_lyre = "lyre"
symbole_plume = "plume"
symbole_planetes = "planetes"
symbole_scie = "scie"
symbole_eclair = "eclair"
symbole_torche = "torche"
symbole_tour = "tour"
symbole_phare = "phare"
symbole_tonneau = "tonneau"
symbole_casque = "casque"

compas = "compas"
tablette = "tablette"
rouage = "rouage"

act_vendre = "vendre"
act_construire_batiment = "construire"
act_construire_merveille = "construire-merveille"

carte_defausse = "carte-defausse"
jouer_derniere_carte = "jouer-derniere-carte"

couleurs_rvb = {
    vert: (90, 160, 60),
    bleu: (0, 150, 200),
    rouge: (200, 25, 25),
    violet: (60, 60, 140),
    gris: (180, 180, 180),
    marron: (150, 70, 20),
    jaune: (230, 170, 50),
}



scale_cartes = 50

propline_sep_carte = 0.25
espace_entre_cartes = 1*scale_cartes*0.3
espace_entre_cartes_vertical = 1*scale_cartes
largeur_carte, hauteur_carte = 6.5*scale_cartes, 10*scale_cartes
marges_board = 1000
largeur_board = (largeur_carte+espace_entre_cartes)*len(couleurs)
hauteur_board = (hauteur_carte+espace_entre_cartes)*4#4
hauteur_merveille = hauteur_carte  # 13.5
largeur_merveille =  hauteur_merveille*764.2/219.2 #0.8*7*(largeur_carte+espace_entre_cartes)  # 27.5
prop_hauteur_etage = 0.3
facteur_arrondi_cartes = 20
border_radius = int(facteur_arrondi_cartes*scale_cartes/30)
zoom_carte = 3.5
croix = "croix"

largeur_boutton_fac = 0.70
hauteur_boutton_fac = 0.15
pos_act = {}

prop_largeur_choix_defausse = 0.95
prop_hauteur_choix_defausse = 0.95
prop_largeur_colonne_resultats = 0.95
prop_hauteur_colonne_resultats = 0.6

import numpy as np
pos_act[act_construire_batiment] = np.array((0.4*largeur_carte, 0.5*hauteur_carte))
pos_act[act_construire_merveille] = np.array((0.4*largeur_carte, 0.7*hauteur_carte))
pos_act[act_vendre] = np.array((0.4*largeur_carte, 0.9*hauteur_carte))

import pygame as pg
pg.font.init()
font = pg.font.SysFont("Comic sans", int(1*scale_cartes))
font_infos = pg.font.SysFont("Comic sans", int(0.4*scale_cartes))
font_scores = pg.font.SysFont("Comic sans", int(0.6*scale_cartes))

images = {
    fer: pg.image.load("Images/Elements_cartes/Ressources/Fer.png"),
    bois: pg.image.load("Images/Elements_cartes/Ressources/Bois.png"),
    pierre: pg.image.load("Images/Elements_cartes/Ressources/Pierre.png"),
    argile: pg.image.load("Images/Elements_cartes/Ressources/Argile.png"),
    verre: pg.image.load("Images/Elements_cartes/Ressources/Verre.png"),
    tissu: pg.image.load("Images/Elements_cartes/Ressources/Tissu.png"),
    parchemin: pg.image.load("Images/Elements_cartes/Ressources/Parchemin.png"),
    argent: pg.image.load("Images/Elements_cartes/Effets/Argent.png"),
    militaire: pg.image.load("Images/Elements_cartes/Effets/Militaire.png"),
    points: pg.image.load("Images/Elements_cartes/Effets/Points victoire.png"),
    merveille: pg.image.load("Images/Elements_cartes/Effets/Merveille_score.png"),
    argent_score: pg.image.load("Images/Elements_cartes/Effets/Piece_scores.png"),
    trait_score: pg.image.load("Images/Elements_cartes/Effets/Trait_scores.png"),
    rond_score: pg.image.load("Images/Elements_cartes/Effets/Rond_scores.png"),
    triangle_score: pg.image.load("Images/Elements_cartes/Effets/Triangle_score.png"),
    etoile_score: pg.image.load("Images/Elements_cartes/Effets/Etoile_scores.png"),
    croix: pg.image.load("Images/Elements_cartes/Effets/Croix.png"),
}

scale_res = 0.1
for res in images:
    images[res] = pg.transform.smoothscale(images[res], (hauteur_carte*images[res].get_width()*scale_res/images[res].get_height(), hauteur_carte*scale_res))
    #images_resources[res] = pg.transform.rotozoom(images_resources[res], 0, 0.5)

change_bouton = "change-bouton"
change_carte = "change-carte"
change_etage = "change-etage"
click_bouton = "click-bouton"
click_carte = "click-carte"
click_etage = "click-etage"