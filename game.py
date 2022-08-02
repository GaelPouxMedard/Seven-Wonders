import constantes as cst
import numpy as np
import pygame as pg
from utils import *
from GUI import *
from pygame import gfxdraw
from PIL import Image

#np.random.seed(66+66)


class Joueur:
    def __init__(self, id_joueur, main, merveille, tresor):
        self.id = id_joueur
        self.tresor = tresor
        self.main = main
        self.cite = Cite()
        self.merveille = merveille
        self.etage_merveille = 0
        self.points_total = 0
        self.points = {couleur: 0 for couleur in cst.couleurs}
        self.points[cst.merveille] = 0
        self.points[cst.militaire] = 0
        self.points[cst.argent] = 0

        self.voisin_gauche = id_joueur-1
        self.voisin_droite = id_joueur+1

        self.liste_actions_possibles = None

        self.rect_surface = None


    def cout_construction(self, carte, jeu):
        if carte.nom in self.cite.batiments_noms:
            possible = False
            return possible, -1
        possible = True
        cout = 0
        res_needed = carte.cout_ressource
        production = self.cite.production.copy()
        cout_ressource = []
        for res in reversed(res_needed):
            for _ in range(res_needed[res]):
                cout_ressource.append(res)

        # Ressources unitaires produites
        for res in reversed(cout_ressource):
            if res == cst.argent:
                cout += 1
                cout_ressource.remove(res)
                continue

            achetee = False
            for res_produite in reversed(production):
                if len(res_produite)==1:
                    if res in res_produite:
                        production.remove(res_produite)
                        cout_ressource.remove(res)
                        achetee = True
                        break
            if achetee:
                continue

        # Achat ressources nécessaires
        res_achetees_gauche_solde = []
        res_achetees_droite_solde = []
        res_achetees_gauche = []
        res_achetees_droite = []
        prod_voisin_gauche = jeu.joueurs[self.voisin_gauche].cite.production_achetable.copy()
        prod_voisin_droite = jeu.joueurs[self.voisin_droite].cite.production_achetable.copy()
        for prod_hypothetique in [False, True]:
            for res in reversed(cout_ressource):
                if (self.cite.reduction_gauche_base and res in cst.base) or (self.cite.reduction_gauche_manufacture and res in cst.manufacture):
                    achetee = False
                    for res_produite_gauche in reversed(prod_voisin_gauche):
                        if len(res_produite_gauche)>1 and not prod_hypothetique:
                            continue
                        if res in res_produite_gauche:
                            res_achetees_gauche_solde.append(res)
                            prod_voisin_gauche.remove(res_produite_gauche)
                            cout_ressource.remove(res)
                            achetee = True
                            break
                    if achetee: continue

                if (self.cite.reduction_droite_base and res in cst.base) or (self.cite.reduction_droite_manufacture and res in cst.manufacture):
                    achetee = False
                    for res_produite_droite in reversed(prod_voisin_droite):
                        if len(res_produite_droite)>1 and not prod_hypothetique:
                            continue
                        if res in res_produite_droite:
                            res_achetees_droite_solde.append(res)
                            prod_voisin_droite.remove(res_produite_droite)
                            cout_ressource.remove(res)
                            achetee = True
                            break
                    if achetee: continue


                if not ((self.cite.reduction_gauche_base and res in cst.base) or (self.cite.reduction_gauche_manufacture and res in cst.manufacture)):
                    achetee = False
                    for res_produite_gauche in reversed(prod_voisin_gauche):
                        if len(res_produite_gauche)>1 and not prod_hypothetique:
                            continue
                        if res in res_produite_gauche:
                            res_achetees_gauche.append(res)
                            prod_voisin_gauche.remove(res_produite_gauche)
                            cout_ressource.remove(res)
                            achetee = True
                            break
                    if achetee: continue

                if not ((self.cite.reduction_droite_base and res in cst.base) or (self.cite.reduction_droite_manufacture and res in cst.manufacture)):
                    achetee = False
                    for res_produite_droite in reversed(prod_voisin_droite):
                        if len(res_produite_droite)>1 and not prod_hypothetique:
                            continue
                        if res in res_produite_droite:
                            res_achetees_droite.append(res)
                            prod_voisin_droite.remove(res_produite_droite)
                            cout_ressource.remove(res)
                            achetee = True
                            break
                    if achetee: continue

        # Ressources non-unitaires produites (bois OU fer p.ex.)
        for res in reversed(cout_ressource):
            if res == cst.argent:
                cout += 1
                cout_ressource.remove(res)
                continue
            achetee = False
            for res_produite in reversed(production):
                if len(res_produite)>1:
                    if res in res_produite:
                        production.remove(res_produite)
                        cout_ressource.remove(res)
                        achetee = True
                        break
            if achetee: continue

        # Si on n'a pas pu obtenir toutes les ressources
        if len(cout_ressource)>0:
            possible = False
            return possible, -1

        # Si on a pu obtenir toutes les ressources, on regarde si les ressources non-unitaires peuvent épargner des achats
        for res_produite in reversed(production):
            achetee = False
            for res in res_produite:
                if res in res_achetees_gauche:
                    res_achetees_gauche.remove(res)
                    production.remove(res_produite)
                    achetee = True
                    break
            if achetee: continue
            achetee = False
            for res in res_produite:
                if res in res_achetees_droite:
                    res_achetees_droite.remove(res)
                    production.remove(res_produite)
                    achetee = True
                    break
            if achetee: continue
            achetee = False
            for res in res_produite:
                if res in res_achetees_gauche_solde:
                    res_achetees_gauche_solde.remove(res)
                    production.remove(res_produite)
                    achetee = True
                    break
            if achetee: continue
            achetee = False
            for res in res_produite:
                if res in res_achetees_droite_solde:
                    res_achetees_droite_solde.remove(res)
                    production.remove(res_produite)
                    achetee = True
                    break
            if achetee: continue

        cout += len(res_achetees_droite_solde)*1 \
                +len(res_achetees_gauche_solde)*1 \
                +len(res_achetees_gauche)*2 \
                +len(res_achetees_droite)*2

        if cout > self.tresor:
            possible = False

        return possible, cout

    def actions_possibles(self, jeu):
        actions = []

        for i, carte in enumerate(self.main):
            actions.append((cst.act_vendre, carte, 0))

        for i, carte in enumerate(self.main):
            if carte.cout_chainage in self.cite.symboles_chainage:
                actions.append((cst.act_construire_batiment, carte, 0))
                continue

            if self.cite.premiere_carte_age_gratuite and jeu.tour==1:
                actions.append((cst.act_construire_batiment, carte, 0))
                continue
            if self.cite.derniere_carte_age_gratuite and jeu.tour==jeu.dernier_tour:
                actions.append((cst.act_construire_batiment, carte, 0))
                continue
            if self.cite.premiere_carte_couleur_gratuite:
                premiere = True
                for bat in self.cite.batiments:
                    if bat.couleur == carte.couleur:
                        premiere = False
                        break
                if premiere:
                    actions.append((cst.act_construire_batiment, carte, 0))
                    continue


            possible, cout = self.cout_construction(carte, jeu)

            if possible:
                actions.append((cst.act_construire_batiment, carte, cout))
                continue

        if self.etage_merveille <= self.merveille.nombre_etages-1:

            possible, cout = self.cout_construction(self.merveille.etages[self.etage_merveille], jeu)

            if possible:
                for i, carte in enumerate(self.main):
                    actions.append((cst.act_construire_merveille, carte, cout))

        self.liste_actions_possibles = actions.copy()

        return actions

    def appliquer_effets(self, effet, jeu, couleur):
        if effet.effet_militaire is not None:
            self.cite.puissance_militaire += effet.effet_militaire
        if effet.effet_points_victoire is not None:
            self.cite.points_victoire += effet.effet_points_victoire
            self.points[couleur] += effet.effet_points_victoire
        if effet.effet_tresor is not None:
            self.tresor += effet.effet_tresor
        production_hypothetique = []
        for res in effet.effet_production:
            if effet.effet_production[res] != -1:
                for _ in range(effet.effet_production[res]):
                    self.cite.production.append([res])
                    if effet.achetable:
                        self.cite.production_achetable.append([res])
            else:
                production_hypothetique.append(res)
        if len(production_hypothetique) != 0:
            self.cite.production.append(production_hypothetique)
            if effet.achetable:
                self.cite.production_achetable.append(production_hypothetique)

        symboles_hypothetiques = []
        for symb in effet.effet_symbole_scientifique:
            if effet.effet_symbole_scientifique[symb] != -1:
                for _ in range(effet.effet_symbole_scientifique[symb]):
                    self.cite.symboles_scientifiques.append([symb])
            else:
                symboles_hypothetiques.append(symb)
        if len(symboles_hypothetiques) != 0:
            self.cite.symboles_scientifiques.append(symboles_hypothetiques)


        if effet.effet_reduction_gauche_base is not None:
            self.cite.reduction_gauche_base = True
        if effet.effet_reduction_droite_base is not None:
            self.cite.reduction_droite_base = True
        if effet.effet_reduction_gauche_manufacture is not None:
            self.cite.reduction_gauche_manufacture = True
        if effet.effet_reduction_droite_manufacture is not None:
            self.cite.reduction_droite_manufacture = True

        for symb in effet.symbole_chainage:
            self.cite.symboles_chainage.append(symb)

        gain = 0
        for i, nb in enumerate(effet.effet_gain_or_cartes_grises):
            if i==0 and nb is not None:
                gain += len([bat for bat in jeu.joueurs[self.voisin_gauche].cite.batiments if bat.couleur==cst.gris])*nb
            if i==1 and nb is not None:
                gain += len([bat for bat in self.cite.batiments if bat.couleur==cst.gris])*nb
            if i==2 and nb is not None:
                gain += len([bat for bat in jeu.joueurs[self.voisin_droite].cite.batiments if bat.couleur==cst.gris])*nb
        self.tresor += gain

        gain = 0
        for i, nb in enumerate(effet.effet_gain_or_cartes_marron):
            if i==0 and nb is not None:
                gain += len([bat for bat in jeu.joueurs[self.voisin_gauche].cite.batiments if bat.couleur==cst.marron])*nb
            if i==1 and nb is not None:
                gain += len([bat for bat in self.cite.batiments if bat.couleur==cst.marron])*nb
            if i==2 and nb is not None:
                gain += len([bat for bat in jeu.joueurs[self.voisin_droite].cite.batiments if bat.couleur==cst.marron])*nb
        self.tresor += gain

        gain = 0
        for i, nb in enumerate(effet.effet_gain_or_cartes_jaunes):
            if i==0 and nb is not None:
                print(jeu.joueurs[self.voisin_gauche].cite.batiments)
                gain += len([bat for bat in jeu.joueurs[self.voisin_gauche].cite.batiments if bat.couleur==cst.jaune])*nb
            if i==1 and nb is not None:
                gain += len([bat for bat in self.cite.batiments if bat.couleur==cst.jaune])*nb
            if i==2 and nb is not None:
                gain += len([bat for bat in jeu.joueurs[self.voisin_droite].cite.batiments if bat.couleur==cst.jaune])*nb
        self.tresor += gain

        gain = 0
        for i, nb in enumerate(effet.effet_gain_or_cartes_rouges):
            if i==0 and nb is not None:
                print(jeu.joueurs[self.voisin_gauche].cite.batiments)
                gain += len([bat for bat in jeu.joueurs[self.voisin_gauche].cite.batiments if bat.couleur==cst.rouge])*nb
            if i==1 and nb is not None:
                gain += len([bat for bat in self.cite.batiments if bat.couleur==cst.rouge])*nb
            if i==2 and nb is not None:
                gain += len([bat for bat in jeu.joueurs[self.voisin_droite].cite.batiments if bat.couleur==cst.rouge])*nb
        self.tresor += gain

        gain = 0
        for i, nb in enumerate(effet.effet_gain_or_etages):
            if i==0 and nb is not None:
                gain += jeu.joueurs[self.voisin_gauche].etage_merveille*nb  # Etage = 0, 1, 2, ... en construction
            if i==1 and nb is not None:
                gain += self.etage_merveille*nb
            if i==2 and nb is not None:
                gain += jeu.joueurs[self.voisin_droite].etage_merveille*nb
        self.tresor += gain

        gain = 0
        for i, nb in enumerate(effet.effet_gain_points_cartes_grises):
            if i==0 and nb is not None:
                gain += len([bat for bat in jeu.joueurs[self.voisin_gauche].cite.batiments if bat.couleur==cst.gris])*nb
            if i==1 and nb is not None:
                gain += len([bat for bat in self.cite.batiments if bat.couleur==cst.gris])*nb
            if i==2 and nb is not None:
                gain += len([bat for bat in jeu.joueurs[self.voisin_droite].cite.batiments if bat.couleur==cst.gris])*nb
        self.cite.points_victoire += gain
        self.points[couleur] += gain

        gain = 0
        for i, nb in enumerate(effet.effet_gain_points_cartes_marron):
            if i==0 and nb is not None:
                gain += len([bat for bat in jeu.joueurs[self.voisin_gauche].cite.batiments if bat.couleur==cst.marron])*nb
            if i==1 and nb is not None:
                gain += len([bat for bat in self.cite.batiments if bat.couleur==cst.marron])*nb
            if i==2 and nb is not None:
                gain += len([bat for bat in jeu.joueurs[self.voisin_droite].cite.batiments if bat.couleur==cst.marron])*nb
        self.cite.points_victoire += gain
        self.points[couleur] += gain

        gain = 0
        for i, nb in enumerate(effet.effet_gain_points_cartes_jaunes):
            if i==0 and nb is not None:
                gain += len([bat for bat in jeu.joueurs[self.voisin_gauche].cite.batiments if bat.couleur==cst.jaune])*nb
            if i==1 and nb is not None:
                gain += len([bat for bat in self.cite.batiments if bat.couleur==cst.jaune])*nb
            if i==2 and nb is not None:
                gain += len([bat for bat in jeu.joueurs[self.voisin_droite].cite.batiments if bat.couleur==cst.jaune])*nb
        self.cite.points_victoire += gain
        self.points[couleur] += gain

        gain = 0
        for i, nb in enumerate(effet.effet_gain_points_cartes_rouges):
            if i==0 and nb is not None:
                gain += len([bat for bat in jeu.joueurs[self.voisin_gauche].cite.batiments if bat.couleur==cst.rouge])*nb
            if i==1 and nb is not None:
                gain += len([bat for bat in self.cite.batiments if bat.couleur==cst.rouge])*nb
            if i==2 and nb is not None:
                gain += len([bat for bat in jeu.joueurs[self.voisin_droite].cite.batiments if bat.couleur==cst.rouge])*nb
        self.cite.points_victoire += gain
        self.points[couleur] += gain

        gain = 0
        for i, nb in enumerate(effet.effet_gain_points_cartes_bleues):
            if i==0 and nb is not None:
                gain += len([bat for bat in jeu.joueurs[self.voisin_gauche].cite.batiments if bat.couleur==cst.bleu])*nb
            if i==1 and nb is not None:
                gain += len([bat for bat in self.cite.batiments if bat.couleur==cst.bleu])*nb
            if i==2 and nb is not None:
                gain += len([bat for bat in jeu.joueurs[self.voisin_droite].cite.batiments if bat.couleur==cst.bleu])*nb
        self.cite.points_victoire += gain
        self.points[couleur] += gain

        gain = 0
        for i, nb in enumerate(effet.effet_gain_points_cartes_vertes):
            if i==0 and nb is not None:
                gain += len([bat for bat in jeu.joueurs[self.voisin_gauche].cite.batiments if bat.couleur==cst.vert])*nb
            if i==1 and nb is not None:
                gain += len([bat for bat in self.cite.batiments if bat.couleur==cst.vert])*nb
            if i==2 and nb is not None:
                gain += len([bat for bat in jeu.joueurs[self.voisin_droite].cite.batiments if bat.couleur==cst.vert])*nb
        self.cite.points_victoire += gain
        self.points[couleur] += gain

        gain = 0
        for i, nb in enumerate(effet.effet_gain_points_cartes_violettes):
            if i==0 and nb is not None:
                gain += len([bat for bat in jeu.joueurs[self.voisin_gauche].cite.batiments if bat.couleur==cst.violet])*nb
            if i==1 and nb is not None:
                gain += len([bat for bat in self.cite.batiments if bat.couleur==cst.violet])*nb
            if i==2 and nb is not None:
                gain += len([bat for bat in jeu.joueurs[self.voisin_droite].cite.batiments if bat.couleur==cst.violet])*nb
        self.cite.points_victoire += gain
        self.points[couleur] += gain

        gain = 0
        for i, nb in enumerate(effet.effet_gain_points_etages):
            if i==0 and nb is not None:
                gain += jeu.joueurs[self.voisin_gauche].etage_merveille*nb
            if i==1 and nb is not None:
                gain += self.etage_merveille*nb
            if i==2 and nb is not None:
                gain += jeu.joueurs[self.voisin_droite].etage_merveille*nb
        self.cite.points_victoire += gain
        self.points[couleur] += gain

        if effet.effet_gain_points_cartes_merveille_complete:
            if self.etage_merveille == self.merveille.nombre_etages-1:  # etages_merveille = 0, 1, 2, ...
                self.cite.points_victoire += 7
                self.points[couleur] += gain


        if effet.premiere_carte_age_gratuite:
            self.cite.premiere_carte_age_gratuite = True
        if effet.derniere_carte_age_gratuite:
            self.cite.derniere_carte_age_gratuite = True
        if effet.premiere_carte_couleur_gratuite:
            self.cite.premiere_carte_couleur_gratuite = True
        if effet.carte_defausse:
            self.cite.carte_defausse = True
        if effet.jouer_derniere_carte:
            self.cite.jouer_derniere_carte = True

    def acte(self, act, cible, cout, jeu):
        extra_action = []

        if act == cst.act_vendre:
            self.tresor += 3
            jeu.defausse.append(cible)

        elif act == cst.act_construire_batiment:
            # Construction
            self.tresor -= cout
            self.cite.batiments.append(cible)
            self.cite.batiments_noms.append(cible.nom)
            cible.construite = True

            # Effet
            effet = cible.effet

            self.appliquer_effets(effet, jeu, cible.couleur)

        elif act == cst.act_construire_merveille:
            # Construction
            self.tresor -= cout
            effet = self.merveille.etages[self.etage_merveille].effet
            self.merveille.etages[self.etage_merveille].done = True
            self.merveille.etages[self.etage_merveille].rendered = False
            if jeu.GUI:
                self.merveille.etages[self.etage_merveille].draw()
            self.etage_merveille += 1

            self.appliquer_effets(effet, jeu, cst.merveille)
            if self.cite.carte_defausse:
                extra_action.append(cst.carte_defausse)
                self.cite.carte_defausse = None

        if self.cite.jouer_derniere_carte and jeu.dernier_tour==jeu.tour:
            extra_action.append(cst.jouer_derniere_carte)

        self.main.remove(cible)

        return extra_action

    def decompte_points(self):
        self.points_total = 0
        for type in self.points:
            self.points_total += self.points[type]
        return self.points_total

