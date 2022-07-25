from game import *
import cartes
import matplotlib.pyplot as plt
import numpy as np
from itertools import product
import pprofile
import pygame as pg
pg.font.init()
import sys
import time
from GUI import Renderer

class Jeu:
    def __init__(self, nombre_joueurs, cartes, merveilles, auto=True, init_window=True):
        # Jeu
        self.cartes = cartes
        self.merveilles = merveilles
        self.joueurs = []
        self.defausse = list()
        self.nombre_joueurs = nombre_joueurs
        self.points_militaire = {1: 1, 2: 3, 3: 5}
        self.scores = list()
        self.scores_detail = list()
        self.tour = 1
        self.age = 1
        self.game_ended = False
        self.dernier_tour = len([carte for carte in self.cartes if carte.age == 1 and carte.nb_joueurs <= self.nombre_joueurs])//self.nombre_joueurs - 1

        self.auto = auto
        self.time_wait = 0.1 #s

        idx_merveille = np.random.choice(list(range(7)), nombre_joueurs, replace=False)*2
        idx_jour_nuit = np.random.choice([0,1], nombre_joueurs, replace=True)
        idx_merveille += idx_jour_nuit
        idx_merveille[0] = 10  # TODO ENLEVER =================================================================================
        merveilles = [merveilles[idx] for idx in idx_merveille]

        for i in range(nombre_joueurs):
            joueur = Joueur(i, main = [], merveille = merveilles[i], tresor=3)
            joueur.appliquer_effets(merveilles[i].effet, self, cst.merveille)
            if i==0: joueur.voisin_gauche = nombre_joueurs-1
            if i==nombre_joueurs-1: joueur.voisin_droite = 0

            self.joueurs.append(joueur)

        # GUI
        self.GUI = True
        if self.GUI and init_window:
            self.renderer = Renderer(self)


    def get_cartes(self):
        cartes_age = [carte for carte in self.cartes if carte.age == self.age and carte.nb_joueurs <= self.nombre_joueurs]
        if self.age == 3:
            cartes_guilde = [carte for carte in self.cartes if carte.age == self.age and carte.couleur == cst.violet]
            cartes_guildes_a_virer = np.random.choice(cartes_guilde, 10-self.nombre_joueurs-2, replace=False)
            for carte_a_virer in cartes_guildes_a_virer:
                cartes_age.remove(carte_a_virer)
        np.random.shuffle(cartes_age)
        return cartes_age

    def conflits_militaires(self):
        for joueur in self.joueurs:
            if joueur.cite.puissance_militaire > self.joueurs[joueur.voisin_gauche].cite.puissance_militaire:
                joueur.points[cst.militaire] += self.points_militaire[self.age]
            elif joueur.cite.puissance_militaire < self.joueurs[joueur.voisin_gauche].cite.puissance_militaire:
                joueur.points[cst.militaire] += -1
            if joueur.cite.puissance_militaire > self.joueurs[joueur.voisin_droite].cite.puissance_militaire:
                joueur.points[cst.militaire] += self.points_militaire[self.age]
            elif joueur.cite.puissance_militaire < self.joueurs[joueur.voisin_droite].cite.puissance_militaire:
                joueur.points[cst.militaire] += -1

    def comptage_points(self):
        for joueur in self.joueurs:
            joueur.points[cst.argent] = joueur.tresor//3

            combinaisons = list(product(*joueur.cite.symboles_scientifiques))
            arr_pts = [0]
            for sequence in combinaisons:
                if len(sequence)==0:
                    continue
                pts_temp = 0
                un, cnt = np.unique(sequence, return_counts=True)
                pts_temp += np.sum(cnt**2)
                if len(un)==3:
                    pts_temp += np.min(cnt)*7
                arr_pts.append(pts_temp)
            joueur.points[cst.vert] = np.max(arr_pts)

            joueur.decompte_points()


        for joueur in self.joueurs:
            self.scores.append(joueur.points_total)
            self.scores_detail.append(joueur.points)

    def run_tour(self, action_saisie = None):
        actions_joueurs = []
        for i, joueur in enumerate(self.joueurs):
            assert len(joueur.main) == self.dernier_tour+1-self.tour+1

            if i != 0 or action_saisie is None:
                actions = joueur.actions_possibles(self)

                idx = np.random.choice(len(actions))
                action_choisie = actions[idx]
                actions_joueurs.append(action_choisie)
            else:
                actions_joueurs.append(action_saisie)

        for i_joueur, (joueur, action_choisie) in enumerate(zip(self.joueurs, actions_joueurs)):
            act, cible, cout = action_choisie
            extra_action = joueur.acte(act, cible, cout, self)
            print(extra_action, self.GUI, self.auto, i_joueur, joueur.id, joueur.cite.carte_defausse)

            if cst.carte_defausse in extra_action:
                # actions = []
                # for carte in self.defausse:
                #     actions.append((cst.act_construire_batiment, carte, 0))
                # idx = np.random.choice(len(actions))
                # act, cible, cout = actions[idx]
                # joueur.main.append(cible)
                # joueur.acte(act, cible, cout, self)

                if self.GUI and not self.auto and i_joueur == 0:
                    size_screen = self.renderer.screen.get_size()
                    props = np.array([cst.prop_largeur_choix_defausse, cst.prop_hauteur_choix_defausse])
                    marges = size_screen-(size_screen-props*size_screen)/2
                    pg.draw.rect(self.renderer.screen, (0,0,0,128), (marges[0], marges[1], *size_screen*props))
                    print("PROUT")
                    time.sleep(10)


            if cst.jouer_derniere_carte in extra_action:
                assert len(joueur.main)==1

                actions = joueur.actions_possibles(self)

                idx = np.random.choice(len(actions))
                act, cible, cout = actions[idx]
                joueur.acte(act, cible, cout, self)

        if self.age == 1 or self.age == 3:
            main_temp = self.joueurs[0].main
            for joueur in self.joueurs[1:]:
                self.joueurs[joueur.voisin_gauche].main = joueur.main
            self.joueurs[-1].main = main_temp
        if self.age == 2:
            main_temp = self.joueurs[-1].main
            for joueur in reversed(self.joueurs[:-1]):
                self.joueurs[joueur.voisin_droite].main = joueur.main
            self.joueurs[0].main = main_temp

    def init_age(self):
        if self.tour == 1:
            cartes_age = self.get_cartes()

            mains = np.array_split(cartes_age, self.nombre_joueurs)
            for i, joueur in enumerate(self.joueurs):
                joueur.main = list(mains[i])

    def run_round(self, action=None):
        self.run_tour(action)

        self.tour += 1

        # Fin âge
        if len(self.joueurs[0].main)<=1:
            self.conflits_militaires()
            self.age += 1
            self.tour = 1
            self.init_age()

        # Fin partie
        if self.age == 4:
            self.comptage_points()
            self.game_ended = True
            if self.GUI:
                self.renderer.end_game()

    def reset(self):
        self.__init__(self.nombre_joueurs, self.cartes, self.merveilles, auto=self.auto, init_window=False)

    def hover(self, changes):
        for joueur in self.joueurs:
            for carte in reversed(joueur.main+joueur.cite.batiments):
                change_state = carte.check_hover()
                for change in change_state: changes.add(change)

            for etage in joueur.merveille.etages:
                change_state = etage.check_hover()
                for change in change_state: changes.add(change)

        return changes


    def do_hover(self):
        one_card_hovered = False
        for joueur in self.joueurs:
            for carte in reversed(joueur.main+joueur.cite.batiments):
                if carte.hovered:
                    if not one_card_hovered:
                        carte.zoom(self.renderer.screen)
                        one_card_hovered = True

            for etage in joueur.merveille.etages:
                if etage.hovered:
                    etage.zoom(self.renderer.screen)
        return one_card_hovered

    def click(self, changes):
        for joueur in self.joueurs:
            for carte in reversed(joueur.main+joueur.cite.batiments):
                change_state = carte.check_hover()

                if carte.is_clicked:
                    for act in carte.buttons:
                        if carte.buttons[act].hovered is not None:
                            if carte.buttons[act].hovered:
                                if not carte.buttons[act].is_clicked: changes.add(cst.click_bouton)
                                carte.buttons[act].is_clicked = True
                            else:
                                if carte.buttons[act].is_clicked: changes.add(cst.click_bouton)
                                carte.buttons[act].is_clicked = False

                if carte.hovered:
                    if not carte.is_clicked:
                        changes.add(cst.click_carte)
                    carte.is_clicked = True
                else:
                    if carte.is_clicked: changes.add(cst.click_carte)
                    carte.is_clicked = False



            for etage in joueur.merveille.etages:
                change_state = etage.check_hover()
                if etage.hovered:
                    if not etage.is_clicked: changes.add(cst.click_etage)
                    etage.is_clicked = True
                else:
                    if etage.is_clicked: changes.add(cst.click_etage)
                    etage.is_clicked = False


        return changes

    def do_click(self):
        card_clicked, objet = False, None
        for joueur in self.joueurs:
            for carte in reversed(joueur.main+joueur.cite.batiments):
                if carte.is_clicked:
                    card_clicked, objet = "card-clicked", carte

                for act in carte.buttons:
                    if carte.buttons[act].is_clicked:
                        card_clicked, objet = "card-and-button-clicked", carte.buttons[act]
                        return card_clicked, carte

            for etage in joueur.merveille.etages:
                if etage.is_clicked:
                    card_clicked, objet = "etage-clicked", etage

        return card_clicked, objet

    def draw_all(self):
        for carte in self.cartes:
            carte.draw()
        for merveille in self.merveilles:
            merveille.draw()
            for etage in merveille.etages:
                etage.draw()


    def run_game(self):
        running = True
        self.game_ended = False
        last = 0
        play_round = False
        click = False
        do_flip = True
        action = None

        self.init_age()
        for joueur in self.joueurs:
            joueur.actions_possibles(self)
        if self.GUI:
            self.draw_all()
            self.renderer.render()

        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RIGHT:
                        play_round = True
                if event.type == pg.MOUSEBUTTONUP:
                    if event.button == 1:
                        click = True


            if self.auto:
                now = time.time()
                if now - last >= self.time_wait:
                    last = now
                    self.run_round()

                    if self.GUI:
                        self.renderer.render()
                        self.renderer.clean()
                        do_flip = True


            else:
                changes = set()
                change = self.hover(changes)

                if click:
                    change = self.click(changes)
                    click = False

                if len(change) > 0:
                    #print(change)
                    self.renderer.render()

                    card_hovered = self.do_hover()
                    out, objet = self.do_click()
                    if out=="card-clicked" and objet is not None:
                        if objet in self.joueurs[0].main: shade = True
                        else: shade = False
                        objet.clicked(self.renderer.screen, shade)
                        if objet in self.joueurs[0].main:
                            self.joueurs[0].actions_possibles(self)
                            objet.update_buttons(self.joueurs[0].liste_actions_possibles)
                            objet.blit_buttons(self.renderer.screen)
                            objet.do_hover_boutons(self.renderer.screen)
                    elif out=="card-and-button-clicked" and objet is not None:
                        action = objet.do_click_boutons(self.renderer.screen)
                        play_round = True
                    elif out=="etage-clicked" and objet is not None:
                        objet.clicked(self.renderer.screen, shade=False)

                    do_flip = True

                if play_round:
                    self.run_round(action)

                    play_round = False

                    if self.GUI:
                        self.renderer.render()
                        self.renderer.clean()
                        do_flip = True


            if do_flip:
                pg.display.flip()
                do_flip = False

            if self.game_ended:
                running = False



jeu = Jeu(7, cartes.paquet_cartes, cartes.merveilles, auto=False)
arr_scores = []

# Profiler = pprofile.Profile()
# with Profiler:
for i in range(10):
    print("Jeu", i)
    jeu.run_game()

    scores = jeu.scores
    for s in scores:
        arr_scores.append(s)

    jeu.reset()

pg.quit()
# Profiler.dump_stats("Benchmark.txt")
# pause()

plt.hist(arr_scores, bins=20)
plt.show()

pause()

arr_scores = []
for i in range(100):
    print("Jeu", i)
    jeu = Jeu(4, cartes.paquet_cartes, cartes.merveilles, auto=True)
    jeu.run()
    scores = jeu.scores
    for s in scores:
        arr_scores.append(s)

plt.hist(arr_scores, bins=20)
plt.show()