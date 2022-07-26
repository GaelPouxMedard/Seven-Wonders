from game import Carte, Effet, Merveille, Etage
import constantes as cst


# ====================== MERVEILLES =======================
#region Merveilles
merveilles = []

merveille = Merveille()
effet = Effet()
effet.effet_production[cst.pierre] = 1
merveille.nom = "Gizeh-(jour)"
merveille.effet = effet
etage_1 = Etage()
etage_1.cout_ressource[cst.bois] = 2
effet_1 = Effet()
effet_1.effet_points_victoire = 3
etage_1.effet = effet_1
merveille.etages.append(etage_1)
etage_2 = Etage()
etage_2.cout_ressource[cst.argile] = 2
etage_2.cout_ressource[cst.tissu] = 1
effet_2 = Effet()
effet_2.effet_points_victoire = 5
etage_2.effet = effet_2
merveille.etages.append(etage_2)
etage_3 = Etage()
etage_3.cout_ressource[cst.pierre] = 4
effet_3 = Effet()
effet_3.effet_points_victoire = 7
etage_3.effet = effet_3
merveille.etages.append(etage_3)
merveille.nombre_etages = len(merveille.etages)
merveilles.append(merveille)

merveille = Merveille()
effet = Effet()
effet.effet_production[cst.fer] = 1
merveille.nom = "Gizeh-(nuit)"
merveille.effet = effet
etage_1 = Etage()
etage_1.cout_ressource[cst.bois] = 2
effet_1 = Effet()
effet_1.effet_points_victoire = 3
etage_1.effet = effet_1
merveille.etages.append(etage_1)
etage_2 = Etage()
etage_2.cout_ressource[cst.pierre] = 3
effet_2 = Effet()
effet_2.effet_points_victoire = 5
etage_2.effet = effet_2
merveille.etages.append(etage_2)
etage_3 = Etage()
etage_3.cout_ressource[cst.argile] = 3
effet_3 = Effet()
effet_3.effet_points_victoire = 5
etage_3.effet = effet_3
merveille.etages.append(etage_3)
etage_4 = Etage()
etage_4.cout_ressource[cst.pierre] = 4
etage_4.cout_ressource[cst.parchemin] = 1
effet_4 = Effet()
effet_4.effet_points_victoire = 7
etage_4.effet = effet_4
merveille.etages.append(etage_4)
merveille.nombre_etages = len(merveille.etages)
merveilles.append(merveille)

merveille = Merveille()
effet = Effet()
effet.effet_production[cst.fer] = 1
merveille.nom = "Rhodos-(jour)"
merveille.effet = effet
etage_1 = Etage()
etage_1.cout_ressource[cst.bois] = 2
effet_1 = Effet()
effet_1.effet_points_victoire = 3
etage_1.effet = effet_1
merveille.etages.append(etage_1)
etage_2 = Etage()
etage_2.cout_ressource[cst.argile] = 3
effet_2 = Effet()
effet_2.effet_militaire = 2
etage_2.effet = effet_2
merveille.etages.append(etage_2)
etage_3 = Etage()
etage_3.cout_ressource[cst.fer] = 4
effet_3 = Effet()
effet_3.effet_points_victoire = 7
etage_3.effet = effet_3
merveille.etages.append(etage_3)
merveille.nombre_etages = len(merveille.etages)
merveilles.append(merveille)

merveille = Merveille()
effet = Effet()
effet.effet_production[cst.fer] = 1
merveille.nom = "Rhodos-(nuit)"
merveille.effet = effet
etage_1 = Etage()
etage_1.cout_ressource[cst.pierre] = 3
effet_1 = Effet()
effet_1.effet_points_victoire = 3
effet_1.effet_tresor = 3
effet_1.effet_militaire = 1
etage_1.effet = effet_1
merveille.etages.append(etage_1)
etage_2 = Etage()
etage_2.cout_ressource[cst.fer] = 4
effet_2 = Effet()
effet_2.effet_points_victoire = 4
effet_2.effet_tresor = 4
effet_2.effet_militaire = 1
etage_2.effet = effet_2
merveille.etages.append(etage_2)
merveille.nombre_etages = len(merveille.etages)
merveilles.append(merveille)

merveille = Merveille()
effet = Effet()
effet.effet_production[cst.parchemin] = 1
merveille.nom = "Ephesos-(jour)"
merveille.effet = effet
etage_1 = Etage()
etage_1.cout_ressource[cst.argile] = 2
effet_1 = Effet()
effet_1.effet_points_victoire = 3
etage_1.effet = effet_1
merveille.etages.append(etage_1)
etage_2 = Etage()
etage_2.cout_ressource[cst.bois] = 2
effet_2 = Effet()
effet_2.effet_tresor = 9
etage_2.effet = effet_2
merveille.etages.append(etage_2)
etage_3 = Etage()
etage_3.cout_ressource[cst.fer] = 2
etage_3.cout_ressource[cst.vert] = 1
effet_3 = Effet()
effet_3.effet_points_victoire = 7
etage_3.effet = effet_3
merveille.etages.append(etage_3)
merveille.nombre_etages = len(merveille.etages)
merveilles.append(merveille)

merveille = Merveille()
effet = Effet()
effet.effet_production[cst.parchemin] = 1
merveille.nom = "Ephesos-(nuit)"
merveille.effet = effet
etage_1 = Etage()
etage_1.cout_ressource[cst.pierre] = 2
effet_1 = Effet()
effet_1.effet_tresor = 4
effet_1.effet_points_victoire = 2
etage_1.effet = effet_1
merveille.etages.append(etage_1)
etage_2 = Etage()
etage_2.cout_ressource[cst.bois] = 2
effet_2 = Effet()
effet_2.effet_tresor = 4
effet_2.effet_points_victoire = 3
etage_2.effet = effet_2
merveille.etages.append(etage_2)
etage_3 = Etage()
etage_3.cout_ressource[cst.fer] = 2
etage_3.cout_ressource[cst.tissu] = 1
effet_3 = Effet()
effet_3.effet_tresor = 4
effet_3.effet_points_victoire = 5
etage_3.effet = effet_3
merveille.etages.append(etage_3)
merveille.nombre_etages = len(merveille.etages)
merveilles.append(merveille)

merveille = Merveille()
effet = Effet()
effet.effet_production[cst.verre] = 1
merveille.nom = "Alexandria-(jour)"
merveille.effet = effet
etage_1 = Etage()
etage_1.cout_ressource[cst.pierre] = 2
effet_1 = Effet()
effet_1.effet_points_victoire = 3
etage_1.effet = effet_1
merveille.etages.append(etage_1)
etage_2 = Etage()
etage_2.cout_ressource[cst.fer] = 2
effet_2 = Effet()
effet_2.effet_production[cst.bois] = -1
effet_2.effet_production[cst.fer] = -1
effet_2.effet_production[cst.argile] = -1
effet_2.effet_production[cst.pierre] = -1
effet_2.achetable = False
etage_2.effet = effet_2
merveille.etages.append(etage_2)
etage_3 = Etage()
etage_3.cout_ressource[cst.parchemin] = 1
etage_3.cout_ressource[cst.tissu] = 1
effet_3 = Effet()
effet_1.effet_points_victoire = 7
etage_3.effet = effet_3
merveille.etages.append(etage_3)
merveille.nombre_etages = len(merveille.etages)
merveilles.append(merveille)