class Cite:
    def __init__(self):
        self.production = list()
        self.production_achetable = list()

        self.symboles_chainage = []

        self.batiments = list()
        self.batiments_noms = list()

        self.puissance_militaire = 0
        self.symboles_scientifiques = list()
        self.points_victoire = 0

        self.reduction_gauche_base = None
        self.reduction_droite_base = None
        self.reduction_gauche_manufacture = None
        self.reduction_droite_manufacture = None

        self.carte_defausse = None
        self.jouer_derniere_carte = None
        self.premiere_carte_age_gratuite = None
        self.derniere_carte_age_gratuite = None
        self.premiere_carte_couleur_gratuite = None

        self.surface = None
        self.surface_screen = None
        self.masque = None

class Carte:
    def __init__(self):
        self.nom = None
        self.cout_ressource = {cst.bois: 0, cst.argile: 0, cst.pierre: 0, cst.fer: 0, cst.tissu: 0, cst.verre: 0, cst.parchemin: 0, cst.argent: 0}
        self.cout_chainage = None
        self.couleur = None
        self.age = None
        self.nb_joueurs = None
        self.effet = None

        self.construite = False

        self.rendered_cite = False
        self.rendered_main = False
        self.surface = None
        self.surface_screen = None
        self.surface_screen_zoomed = None
        self.masque = None
        self.rect = None
        self.pos = None
        self.hovered = False
        self.unzoom = 1
        self.is_clicked = False
        self.justclicked = False
        self.buttons = {}

    def draw(self):
        draw_manual = False
        epaisseur_ligne_sep = 4

        if not draw_manual:
            decalage_ombre = cst.decalage_ombre
            self.surface = pg.Surface((cst.largeur_carte+decalage_ombre, cst.hauteur_carte+decalage_ombre), pg.SRCALPHA, 32)
            pg.draw.rect(self.surface, (0,0,0,130), pg.Rect(decalage_ombre, decalage_ombre, cst.largeur_carte, cst.hauteur_carte), border_radius=int(0.55*cst.border_radius))

            img = pg.image.load(f"Images/Cartes/Age {self.age}/{self.nom.replace('-', '_').capitalize()}.png")
            img = pg.transform.smoothscale(img, (cst.largeur_carte, cst.hauteur_carte))
            self.surface.blit(img, (0,0))
            pg.draw.rect(self.surface, pg.Color("black"), pg.Rect(0, 0, cst.largeur_carte, cst.hauteur_carte), int(epaisseur_ligne_sep*cst.scale_cartes/60), border_radius=int(0.55*cst.border_radius))

        else:
            color = pg.Color(cst.couleurs_rvb[self.couleur])

            pos = [0,0]

            self.surface = pg.Surface((cst.largeur_carte, cst.hauteur_carte), pg.SRCALPHA, 32)

            pg.draw.rect(self.surface, color, pg.Rect(pos[0], pos[1], cst.largeur_carte, cst.hauteur_carte), border_radius=cst.border_radius)
            pg.draw.rect(self.surface, pg.Color("white"), pg.Rect(pos[0], pos[1]+cst.hauteur_carte*cst.propline_sep_carte, cst.largeur_carte, cst.hauteur_carte*(1-cst.propline_sep_carte)), border_bottom_left_radius=cst.border_radius, border_bottom_right_radius=cst.border_radius)

            pg.draw.line(self.surface, pg.Color("black"), (pos[0], pos[1]+cst.hauteur_carte*cst.propline_sep_carte), (pos[0]+cst.largeur_carte*0.98, pos[1]+cst.hauteur_carte*cst.propline_sep_carte), width=int(epaisseur_ligne_sep*cst.scale_cartes/30))
            pg.draw.rect(self.surface, pg.Color("black"), pg.Rect(pos[0], pos[1], cst.largeur_carte, cst.hauteur_carte), int(epaisseur_ligne_sep*cst.scale_cartes/30), border_radius=cst.border_radius)

            i = 0
            for res in self.cout_ressource:
                for _ in range(self.cout_ressource[res]):
                    pos_img = (pos[0]+cst.largeur_carte*0.05, pos[1]+cst.hauteur_carte*(cst.propline_sep_carte+0.02)+i*cst.hauteur_carte*cst.scale_res)
                    self.surface.blit(cst.images[res].convert_alpha(), pos_img)

                    if res == cst.argent:
                        font_argent = pg.font.SysFont("Arial", int(0.7*cst.scale_cartes))
                        num_argent = font_argent.render(str(self.cout_ressource[res]), False, (0, 0, 0))
                        self.surface.blit(num_argent, (pos[0]+cst.largeur_carte*0.097, pos[1]+cst.hauteur_carte*(cst.propline_sep_carte+0.03)+i*cst.hauteur_carte*cst.scale_res))
                        break
                    i+=1

    def check_hover(self):
        pos = pg.mouse.get_pos()
        change = set()
        if self.rect is not None and self.masque is not None:
            pos_in_mask = pos[0] - self.pos[0], pos[1] - self.pos[1]
            if self.rect.collidepoint(*pos):
                if self.masque.get_at(pos_in_mask):
                    if not self.hovered: change.add(cst.change_carte)
                    self.hovered = True
                else:
                    if self.hovered: change.add(cst.change_carte)
                    self.hovered = False
            else:
                if self.hovered: change.add(cst.change_carte)
                self.hovered = False


        for act in self.buttons:
            if not self.buttons[act].clickable:
                continue

            pos_in_mask = pos[0] - self.buttons[act].pos[0], pos[1] - self.buttons[act].pos[1]
            if self.buttons[act].rect.collidepoint(*pos):
                if self.buttons[act].masque.get_at(pos_in_mask):
                    if not self.buttons[act].hovered: change.add(cst.change_bouton)
                    self.buttons[act].hovered = True
                else:
                    if self.buttons[act].hovered: change.add(cst.change_bouton)
                    self.buttons[act].hovered = False
            else:
                if self.buttons[act].hovered: change.add(cst.change_bouton)
                self.buttons[act].hovered = False


        return change

    def zoom(self, screen):
        dims = np.array([self.surface_screen_zoomed.get_width(), self.surface_screen_zoomed.get_height()])*cst.zoom_carte*self.unzoom
        dims_base = np.array([self.surface_screen.get_width(), self.surface_screen.get_height()])

        if self.surface_screen_zoomed is not None:
            screen.blit(pg.transform.rotozoom(self.surface_screen_zoomed, 0, cst.zoom_carte*self.unzoom), self.pos-dims/2+dims_base/2)

    def clicked(self, screen, shade = True):
        if len(self.buttons)!=3:
            self.draw_buttons()

        dims = np.array([self.surface_screen_zoomed.get_width(), self.surface_screen_zoomed.get_height()])*cst.zoom_carte*self.unzoom
        dims_base = np.array([self.surface_screen.get_width(), self.surface_screen.get_height()])

        screen.blit(pg.transform.rotozoom(self.surface_screen_zoomed, 0, cst.zoom_carte*self.unzoom), self.pos-dims/2+dims_base/2)

        if self.surface_screen_zoomed is not None and shade:
            self.surface_shaded = shaded_image(self.surface_screen_zoomed, (0,0,0,128))
            screen.blit(pg.transform.rotozoom(self.surface_shaded, 0, cst.zoom_carte*self.unzoom), self.pos-dims/2+dims_base/2)

    def draw_buttons(self):
        buttons = {}
        for act_name in [cst.act_construire_batiment, cst.act_construire_merveille, cst.act_vendre]:
            buttons[act_name] = Bouton(dims_carte = self.surface_screen_zoomed.get_size())

            buttons[act_name].draw()
            buttons[act_name].pos = cst.pos_act[act_name]*cst.zoom_carte*self.unzoom

            buttons[act_name].surface_screen = buttons[act_name].surface
            buttons[act_name].rect = buttons[act_name].surface_screen.get_rect(topleft=buttons[act_name].pos)
            buttons[act_name].masque = pg.mask.from_surface(buttons[act_name].surface_screen)

            self.buttons[act_name] = buttons[act_name]

    def update_buttons(self, actions):
        act_carte = []
        if actions is not None:
            for action in actions:
                if action[1] == self:
                    act_carte.append(action)

        for act_name in [cst.act_construire_batiment, cst.act_construire_merveille, cst.act_vendre]:
            txt = ""
            if act_name == cst.act_vendre: txt = "Vendre"
            if act_name == cst.act_construire_merveille: txt = "Merveille"
            if act_name == cst.act_construire_batiment: txt = "Construire"

            action_consideree = None
            for act in act_carte:
                if act[0]==act_name:
                    action_consideree = act

            if action_consideree is not None:
                self.buttons[act_name].clickable = True

                if action_consideree[0]==act_name and action_consideree[2]!=0:
                    txt += f" ({str(action_consideree[2])})"

            else:
                self.buttons[act_name].clickable = False

            self.buttons[act_name].action = action_consideree
            self.buttons[act_name].texte = txt
            self.buttons[act_name].draw()
            self.buttons[act_name].pos = cst.pos_act[act_name]*cst.zoom_carte*self.unzoom

            self.buttons[act_name].surface_screen = self.buttons[act_name].surface
            self.buttons[act_name].surface_screen = pg.transform.rotozoom(self.buttons[act_name].surface_screen, 0, cst.zoom_carte*self.unzoom)
            self.buttons[act_name].rect = self.buttons[act_name].surface_screen.get_rect(topleft=self.buttons[act_name].pos)
            self.buttons[act_name].masque = pg.mask.from_surface(self.buttons[act_name].surface_screen)

    def blit_buttons(self, screen):
        dims_zoomed = np.array([self.surface_screen.get_width(), self.surface_screen.get_height()])*cst.zoom_carte
        for act_name in [cst.act_construire_batiment, cst.act_construire_merveille, cst.act_vendre]:
            screen.blit(self.buttons[act_name].surface_screen, self.pos-dims_zoomed/2+self.buttons[act_name].pos)
            self.buttons[act_name].pos = self.pos-dims_zoomed/2+self.buttons[act_name].pos
            self.buttons[act_name].rect = self.buttons[act_name].surface_screen.get_rect(topleft=self.buttons[act_name].pos)
            self.buttons[act_name].masque = pg.mask.from_surface(self.buttons[act_name].surface_screen)

    def do_hover_boutons(self, screen):
        for act_name in self.buttons:
            if self.buttons[act_name].hovered:
                screen.blit(self.buttons[act_name].surface_screen, self.buttons[act_name].pos-np.array([1, 1]))

    def do_click_boutons(self, screen):
        for act_name in self.buttons:
            if self.buttons[act_name].is_clicked:
                txt = cst.font.render(act_name, False, (255, 0, 255))
                screen.blit(txt, (100, 100))
                return self.buttons[act_name].action

