# Setup your machine 
## Installing Python 3 in a Unix environment
```bash
sudo apt-get update
sudo apt-get install python3.6
```

## Installation pip
```bash
python3 -m pip install --user --upgrade pip

python3 -m pip --version
```

## Installation virtualenv

```bash
python3 -m pip install --user virtualenv
```

[En savoir plus sur pip et virtualenev](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

## Créer un environnement virtuel
Cela créera un environnement virtuel sous un dossier "mon-projet".
```bash
python3 -m venv mon-projet
```

## Activation d'un environnement virtuel
```bash
source mon-projet/bin/activate
```

## Décompresser les scripts du brief
Installer l'utilitaire unzip
```bash
sudo apt-get install unzip
```
Après avoir installé l'utilitaire unzip, si vous voulez extraire vers un dossier de destination particulier, vous pouvez utiliser :

```bash
unzip brief_scripts.zip -d dossier_destination
```
Votre dossier de destination est le "path" où vous avez créé l'environnement virtuel.

## Installer les bibliothèques Python 
Placez-vous dans le dossier "mon-projet" et exécutez:
```bash
pip install BeautifulSoup urlunparse
```

## Lancer le script
```bash
python forum_scrapper.py
```

## Quitter l'environnement virtuel
Lorsque vous avez fini de travailler sur le projet, vous pouvez désactiver l'environnement virtuel pour libérer des ressources:
```bash
deactivate
```