merveille = Merveille()
effet = Effet()
effet.effet_production[cst.verre] = 1
merveille.nom = "Alexandria-(nuit)"
merveille.effet = effet
etage_1 = Etage()
etage_1.cout_ressource[cst.argile] = 2
effet_1 = Effet()
effet_1.effet_production[cst.bois] = -1
effet_1.effet_production[cst.fer] = -1
effet_1.effet_production[cst.argile] = -1
effet_1.effet_production[cst.pierre] = -1
etage_1.effet = effet_1
merveille.etages.append(etage_1)
etage_2 = Etage()
etage_2.cout_ressource[cst.fer] = 3
effet_2 = Effet()
effet_2.effet_production[cst.verre] = -1
effet_2.effet_production[cst.parchemin] = -1
effet_2.effet_production[cst.tissu] = -1
effet_2.achetable = False
etage_2.effet = effet_2
merveille.etages.append(etage_2)
etage_3 = Etage()
etage_3.cout_ressource[cst.bois] = 4
effet_3 = Effet()
effet_3.effet_points_victoire = 7
etage_3.effet = effet_3
merveille.etages.append(etage_3)
merveille.nombre_etages = len(merveille.etages)
merveilles.append(merveille)

merveille = Merveille()
effet = Effet()
effet.effet_production[cst.argile] = 1
merveille.nom = "Olympia-(jour)"
merveille.effet = effet
etage_1 = Etage()
etage_1.cout_ressource[cst.pierre] = 2
effet_1 = Effet()
effet_1.effet_points_victoire = 3
etage_1.effet = effet_1
merveille.etages.append(etage_1)
etage_2 = Etage()
etage_2.cout_ressource[cst.bois] = 2
effet_2 = Effet()
effet_2.premiere_carte_couleur_gratuite = True
etage_2.effet = effet_2
merveille.etages.append(etage_2)
etage_3 = Etage()
etage_3.cout_ressource[cst.argile] = 3
effet_3 = Effet()
effet_3.effet_points_victoire = 7
etage_3.effet = effet_3
merveille.etages.append(etage_3)
merveille.nombre_etages = len(merveille.etages)
merveilles.append(merveille)

merveille = Merveille()
effet = Effet()
effet.effet_production[cst.argile] = 1
merveille.nom = "Olympia-(nuit)"
merveille.effet = effet
etage_1 = Etage()
etage_1.cout_ressource[cst.fer] = 2
effet_1 = Effet()
effet_1.premiere_carte_age_gratuite = True
effet_1.effet_points_victoire = 2
etage_1.effet = effet_1
merveille.etages.append(etage_1)
etage_2 = Etage()
etage_2.cout_ressource[cst.argile] = 3
effet_2 = Effet()
effet_2.derniere_carte_age_gratuite = True
effet_2.effet_points_victoire = 3
etage_2.effet = effet_2
merveille.etages.append(etage_2)
etage_3 = Etage()
etage_3.cout_ressource[cst.parchemin] = 1
etage_3.cout_ressource[cst.verre] = 1
etage_3.cout_ressource[cst.tissu] = 1
effet_3 = Effet()
effet_3.effet_points_victoire = 5
etage_3.effet = effet_3
merveille.etages.append(etage_3)
merveille.nombre_etages = len(merveille.etages)
merveilles.append(merveille)

merveille = Merveille()
effet = Effet()
effet.effet_production[cst.tissu] = 1
merveille.nom = "Halikarnassos-(jour)"
merveille.effet = effet
etage_1 = Etage()
etage_1.cout_ressource[cst.fer] = 2
effet_1 = Effet()
effet_1.effet_points_victoire = 3
etage_1.effet = effet_1
merveille.etages.append(etage_1)
etage_2 = Etage()
etage_2.cout_ressource[cst.parchemin] = 1
etage_2.cout_ressource[cst.verre] = 1
effet_2 = Effet()
effet_2.carte_defausse = True
etage_2.effet = effet_2
merveille.etages.append(etage_2)
etage_3 = Etage()
etage_3.cout_ressource[cst.pierre] = 3
effet_3 = Effet()
effet_3.effet_points_victoire = 7
etage_3.effet = effet_3
merveille.etages.append(etage_3)
merveille.nombre_etages = len(merveille.etages)
merveilles.append(merveille)

merveille = Merveille()
effet = Effet()
effet.effet_production[cst.tissu] = 1
merveille.nom = "Halikarnassos-(nuit)"
merveille.effet = effet
etage_1 = Etage()
etage_1.cout_ressource[cst.argile] = 2
effet_1 = Effet()
effet_1.effet_points_victoire = 2
effet_1.carte_defausse = True
etage_1.effet = effet_1
merveille.etages.append(etage_1)
etage_2 = Etage()
etage_2.cout_ressource[cst.parchemin] = 1
etage_2.cout_ressource[cst.verre] = 1
effet_2 = Effet()
effet_2.effet_points_victoire = 1
effet_2.carte_defausse = True
etage_2.effet = effet_2
merveille.etages.append(etage_2)
etage_3 = Etage()
etage_3.cout_ressource[cst.pierre] = 3
effet_3 = Effet()
effet_3.carte_defausse = True
etage_3.effet = effet_3
merveille.etages.append(etage_3)
merveille.nombre_etages = len(merveille.etages)
merveilles.append(merveille)

merveille = Merveille()
effet = Effet()
effet.effet_production[cst.bois] = 1
merveille.nom = "Babylon-(jour)"
merveille.effet = effet
etage_1 = Etage()
etage_1.cout_ressource[cst.argile] = 2
effet_1 = Effet()
effet_1.effet_points_victoire = 3
etage_1.effet = effet_1
merveille.etages.append(etage_1)
etage_2 = Etage()
etage_2.cout_ressource[cst.fer] = 2
etage_2.cout_ressource[cst.tissu] = 1
effet_2 = Effet()
effet_2.effet_symbole_scientifique[cst.rouage] = -1
effet_2.effet_symbole_scientifique[cst.compas] = -1
effet_2.effet_symbole_scientifique[cst.tablette] = -1
etage_2.effet = effet_2
merveille.etages.append(etage_2)
etage_3 = Etage()
etage_3.cout_ressource[cst.bois] = 4
effet_3 = Effet()
effet_3.effet_points_victoire = 7
etage_3.effet = effet_3
merveille.etages.append(etage_3)
merveille.nombre_etages = len(merveille.etages)
merveilles.append(merveille)

merveille = Merveille()
effet = Effet()
effet.effet_production[cst.bois] = 1
merveille.nom = "Babylon-(nuit)"
merveille.effet = effet
etage_1 = Etage()
etage_1.cout_ressource[cst.pierre] = 2
effet_1 = Effet()
effet_1.jouer_derniere_carte = True
etage_1.effet = effet_1
merveille.etages.append(etage_1)
etage_2 = Etage()
etage_2.cout_ressource[cst.argile] = 3
etage_2.cout_ressource[cst.verre] = 1
effet_2 = Effet()
effet_2.effet_symbole_scientifique[cst.rouage] = -1
effet_2.effet_symbole_scientifique[cst.compas] = -1
effet_2.effet_symbole_scientifique[cst.tablette] = -1
etage_2.effet = effet_2
merveille.etages.append(etage_2)
merveille.nombre_etages = len(merveille.etages)
merveilles.append(merveille)

