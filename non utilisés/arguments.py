# On a choisi de ne pas implémenter une utilisation dirrectement en ligne de commande car peut pertinante


import argparse


def arguments():
    """
    On utilise cette fonction pour obtenir toutes les variables que peut selectionner un utilisateur à travers le terminal
    """
    parser = argparse.ArgumentParser()

    # Variables obligatoires
    parser.add_argument(
        "--univers",
        nargs=5,
        help="""
            passe les arguments dirrectement à l'affichage sans fenetre utilisateur
            ordre des arguments : D univers sources n dt
            D : coeficient de diffusion thermique
            univers : liste de liste des température
            sources : liste de liste de température et positions x et y
            n : nombre de tour de la simulation
            dt : pas de temps
            """)

    return parser.parse_args()
