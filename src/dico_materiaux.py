# On crée un dictionnaire avec la diffusivité thermique de différents matériaux.
dico_materiaux = {
    'Aluminium': 98.8*10**(-6),
    'Plomb': 23.9*10**(-6),
    'Fer': 22.8*10**(-6),
    'Cuivre': 117*10**(-6),
    'Zinc': 44*10**(-6),
    'Argent': 173*10**(-6),
    'Or': 127.2*10**(-6)
}

# On crée un dictionnaire avec les coefficients de conductivité thermique.
dico_lambda = {
    'Aluminium': 237,
    'Plomb': 35,
    'Fer': 80,
    'Cuivre': 390,
    'Zinc': 116,
    'Argent': 418,
    'Or': 317
}

# Cette liste est utilisée pour le menu déroulant
liste_materiau = dico_materiaux.keys()