#endregion

# ====================== CARTES =======================
paquet_cartes = []

#region Cartes 3 joueurs
carte = Carte()
effet = Effet()
carte.age = 1
carte.nb_joueurs = 3
carte.nom = "Fosse-argileuse"
carte.couleur = cst.marron
carte.cout_ressource[cst.argent] = 1
effet.effet_production[cst.argile] = -1
effet.effet_production[cst.fer] = -1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 1
carte.nb_joueurs = 3
carte.nom = "Chantier"
carte.couleur = cst.marron
effet.effet_production[cst.bois] = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 1
carte.nb_joueurs = 3
carte.nom = "Cavité"
carte.couleur = cst.marron
effet.effet_production[cst.pierre] = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 1
carte.nb_joueurs = 3
carte.nom = "Exploitation-forestière"
carte.couleur = cst.marron
carte.cout_ressource[cst.argent] = 1
effet.effet_production[cst.bois] = -1
effet.effet_production[cst.pierre] = -1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 1
carte.nb_joueurs = 3
carte.nom = "Filon"
carte.couleur = cst.marron
effet.effet_production[cst.fer] = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 1
carte.nb_joueurs = 3
carte.nom = "Bassin-argileux"
carte.couleur = cst.marron
effet.effet_production[cst.argile] = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 1
carte.nb_joueurs = 3
carte.nom = "Caserne"
carte.couleur = cst.rouge
carte.cout_ressource[cst.fer] = 1
effet.effet_militaire = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 1
carte.nb_joueurs = 3
carte.nom = "Tour-de-garde"
carte.couleur = cst.rouge
carte.cout_ressource[cst.argile] = 1
effet.effet_militaire = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 1
carte.nb_joueurs = 3
carte.nom = "Palissade"
carte.couleur = cst.rouge
carte.cout_ressource[cst.bois] = 1
effet.effet_militaire = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 1
carte.nb_joueurs = 3
carte.nom = "Autel"
carte.couleur = cst.bleu
carte.symbole_chainage = [cst.symbole_etoile]
effet.effet_points_victoire = 3
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 1
carte.nb_joueurs = 3
carte.nom = "Théâtre"
carte.couleur = cst.bleu
carte.symbole_chainage = [cst.symbole_masque]
effet.effet_points_victoire = 3
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 1
carte.nb_joueurs = 3
carte.nom = "Bains"
carte.couleur = cst.bleu
carte.symbole_chainage = [cst.symbole_goutte]
carte.cout_ressource[cst.pierre] = 1
effet.effet_points_victoire = 3
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 1
carte.nb_joueurs = 3
carte.nom = "Métier-à-tisser"
carte.couleur = cst.gris
effet.effet_production[cst.tissu] = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 1
carte.nb_joueurs = 3
carte.nom = "Verrerie"
carte.couleur = cst.gris
effet.effet_production[cst.verre] = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 1
carte.nb_joueurs = 3
carte.nom = "Presse"
carte.couleur = cst.gris
effet.effet_production[cst.parchemin] = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 1
carte.nb_joueurs = 3
carte.nom = "Marché"
carte.couleur = cst.jaune
carte.symbole_chainage = [cst.symbole_chameau]
effet.effet_reduction_gauche_manufacture = True
effet.effet_reduction_droite_manufacture = True
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 1
carte.nb_joueurs = 3
carte.nom = "Comptoir-ouest"
carte.couleur = cst.jaune
carte.symbole_chainage = [cst.symbole_devanture]
effet.effet_reduction_gauche_base = True
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 1
carte.nb_joueurs = 3
carte.nom = "Comptoir-est"
carte.couleur = cst.jaune
carte.symbole_chainage = [cst.symbole_devanture]
effet.effet_reduction_droite_base = True
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 1
carte.nb_joueurs = 3
carte.nom = "Officine"
carte.couleur = cst.vert
carte.symbole_chainage = [cst.symbole_fer_a_cheval, cst.symbole_bol]
carte.cout_ressource[cst.tissu] = 1
effet.effet_symbole_scientifique[cst.compas] = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 1
carte.nb_joueurs = 3
carte.nom = "Scriptorium"
carte.couleur = cst.vert
carte.symbole_chainage = [cst.symbole_balance, cst.symbole_livre]
carte.cout_ressource[cst.parchemin] = 1
effet.effet_symbole_scientifique[cst.tablette] = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 1
carte.nb_joueurs = 3
carte.nom = "Atelier"
carte.couleur = cst.vert
carte.symbole_chainage = [cst.symbole_cible, cst.symbole_lampe]
carte.cout_ressource[cst.verre] = 1
effet.effet_symbole_scientifique[cst.rouage] = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 2
carte.nb_joueurs = 3
carte.nom = "Verrerie"
carte.couleur = cst.gris
effet.effet_production[cst.verre] = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 2
carte.nb_joueurs = 3
carte.nom = "Métier-à-tisser"
carte.couleur = cst.gris
effet.effet_production[cst.tissu] = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 2
carte.nb_joueurs = 3
carte.nom = "Presse"
carte.couleur = cst.gris
effet.effet_production[cst.parchemin] = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 2
carte.nb_joueurs = 3
carte.nom = "Statue"
carte.couleur = cst.bleu
carte.cout_chainage = cst.symbole_marteau
carte.cout_ressource[cst.fer] = 2
carte.cout_ressource[cst.bois] = 1
effet.effet_points_victoire = 4
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 2
carte.nb_joueurs = 3
carte.nom = "Aqueduc"
carte.couleur = cst.bleu
carte.cout_chainage = cst.symbole_goutte
carte.cout_ressource[cst.pierre] = 3
effet.effet_points_victoire = 5
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 2
carte.nb_joueurs = 3
carte.nom = "Tribunal"
carte.couleur = cst.bleu
carte.cout_chainage = cst.symbole_balance
carte.cout_ressource[cst.argile] = 2
carte.cout_ressource[cst.tissu] = 1
effet.effet_points_victoire = 4
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 2
carte.nb_joueurs = 3
carte.nom = "Temple"
carte.couleur = cst.bleu
carte.cout_ressource[cst.bois] = 1
carte.cout_ressource[cst.argile] = 1
carte.cout_ressource[cst.verre] = 1
effet.effet_points_victoire = 4
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 2
carte.nb_joueurs = 3
carte.nom = "Bibliothèque"
carte.couleur = cst.vert
carte.cout_ressource[cst.pierre] = 2
carte.cout_ressource[cst.tissu] = 1
carte.cout_chainage = cst.symbole_livre
effet.symbole_chainage = [cst.symbole_temple, cst.symbole_parchemin]
effet.effet_symbole_scientifique[cst.tablette] = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 2
carte.nb_joueurs = 3
carte.nom = "École"
carte.couleur = cst.vert
carte.cout_ressource[cst.bois] = 1
carte.cout_ressource[cst.parchemin] = 1
effet.symbole_chainage = [cst.symbole_lyre, cst.symbole_plume]
effet.effet_symbole_scientifique[cst.tablette] = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 2
carte.nb_joueurs = 3
carte.nom = "Laboratoire"
carte.couleur = cst.vert
carte.cout_ressource[cst.argile] = 2
carte.cout_ressource[cst.parchemin] = 1
carte.cout_chainage = cst.symbole_lampe
effet.symbole_chainage = [cst.symbole_planetes, cst.symbole_scie]
effet.effet_symbole_scientifique[cst.rouage] = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 2
carte.nb_joueurs = 3
carte.nom = "Dispensaire"
carte.couleur = cst.vert
carte.cout_ressource[cst.fer] = 2
carte.cout_ressource[cst.verre] = 1
carte.cout_chainage = cst.symbole_bol
effet.symbole_chainage = [cst.symbole_eclair, cst.symbole_torche]
effet.effet_symbole_scientifique[cst.compas] = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 2
carte.nb_joueurs = 3
carte.nom = "Écuries"
carte.couleur = cst.rouge
carte.cout_ressource[cst.bois] = 1
carte.cout_ressource[cst.fer] = 1
carte.cout_ressource[cst.argile] = 1
carte.cout_chainage = cst.symbole_fer_a_cheval
effet.effet_militaire = 2
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 2
carte.nb_joueurs = 3
carte.nom = "Muraille"
carte.couleur = cst.rouge
carte.cout_ressource[cst.pierre] = 3
effet.effet_militaire = 2
effet.symbole_chainage = [cst.symbole_tour]
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 2
carte.nb_joueurs = 3
carte.nom = "Champs-de-tir"
carte.couleur = cst.rouge
carte.cout_ressource[cst.bois] = 2
carte.cout_ressource[cst.fer] = 1
carte.cout_chainage = cst.symbole_cible
effet.effet_militaire = 2
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 2
carte.nb_joueurs = 3
carte.nom = "Briquetterie"
carte.couleur = cst.marron
carte.cout_ressource[cst.argent] = 1
effet.effet_production[cst.argile] = 2
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 2
carte.nb_joueurs = 3
carte.nom = "Fonderie"
carte.couleur = cst.marron
carte.cout_ressource[cst.argent] = 1
effet.effet_production[cst.fer] = 2
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 2
carte.nb_joueurs = 3
carte.nom = "Carrière"
carte.couleur = cst.marron
carte.cout_ressource[cst.argent] = 1
effet.effet_production[cst.pierre] = 2
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 2
carte.nb_joueurs = 3
carte.nom = "Scierie"
carte.couleur = cst.marron
carte.cout_ressource[cst.argent] = 1
effet.effet_production[cst.bois] = 2
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 2
carte.nb_joueurs = 3
carte.nom = "Caravansérail"
carte.couleur = cst.jaune
carte.cout_ressource[cst.bois] = 2
carte.cout_chainage = cst.symbole_chameau
effet.effet_production[cst.bois] = -1
effet.effet_production[cst.argile] = -1
effet.effet_production[cst.pierre] = -1
effet.effet_production[cst.fer] = -1
effet.achetable = False
effet.symbole_chainage = [cst.symbole_phare]
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 2
carte.nb_joueurs = 3
carte.nom = "Vignoble"
carte.couleur = cst.jaune
effet.effet_gain_or_cartes_marron = [1, 1, 1]
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 2
carte.nb_joueurs = 3
carte.nom = "Forum"
carte.couleur = cst.jaune
carte.cout_ressource[cst.argile] = 2
carte.cout_chainage = cst.symbole_devanture
effet.effet_production[cst.verre] = -1
effet.effet_production[cst.tissu] = -1
effet.effet_production[cst.parchemin] = -1
effet.achetable = False
effet.symbole_chainage = [cst.symbole_tonneau]
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 3
carte.nb_joueurs = 3
carte.nom = "Palace"
carte.couleur = cst.bleu
carte.cout_ressource[cst.argile] = 1
carte.cout_ressource[cst.bois] = 1
carte.cout_ressource[cst.pierre] = 1
carte.cout_ressource[cst.fer] = 1
carte.cout_ressource[cst.parchemin] = 1
carte.cout_ressource[cst.tissu] = 1
carte.cout_ressource[cst.verre] = 1
effet.effet_points_victoire = 8
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 3
carte.nb_joueurs = 3
carte.nom = "Jardins"
carte.couleur = cst.bleu
carte.cout_ressource[cst.argile] = 2
carte.cout_ressource[cst.bois] = 1
carte.cout_chainage = cst.symbole_masque
effet.effet_points_victoire = 5
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 3
carte.nb_joueurs = 3
carte.nom = "Panthéon"
carte.couleur = cst.bleu
carte.cout_ressource[cst.argile] = 2
carte.cout_ressource[cst.fer] = 1
carte.cout_ressource[cst.verre] = 1
carte.cout_ressource[cst.parchemin] = 1
carte.cout_ressource[cst.tissu] = 1
carte.cout_chainage = cst.symbole_etoile
effet.effet_points_victoire = 7
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 3
carte.nb_joueurs = 3
carte.nom = "Hôtel-de-ville"
carte.couleur = cst.bleu
carte.cout_ressource[cst.pierre] = 2
carte.cout_ressource[cst.fer] = 1
carte.cout_ressource[cst.verre] = 1
effet.effet_points_victoire = 6
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 3
carte.nb_joueurs = 3
carte.nom = "Sénat"
carte.couleur = cst.bleu
carte.cout_ressource[cst.bois] = 2
carte.cout_ressource[cst.pierre] = 1
carte.cout_ressource[cst.fer] = 1
carte.cout_chainage = cst.symbole_temple
effet.effet_points_victoire = 6
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 3
carte.nb_joueurs = 3
carte.nom = "Étude"
carte.couleur = cst.vert
carte.cout_ressource[cst.bois] = 1
carte.cout_ressource[cst.tissu] = 1
carte.cout_ressource[cst.parchemin] = 1
carte.cout_chainage = cst.symbole_plume
effet.effet_symbole_scientifique[cst.rouage] = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 3
carte.nb_joueurs = 3
carte.nom = "Observatoire"
carte.couleur = cst.vert
carte.cout_ressource[cst.fer] = 2
carte.cout_ressource[cst.verre] = 1
carte.cout_ressource[cst.tissu] = 1
carte.cout_chainage = cst.symbole_planetes
effet.effet_symbole_scientifique[cst.rouage] = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 3
carte.nb_joueurs = 3
carte.nom = "Université"
carte.couleur = cst.vert
carte.cout_ressource[cst.bois] = 2
carte.cout_ressource[cst.verre] = 1
carte.cout_ressource[cst.parchemin] = 1
carte.cout_chainage = cst.symbole_parchemin
effet.effet_symbole_scientifique[cst.tablette] = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 3
carte.nb_joueurs = 3
carte.nom = "Académie"
carte.couleur = cst.vert
carte.cout_ressource[cst.pierre] = 3
carte.cout_ressource[cst.verre] = 1
carte.cout_chainage = cst.symbole_lyre
effet.effet_symbole_scientifique[cst.compas] = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 3
carte.nb_joueurs = 3
carte.nom = "Loge"
carte.couleur = cst.vert
carte.cout_ressource[cst.argile] = 2
carte.cout_ressource[cst.parchemin] = 1
carte.cout_ressource[cst.tissu] = 1
carte.cout_chainage = cst.symbole_torche
effet.effet_symbole_scientifique[cst.compas] = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 3
carte.nb_joueurs = 3
carte.nom = "Atelier-de-siège"
carte.couleur = cst.rouge
carte.cout_ressource[cst.argile] = 3
carte.cout_ressource[cst.bois] = 1
carte.cout_chainage = cst.symbole_scie
effet.effet_militaire = 3
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 3
carte.nb_joueurs = 3
carte.nom = "Fortifications"
carte.couleur = cst.rouge
carte.cout_ressource[cst.fer] = 3
carte.cout_ressource[cst.argile] = 1
carte.cout_chainage = cst.symbole_tour
effet.effet_militaire = 3
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 3
carte.nb_joueurs = 3
carte.nom = "Arsenal"
carte.couleur = cst.rouge
carte.cout_ressource[cst.bois] = 2
carte.cout_ressource[cst.fer] = 1
carte.cout_ressource[cst.tissu] = 1
effet.effet_militaire = 3
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 3
carte.nb_joueurs = 3
carte.nom = "Arène"
carte.couleur = cst.jaune
carte.cout_ressource[cst.pierre] = 2
carte.cout_ressource[cst.fer] = 1
carte.cout_chainage = cst.symbole_eclair
effet.effet_gain_or_etages = [None, 3, None]
effet.effet_gain_points_etages = [None, 1, None]
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 3
carte.nb_joueurs = 3
carte.nom = "Phare"
carte.couleur = cst.jaune
carte.cout_ressource[cst.pierre] = 1
carte.cout_ressource[cst.verre] = 1
carte.cout_chainage = cst.symbole_phare
effet.effet_gain_or_cartes_jaunes = [None, 1, None]
effet.effet_gain_points_cartes_jaunes = [None, 1, None]
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 3
carte.nb_joueurs = 3
carte.nom = "Port"
carte.couleur = cst.jaune
carte.cout_ressource[cst.bois] = 1
carte.cout_ressource[cst.fer] = 1
carte.cout_ressource[cst.tissu] = 1
carte.cout_chainage = cst.symbole_tonneau
effet.effet_gain_or_cartes_marron = [None, 1, None]
effet.effet_gain_points_cartes_marron = [None, 1, None]
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 3
carte.nb_joueurs = 3
carte.nom = "Guilde-des-artisans"
carte.couleur = cst.violet
carte.cout_ressource[cst.pierre] = 2
carte.cout_ressource[cst.fer] = 2
effet.effet_gain_points_cartes_grises = [2, None, 2]
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 3
carte.nb_joueurs = 3
carte.nom = "Guilde-des-armateurs"
carte.couleur = cst.violet
carte.cout_ressource[cst.bois] = 3
carte.cout_ressource[cst.verre] = 1
carte.cout_ressource[cst.parchemin] = 1
effet.effet_gain_points_cartes_marron = [None, 1, None]
effet.effet_gain_points_cartes_grises = [None, 1, None]
effet.effet_gain_points_cartes_violettes = [None, 1, None]
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 3
carte.nb_joueurs = 3
carte.nom = "Guilde-des-espions"
carte.couleur = cst.violet
carte.cout_ressource[cst.argile] = 2
carte.cout_ressource[cst.verre] = 1
effet.effet_gain_points_cartes_grises = [1, None, 1]
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 3
carte.nb_joueurs = 3
carte.nom = "Guilde-des-commercants"
carte.couleur = cst.violet
carte.cout_ressource[cst.parchemin] = 1
carte.cout_ressource[cst.verre] = 1
carte.cout_ressource[cst.tissu] = 1
effet.effet_gain_points_cartes_jaunes = [1, None, 1]
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 3
carte.nb_joueurs = 3
carte.nom = "Guilde-des-magistrats"
carte.couleur = cst.violet
carte.cout_ressource[cst.bois] = 3
carte.cout_ressource[cst.pierre] = 1
carte.cout_ressource[cst.tissu] = 1
effet.effet_gain_points_cartes_bleues = [1, None, 1]
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 3
carte.nb_joueurs = 3
carte.nom = "Guilde-des-travailleurs"
carte.couleur = cst.violet
carte.cout_ressource[cst.fer] = 2
carte.cout_ressource[cst.bois] = 1
carte.cout_ressource[cst.pierre] = 1
carte.cout_ressource[cst.argile] = 1
effet.effet_gain_points_cartes_marron = [1, None, 1]
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 3
carte.nb_joueurs = 3
carte.nom = "Guilde-des-philosophes"
carte.couleur = cst.violet
carte.cout_ressource[cst.argile] = 3
carte.cout_ressource[cst.parchemin] = 1
carte.cout_ressource[cst.tissu] = 1
effet.effet_gain_points_cartes_vertes = [1, None, 1]
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 3
carte.nb_joueurs = 3
carte.nom = "Guilde-des-bâtisseurs"
carte.couleur = cst.violet
carte.cout_ressource[cst.pierre] = 3
carte.cout_ressource[cst.argile] = 2
carte.cout_ressource[cst.verre] = 1
effet.effet_gain_points_etages = [1, 1, 1]
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 3
carte.nb_joueurs = 3
carte.nom = "Guilde-des-décorateurs"
carte.couleur = cst.violet
carte.cout_ressource[cst.fer] = 2
carte.cout_ressource[cst.pierre] = 1
carte.cout_ressource[cst.tissu] = 1
effet.effet_gain_points_cartes_merveille_complete = True
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 3
carte.nb_joueurs = 3
carte.nom = "Guilde-des-scientifiques"
carte.couleur = cst.violet
carte.cout_ressource[cst.bois] = 2
carte.cout_ressource[cst.fer] = 2
carte.cout_ressource[cst.parchemin] = 1
effet.effet_symbole_scientifique[cst.rouage] = -1
effet.effet_symbole_scientifique[cst.tablette] = -1
effet.effet_symbole_scientifique[cst.compas] = -1
carte.effet = effet
paquet_cartes.append(carte)