class Merveille:
    def __init__(self):
        self.nombre_etages = None
        self.nom = None
        self.effet = None
        self.etages = list()

        self.surface = None
        self.surface_screen = None
        self.masque = None

    def draw(self):
        draw_manual = False

        if not draw_manual:
            decalage_ombre = cst.decalage_ombre
            self.surface = pg.Surface((cst.largeur_merveille+decalage_ombre, cst.hauteur_merveille+decalage_ombre), pg.SRCALPHA, 32)
            pg.draw.rect(self.surface, (0,0,0,130), pg.Rect(decalage_ombre, decalage_ombre, cst.largeur_merveille, cst.hauteur_merveille), border_radius=int(0.55*cst.border_radius))

            img = pg.image.load(f"Images/Cartes/Merveilles/{self.nom.replace('-', '_').capitalize()}_étiré.png").convert_alpha()
            img = pg.transform.smoothscale(img, (cst.largeur_merveille, cst.hauteur_merveille))
            self.surface.blit(img, (0,0))

        else:
            color = pg.Color(pg.Color("gray"))

            self.surface = pg.Surface((cst.largeur_merveille, cst.hauteur_merveille), pg.SRCALPHA, 32)

            pg.draw.rect(self.surface, color, pg.Rect(0, 0, cst.largeur_merveille, cst.hauteur_carte), border_radius=cst.border_radius)
            pg.draw.rect(self.surface, pg.Color("black"), pg.Rect(0, 0, cst.largeur_merveille, cst.hauteur_carte), int(3*cst.scale_cartes/30), border_radius=cst.border_radius)

        self.prop_hauteur_rect_or = 0.4
        self.nb_infos = 3
        img_argent = pg.transform.smoothscale(cst.images["argent"], np.array(cst.images["argent"].get_size())*8*self.prop_hauteur_rect_or)
        img_militaire = pg.transform.smoothscale(cst.images["militaire"], np.array(cst.images["militaire"].get_size())*8*self.prop_hauteur_rect_or)
        img_points = pg.transform.smoothscale(cst.images["points"], np.array(cst.images["points"].get_size())*8*self.prop_hauteur_rect_or)

        cote_carre = cst.hauteur_merveille*self.prop_hauteur_rect_or
        pg.draw.rect(self.surface, (210, 210, 210), pg.Rect(cst.largeur_merveille-cote_carre*self.nb_infos, 0, cote_carre*self.nb_infos, cote_carre), border_bottom_left_radius=cst.border_radius)
        pg.draw.rect(self.surface, (0,0,0), pg.Rect(cst.largeur_merveille-cote_carre*self.nb_infos, 0, cote_carre*self.nb_infos, cote_carre), 4, border_bottom_left_radius=cst.border_radius)

        centre_piece = np.array((cst.largeur_merveille-cote_carre*(1/2), cote_carre/2))
        centre_militaire = np.array((cst.largeur_merveille-cote_carre*(1+1/2), cote_carre/2))
        centre_points = np.array((cst.largeur_merveille-cote_carre*(2+1/2), cote_carre/2))
        pos_argent = centre_piece-np.array(img_argent.get_size())/2
        pos_militaire = centre_militaire-np.array(img_militaire.get_size())/2
        pos_points = centre_points-np.array(img_points.get_size())/2

        self.surface.blit(img_argent, pos_argent)
        self.surface.blit(img_militaire, pos_militaire)
        self.surface.blit(img_points, pos_points)
        self.surface_avec_infos = None

    def draw_infos(self, joueur, unzoom):
        largeur_merveille, hauteur_merveille = cst.largeur_merveille*unzoom, cst.hauteur_merveille*unzoom

        self.surface_avec_infos = pg.Surface((largeur_merveille, hauteur_merveille), pg.SRCALPHA, 32)
        self.surface_avec_infos.fill((0,0,0,0))
        cote_carre = hauteur_merveille*self.prop_hauteur_rect_or

        joueur.decompte_points()
        nb_or_text = cst.font_infos.render(f"{joueur.tresor}", True, (0,0,0))
        nb_militaire_text = cst.font_infos.render(f"{joueur.cite.puissance_militaire}", True, (0,0,0))
        nb_points_text = cst.font_infos.render(f"{joueur.points_total}", True, (0,0,0))


        centre_piece = np.array((largeur_merveille-cote_carre*(1/2), cote_carre/2))
        centre_militaire = np.array((largeur_merveille-cote_carre*(1+1/2), cote_carre/2))
        centre_points = np.array((largeur_merveille-cote_carre*(2+1/2), cote_carre/2))
        pos_txt_or = centre_piece-np.array(nb_or_text.get_size())/2
        pos_txt_militaire = centre_militaire-np.array(nb_militaire_text.get_size())/2
        pos_txt_points = centre_points-np.array(nb_points_text.get_size())/2

        self.surface_avec_infos.blit(nb_or_text, pos_txt_or)
        self.surface_avec_infos.blit(nb_militaire_text, pos_txt_militaire)
        self.surface_avec_infos.blit(nb_points_text, pos_txt_points)

