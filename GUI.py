import numpy as np
import sys, ctypes
import pygame as pg
import constantes as cst
from utils import *

class Renderer():
    def __init__(self, jeu):
        self.jeu = jeu
        pg.init()
        self.screen = pg.display.set_mode((0, 0))#, pg.RESIZABLE)
        if sys.platform == "win32":
            HWND = pg.display.get_wm_info()['window']
            SW_MAXIMIZE = 3
            ctypes.windll.user32.ShowWindow(HWND, SW_MAXIMIZE)

        self.background = pg.transform.smoothscale(pg.image.load("Images/Background.jpg"), np.array(pg.display.get_surface().get_size()))
        self.background = pg.transform.smoothscale(pg.image.load("Images/Table.jpg"), np.array(pg.display.get_surface().get_size()))
        self.init_background()

    def init_background(self):
        self.screen.blit(self.background, (0, 0))
        bouton_quit = BoutonQuit(self.screen)
        bouton_quit.draw()
        self.screen.blit(bouton_quit.surface, bouton_quit.pos)
        #self.screen.fill((255,255,255))

    def rotation_matrix(self, angle, a=1, b=1):
        mat = [[a*np.cos(angle), a*np.sin(angle)], [-b*np.sin(angle), b*np.cos(angle)]]
        return np.array(mat)

    def calcul_angle_rotation_plateau(self, angle, excentricite):
        phase = np.pi/2
        theta = np.arctan(excentricite * np.tan(angle)) + phase
        angle_rot_plateau = np.arctan(excentricite**2 * np.tan(theta)) + np.pi/2
        if 0==angle:
            angle_rot_plateau = angle_rot_plateau+np.pi
        if 0<(angle)<=np.pi/2:
            angle_rot_plateau = angle_rot_plateau
        if np.pi/2<(angle)<=np.pi/2:
            angle_rot_plateau = np.pi/2+angle_rot_plateau
        if np.pi<(angle)<=3*np.pi/2:
            angle_rot_plateau = angle_rot_plateau - np.pi
        if 3*np.pi/2<(angle)<=2*np.pi:
            angle_rot_plateau = 2*np.pi+angle_rot_plateau - np.pi
        return angle_rot_plateau

    def distances_plateaux(self):
        excentricite, eloignement_facteur, zoom_facteur, angles_pos, fac_player = 0., 0., 0., None, 0.00025
        if self.jeu.nombre_joueurs==3:
            excentricite = 1.*self.screen.get_width()/self.screen.get_height()
            eloignement_facteur = 2.
            zoom_facteur = 0.8
            fac_player *= 1.
        elif self.jeu.nombre_joueurs==4:
            excentricite = 1.05*self.screen.get_width()/self.screen.get_height()
            eloignement_facteur = 1.8
            zoom_facteur = 0.8
            fac_player *= 1.1
        elif self.jeu.nombre_joueurs==5:
            excentricite = 1.4*self.screen.get_width()/self.screen.get_height()
            eloignement_facteur = 1.85
            zoom_facteur = 0.65
            angles_pos = [0, 50, 160, 200, 310]
            fac_player *= 1.2
        elif self.jeu.nombre_joueurs==6:
            excentricite = 2*self.screen.get_width()/self.screen.get_height()
            eloignement_facteur = 1.75
            zoom_facteur = 0.6
            angles_pos = [0, 35, 145, 180, 215, 325]
            fac_player *= 1.25
        elif self.jeu.nombre_joueurs==7:
            excentricite = 1.5*self.screen.get_width()/self.screen.get_height()
            eloignement_facteur = 1.75
            zoom_facteur = 0.55
            x = 360/7
            angles_pos = [0, 0.85*1*x, 2.58*x, 3.27*x, 3.83*x, 4.57*x, 6.15*x]
            fac_player *= 1.2

        if angles_pos is not None:
            angles_pos = np.array(angles_pos)*np.pi/180

        return excentricite, eloignement_facteur, zoom_facteur, angles_pos, fac_player

    def render(self):
        self.init_background()
        nb_joueurs = self.jeu.nombre_joueurs
        angle_sub = (360/nb_joueurs)*np.pi/180

        excentricite, eloignement_facteur, zoom_facteur, angles_pos, fac_player = self.distances_plateaux()

        centre_screen = np.array([self.screen.get_width()/2, self.screen.get_height()/2])
        R = ((self.screen.get_width()/2)*eloignement_facteur)
        dim_board_base = np.array([cst.largeur_board, cst.hauteur_board])
        unzoom = zoom_facteur*self.screen.get_height()/(cst.hauteur_board*4/3)

        coords_carte = np.array([[-cst.largeur_carte/2,-cst.hauteur_carte/2],  # topleft
                                 [cst.largeur_carte/2,-cst.hauteur_carte/2],  # topright
                                 [-cst.largeur_carte/2,cst.hauteur_carte/2],  # bottomleft
                                 [cst.largeur_carte/2,cst.hauteur_carte/2]  # bottomright
                                 ])*unzoom
        coords_merveille = np.array([[-cst.largeur_merveille/2,-cst.hauteur_merveille/2],  # topleft
                                     [cst.largeur_merveille/2,-cst.hauteur_merveille/2],  # topright
                                     [-cst.largeur_merveille/2,cst.hauteur_merveille/2],  # bottomleft
                                     [cst.largeur_merveille/2,cst.hauteur_merveille/2]  # bottomright
                                     ])*unzoom
        coords_etage = np.array([[-cst.largeur_carte/2,-(cst.hauteur_merveille*cst.prop_hauteur_etage)/2],  # topleft
                                 [cst.largeur_carte/2,-(cst.hauteur_merveille*cst.prop_hauteur_etage)/2],  # topright
                                 [-cst.largeur_carte/2,(cst.hauteur_merveille*cst.prop_hauteur_etage)/2],  # bottomleft
                                 [cst.largeur_carte/2,(cst.hauteur_merveille*cst.prop_hauteur_etage)/2]  # bottomright
                                 ])*unzoom
        cartes_vues = []

        for num_joueur, joueur in enumerate(self.jeu.joueurs):
            dim_board = dim_board_base
            if num_joueur==0:
                dim_board[1] += (cst.hauteur_carte+cst.espace_entre_cartes)
            if angles_pos is not None:
                angle_pos_plateau = angles_pos[num_joueur]
            else:
                angle_pos_plateau = angle_sub*num_joueur

            if num_joueur==0:
                unzoom = np.max([fac_player*self.screen.get_height(), zoom_facteur*self.screen.get_height()/(cst.hauteur_board*4/3)])
            else:
                unzoom = zoom_facteur*self.screen.get_height()/(cst.hauteur_board*4/3)

            angle_rot_plateau = self.calcul_angle_rotation_plateau(angle_pos_plateau, excentricite)

            rot = self.rotation_matrix(angle_rot_plateau)
            dim_board_rot = rot.dot(dim_board)


            position_plateau_ellipse = self.rotation_matrix(angle_pos_plateau, a=excentricite).dot(np.array([0,R*0.20/unzoom]))
            pos_plateau = position_plateau_ellipse
            pos_plateau -= dim_board_rot/2
            pos_plateau_rot = pos_plateau

            debut_cartes = (dim_board[0]-(cst.largeur_carte+cst.espace_entre_cartes)*(len(joueur.main)))/2

            coords_carte_rot = coords_carte.dot(rot.T)
            coords_merveille_rot = coords_merveille.dot(rot.T)
            coords_etage_rot = coords_etage.dot(rot.T)
            pos_centre_carte = (coords_carte[-1]-coords_carte[0])/2
            pos_centre_merveille = (coords_merveille_rot[-1]-coords_merveille_rot[0])/2
            pos_centre_etage = (coords_etage_rot[-1]-coords_etage_rot[0])/2
            shift_topleft_carte = -(coords_carte_rot[0]-np.min(coords_carte_rot, axis=0))
            shift_topleft_merveille = -(coords_merveille_rot[0]-np.min(coords_merveille_rot, axis=0))
            shift_topleft_etage = -(coords_etage_rot[0]-np.min(coords_etage_rot, axis=0))

            # Main
            if num_joueur == 0 or False:
                for num_carte, carte in enumerate(joueur.main):
                    #carte.draw()

                    carte.pos_plateau = np.array([(cst.largeur_carte+cst.espace_entre_cartes)*num_carte+debut_cartes, 0])
                    carte_pos_plateau_rot = rot.dot(carte.pos_plateau)
                    carte.unzoom = unzoom

                    if (not carte.construite and not carte.rendered_main):
                        carte.surface_screen = pg.transform.smoothscale(carte.surface, np.array(carte.surface.get_size())*unzoom)
                        carte.surface_screen_zoomed, _ = rot_center(carte.surface, angle_rot_plateau*180/np.pi, pos_centre_carte)
                        carte.surface_screen, rot_rect = rot_center(carte.surface_screen, angle_rot_plateau*180/np.pi, pos_centre_carte)
                        carte.rendered_main = True

                    carte.pos = centre_screen+(pos_plateau_rot+carte_pos_plateau_rot)*unzoom + shift_topleft_carte
                    cartes_vues.append(carte)
                    self.screen.blit(carte.surface_screen, carte.pos)

            # Cité
            pos_couleur = {couleur: i for i, couleur in enumerate(cst.couleurs)}
            num_couleur = {couleur: 0 for i, couleur in enumerate(cst.couleurs)}
            for num_carte, carte in enumerate(joueur.cite.batiments):
                #carte.draw()

                debut_cartes = (dim_board[0]-(cst.largeur_carte+cst.espace_entre_cartes)*(len(pos_couleur)))/2
                carte.pos_plateau = np.array([pos_couleur[carte.couleur]*(cst.largeur_carte+cst.espace_entre_cartes)+debut_cartes,
                                              num_couleur[carte.couleur]*(cst.propline_sep_carte*cst.hauteur_carte)+2*(cst.hauteur_carte+cst.espace_entre_cartes_vertical)])
                carte_pos_plateau_rot = rot.dot(carte.pos_plateau)


                carte.unzoom = unzoom
                if (carte.construite and not carte.rendered_cite):
                    carte.surface_screen = pg.transform.smoothscale(carte.surface, np.array(carte.surface.get_size())*unzoom)
                    carte.surface_screen_zoomed, _ = rot_center(carte.surface, angle_rot_plateau*180/np.pi, pos_centre_carte)
                    carte.surface_screen, rot_rect = rot_center(carte.surface_screen, angle_rot_plateau*180/np.pi, pos_centre_carte)
                    carte.rendered_cite = True

                carte.pos = centre_screen+(pos_plateau_rot+carte_pos_plateau_rot)*unzoom + shift_topleft_carte
                cartes_vues.append(carte)
                self.screen.blit(carte.surface_screen, carte.pos)

                num_couleur[carte.couleur] += 1

            # Merveille
            if True:
                #joueur.merveille.draw()

                debut_merveille = (dim_board[0]-cst.largeur_merveille)/2

                joueur.merveille.pos_plateau = np.array([debut_merveille, cst.hauteur_carte+cst.espace_entre_cartes_vertical])
                merveille_pos_plateau_rot = rot.dot(joueur.merveille.pos_plateau)

                joueur.merveille.draw_infos(joueur, unzoom)
                joueur.merveille.surface_screen_infos, rot_rect = rot_center(joueur.merveille.surface_avec_infos, angle_rot_plateau*180/np.pi, pos_centre_merveille)

                if (joueur.merveille.surface_screen is None):
                    joueur.merveille.surface_screen = pg.transform.smoothscale(joueur.merveille.surface, np.array(joueur.merveille.surface.get_size())*unzoom)
                    joueur.merveille.surface_screen, rot_rect = rot_center(joueur.merveille.surface_screen, angle_rot_plateau*180/np.pi, pos_centre_merveille)

                joueur.merveille.pos = centre_screen+(pos_plateau_rot+merveille_pos_plateau_rot)*unzoom + shift_topleft_merveille

                self.screen.blit(joueur.merveille.surface_screen, joueur.merveille.pos)
                self.screen.blit(joueur.merveille.surface_screen_infos, joueur.merveille.pos)

                nombre_etages = len(joueur.merveille.etages)
                for num_etage, etage in enumerate(joueur.merveille.etages):
                    #etage.draw()

                    pos_x = cst.largeur_merveille*(num_etage+1)/(nombre_etages+1) - cst.largeur_carte/2
                    etage.pos_plateau = np.array([debut_merveille+pos_x,
                                    cst.hauteur_carte+cst.espace_entre_cartes_vertical+(cst.hauteur_merveille)*(1-cst.prop_hauteur_etage)])
                    etage_pos_plateau_rot = rot.dot(etage.pos_plateau)

                    etage.unzoom = unzoom
                    if (etage.surface_screen is None or not etage.rendered):
                        etage.surface_screen = pg.transform.smoothscale(etage.surface, np.array(etage.surface.get_size())*unzoom)
                        etage.surface_screen_zoomed, _ = rot_center(etage.surface, angle_rot_plateau*180/np.pi, pos_centre_etage)
                        etage.surface_screen, rot_rect = rot_center(etage.surface_screen, angle_rot_plateau*180/np.pi, pos_centre_etage)
                        etage.rendered = True

                    etage.pos = centre_screen+(pos_plateau_rot+etage_pos_plateau_rot)*unzoom + shift_topleft_etage

                    self.screen.blit(etage.surface_screen, etage.pos)

        # for angle in range(0, 360, 1):
        #     rot = self.rotation_matrix(angle, a=excentricite)
        #     pg.draw.circle(self.screen, (0,0,0), centre_screen+rot.dot(np.array([0,-R*unzoom])), 3)

        for carte in self.jeu.cartes:
            if carte not in cartes_vues and carte.surface_screen is not None:
                carte.rect = None
                carte.masque = None
                for act in carte.buttons:
                    carte.buttons[act].rect = None
                    carte.buttons[act].masque = None
            elif carte.surface_screen is not None:
                carte.rect = carte.surface_screen.get_rect(topleft=carte.pos)
                carte.masque = pg.mask.from_surface(carte.surface_screen)
                for act in carte.buttons:
                    if carte.buttons[act].surface_screen is not None:
                        carte.buttons[act].rect = carte.buttons[act].surface_screen.get_rect(topleft=carte.buttons[act].pos)
                        carte.buttons[act].masque = pg.mask.from_surface(carte.buttons[act].surface_screen)
        for joueur in self.jeu.joueurs:
            joueur.merveille.rect = joueur.merveille.surface_screen.get_rect(topleft=joueur.merveille.pos)
            joueur.merveille.masque = pg.mask.from_surface(joueur.merveille.surface_screen)
            for etage in joueur.merveille.etages:
                if etage.surface_screen is not None:
                    etage.rect = etage.surface_screen.get_rect(topleft=etage.pos)
                    etage.masque = pg.mask.from_surface(etage.surface_screen)

    def clean(self):
        for carte in self.jeu.cartes:
            carte.is_clicked = False
            carte.justclicked = False
            carte.hovered = False
            for act in carte.buttons:
                carte.buttons[act].clickable = False
                carte.buttons[act].hovered = False
                carte.buttons[act].is_clicked = False

        for joueur in self.jeu.joueurs:
            for etage in joueur.merveille.etages:
                etage.is_clicked = False
                etage.hovered = False

    def draw_results_sheet(self):
        alpha = 200
        width = 1
        size_screen = self.screen.get_size()
        props = np.array([cst.prop_largeur_colonne_resultats, cst.prop_hauteur_colonne_resultats])
        marges = (size_screen-props*size_screen)/2
        largeur_colonne = (size_screen[0]-marges[0]*2)/9
        hauteur_ligne = (size_screen[1]-marges[1]*2)/9
        surface_fond = pg.Surface(size_screen, pg.SRCALPHA, 32)
        pg.draw.rect(surface_fond, (255,255,255,alpha), pg.Rect(*marges, *size_screen*props), border_radius=cst.border_radius)
        pg.draw.rect(surface_fond, (0,0,0,alpha), pg.Rect(*marges, *size_screen*props), width, border_radius=cst.border_radius)

        for i in range(1, 10):
            if i == 2:
                img = cst.images[cst.merveille]
                pos = np.array((marges[0]/2 + largeur_colonne*2/2, marges[1] + (i-1)*hauteur_ligne)+hauteur_ligne/2)
                pos -= np.array(img.get_size())/2
                surface_fond.blit(img, pos)
            elif i == 3:
                img = cst.images[cst.argent_score]
                pos = np.array((marges[0]/2 + largeur_colonne*2/2, marges[1] + (i-1)*hauteur_ligne)+hauteur_ligne/2)
                pos -= np.array(img.get_size())/2
                surface_fond.blit(img, pos)
            elif i == 4:
                img = cst.images[cst.militaire]
                pos = np.array((marges[0]/2 + largeur_colonne*2/2, marges[1] + (i-1)*hauteur_ligne)+hauteur_ligne/2)
                pos -= np.array(img.get_size())/2
                surface_fond.blit(img, pos)
            elif i == 5:
                pg.draw.rect(surface_fond, (16,143,211,alpha), (marges[0], marges[1] + (i-1)*hauteur_ligne, 2*largeur_colonne, hauteur_ligne))
                img = cst.images[cst.trait_score]
                pos = np.array((marges[0]/2 + largeur_colonne*2/2, marges[1] + (i-1)*hauteur_ligne)+hauteur_ligne/2)
                pos -= np.array(img.get_size())/2
                surface_fond.blit(img, pos)
            elif i == 6:
                pg.draw.rect(surface_fond, (246,154,35,alpha), (marges[0], marges[1] + (i-1)*hauteur_ligne, 2*largeur_colonne, hauteur_ligne))
                img = cst.images[cst.rond_score]
                pos = np.array((marges[0]/2 + largeur_colonne*2/2, marges[1] + (i-1)*hauteur_ligne)+hauteur_ligne/2)
                pos -= np.array(img.get_size())/2
                surface_fond.blit(img, pos)
            elif i == 7:
                pg.draw.rect(surface_fond, (66,176,40,alpha), (marges[0], marges[1] + (i-1)*hauteur_ligne, 2*largeur_colonne, hauteur_ligne))
                img = cst.images[cst.triangle_score]
                pos = np.array((marges[0]/2 + largeur_colonne*2/2, marges[1] + (i-1)*hauteur_ligne)+hauteur_ligne/2)
                pos -= np.array(img.get_size())/2
                surface_fond.blit(img, pos)
            elif i == 8:
                pg.draw.rect(surface_fond, (105,85,175,alpha), (marges[0], marges[1] + (i-1)*hauteur_ligne, 2*largeur_colonne, hauteur_ligne))
                img = cst.images[cst.etoile_score]
                pos = np.array((marges[0]/2 + largeur_colonne*2/2, marges[1] + (i-1)*hauteur_ligne)+hauteur_ligne/2)
                pos -= np.array(img.get_size())/2
                surface_fond.blit(img, pos)
            elif i == 9:
                img = cst.images[cst.somme]
                pos = np.array((marges[0]/2 + largeur_colonne*2/2, marges[1] + (i-1)*hauteur_ligne)+hauteur_ligne/2)
                pos -= np.array(img.get_size())/2
                surface_fond.blit(img, pos)

        for i in range(2, 9):
            w = width
            if i==2:
                w = 3*width
            pg.draw.line(surface_fond, (0,0,0,alpha), (marges[0]+i*largeur_colonne, marges[1]), (marges[0]+i*largeur_colonne, marges[1]+int((props[1])*size_screen[1])), width=w)
        for i in range(1, 9):
            w = width
            if i==1 or i==8:
                w = 3*width
            pg.draw.line(surface_fond, (0,0,0,alpha), (marges[0], marges[1] + i*hauteur_ligne), (marges[0]+int((props[0])*size_screen[0]), marges[1] + i*hauteur_ligne), width=w)


        self.surface_results_vierge = surface_fond

    def end_game(self, jeu):
        self.render()
        jeu.comptage_points()
        self.draw_results_sheet()
        surface_fond = self.surface_results_vierge

        alpha = 200
        width = 1
        size_screen = self.screen.get_size()
        props = np.array([cst.prop_largeur_colonne_resultats, cst.prop_hauteur_colonne_resultats])
        marges = (size_screen-props*size_screen)/2
        largeur_colonne = (size_screen[0]-marges[0]*2)/9
        hauteur_ligne = (size_screen[1]-marges[1]*2)/9

        gagnants, pts_max = [], 0
        for i, joueur in enumerate(jeu.joueurs):
            if joueur.points_total>pts_max:
                pts_max = joueur.points_total
                gagnants = [i]
            elif joueur.points_total==pts_max:
                gagnants.append(i)

        for i, joueur in enumerate(jeu.joueurs):
            for j, ligne in enumerate([cst.nom, cst.merveille, cst.argent, cst.militaire, cst.bleu, cst.jaune, cst.vert, cst.violet, cst.somme]):
                if i in gagnants and not (j in [0, 8] and i==6):
                    pg.draw.rect(surface_fond, (255,213,70,alpha), (marges[0]+int((i+2)*largeur_colonne), marges[1] + (j)*hauteur_ligne, largeur_colonne, hauteur_ligne))
                elif i in gagnants and (j==0 and i==6):
                    pg.draw.rect(surface_fond, (255,213,70,alpha), (marges[0]+int((i+2)*largeur_colonne), marges[1] + (j)*hauteur_ligne, largeur_colonne, hauteur_ligne), border_top_right_radius=cst.border_radius)
                elif i in gagnants and (j==8 and i==6):
                    pg.draw.rect(surface_fond, (255,213,70,alpha), (marges[0]+int((i+2)*largeur_colonne), marges[1] + (j)*hauteur_ligne, largeur_colonne, hauteur_ligne), border_bottom_right_radius=cst.border_radius)

                if ligne == cst.nom:
                    id_joueur = "Joueur "+str(joueur.id+1)
                    if joueur.id == 0:
                        id_joueur = "Vous"
                    texte = cst.font_scores.render(f"{id_joueur}", True, (0,0,0))
                elif ligne == cst.somme:
                    texte = cst.font_scores.render(f"{joueur.points_total}", True, (0,0,0))
                else:
                    texte = cst.font_scores.render(f"{joueur.points[ligne]}", True, (0,0,0))
                dims_texte = texte.get_size()
                pos = (marges[0]+int((i+2+0.5)*largeur_colonne - dims_texte[0]/2), marges[1]+int((j+0.5)*hauteur_ligne - dims_texte[1]/2))
                surface_fond.blit(texte, pos)


        for i in range(2, 9):
            w = width
            if i==2:
                w = 3*width
            pg.draw.line(surface_fond, (0,0,0,alpha), (marges[0]+i*largeur_colonne, marges[1]), (marges[0]+i*largeur_colonne, marges[1]+int((props[1])*size_screen[1])), width=w)
        for i in range(1, 9):
            w = width
            if i==1 or i==8:
                w = 3*width
            pg.draw.line(surface_fond, (0,0,0,alpha), (marges[0], marges[1] + i*hauteur_ligne), (marges[0]+int((props[0])*size_screen[0]), marges[1] + i*hauteur_ligne), width=w)


        pos = np.array([0., 0.])
        pos[1] = size_screen[1]*0.9
        bouton_continuer = Bouton((cst.largeur_carte*2, cst.hauteur_carte), "Continuer", size_txt_fac=0.5)
        bouton_continuer.clickable = True
        bouton_continuer.draw()
        pos[0] = size_screen[0]/4
        pos_continuer = pos - np.array(bouton_continuer.surface.get_size())/2
        bouton_continuer.pos = pos_continuer.copy()
        surface_fond.blit(bouton_continuer.surface, bouton_continuer.pos)
        bouton_menu = Bouton((cst.largeur_carte*2, cst.hauteur_carte), "Menu", size_txt_fac=0.5)
        bouton_menu.clickable = True
        bouton_menu.draw()
        pos[0] = 3*size_screen[0]/4
        pos_menu = pos - np.array(bouton_menu.surface.get_size())/2
        bouton_menu.pos = pos_menu.copy()
        surface_fond.blit(bouton_menu.surface, bouton_menu.pos)

        bouton_continuer.rect = bouton_continuer.surface.get_rect(topleft=bouton_continuer.pos)
        bouton_continuer.masque = pg.mask.from_surface(bouton_continuer.surface)
        bouton_menu.rect = bouton_menu.surface.get_rect(topleft=bouton_menu.pos)
        bouton_menu.masque = pg.mask.from_surface(bouton_menu.surface)
        bouton_quit = BoutonQuit(self.screen)
        bouton_quit.draw()
        surface_fond.blit(bouton_quit.surface, bouton_quit.pos)

        self.screen.blit(surface_fond, (0,0))
        pg.display.flip()

        click = False
        while True:
            event = pg.event.wait()
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    break
            if event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    click = True
                    bouton_quit.check_hover()
                    if bouton_quit.hovered:
                        pg.quit()
                        sys.exit()


            change_continuer = bouton_continuer.check_hover()
            change_menu = bouton_menu.check_hover()
            if change_menu or change_continuer:
                self.render()
                self.screen.blit(surface_fond, (0,0))
            if bouton_continuer.hovered:
                self.screen.blit(bouton_continuer.surface, bouton_continuer.pos-1)
                if click:
                    return "Continuer"
            if bouton_menu.hovered:
                self.screen.blit(bouton_menu.surface, bouton_menu.pos-1)
                if click:
                    return "Menu"

            click = False
            pg.display.flip()

    def menu(self):
        self.init_background()
        size_screen = self.screen.get_size()
        surface_fond = pg.Surface(size_screen, pg.SRCALPHA, 32)
        boutons = []
        largeur_bouton = int(0.75*cst.largeur_carte)
        hauteur_bouton = cst.hauteur_carte
        espacement = 30
        pos = np.array([0., 0.])
        pos[1] = size_screen[1]*0.5

        bouton_texte = Bouton(((largeur_bouton+espacement)*5+largeur_bouton, hauteur_bouton), f"Nombre de joueurs", size_txt_fac=0.2)
        bouton_texte.clickable = True
        bouton_texte.draw()
        bouton_texte.pos = (int(size_screen[0]/2+(-2.0)*(largeur_bouton+espacement)), size_screen[1]*0.3)
        surface_fond.blit(bouton_texte.surface, bouton_texte.pos)
        bouton_quit = BoutonQuit(self.screen)
        bouton_quit.draw()
        surface_fond.blit(bouton_quit.surface, bouton_quit.pos)
        for i, nombre in enumerate(range(3, 8)):
            pos[0] = size_screen[0]/2+(i-2.0)*(largeur_bouton+espacement)
            bouton = Bouton((largeur_bouton, hauteur_bouton), f"{nombre}", size_txt_fac=1.)
            bouton.nombre = nombre
            bouton.clickable = True
            bouton.draw()
            pos_continuer = pos - np.array(bouton.surface.get_size())/2
            bouton.pos = pos_continuer.copy()
            bouton.rect = bouton.surface.get_rect(topleft=bouton.pos)
            bouton.masque = pg.mask.from_surface(bouton.surface)

            boutons.append(bouton)

        for bouton in boutons:
            surface_fond.blit(bouton.surface, bouton.pos)

        self.screen.blit(surface_fond, (0,0))
        pg.display.flip()

        click = False
        while True:
            event = pg.event.wait()
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    break
            if event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    click = True

                    bouton_quit.check_hover()
                    if bouton_quit.hovered:
                        pg.quit()
                        sys.exit()



            for bouton in boutons:
                change = bouton.check_hover()
                if change:
                    self.init_background()
                    self.screen.blit(surface_fond, (0,0))
                if bouton.hovered:
                    self.screen.blit(bouton.surface, bouton.pos-1)
                    if click:
                        return bouton.nombre

            click = False
            pg.display.flip()

        return self.jeu.nombre_joueurs