#endregion

#region Cartes 4 joueurs
carte = Carte()
effet = Effet()
carte.age = 1
carte.nb_joueurs = 4
carte.nom = "Puits"
carte.couleur = cst.bleu
effet.effet_points_victoire = 3
effet.symbole_chainage = [cst.symbole_marteau]
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 1
carte.nb_joueurs = 4
carte.nom = "Scriptorium"
carte.couleur = cst.vert
carte.symbole_chainage = [cst.symbole_balance, cst.symbole_livre]
carte.cout_ressource[cst.parchemin] = 1
effet.effet_symbole_scientifique[cst.tablette] = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 1
carte.nb_joueurs = 4
carte.nom = "Chantier"
carte.couleur = cst.marron
effet.effet_production[cst.bois] = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 1
carte.nb_joueurs = 4
carte.nom = "Filon"
carte.couleur = cst.marron
effet.effet_production[cst.fer] = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 1
carte.nb_joueurs = 4
carte.nom = "Excavation"
carte.couleur = cst.marron
carte.cout_ressource[cst.argent] = 1
effet.effet_production[cst.pierre] = -1
effet.effet_production[cst.argile] = -1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 1
carte.nb_joueurs = 4
carte.nom = "Tour-de-garde"
carte.couleur = cst.rouge
carte.cout_ressource[cst.argile] = 1
effet.effet_militaire = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 1
carte.nb_joueurs = 4
carte.nom = "Taverne"
carte.couleur = cst.jaune
effet.effet_tresor = 5
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 2
carte.nb_joueurs = 4
carte.nom = "Carrière"
carte.couleur = cst.marron
carte.cout_ressource[cst.argent] = 1
effet.effet_production[cst.pierre] = 2
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 2
carte.nb_joueurs = 4
carte.nom = "Fonderie"
carte.couleur = cst.marron
carte.cout_ressource[cst.argent] = 1
effet.effet_production[cst.fer] = 2
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 2
carte.nb_joueurs = 4
carte.nom = "Scierie"
carte.couleur = cst.marron
carte.cout_ressource[cst.argent] = 1
effet.effet_production[cst.bois] = 2
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 2
carte.nb_joueurs = 4
carte.nom = "Briquetterie"
carte.couleur = cst.marron
carte.cout_ressource[cst.argent] = 1
effet.effet_production[cst.argile] = 2
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 2
carte.nb_joueurs = 4
carte.nom = "Dispensaire"
carte.couleur = cst.vert
carte.cout_ressource[cst.fer] = 2
carte.cout_ressource[cst.verre] = 1
carte.cout_chainage = cst.symbole_bol
effet.symbole_chainage = [cst.symbole_eclair, cst.symbole_torche]
effet.effet_symbole_scientifique[cst.compas] = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 2
carte.nb_joueurs = 4
carte.nom = "Bazar"
carte.couleur = cst.jaune
effet.effet_gain_or_cartes_marron = [2, 2, 2]
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 2
carte.nb_joueurs = 4
carte.nom = "Place-d'armes"
carte.couleur = cst.jaune
carte.cout_ressource[cst.fer] = 2
carte.cout_ressource[cst.bois] = 1
effet.effet_militaire = 2
effet.symbole_chainage = [cst.symbole_casque]
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 3
carte.nb_joueurs = 4
carte.nom = "Jardins"
carte.couleur = cst.bleu
carte.cout_ressource[cst.argile] = 2
carte.cout_ressource[cst.bois] = 1
carte.cout_chainage = cst.symbole_masque
effet.effet_points_victoire = 5
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 3
carte.nb_joueurs = 4
carte.nom = "Port"
carte.couleur = cst.jaune
carte.cout_ressource[cst.bois] = 1
carte.cout_ressource[cst.fer] = 1
carte.cout_ressource[cst.tissu] = 1
carte.cout_chainage = cst.symbole_tonneau
effet.effet_gain_or_cartes_marron = [None, 1, None]
effet.effet_gain_points_cartes_marron = [None, 1, None]
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 3
carte.nb_joueurs = 4
carte.nom = "Chambre-de-commerce"
carte.couleur = cst.jaune
carte.cout_ressource[cst.argile] = 2
carte.cout_ressource[cst.parchemin] = 1
effet.effet_gain_or_cartes_grises = [None, 2, None]
effet.effet_gain_points_cartes_grises = [None, 2, None]
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 3
carte.nb_joueurs = 4
carte.nom = "Cirque"
carte.couleur = cst.rouge
carte.cout_ressource[cst.pierre] = 3
carte.cout_ressource[cst.fer] = 1
carte.cout_chainage = cst.symbole_casque
effet.effet_militaire = 3
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 3
carte.nb_joueurs = 4
carte.nom = "Castrum"
carte.couleur = cst.rouge
carte.cout_ressource[cst.argile] = 2
carte.cout_ressource[cst.bois] = 1
carte.cout_ressource[cst.parchemin] = 1
effet.effet_militaire = 3
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 3
carte.nb_joueurs = 4
carte.nom = "Université"
carte.couleur = cst.vert
carte.cout_ressource[cst.bois] = 2
carte.cout_ressource[cst.verre] = 1
carte.cout_ressource[cst.parchemin] = 1
carte.cout_chainage = cst.symbole_parchemin
effet.effet_symbole_scientifique[cst.tablette] = 1
carte.effet = effet
paquet_cartes.append(carte)

