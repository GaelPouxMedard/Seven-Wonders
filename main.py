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
from copy import deepcopy as copy

class Jeu:
    def __init__(self, nombre_joueurs, cartes, merveilles, auto=True, GUI=True):
        # Jeu
        self.cartes = copy(cartes)
        self.merveilles = copy(merveilles)
        self.joueurs = []
        self.defausse = list()
        self.nombre_joueurs = nombre_joueurs
        self.points_militaire = {1: 1, 2: 3, 3: 5}
        self.scores = list()
        self.scores_detail = list()
        self.tour = 1
        self.age = 1
        self.game_ended = False
        self.dernier_tour = 6  #len([carte for carte in cartes if carte.age == 1 and carte.nb_joueurs <= self.nombre_joueurs])//self.nombre_joueurs - 1

        self.auto = auto
        self.time_wait = 0.000001 #s

        # GUI
        self.GUI = GUI
        if self.GUI:
            self.renderer = Renderer(self)
            self.draw_all()

    def init_partie(self):
        idx_merveille = np.random.choice(list(range(7)), self.nombre_joueurs, replace=False)*2
        idx_jour_nuit = np.random.choice([0,1], self.nombre_joueurs, replace=True)
        idx_merveille += idx_jour_nuit
        merveilles = [self.merveilles[idx] for idx in idx_merveille]

        for i in range(self.nombre_joueurs):
            joueur = Joueur(i, main = [], merveille = merveilles[i], tresor=3)
            joueur.appliquer_effets(merveilles[i].effet, self, cst.merveille)
            if i==0: joueur.voisin_gauche = self.nombre_joueurs-1
            if i==self.nombre_joueurs-1: joueur.voisin_droite = 0

            self.joueurs.append(joueur)
        self.init_age()

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
            assert (len(joueur.main) == self.dernier_tour+1-self.tour+1) or (len(joueur.main) == 1 and joueur.cite.jouer_derniere_carte)

            if i != 0 or action_saisie is None:
                actions = joueur.actions_possibles(self)

                idx = np.random.choice(len(actions))
                action_choisie = actions[idx]
                actions_joueurs.append(action_choisie)
            else:
                actions_joueurs.append(action_saisie)

        extra_actions = []
        for i_joueur, (joueur, action_choisie) in enumerate(zip(self.joueurs, actions_joueurs)):
            act, cible, cout = action_choisie
            extra_action = joueur.acte(act, cible, cout, self)
            extra_actions.append(extra_action)

        for i_joueur, (joueur, extra_action) in enumerate(zip(self.joueurs, extra_actions)):
            if cst.carte_defausse in extra_action and len(self.defausse)>=1:
                if self.GUI and not self.auto and joueur.id == 0:
                    size_screen = self.renderer.screen.get_size()
                    props = np.array([cst.prop_largeur_choix_defausse, cst.prop_hauteur_choix_defausse])
                    marges = (size_screen-props*size_screen)/2
                    largeur_carte = (size_screen[0])/16
                    hauteur_carte = largeur_carte*cst.hauteur_carte/cst.largeur_carte
                    surface_fond = pg.Surface(size_screen, pg.SRCALPHA, 32)
                    pg.draw.rect(surface_fond, (0,0,0,128), pg.Rect(*marges, *size_screen*props), border_radius=cst.border_radius)
                    self.renderer.screen.blit(surface_fond, (0,0))
                    surface_fond = self.renderer.screen.copy()
                    i_large, i_haut = -1, -1
                    for i, carte in enumerate(self.defausse):
                        i_large += 1
                        if i%15==0:
                            i_haut += 1
                            i_large = 0
                        carte.pos = np.array([(i_large)*largeur_carte, marges[0] + i_haut*hauteur_carte])-np.array([-largeur_carte, 0])/2
                        carte.unzoom = 1./cst.zoom_carte
                        carte.is_clicked = False
                        #carte.surface = pg.transform.smoothscale(carte.surface, (largeur_carte, hauteur_carte))
                        carte.surface_screen = pg.transform.smoothscale(carte.surface, (largeur_carte, hauteur_carte))
                        carte.surface_screen_zoomed = pg.transform.smoothscale(carte.surface, (largeur_carte*1.3, hauteur_carte*1.3))
                        surface_fond.blit(carte.surface_screen, carte.pos)
                        carte.rect = carte.surface_screen.get_rect(topleft=carte.pos)
                        carte.masque = pg.mask.from_surface(carte.surface_screen)
                    self.renderer.screen.blit(surface_fond, (0,0))
                    self.flip()

                    click = False
                    while True:
                        event = pg.event.wait()
                        if event.type == pg.QUIT:
                            pg.quit()
                            sys.exit()
                        if event.type == pg.MOUSEBUTTONUP:
                            if event.button == 1:
                                click = True

                        changes = set()
                        changes = self.hover(changes, defausse=True)

                        if click:
                            changes = self.click(changes, defausse=True)
                            click = False
                        if len(changes) > 0:
                            self.renderer.screen.blit(surface_fond, (0,0))

                            card_hovered = self.do_hover(defausse=True)
                            out, objet = self.do_click(defausse=True)
                            if out=="card-clicked" and objet is not None:
                                if objet in self.defausse:
                                    act, cible, cout = (cst.act_construire_batiment, objet, 0)
                                    self.defausse.remove(cible)
                                    joueur.main.append(cible)
                                    joueur.acte(act, cible, cout, self)
                                    break

                            self.flip()

                else:
                    actions = []
                    for carte in self.defausse:
                        actions.append((cst.act_construire_batiment, carte, 0))
                    idx = np.random.choice(len(actions))
                    act, cible, cout = actions[idx]
                    joueur.main.append(cible)
                    self.defausse.remove(cible)
                    joueur.acte(act, cible, cout, self)

            if cst.jouer_derniere_carte in extra_action:
                assert len(joueur.main)==1

                auto_temp = False
                if self.GUI and not self.auto and joueur.id == 0:
                    action = None
                    click = False
                    do_flip = False
                    play_round = False
                    self.renderer.render()
                    self.renderer.clean()
                    self.flip()

                    while True:
                        events = [pg.event.wait()]
                        for event in events:
                            if event.type == pg.QUIT:
                                pg.quit()
                                sys.exit()
                            if event.type == pg.KEYDOWN:
                                if event.key == pg.K_RIGHT:
                                    auto_temp = True
                                    break
                            if event.type == pg.MOUSEBUTTONUP:
                                if event.button == 1:
                                    click = True
                        if auto_temp: break

                        changes = set()
                        change = self.hover(changes)
                        if click:
                            change = self.click(changes)
                            click = False

                        if len(change) > 0:
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
                            act, cible, cout = action
                            joueur.acte(act, cible, cout, self)
                            break

                        if do_flip:
                            self.flip()
                            do_flip = False

                if not (self.GUI and not self.auto and joueur.id == 0) or auto_temp:
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
            if self.age == 1:
                self.reset()
            cartes_age = self.get_cartes()

            mains = np.array_split(cartes_age, self.nombre_joueurs)
            for i, joueur in enumerate(self.joueurs):
                joueur.main = list(mains[i])

    def run_round(self, action=None):
        self.run_tour(action)

        self.tour += 1

        # Fin âge
        if len(self.joueurs[0].main)<=1:
            for joueur in self.joueurs:
                for carte in joueur.main:
                    self.defausse.append(carte)
                    joueur.main.remove(carte)
            self.conflits_militaires()

            self.age += 1
            self.tour = 1
            self.init_age()

        # Fin partie
        if self.age == 4:
            self.comptage_points()
            self.game_ended = True
            if self.GUI and not self.auto:
                choix = self.renderer.end_game(self)
                if choix == "Menu":
                    self.nombre_joueurs = self.renderer.menu()

    def reset(self):
        self.joueurs = []
        self.defausse = list()
        self.scores = list()
        self.scores_detail = list()
        self.tour = 1
        self.age = 1
        self.game_ended = False

        if self.GUI:
            for carte in self.cartes:
                carte.construite = False
                carte.rendered_cite = False
                carte.rendered_main = False
            for merveille in self.merveilles:
                merveille.surface_screen = None
                for etage in merveille.etages:
                    etage.done = False
                    etage.rendered = False
                    etage.draw()
                    etage.surface_screen = None


        idx_merveille = np.random.choice(list(range(7)), self.nombre_joueurs, replace=False)*2
        idx_jour_nuit = np.random.choice([0,1], self.nombre_joueurs, replace=True)
        idx_merveille += idx_jour_nuit
        merveilles = [self.merveilles[idx] for idx in idx_merveille]

        for i in range(self.nombre_joueurs):
            joueur = Joueur(i, main = [], merveille = merveilles[i], tresor=3)
            joueur.appliquer_effets(merveilles[i].effet, self, cst.merveille)
            if i==0: joueur.voisin_gauche = self.nombre_joueurs-1
            if i==self.nombre_joueurs-1: joueur.voisin_droite = 0

            self.joueurs.append(joueur)

    def hover(self, changes, defausse=False):
        if not defausse:
            for joueur in self.joueurs:
                for carte in reversed(joueur.main+joueur.cite.batiments):
                    change_state = carte.check_hover()
                    for change in change_state: changes.add(change)

                for etage in joueur.merveille.etages:
                    change_state = etage.check_hover()
                    for change in change_state: changes.add(change)
        else:
            for carte in reversed(self.defausse):
                change_state = carte.check_hover()
                for change in change_state: changes.add(change)

        return changes

    def do_hover(self, defausse = False):
        one_card_hovered = False
        if not defausse:
            for joueur in self.joueurs:
                for carte in reversed(joueur.main+joueur.cite.batiments):
                    if carte.hovered:
                        if not one_card_hovered:
                            carte.zoom(self.renderer.screen)
                            one_card_hovered = True

                for etage in joueur.merveille.etages:
                    if etage.hovered:
                        etage.zoom(self.renderer.screen)
        else:
            for carte in reversed(self.defausse):
                if carte.hovered:
                    if not one_card_hovered:
                        carte.zoom(self.renderer.screen)
                        one_card_hovered = True

        return one_card_hovered

    def click(self, changes, defausse = False):
        if not defausse:
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

        else:
            for carte in self.defausse:
                if carte.hovered:
                    if not carte.is_clicked:
                        changes.add(cst.click_carte)
                    carte.is_clicked = True
                else:
                    if carte.is_clicked: changes.add(cst.click_carte)
                    carte.is_clicked = False


        return changes

    def do_click(self, defausse = False):
        card_clicked, objet = False, None
        if not defausse:
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
        else:
            for carte in self.defausse:
                if carte.is_clicked:
                    card_clicked, objet = "card-clicked", carte

                for act in carte.buttons:
                    if carte.buttons[act].is_clicked:
                        card_clicked, objet = "card-and-button-clicked", carte.buttons[act]
                        return card_clicked, carte


        return card_clicked, objet

    def draw_all(self):
        for carte in self.cartes:
            carte.draw()
        for merveille in self.merveilles:
            merveille.draw()
            for etage in merveille.etages:
                etage.draw()

    def flip(self):
        # toblit = pg.transform.scale(self.renderer.screen, pg.display.get_surface().get_size())
        # self.renderer.window.blit(toblit, (0,0))
        pg.display.flip()

    def run_game(self):
        self.reset()
        running = True
        self.game_ended = False
        last = 0
        play_round = False
        auto_temp = False
        click = False
        do_flip = True
        action = None

        self.init_partie()

        for joueur in self.joueurs:
            joueur.actions_possibles(self)
        if self.GUI:
            self.renderer.render()

        while running:
            if self.GUI:
                if not self.auto:
                    events = [pg.event.wait()]
                else:
                    events = pg.event.get()
                for event in events:
                    if event.type == pg.QUIT:
                        pg.quit()
                        sys.exit()
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_RIGHT:
                            self.auto = True
                            auto_temp = True
                    if event.type == pg.MOUSEBUTTONUP:
                        if event.button == 1:
                            click = True


            if self.auto:
                if auto_temp:
                    self.auto = False
                    auto_temp = False
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


            if do_flip and self.GUI:
                self.flip()
                do_flip = False

            if self.game_ended:
                running = False

    def run(self, nombre_runs=10000000):
        for i in range(nombre_runs):
            print("Jeu", i)
            jeu.run_game()
            jeu.reset()
        pg.quit()



jeu = Jeu(7, cartes.paquet_cartes, cartes.merveilles, auto=False, GUI=True)
arr_scores = []

# Profiler = pprofile.Profile()
# with Profiler:
jeu.run(nombre_runs=100)
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