class Bouton():
    def __init__(self, dims_carte, texte="", size_txt_fac=1.):
        self.is_clicked = False
        self.clickable = False
        self.hovered = False
        self.texte = texte
        self.pos = None
        self.dims_carte = dims_carte
        self.action = None
        size_txt = int(size_txt_fac*1.*self.dims_carte[0]*cst.largeur_boutton_fac/7)
        self.font = pg.font.SysFont("Comic sans", size_txt)

        self.surface = pg.Surface((dims_carte[0]*cst.largeur_boutton_fac+cst.decalage_ombre, dims_carte[1]*cst.hauteur_boutton_fac+cst.decalage_ombre), pg.SRCALPHA, 32)
        self.surface_screen = None
        self.masque = None
        self.rect = None

    def draw(self):
        color = (255, 255, 255, 255)
        if not self.clickable:
            color = (255, 255, 255, 50)


        largeur_bouton, hauteur_bouton = self.dims_carte[0]*cst.largeur_boutton_fac, self.dims_carte[1]*cst.hauteur_boutton_fac

        epaisseur_ligne_sep = 4

        decalage_ombre = cst.decalage_ombre
        pg.draw.rect(self.surface, (0,0,0,130), pg.Rect(decalage_ombre, decalage_ombre, largeur_bouton, hauteur_bouton), border_radius=int(0.5*cst.border_radius))

        pg.draw.rect(self.surface, color, pg.Rect(0, 0, largeur_bouton, hauteur_bouton), border_radius=int(0.5*cst.border_radius))
        pg.draw.rect(self.surface, (0,0,0), pg.Rect(0, 0, largeur_bouton, hauteur_bouton), int(0.5*epaisseur_ligne_sep*cst.scale_cartes/30), border_radius=int(0.5*cst.border_radius))

        font = self.font
        text_surface = font.render(self.texte, False, (0, 0, 0))
        pos = [(largeur_bouton-text_surface.get_width())/2, (hauteur_bouton-text_surface.get_height())/2]
        self.surface.blit(text_surface, pos)

    def check_hover(self):
        pos = pg.mouse.get_pos()
        change = False
        if self.rect is not None and self.masque is not None:
            pos_in_mask = pos[0] - self.pos[0], pos[1] - self.pos[1]
            if self.rect.collidepoint(*pos):
                if self.masque.get_at(pos_in_mask):
                    if not self.hovered: change = True
                    self.hovered = True
                else:
                    if self.hovered: change = True
                    self.hovered = False
            else:
                if self.hovered: change = True
                self.hovered = False
        return change