#endregion

#region Cartes 5 joueurs
carte = Carte()
effet = Effet()
carte.age = 1
carte.nb_joueurs = 5
carte.nom = "Autel"
carte.couleur = cst.bleu
carte.symbole_chainage = [cst.symbole_etoile]
effet.effet_points_victoire = 3
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 1
carte.nb_joueurs = 5
carte.nom = "Bassin-argileux"
carte.couleur = cst.marron
effet.effet_production[cst.argile] = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 1
carte.nb_joueurs = 5
carte.nom = "Cavité"
carte.couleur = cst.marron
effet.effet_production[cst.pierre] = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 1
carte.nb_joueurs = 5
carte.nom = "Gisement"
carte.couleur = cst.marron
carte.cout_ressource[cst.argent] = 1
effet.effet_production[cst.bois] = 1
effet.effet_production[cst.fer] = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 1
carte.nb_joueurs = 5
carte.nom = "Officine"
carte.couleur = cst.vert
carte.symbole_chainage = [cst.symbole_fer_a_cheval, cst.symbole_bol]
carte.cout_ressource[cst.tissu] = 1
effet.effet_symbole_scientifique[cst.compas] = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 1
carte.nb_joueurs = 5
carte.nom = "Taverne"
carte.couleur = cst.jaune
effet.effet_tresor = 5
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 1
carte.nb_joueurs = 5
carte.nom = "Caserne"
carte.couleur = cst.rouge
carte.cout_ressource[cst.fer] = 1
effet.effet_militaire = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 2
carte.nb_joueurs = 5
carte.nom = "Caravansérail"
carte.couleur = cst.jaune
carte.cout_ressource[cst.bois] = 2
carte.cout_chainage = cst.symbole_chameau
effet.effet_production[cst.bois] = -1
effet.effet_production[cst.argile] = -1
effet.effet_production[cst.pierre] = -1
effet.effet_production[cst.fer] = -1
effet.achetable = False
effet.symbole_chainage = [cst.symbole_phare]
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 2
carte.nb_joueurs = 5
carte.nom = "Tribunal"
carte.couleur = cst.bleu
carte.cout_chainage = cst.symbole_balance
carte.cout_ressource[cst.argile] = 2
carte.cout_ressource[cst.tissu] = 1
effet.effet_points_victoire = 4
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 2
carte.nb_joueurs = 5
carte.nom = "Métier-à-tisser"
carte.couleur = cst.gris
effet.effet_production[cst.tissu] = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 2
carte.nb_joueurs = 5
carte.nom = "Presse"
carte.couleur = cst.gris
effet.effet_production[cst.parchemin] = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 2
carte.nb_joueurs = 5
carte.nom = "Verrerie"
carte.couleur = cst.gris
effet.effet_production[cst.verre] = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 2
carte.nb_joueurs = 5
carte.nom = "Laboratoire"
carte.couleur = cst.vert
carte.cout_ressource[cst.argile] = 2
carte.cout_ressource[cst.parchemin] = 1
carte.cout_chainage = cst.symbole_lampe
effet.symbole_chainage = [cst.symbole_planetes, cst.symbole_scie]
effet.effet_symbole_scientifique[cst.rouage] = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 2
carte.nb_joueurs = 5
carte.nom = "Écuries"
carte.couleur = cst.rouge
carte.cout_ressource[cst.bois] = 1
carte.cout_ressource[cst.fer] = 1
carte.cout_ressource[cst.argile] = 1
carte.cout_chainage = cst.symbole_fer_a_cheval
effet.effet_militaire = 2
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 3
carte.nb_joueurs = 5
carte.nom = "Sénat"
carte.couleur = cst.bleu
carte.cout_ressource[cst.bois] = 2
carte.cout_ressource[cst.pierre] = 1
carte.cout_ressource[cst.fer] = 1
carte.cout_chainage = cst.symbole_temple
effet.effet_points_victoire = 6
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 3
carte.nb_joueurs = 5
carte.nom = "Étude"
carte.couleur = cst.vert
carte.cout_ressource[cst.bois] = 1
carte.cout_ressource[cst.tissu] = 1
carte.cout_ressource[cst.parchemin] = 1
carte.cout_chainage = cst.symbole_plume
effet.effet_symbole_scientifique[cst.rouage] = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 3
carte.nb_joueurs = 5
carte.nom = "Arsenal"
carte.couleur = cst.rouge
carte.cout_ressource[cst.bois] = 2
carte.cout_ressource[cst.fer] = 1
carte.cout_ressource[cst.tissu] = 1
effet.effet_militaire = 3
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 3
carte.nb_joueurs = 5
carte.nom = "Atelier-de-siège"
carte.couleur = cst.rouge
carte.cout_ressource[cst.argile] = 3
carte.cout_ressource[cst.bois] = 1
carte.cout_chainage = cst.symbole_scie
effet.effet_militaire = 3
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 3
carte.nb_joueurs = 5
carte.nom = "Arène"
carte.couleur = cst.jaune
carte.cout_ressource[cst.pierre] = 2
carte.cout_ressource[cst.fer] = 1
carte.cout_chainage = cst.symbole_eclair
effet.effet_gain_or_etages = [None, 3, None]
effet.effet_gain_points_etages = [None, 1, None]
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 3
carte.nb_joueurs = 5
carte.nom = "Ludus"
carte.couleur = cst.jaune
carte.cout_ressource[cst.pierre] = 1
carte.cout_ressource[cst.fer] = 1
carte.cout_chainage = cst.symbole_eclair
effet.effet_gain_or_cartes_rouges = [None, 3, None]
effet.effet_gain_points_cartes_rouges = [None, 1, None]
carte.effet = effet
paquet_cartes.append(carte)

