def ajouter_source(T_src, x_init, y_init, univers):
    """
    Cette fonction initialise l'univers vierge en lui ajoutant la source
    à la température T_src à la coordonnée (x_init, y_init)
    """

    # On modifie uniquement les valeurs concernées par la source de chaleur
    univers[y_init, x_init] = T_src

    return univers


def ajouter_plusieurs_sources(l_src, univers):
    """
    Cette fonction initialise l'univers vierge en lui ajoutant plusieurs sources de chaleur
    l_src est une liste de listes de la forme [[T_src1, x_src1, y_src1], [T_src2, x_src2, y_src2]]
    """

    # On modifie uniquement les valeurs concernées par les sources de chaleur
    for source in l_src:
        univers = ajouter_source(source[0], source[1], source[2], univers)

    return univers