class BoutonQuit():
    def __init__(self, screen):
        self.is_clicked = False
        self.hovered = False
        self.pos = None
        self.largeur_bouton = self.hauteur_bouton = 20

        self.surface = pg.Surface((self.largeur_bouton, self.hauteur_bouton), pg.SRCALPHA, 32)
        self.pos = (screen.get_size()[0]-self.largeur_bouton, 0)
        self.surface_screen = None
        self.masque = None
        self.rect = None

    def draw(self):
        color = (255, 255, 255, 255)

        pg.draw.rect(self.surface, color, pg.Rect(0, 0, self.largeur_bouton, self.hauteur_bouton), border_bottom_left_radius=2)
        pg.draw.rect(self.surface, (0,0,0), pg.Rect(0, 0, self.largeur_bouton, self.hauteur_bouton), 1, border_bottom_left_radius=2)
        self.surface.blit(cst.images[cst.croix], (self.largeur_bouton/2-cst.images[cst.croix].get_size()[0]/2, self.hauteur_bouton/2-cst.images[cst.croix].get_size()[1]/2))
        self.rect = self.surface.get_rect(topleft=self.pos)
        self.masque = pg.mask.from_surface(self.surface)

    def check_hover(self):
        pos = pg.mouse.get_pos()
        if self.rect is not None and self.masque is not None:
            pos_in_mask = pos[0] - self.pos[0], pos[1] - self.pos[1]
            if self.rect.collidepoint(*pos):
                if self.masque.get_at(pos_in_mask):
                    self.hovered = True
                else:
                    self.hovered = False
            else:
                self.hovered = False