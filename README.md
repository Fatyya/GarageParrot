# Garage_v_parrot
## Site de Réparation Automobile avec Vente de Voitures

Ce référentiel contient le code source d'un site web de réparation automobile avec une fonctionnalité de vente de voitures. Le projet est construit en utilisant Django et MySQL.

## Prérequis

- [WampServer](https://www.wampserver.com/) installé et en cours d'exécution.
- Python et pip installés sur votre système.
- Un environnement virtuel (recommandé).

## Installation et Exécution en Local

1. Clonez ce référentiel sur votre machine locale :

   ```bash
   git clone https://github.com/asidev7/Garage_v_parrot.git
   cd Garage_v_parrot

2. Créez et activez un environnement virtuel (recommandé) :
   ```bash 
   python -m venv venv
   source venv/bin/activate  # Sur Windows : venv\Scripts\activate
3. Installez les dépendances du projet :
    ```bash 
     pip install -r requirements.txt
4. Configurez la base de données MySQL avec XAMPP :
 - Lancez XAMPP et démarrez les modules Apache et MySQL.
  - Accédez à phpMyAdmin (généralement via http://localhost/phpmyadmin) et 
- Créez une nouvelle base de données (par exemple dv_gvp).
 - Ouvrez le fichier settings.py dans le répertoire main.
   
 - Modifiez la configuration de la base de données dans la section DATABASES en utilisant les informations de votre base de données MySQL XAMPP.

   ```bash
   DATABASES = {  
   'default': {  
      'ENGINE': 'django.db.backends.mysql',  
      'NAME': 'db_gvp',  
      'USER': 'root',  
      'PASSWORD': '',  
      'HOST': '127.0.0.1',  
      'PORT': '3306',  
      'OPTIONS': {  
          'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"  
      }  
     }  
   } 

5. Effectuez les migrations pour créer les tables de la base de données
   ```bash
    python manage.py makemigrations
    python manage.py migrate 
6. Créez un superutilisateur pour accéder à l'interface d'administration :
   ```bash
     python manage.py createsuperuser

7. Lancez le serveur de développement :
   ```bash
    python manage.py runserver
- Le site devrait être accessible à l'adresse http://127.0.0.1:8000/.

- Connectez-vous en tant que administrateur et Employer  à http://127.0.0.1:8000/connexion pour gérer les données du site.





<<<<<<< HEAD

## Captures d'écran
=======
>>>>>>> refs/remotes/origin/main
#   G a r a g e P a r r o t  
 