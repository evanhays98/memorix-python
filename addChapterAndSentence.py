import requests


def highlight_word(word, sentence):
    word = word.lower()

    if word in sentence:
        return sentence.replace(word, f"//{word}//")  # Replace only the first occurrence
    wordCaps = word.capitalize()
    if wordCaps in sentence:
        return sentence.replace(wordCaps, f"//{wordCaps}//")  # Replace only the first occurrence
    else:
        return None


headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjQyOTQ2N2FjLWIwNjAtNDA4Ny05MjM5LTg1ZGI1ZTNkZWM3ZCIsInBzZXVkbyI6ImV2YW5oYXlzOTgiLCJtYWlsIjoidmFub3UuaGF5c0BnbWFpbC5jb20iLCJpYXQiOjE2OTc1NTI1OTYsImV4cCI6MTczMDg4NjI1Nn0.PTooeWg7i-9rQEBbdhuNek3QL30LpYRD3Gwz-VS0hEs"
}
base_url = 'https://clear-waistcoat-colt.cyclic.app/'


def addAChapter(title="Titre du chapitre", description="Contenu du chapitre"):
    data = {
        "title": title,
        "description": description,
    }
    response = requests.post(base_url + 'chapters', json=data, headers=headers)
    if response.status_code == 201:
        print("Chapitre créé avec succès.")
    else:
        print("Erreur lors de la création du chapitre. Statut de réponse:", response.status_code)
    print("Réponse du serveur:", response.text)
    print("Données envoyées:", response.text)
    return response.json()


def addASentence(chapterId, sentence, translation, information):
    data = {
        "chapterId": chapterId,
        "sentence": sentence,
        "translation": translation,
        "information": information
    }
    response = requests.post(base_url + 'fields-translation', json=data, headers=headers)
    if response.status_code == 201:
        print("Chapitre créé avec succès.")
    else:
        print("Erreur lors de la création du chapitre. Statut de réponse:", response.status_code)
    print("Réponse du serveur:", response.text)
    print("Données envoyées:", response.text)
    return response.json()

chapter = addAChapter("Lern English from French", "Apprends le français depuis la langue française avec des phrases simples et en les répétant.")
f = open("EnglishTradToFrench.txt", "r")
for sentence in f:
    sentenceSplit = sentence.split("|")
    sent = highlight_word(sentenceSplit[0], sentenceSplit[1])
    indication = sentenceSplit[2]
    translation = sentenceSplit[3].split("\n")[0]
    if sent is None:
        continue
    print("|" + sent+ "|", "|" + indication + "|", "|" + translation + "|")

    addASentence(chapter['id'], sent, translation, indication)
