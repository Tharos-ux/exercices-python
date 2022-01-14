import random
import unittest
from unittest.main import main
from unittest.mock import patch
import io
import sys
import exercices

""" Il est conseillé d'utiliser la commande
python -m unittest -v tests.py
dans un shell afin d'exécuter les tests unitaires.
"""

def documentation():
    "Affiche la doc utilisateur"
    print("\nIl est conseillé d'utiliser la commande\n\"python -m unittest -v tests.py\"\ndans un shell afin d'exécuter les tests unitaires.\n")

class TestMethods(unittest.TestCase):

############################# UNITTEST ##################################

    def test_raiseError(self):
        "Check la ValueError"
        error_type = ValueError
        with self.assertRaises(error_type):
            exercices.fonction_erreur()

    def test_valide(self):
        "Vérifie qu'un traitement décrit est fait"
        condition = 3
        resultat = exercices.fonction_test()
        self.assertEqual(resultat,condition)

    # TODO vos tests ici :)

############################# AUTORUN ##################################

# si on lance le fichier en ligne de commande, on affiche la documentation générale
# pour que l'utilisateur sache comment utiliser les tests unitaires
if __name__ == "__main__":
    documentation()