#endregion


#region Cartes âge 6
carte = Carte()
effet = Effet()
carte.age = 1
carte.nb_joueurs = 6
carte.nom = "Théâtre"
carte.couleur = cst.bleu
carte.symbole_chainage = [cst.symbole_masque]
effet.effet_points_victoire = 3
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 1
carte.nb_joueurs = 6
carte.nom = "Marché"
carte.couleur = cst.jaune
carte.symbole_chainage = [cst.symbole_chameau]
effet.effet_reduction_gauche_manufacture = True
effet.effet_reduction_droite_manufacture = True
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 1
carte.nb_joueurs = 6
carte.nom = "Mine"
carte.couleur = cst.marron
carte.cout_ressource[cst.argent] = 1
effet.effet_production[cst.pierre] = 1
effet.effet_production[cst.fer] = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 1
carte.nb_joueurs = 6
carte.nom = "Friche"
carte.couleur = cst.marron
carte.cout_ressource[cst.argent] = 1
effet.effet_production[cst.argile] = 1
effet.effet_production[cst.bois] = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 1
carte.nb_joueurs = 6
carte.nom = "Métier-à-tisser"
carte.couleur = cst.gris
effet.effet_production[cst.tissu] = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 1
carte.nb_joueurs = 6
carte.nom = "Verrerie"
carte.couleur = cst.gris
effet.effet_production[cst.verre] = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 1
carte.nb_joueurs = 6
carte.nom = "Presse"
carte.couleur = cst.gris
effet.effet_production[cst.parchemin] = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 2
carte.nb_joueurs = 6
carte.nom = "Caravansérail"
carte.couleur = cst.jaune
carte.cout_ressource[cst.bois] = 2
carte.cout_chainage = cst.symbole_chameau
effet.effet_production[cst.bois] = -1
effet.effet_production[cst.argile] = -1
effet.effet_production[cst.pierre] = -1
effet.effet_production[cst.fer] = -1
effet.achetable = False
effet.symbole_chainage = [cst.symbole_phare]
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 2
carte.nb_joueurs = 6
carte.nom = "Temple"
carte.couleur = cst.bleu
carte.cout_ressource[cst.bois] = 1
carte.cout_ressource[cst.argile] = 1
carte.cout_ressource[cst.verre] = 1
effet.effet_points_victoire = 4
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 2
carte.nb_joueurs = 6
carte.nom = "Bibliothèque"
carte.couleur = cst.vert
carte.cout_ressource[cst.pierre] = 2
carte.cout_ressource[cst.tissu] = 1
carte.cout_chainage = cst.symbole_livre
effet.symbole_chainage = [cst.symbole_temple, cst.symbole_parchemin]
effet.effet_symbole_scientifique[cst.tablette] = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 2
carte.nb_joueurs = 6
carte.nom = "Place-d'armes"
carte.couleur = cst.jaune
carte.cout_ressource[cst.fer] = 2
carte.cout_ressource[cst.bois] = 1
effet.effet_militaire = 2
effet.symbole_chainage = [cst.symbole_casque]
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 2
carte.nb_joueurs = 6
carte.nom = "Champs-de-tir"
carte.couleur = cst.rouge
carte.cout_ressource[cst.bois] = 2
carte.cout_ressource[cst.fer] = 1
carte.cout_chainage = cst.symbole_cible
effet.effet_militaire = 2
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 2
carte.nb_joueurs = 6
carte.nom = "Vignoble"
carte.couleur = cst.jaune
effet.effet_gain_or_cartes_marron = [1, 1, 1]
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 2
carte.nb_joueurs = 6
carte.nom = "Forum"
carte.couleur = cst.jaune
carte.cout_ressource[cst.argile] = 2
carte.cout_chainage = cst.symbole_devanture
effet.effet_production[cst.verre] = -1
effet.effet_production[cst.tissu] = -1
effet.effet_production[cst.parchemin] = -1
effet.achetable = False
effet.symbole_chainage = [cst.symbole_tonneau]
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 3
carte.nb_joueurs = 6
carte.nom = "Phare"
carte.couleur = cst.jaune
carte.cout_ressource[cst.pierre] = 1
carte.cout_ressource[cst.verre] = 1
carte.cout_chainage = cst.symbole_phare
effet.effet_gain_or_cartes_jaunes = [None, 1, None]
effet.effet_gain_points_cartes_jaunes = [None, 1, None]
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 3
carte.nb_joueurs = 6
carte.nom = "Chambre-de-commerce"
carte.couleur = cst.jaune
carte.cout_ressource[cst.argile] = 2
carte.cout_ressource[cst.parchemin] = 1
effet.effet_gain_or_cartes_grises = [None, 2, None]
effet.effet_gain_points_cartes_grises = [None, 2, None]
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 3
carte.nb_joueurs = 6
carte.nom = "Loge"
carte.couleur = cst.vert
carte.cout_ressource[cst.argile] = 2
carte.cout_ressource[cst.parchemin] = 1
carte.cout_ressource[cst.tissu] = 1
carte.cout_chainage = cst.symbole_torche
effet.effet_symbole_scientifique[cst.compas] = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 3
carte.nb_joueurs = 6
carte.nom = "Cirque"
carte.couleur = cst.rouge
carte.cout_ressource[cst.pierre] = 3
carte.cout_ressource[cst.fer] = 1
carte.cout_chainage = cst.symbole_casque
effet.effet_militaire = 3
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 3
carte.nb_joueurs = 6
carte.nom = "Panthéon"
carte.couleur = cst.bleu
carte.cout_ressource[cst.argile] = 2
carte.cout_ressource[cst.fer] = 1
carte.cout_ressource[cst.verre] = 1
carte.cout_ressource[cst.parchemin] = 1
carte.cout_ressource[cst.tissu] = 1
carte.cout_chainage = cst.symbole_etoile
effet.effet_points_victoire = 7
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 3
carte.nb_joueurs = 6
carte.nom = "Hôtel-de-ville"
carte.couleur = cst.bleu
carte.cout_ressource[cst.pierre] = 2
carte.cout_ressource[cst.fer] = 1
carte.cout_ressource[cst.verre] = 1
effet.effet_points_victoire = 6
carte.effet = effet
paquet_cartes.append(carte)

