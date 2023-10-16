# Simulation diffusion thermique

## Contributeurs
- Xavier Fiat
- Charlotte Allard
- Elise Meissirel
- Virgile Rapegno

## Description
Notre projet permet de visualiser la diffusion thermique dans un matériau donné soumis à des conditions initiales et exposé à des sources de chaleur. \
L'utilisateur peut choisir le matériau utilisé parmi une liste de matériaux usuels prédéfinie, la température initiale des cellules et la position et température des sources de chaleur.

## Utilisation
Pour lancer le code, exécutez le fichier \_\_main\_\_.py. \
L'utilisateur choisit alors la taille de l'univers et le matériau grâce à un menu déroulant. \
On prend en compte les échanges aux bords par conducto-convection. Il faut choisir le milieu et sa température (fixe comme un thermostat). \
Il modifie ensuite les températures des cellules, en précisant s'il s'agit d'une source fixe de chaleur avec l'ajout de '*'. \
Ou il fournit une liste cette fois uniquement de sources de chaleur avec le format T1,x1,y1;T2,x2,y2... \
La simulation peut alors commencer.

## Dépendance
Il est nécessaire d'avoir les packages suivants:
- numpy
- matplotlib
- tkinter
- time

## Consigne de contribution

Projet étudiant, il n'est pas possible de contribuer, mais vous pouvez toujours nous donner votre avis.
