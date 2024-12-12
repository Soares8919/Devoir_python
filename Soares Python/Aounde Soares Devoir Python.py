import random

# Dictionnaire des régions de Côte d'Ivoire et leurs chefs-lieux
regions = {
    "Abidjan": "Abidjan",
    "Agneby-Tiassa": "Agboville",
    "Belier": "Yamoussoukro",
    "Bleketre": "Divo",
    "Bouafle": "Bouafle",
    "Boukani": "Bouna",
    "Cavally": "Guiglo",
    "Dix-Huit Montagnes": "Man",
    "Fromager": "Gagnoa",
    "Gbeke": "Bouaké",
    "Gbêkê": "Bouaké", # Orthographe alternative
    "Grand Bassam": "Grand Bassam",
    "Guemon": "Bangolo",
    "Haut-Sassandra": "Daloa",
    "Indenie-Djuablin": "Abengourou",
    "Kabadougou": "Ferké",
    "Loh-Djiboua": "Zoukougbeu",
    "Marahoué": "Bouaflé",
    "Moronou": "Bongouanou",
    "Nawa": "Soubré",
    "N'Zi": "Dimbokro",
    "Poro": "Korhogo",
    "San-Pedro": "San-Pedro",
    "Sassandra": "Sassandra",
    "Sud-Bandama": "Divo",
    "Sud-Comoé": "Aboisso",
    "Tchologo": "Ferkessédougou",
    "Tonkpi": "Man",
    "Valle du Bandama": "Bouaké",
    "Worodougou": "Séguéla",
    "Yamoussoukro": "Yamoussoukro"
}

def charger_meilleurs_scores():
    """Charger les meilleurs scores depuis un fichier ou renvoyer des scores par défaut."""
    try:
        with open('meilleurs_scores.txt', 'r') as f:
            scores = [int(ligne.strip()) for ligne in f.readlines()]
            return sorted(scores, reverse=True)[:5]
    except FileNotFoundError:
        return [0] * 5

def sauvegarder_meilleurs_scores(scores):
    """Sauvegarder les meilleurs scores dans un fichier."""
    with open('meilleurs_scores.txt', 'w') as f:
        for score in scores[:5]:
            f.write(f"{score}\n")

def afficher_meilleurs_scores(scores):
    """Afficher les 5 meilleurs scores."""
    print("\n--- 5 Meilleurs Scores ---")
    for i, score in enumerate(scores, 1):
        print(f"{i}. {score}")
    print()

def jouer_quiz():
    # Afficher les meilleurs scores au début du jeu
    meilleurs_scores = charger_meilleurs_scores()
    afficher_meilleurs_scores(meilleurs_scores)

    # Sélectionner 10 questions uniques aléatoirement
    questions_quiz = random.sample(list(regions.items()), 10)
    score = 0

    print("Bienvenue au Quiz des Régions de Côte d'Ivoire !")
    print("Répondez aux questions suivantes sur les régions ivoiriennes et leurs chefs-lieux.\n")

    for region, chef_lieu_correct in questions_quiz:
        # Poser la question
        print(f"Quel est le chef-lieu de la région {region} ?")
        
        # Obtenir la réponse de l'utilisateur
        reponse_utilisateur = input("Votre réponse : ").strip()

        # Vérifier la réponse
        if reponse_utilisateur.lower() == chef_lieu_correct.lower():
            print("Correct ! 🎉")
            score += 1
        else:
            print(f"Incorrect ! Le chef-lieu de la région {region} est {chef_lieu_correct}.")

    # Fin du quiz
    print(f"\nQuiz terminé ! Votre score : {score}/10")

    # Mettre à jour les meilleurs scores
    meilleurs_scores.append(score)
    meilleurs_scores = sorted(meilleurs_scores, reverse=True)[:5]
    sauvegarder_meilleurs_scores(meilleurs_scores)

    # Afficher les meilleurs scores mis à jour
    afficher_meilleurs_scores(meilleurs_scores)

    # Demander si le joueur veut rejouer
    rejouer = input("Voulez-vous rejouer ? (oui/non) : ").lower()
    return rejouer == 'oui'

def principale():
    while True:
        if not jouer_quiz():
            print("Merci d'avoir joué au Quiz des Régions de Côte d'Ivoire !")
            break

if __name__ == "__main__":
    principale()