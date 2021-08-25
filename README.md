# Loi de distribution de Benford

Wikipedia : https://fr.wikipedia.org/wiki/Loi_de_Benford

La loi de Benford, initialement appelée loi des nombres anormaux par Benford1, fait référence à une fréquence de distribution statistique observée empiriquement sur de nombreuses sources de données dans la vraie vie, ainsi qu'en mathématiques.

Dans une série de données numériques, on pourrait s'attendre à voir les chiffres de 1 à 9 apparaître à peu près aussi fréquemment comme premier chiffre significatif, soit avec une fréquence de 1/9 = 11,1 % pour chacun. Or, contrairement à cette intuition (biais d'équiprobabilité), la série suit très souvent approximativement la loi de Benford : pour près du tiers des données, le 1er chiffre significatif le plus fréquent est le 1. Viennent ensuite le chiffre 2, puis le 3, etc., et la probabilité d'avoir un 9 comme premier chiffre significatif n'est que de 4,6 %. C'est une loi observée aussi bien dans les mathématiques sociales, c'est-à-dire les sciences humaines et sociales, que dans des tables de valeurs numériques comme celles qu'on rencontre en physique, en volcanologie, génétique, en BTP, en économie (taux de change), ou même dans les numéros de rue de son carnet d'adresses.

La fréquence d'apparition du premier chiffre significatif (1 à 9) suit une courbe logarithmique : log10 (1+ 1/c)
  
![Benford curve](https://upload.wikimedia.org/wikipedia/commons/b/b7/Loi_de_Benford_freq_relat.PNG)  

On vérifie que la somme de ces fréquences vaut log(10) = 1.

# Python

Le programme se propose de tirer 100 nombres qui sont un produit de 2 ou plus nombres aléatoires entre 1 et max=10000.
Ensuite on prend le premier chiffre significatifs de ces produits (1 à 9) et de les dénombrer.

Le résultat est mis dans une liste freq qu'on affiche en comparaison avec la courbe théorique de Benford.

![Benford curve](Loi_de_Benford_freq_relat.PNG) 


