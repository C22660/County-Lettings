## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `https://github.com/C22660/County-Lettings.git`

#### Créer l'environnement virtuel

- `cd /path/to/County-Lettings`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/County-Lettings`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/County-Lettings`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/County-Lettings`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/County-Lettings`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(County-Lettings_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  County-Lettings_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

#### Sentry
- Aller sur `https://sentry.io/`
- Créez un nouveau projet Django pour obtenir une clé DNS

#### CircleCi
The command assumes that you have:
- created a Heroku account.
- created a Heroku application.
- set the HEROKU_APP_NAME and HEROKU_API_KEY environment variables.

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`


---

## Pipeline CI/CD en utilisant CircleCi, Docker et Heroku

### Configuration des applications :  
#### CircleCI :  
1. Si ce n'est déjà fait, [créez un compte sur CircleCi](https://circleci.com/ "créez un compte sur CircleCI")
2. [installation du projet sur CircleCI](https://circleci.com/docs/2.0/getting-started/ "installation du projet sur CircleCI")

#### Docker :  
1. Si ce n'est déjà fait, [créez un compte sur Docker](https://hub.docker.com/signup"créez un compte sur Docker")
2. Créez en nouveau repository. 
3. Une fois affectué, remplacez, à la ligne 42 du fichier .circleci/config.yml
oc-lettings ($DOCKERHUB_USERNAME/oc-lettings) par votre repository  


Vous avez donc un DOCKERHUB_USERNAME, un DOCKERHUB_PASSWORD
Vous pouvez retourner dans CircleCi - Organization Settings - Create a context, et y ajouter ces variables d'environnement

#### Heroku : 
Si ce n'est déjà fait, [créez un compte sur Heroku](https://www.heroku.com/home "créez un compte sur Heroku")
1. Création de l'application
2. Ajoutez une base de donnés à votre application :  
Dans Resources, Add-ons, tapez Postgres
3. Cnfigurez vos variables d'environnement :  
Dans Settings, Config Vars, vous y verez la variable de votre base de donnée (DATABASE_URL)
Ajoutez la variable ENV (production), une SECRET_KEY django et, quand vous l'aurez, la variable SENTRY_DNS
4. Identification compte Heroku
Heroku propose [3 modes d'identification différents](https://help.heroku.com/PBGP6IDE/how-should-i-generate-an-api-key-that-allows-me-to-use-the-heroku-platform-api "3 modes d'identification différents")
Le plus simple étant de reprendre l'API Key qui se trouve en bas des [settings de votre compte](https://dashboard.heroku.com/account "settings de votre compte")


Retournez dans les organization settings de CircleCi pour y ajouter cette HEROKU_API_KEY
Retournez dans les settings du projet de CircleCi pour y ajouter l'HEROKU_APP_NAME

#### Sentry :
1. Si ce n'est déjà fait, [créez un compte sur Sentry](https://sentry.io/signup/ "créez un compte sur Sentry")
2. Créez un projet Django et collectez la clé dsn


Retournez dans les settings du projet de CircleCi pour y ajouter cette clé SENTRY_DNS dans les variables d'environnement
Retournez dans les settings de l'application d'Heroku pour y ajouter cette clé SENTRY_DNS dans les variables d'environnement

### Deploiement :
Rendez-vous sur votre projet dans CicrleCI.
SI celui-ci a été détecter, un bouton à droite permet de relancer le déploiement.
Dans le cas contraire, apportez une modification à un élément de votre code, ajoutez le scripte modifié à votre repo.
Retrournez sur votre projet dans CicrleCI.


CircleCI devrait démarer les tests, puis le déploiement.


Alimentez la base de donnée depuis le terminal :  
`>>> heroku run python manage.py -a "nom de l'application" loaddata datafromsqlite.json`
Vous devriez avoir accès au site de l'application sous http://<nom-de-l'application>.herokuapp.com/