#endregion

#region Cartes âge 7
carte = Carte()
effet = Effet()
carte.age = 1
carte.nb_joueurs = 7
carte.nom = "Palissade"
carte.couleur = cst.rouge
carte.cout_ressource[cst.bois] = 1
effet.effet_militaire = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 1
carte.nb_joueurs = 7
carte.nom = "Atelier"
carte.couleur = cst.vert
carte.symbole_chainage = [cst.symbole_cible, cst.symbole_lampe]
carte.cout_ressource[cst.verre] = 1
effet.effet_symbole_scientifique[cst.rouage] = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 1
carte.nb_joueurs = 7
carte.nom = "Puits"
carte.couleur = cst.bleu
effet.effet_points_victoire = 3
effet.symbole_chainage = [cst.symbole_marteau]
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 1
carte.nb_joueurs = 7
carte.nom = "Bains"
carte.couleur = cst.bleu
carte.symbole_chainage = [cst.symbole_goutte]
carte.cout_ressource[cst.pierre] = 1
effet.effet_points_victoire = 3
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 1
carte.nb_joueurs = 7
carte.nom = "Taverne"
carte.couleur = cst.jaune
effet.effet_tresor = 5
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 1
carte.nb_joueurs = 7
carte.nom = "Comptoir-ouest"
carte.couleur = cst.jaune
carte.symbole_chainage = [cst.symbole_devanture]
effet.effet_reduction_gauche_base = True
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 1
carte.nb_joueurs = 7
carte.nom = "Comptoir-est"
carte.couleur = cst.jaune
carte.symbole_chainage = [cst.symbole_devanture]
effet.effet_reduction_droite_base = True
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 2
carte.nb_joueurs = 7
carte.nom = "Aqueduc"
carte.couleur = cst.bleu
carte.cout_chainage = cst.symbole_goutte
carte.cout_ressource[cst.pierre] = 3
effet.effet_points_victoire = 5
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 2
carte.nb_joueurs = 7
carte.nom = "Statue"
carte.couleur = cst.bleu
carte.cout_chainage = cst.symbole_marteau
carte.cout_ressource[cst.fer] = 2
carte.cout_ressource[cst.bois] = 1
effet.effet_points_victoire = 4
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 2
carte.nb_joueurs = 7
carte.nom = "École"
carte.couleur = cst.vert
carte.cout_ressource[cst.bois] = 1
carte.cout_ressource[cst.parchemin] = 1
effet.symbole_chainage = [cst.symbole_lyre, cst.symbole_plume]
effet.effet_symbole_scientifique[cst.tablette] = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 2
carte.nb_joueurs = 7
carte.nom = "Place-d'armes"
carte.couleur = cst.jaune
carte.cout_ressource[cst.fer] = 2
carte.cout_ressource[cst.bois] = 1
effet.effet_militaire = 2
effet.symbole_chainage = [cst.symbole_casque]
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 2
carte.nb_joueurs = 7
carte.nom = "Muraille"
carte.couleur = cst.rouge
carte.cout_ressource[cst.pierre] = 3
effet.effet_militaire = 2
effet.symbole_chainage = [cst.symbole_tour]
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 2
carte.nb_joueurs = 7
carte.nom = "Bazar"
carte.couleur = cst.jaune
effet.effet_gain_or_cartes_marron = [2, 2, 2]
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 2
carte.nb_joueurs = 7
carte.nom = "Forum"
carte.couleur = cst.jaune
carte.cout_ressource[cst.argile] = 2
carte.cout_chainage = cst.symbole_devanture
effet.effet_production[cst.verre] = -1
effet.effet_production[cst.tissu] = -1
effet.effet_production[cst.parchemin] = -1
effet.achetable = False
effet.symbole_chainage = [cst.symbole_tonneau]
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 3
carte.nb_joueurs = 7
carte.nom = "Castrum"
carte.couleur = cst.rouge
carte.cout_ressource[cst.argile] = 2
carte.cout_ressource[cst.bois] = 1
carte.cout_ressource[cst.parchemin] = 1
effet.effet_militaire = 3
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 3
carte.nb_joueurs = 7
carte.nom = "Fortifications"
carte.couleur = cst.rouge
carte.cout_ressource[cst.fer] = 3
carte.cout_ressource[cst.argile] = 1
carte.cout_chainage = cst.symbole_tour
effet.effet_militaire = 3
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 3
carte.nb_joueurs = 7
carte.nom = "Observatoire"
carte.couleur = cst.vert
carte.cout_ressource[cst.fer] = 2
carte.cout_ressource[cst.verre] = 1
carte.cout_ressource[cst.tissu] = 1
carte.cout_chainage = cst.symbole_planetes
effet.effet_symbole_scientifique[cst.rouage] = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 3
carte.nb_joueurs = 7
carte.nom = "Académie"
carte.couleur = cst.vert
carte.cout_ressource[cst.pierre] = 3
carte.cout_ressource[cst.verre] = 1
carte.cout_chainage = cst.symbole_lyre
effet.effet_symbole_scientifique[cst.compas] = 1
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 3
carte.nb_joueurs = 7
carte.nom = "Palace"
carte.couleur = cst.bleu
carte.cout_ressource[cst.argile] = 1
carte.cout_ressource[cst.bois] = 1
carte.cout_ressource[cst.pierre] = 1
carte.cout_ressource[cst.fer] = 1
carte.cout_ressource[cst.parchemin] = 1
carte.cout_ressource[cst.tissu] = 1
carte.cout_ressource[cst.verre] = 1
effet.effet_points_victoire = 8
carte.effet = effet
paquet_cartes.append(carte)

carte = Carte()
effet = Effet()
carte.age = 3
carte.nb_joueurs = 7
carte.nom = "Ludus"
carte.couleur = cst.jaune
carte.cout_ressource[cst.pierre] = 1
carte.cout_ressource[cst.fer] = 1
carte.cout_chainage = cst.symbole_eclair
effet.effet_gain_or_cartes_rouges = [None, 3, None]
effet.effet_gain_points_cartes_rouges = [None, 1, None]
carte.effet = effet
paquet_cartes.append(carte)

#endregion