# Utiliser une image de base Python 3.9
FROM python:3.9

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le script app.py dans le répertoire de travail du conteneur
COPY app.py .

# Installer les dépendances du script (si nécessaire)
RUN pip install requests

# Exécuter le script app.py lors de l'exécution d'un conteneur à partir de cette image
CMD ["python", "app.py"]