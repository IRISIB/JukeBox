#Django en resumé : [Les premiers pas](http://openclassrooms.com/courses/developpez-votre-site-web-avec-le-framework-django/votre-premiere-page-grace-aux-vues)

[PREV](https://github.com/IRISIB/JukeBox/blob/master/Documents/Django/1-Django_resume_presentation.md)
[NEXT](https://github.com/IRISIB/JukeBox/blob/master/Documents/Django/3-Django_resume_techniques_avancees)

##Votre première page grâce aux vues
En résumé:
![alt text](http://uploads.siteduzero.com/thb/394001_395000/394741.png)

* Le minimum requis pour obtenir une page web avec Django est une vue, associée à une URL.

* Une vue est une fonction placée dans le fichier views.py d'une application. Cette fonction doit toujours renvoyer un objet HttpResponse.

* Pour être accessible, une vue doit être liée à une ou plusieurs URL dans les fichiers urls.py du projet.

* Les URL sont désignées par des expressions régulières, permettant la gestion d'arguments qui peuvent être passés à la vue pour rendre l'affichage différent selon l'URL visitée.

* Il est conseillé de diviser le urls.py du projet en plusieurs fichiers, en créant un fichier urls.py par application.

* Il existe des réponses plus spéciales permettant d'envoyer au navigateur du client les codes d'erreur 404 (page non trouvée) et 403 (accès refusé), ou encore d'effectuer des redirections.

##Les templates
En résumé:
![alt text](http://uploads.siteduzero.com/files/386001_387000/386517.png)

* En pratique, et pour respecter l'architecture dictée par le framework Django, toute vue doit retourner un objet HttpResponse construit via un template.

* Pour respecter cette règle, il existe des fonctions nous facilitant le travail, comme render, présentée tout au long de ce chapitre. Elle permet de construire la réponse HTML en fonction d'un fichier template et de variables.

* Les templates permettent également de faire plusieurs traitements, comme afficher une variable, la transformer, faire des conditions... Attention cependant, ces traitements ont pour unique but d'afficher les données, pas de les modifier.

* Il est possible de factoriser des blocs HTML (comme le début et la fin d'une page) via l'utilisation des tags {% block %} et {% extends %}.

* Afin de faciliter le développement, Django possède un tag {% url %} permettant la construction d'URL en lui fournissant la vue à appeler et ses éventuels paramètres.

* L'ajout de fichiers statiques dans notre template (images, CSS, JavaScript) peut se faire via l'utilisation du tag {% static %}.

##Les modèles
En résumé:

* Un modèle représente une table dans la base de données et ses attributs correspondent aux champs de la table.

* Tout modèle Django hérite de la classe mère Model incluse dans django.db.models.

* Chaque attribut du modèle est typé et décrit le contenu du champ, en fonction de la classe utilisée : CharField, DateTimeField, IntegerField…

* Les requêtes à la base de données sur le modèle Article peuvent être effectuées via des appels de méthodes sur Article.objects, tels que all(), filter(nom="Un nom") ou encore order_by('date').

* L'enregistrement et la mise à jour d'articles dans la base de données se fait par la manipulation d'objets de la classe Article, et via l'appel à la méthode save().

* Deux modèles peuvent être liés ensemble par le principe des clés étrangères. La relation dépend cependant des contraintes de multiplicité qu'il faut respecter : OneToOneField, ManyToManyField.

* Il est possible d'afficher les attributs d'un objet dans un template de la même façon qu'en Python via des appels du type article.nom. Il est également possible d'itérer une liste d'objets, pour afficher une liste d'articles par exemple.

##L'administration
En résumé :

* L'administration est un outil optionnel : il est possible de ne pas l'utiliser. Une fois activée, de très nombreuses options sont automatisées, sans qu'il y ait besoin d'ajouter une seule ligne de code !

* Ce module requiert l'usage de l'authentification, et la création d'un super-utilisateur afin d'en restreindre l'accès aux personnes de confiance.

* De base, l'administration permet la gestion complète des utilisateurs, de groupes et des droits de chacun, de façon très fine.

* L'administration d'un modèle créé dans une de nos applications est possible en l'enregistrant dans le module d'administration, via admin.site.register(MonModele) dans le fichier admin.py de l'application.

* Il est également possible de personnaliser cette interface pour chaque module, en précisant ce qu'il faut afficher dans les tableaux de listes, ce qui peut être édité, etc.

##Les formulaires
En résumé :

* Un formulaire est décrit par une classe, héritant de django.forms.Form, où chaque attribut est un champ du formulaire défini par le type des données attendues.

* Chaque classe de django.forms permet d'affiner les données attendues : taille maximale du contenu du champ, champ obligatoire ou optionnel, valeur par défaut…

* Il est possible de récupérer un objet Form après la validation du formulaire et de vérifier si les données envoyées sont valides, via form.is_valid().

* La validation est personnalisable, grâce à la réécriture des méthodes clean_NOM_DU_CHAMP() et clean().

* Pour moins de redondances, la création de formulaires à partir de modèles existant se fait en héritant de la classe ModelForm, à partir de laquelle nous pouvons modifier les champs éditables et leurs comportements.

##La gestion des fichiers
En résumé:

* L'installation de la bibliothèque Pillow est nécessaire pour gérer les images dans Django. Cette bibliothèque permet de faire des traitements sur les images (vérification et redimensionnement notamment).

* Le stockage d'une image dans un objet en base se fait via un champ models.ImageField. Le stockage d'un fichier quelconque est similaire, avec models.FileField.

* Les fichiers uploadés seront stockés dans le répertoire fourni par MEDIA_ROOT dans votre settings.py.

[PREV](https://github.com/IRISIB/JukeBox/blob/master/Documents/Django/1-Django_resume_presentation.md)
[NEXT](https://github.com/IRISIB/JukeBox/blob/master/Documents/Django/3-Django_resume_techniques_avancees)XT]()