def evolution_cellule(univers, h, D, lambda_0, T_amb, x, y, dt, dx=0.1):
    '''
    Cette fonction détermine pour une cellule donnée
    de coordonnées x,y la température à l'instant t+dt
    '''

    # on choisit un dx par défaut égal à 0.1, et on considère que dy = dx
    dy = dx
    T = univers[y, x]    # désigne la température à un instant t

    # on détermine l'étape suivante pour tous les cas possibles : pour cela on doit d'abord
    # déterminer les températures des cellules voisines :
    # T_x_1 désigne la température de la cellule à gauche
    # T_x_2 désigne la température de la cellule à droite
    # T_y_1 désigne la température de la cellule au dessus
    # T_y_2 désigne la température de la cellule au dessous

    # 4 premiers cas : la cellule est située sur un des bords mais pas sur un des coins
    if x == len(univers[0]) - 1 and 0 < y < len(univers) - 1:
        T_x_2 = T_amb
        T_x_1 = univers[y, x-1]
        T_y_2 = univers[y+1, x]
        T_y_1 = univers[y-1, x]

        T_dt = (lambda_0/(lambda_0 + h*dx))*T_x_1 + (h/(h + lambda_0/dx))*T_x_2

    elif x == 0 and 0 < y < len(univers) - 1:
        T_x_1 = T_amb
        T_x_2 = univers[y, x+1]
        T_y_2 = univers[y+1, x]
        T_y_1 = univers[y-1, x]

        T_dt = (lambda_0/(lambda_0 + h*dx))*T_x_2 + (h/(h + lambda_0/dx))*T_x_1

    elif y == len(univers) - 1 and 0 < x < len(univers[0]) - 1:
        T_y_2 = T_amb
        T_x_2 = univers[y, x+1]
        T_x_1 = univers[y, x-1]
        T_y_1 = univers[y-1, x]

        T_dt = (lambda_0/(lambda_0 + h*dy))*T_y_1 + (h/(h + lambda_0/dy))*T_y_2

    elif y == 0 and 0 < x < len(univers[0]) - 1:
        T_y_1 = T_amb
        T_x_2 = univers[y, x+1]
        T_x_1 = univers[y, x-1]
        T_y_2 = univers[y+1, x]

        T_dt = (lambda_0/(lambda_0 + h*dy))*T_y_2 + (h/(h + lambda_0/dy))*T_y_1

    # 4 cas suivants : la cellule est située sur un des coins
    elif x == 0 and y == 0:
        T_y_1 = T_amb
        T_x_2 = univers[y, x+1]
        T_x_1 = T_amb
        T_y_2 = univers[y+1, x]

        T_dt = ((lambda_0/(lambda_0 + h*dy))*T_y_2 + (h/(h + lambda_0/dy))*T_y_1 +
                (lambda_0/(lambda_0 + h*dx))*T_x_2 + (h/(h + lambda_0/dx))*T_x_1)/2

    elif x == 0 and y == len(univers) - 1:
        T_x_1 = T_amb
        T_x_2 = univers[y, x+1]
        T_y_2 = T_amb
        T_y_1 = univers[y-1, x]

        T_dt = ((lambda_0/(lambda_0 + h*dx))*T_x_2 + (h/(h + lambda_0/dx))*T_x_1 +
                (lambda_0/(lambda_0 + h*dy))*T_y_1 + (h/(h + lambda_0/dy))*T_y_2)/2

    elif x == len(univers[0]) - 1 and y == 0:
        T_y_1 = T_amb
        T_x_2 = T_amb
        T_x_1 = univers[y, x-1]
        T_y_2 = univers[y+1, x]

        T_dt = ((lambda_0/(lambda_0 + h*dx))*T_x_1 + (h/(h + lambda_0/dx))*T_x_2 +
                (lambda_0/(lambda_0 + h*dy))*T_y_2 + (h/(h + lambda_0/dy))*T_y_1)/2

    elif x == len(univers[0]) - 1 and y == len(univers) - 1:
        T_y_2 = T_amb
        T_x_2 = T_amb
        T_x_1 = univers[y, x-1]
        T_y_1 = univers[y-1, x]

        T_dt = ((lambda_0/(lambda_0 + h*dx))*T_x_1 + (h/(h + lambda_0/dx))*T_x_2 +
                (lambda_0/(lambda_0 + h*dy))*T_y_1 + (h/(h + lambda_0/dy))*T_y_2)/2

    # dernier cas : la cellule n'est pas située en bordure de l'univers
    else:
        T_x_2 = univers[y, x+1]
        T_x_1 = univers[y, x-1]
        T_y_2 = univers[y+1, x]
        T_y_1 = univers[y-1, x]

    # on utilise l'équation de la chaleur avec une différenciation finie
    # T_dt désigne la température à l'instant t+dt
        T_dt = T + dt * D * ((T_x_2 + T_x_1 - 2 * T)/(dx**2) +
                             (T_y_2 + T_y_1 - 2 * T)/(dy**2))
    return T_dt