class Etage:
    def __init__(self, nom_merveille=None, numero=None):
        self.nom = nom_merveille
        self.cout_ressource = {cst.bois: 0, cst.argile: 0, cst.pierre: 0, cst.fer: 0, cst.tissu: 0, cst.verre: 0, cst.parchemin: 0, cst.argent: 0}
        self.effet = None
        self.numero = numero

        self.done = False
        self.rendered = False

        self.surface = None
        self.surface_screen = None
        self.surface_screen_zoomed = None
        self.masque = None
        self.rect = None
        self.pos = None
        self.hovered = False
        self.unzoom = 1
        self.is_clicked = False
        
    def draw(self):
        draw_manual = False
        prop_hauteur_etage = cst.prop_hauteur_etage

        if not draw_manual:
            self.surface = pg.image.load(f"Images/Cartes/Merveilles/{self.nom.replace('-', '_').capitalize()}_{self.numero}.png").convert_alpha()
            self.surface = pg.transform.smoothscale(self.surface, (cst.largeur_carte, (cst.hauteur_carte)*prop_hauteur_etage))

        else:
            self.surface = pg.Surface((cst.largeur_carte, (cst.hauteur_carte)*prop_hauteur_etage), pg.SRCALPHA, 32)
            pg.draw.rect(self.surface, pg.Color(pg.Color("white")), pg.Rect(0, 0, cst.largeur_carte, (cst.hauteur_carte)*prop_hauteur_etage), border_top_left_radius=cst.border_radius, border_top_right_radius=cst.border_radius)
            pg.draw.rect(self.surface, pg.Color(pg.Color("black")), pg.Rect(0, 0, cst.largeur_carte, (cst.hauteur_carte)*prop_hauteur_etage), int(3*cst.scale_cartes/30), border_top_left_radius=cst.border_radius, border_top_right_radius=cst.border_radius)

        if not self.done:
            self.surface_shaded = shaded_image(self.surface, (0,0,0,170))
            self.surface.blit(self.surface_shaded, (0, 0))

    def check_hover(self):
        pos = pg.mouse.get_pos()
        change = set()
        if self.rect is not None and self.masque is not None:
            pos_in_mask = pos[0] - self.pos[0], pos[1] - self.pos[1]
            if self.rect.collidepoint(*pos):
                if self.masque.get_at(pos_in_mask):
                    if not self.hovered: change.add(cst.change_etage)
                    self.hovered = True

                else:
                    if self.hovered: change.add(cst.change_etage)
                    self.hovered = False
            else:
                if self.hovered: change.add(cst.change_etage)
                self.hovered = False

        return change

    def zoom(self, screen):
        dims = np.array([self.surface_screen_zoomed.get_width(), self.surface_screen_zoomed.get_height()])*cst.zoom_carte*self.unzoom
        dims_base = np.array([self.surface_screen.get_width(), self.surface_screen.get_height()])

        if self.surface_screen_zoomed is not None:
            toblit = self.surface_screen_zoomed.copy()
            if not self.done:
                toblit.blit(self.surface_screen_zoomed, (0, 0))
            screen.blit(pg.transform.rotozoom(toblit, 0, cst.zoom_carte*self.unzoom), self.pos-dims/2+dims_base/2)

    def clicked(self, screen, shade=True):
        dims = np.array([self.surface_screen_zoomed.get_width(), self.surface_screen_zoomed.get_height()])*cst.zoom_carte*self.unzoom
        dims_base = np.array([self.surface_screen.get_width(), self.surface_screen.get_height()])

        toblit = self.surface_screen_zoomed.copy()
        if not self.done:
            toblit.blit(self.surface_screen_zoomed, (0, 0))
        screen.blit(pg.transform.rotozoom(toblit, 0, cst.zoom_carte*self.unzoom), self.pos-dims/2+dims_base/2)

        if self.surface_screen_zoomed is not None and shade:
            self.surface_shaded = shaded_image(self.surface_screen_zoomed, (0,0,0,128))
            screen.blit(pg.transform.rotozoom(self.surface_shaded, 0, cst.zoom_carte*self.unzoom), self.pos-dims/2+dims_base/2)

