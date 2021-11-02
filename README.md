# OC_P7_AlgoInvestTrade
Projet n°7 de la Formation Développeur d'Applications Python d'OpenClassrooms

Programme développé pour une société d'investissement financier fictive.  
AlgoInvest&Trade est une société financière spécialisée dans l’investissement.  
La société cherche à optimiser ses stratégies d’investissement à l’aide d’algorithmes, afin de dégager davantage de bénéfices pour ses clients.  
  
2 algorithmes ont été développés. 

## Contraintes

- La valeur d'un portefeuille ne doit pas dépasser 500€.  
- Une même action ne doit pas être achetée 2 fois.  
- Il n'est pas possible d'acheter des fractions d'action.

## Algorithme Bruteforce
L’algorithme de force brute commence par créer toutes les combinaisons possible de portefeuille au format binaire.  
Ensuite, il créé tout ces portefeuilles à partir du dataset sélectionné.  
Pour terminer, il classe tout les portefeuilles du plus ou moins rentable, et donne en sortie la meilleure combinaison possible d’investissement.   
Attention: Ne pas utiliser l'algorithme sur un dataset de plus de 100 actions sous peine d'un freeze de la machine.  
En effet, l'algorithme de bruteforce calculera 2**n possibilités de combinaisons, n étant le nombre d'actions.

## Algorithme Optimisé
Après avoir supprimé les actions invalides (rendement ou prix inférieur ou égal à 0), l’algorithme optimisé commence par classer toutes les actions de la plus rentable à la moins rentable.  
Ensuite, il créé un portefeuille en lui ajoutant une par une les actions tant que le budget de 500€ n’est pas entièrement consommé.  
Il s’agit d’un algorithme glouton basé sur le problème du sac à dos.

## Installation & lancement:
Commencez tout d'abord par installer Python.  
Lancez ensuite la console, placez vous dans le dossier de votre choix puis clonez ce repository:
```
git clone https://github.com/FlorianMgs/OC_P7_AlgoInvestTrade.git
```
Placez vous dans le dossier OC_P7_AlgoInvestTrade, puis créez un nouvel environnement virtuel:
```
python -m venv env
```
Ensuite, activez-le.
Windows:
```
env\scripts\activate.bat
```
Linux:
```
source env/bin/activate
```
Il ne reste plus qu'à installer les packages requis:
```
pip install -r requirements.txt
```
Vous pouvez enfin lancer le script:
```
python main.py
```