class Effet:
    def __init__(self):
        self.effet_militaire = None
        self.effet_symbole_scientifique = dict()
        self.effet_points_victoire = None
        self.symbole_chainage = list()

        self.effet_tresor = None
        self.effet_production = dict()
        self.achetable = True

        self.effet_reduction_gauche_base = None
        self.effet_reduction_droite_base = None
        self.effet_reduction_gauche_manufacture = None
        self.effet_reduction_droite_manufacture = None

        self.effet_gain_or_cartes_grises = [None, None, None]  # Gauche, Soi, Droite
        self.effet_gain_or_cartes_marron = [None, None, None]
        self.effet_gain_or_cartes_jaunes = [None, None, None]
        self.effet_gain_or_cartes_rouges = [None, None, None]
        self.effet_gain_or_etages = [None, None, None]
        self.effet_gain_points_cartes_grises = [None, None, None]
        self.effet_gain_points_cartes_marron = [None, None, None]
        self.effet_gain_points_cartes_jaunes = [None, None, None]
        self.effet_gain_points_cartes_rouges = [None, None, None]
        self.effet_gain_points_cartes_bleues = [None, None, None]
        self.effet_gain_points_cartes_vertes = [None, None, None]
        self.effet_gain_points_cartes_violettes = [None, None, None]
        self.effet_gain_points_etages = [None, None, None]
        self.effet_gain_points_cartes_merveille_complete = False

        self.carte_defausse = None
        self.jouer_derniere_carte = None
        self.premiere_carte_age_gratuite = None
        self.derniere_carte_age_gratuite = None
        self.premiere_carte_couleur_gratuite = None








