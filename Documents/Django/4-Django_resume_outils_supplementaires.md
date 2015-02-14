#Django en resumé : [Des outils supplémentaires](http://openclassrooms.com/courses/developpez-votre-site-web-avec-le-framework-django/les-utilisateurs-2)

##  Les utilisateurs 
En résumé :

* Django propose une base de modèles qui permettent de décrire les utilisateurs et groupes d'utilisateurs au sein du projet. Ces modèles possèdent l'ensemble des fonctions nécessaires pour une gestion détaillée des objets : make_password, check_password…

* Il est possible d'étendre le modèle d'utilisateur de base, pour ajouter ses propres champs.

* Le framework dispose également de vues génériques pour la création d'utilisateurs, la connexion, l'inscription, la déconnexion, le changement de mot de passe… En cas de besoin plus spécifique, il peut être nécessaire de les réécrire soi-même.

* Il est possible de restreindre l'accès à une vue aux personnes connectées via @login_required ou à un groupe encore plus précis via les permissions. 

## Les messages 
En résumé :

* Les messages permettent d'afficher des notifications à l'utilisateur, en cas de succès ou d'échec lors d'une action, ou si un événement particulier se produit.

* Il existe différents types de messages : ceux d'information, de succès, d'erreur, d'avertissement, et enfin de débogage.

* Il est possible de créer son propre type de message et de configurer son comportement.

* L'affichage de messages peut être limité : chaque type de message est caractérisé par une constante entière, et nous pouvons afficher les messages ayant un niveau supérieur ou égal à un certain seuil, via messages.set_level.

## La mise en cache 
En résumé :

* Le cache permet de sauvegarder le résultat de calculs ou traitements relativement longs, afin de présenter le résultat sauvegardé pour les prochaines visites, plutôt que de recalculer la même donnée à chaque fois.

* Il existe plusieurs systèmes de mise en cache : par fichier, en base de données, dans la mémoire RAM.

* La mise en cache peut être définie au niveau de la vue, via @cache_page, dans le fichier urls.py, ou encore dans les templates avec le tag {% cache %}.

* Django fournit également un ensemble de fonctions permettant d'appliquer une mise en cache à tout ce que nous souhaitons, et d'en gérer précisément l'expiration de la validité.

## La pagination 
En résumé :

* La classe django.core.paginator.Paginator permet de générer la pagination de plusieurs types de listes d'objets et s'instancie avec au minimum une liste et le nombre d'éléments à afficher par page.

* Les attributs et méthodes clés de Paginator à retenir sont p.num_pages et p.page(). La classe Page a notamment les méthodes has_next(), has_previous() et est itérable afin de récupérer les objets de la page courante.

* Il est possible de rendre la pagination plus pratique en prenant en compte l'argument orphans de Paginator.

* Pensez à uniformiser vos paginations en terme d'affichage au sein de votre site web, pour ne pas perturber vos visiteurs.

## L'internationalisation 
Cycle de traduction d'un logiciel:
![alt text](http://uploads.siteduzero.com/files/420001_421000/420517.png)

En résumé :

* Le processus de traduction se divise en deux parties :

** L'internationalisation, où nous indiquons ce qui est à traduire ;

** La localisation, où nous effectuons la traduction et l'adaptation à la culture.

* Ce processus se base essentiellement sur l'utilisation de l'outil gettext, permettant la génération de fichiers de traduction utilisables par des novices en développement.

* Django permet également d'adapter l'affichage des dates et des nombres à la langue, en même temps que leur traduction.

* Grâce aux sessions et aux middlewares, le framework peut deviner la langue de l'utilisateur automatiquement, en fonction de son navigateur ou de ses précédentes visites.

## Les tests unitaires 
En résumé :

* Les tests unitaires permettent de s'assurer que vous n'avez introduit aucune erreur lors de votre développement, et assurent la robustesse de votre application au fil du temps.

* Les tests sont présentés comme une suite de fonctions à exécuter, testant plusieurs assertions. En cas d'échec d'une seule assertion, il est nécessaire de vérifier son code (ou le code du test), qui renvoie un comportement anormal.

* Les tests sont réalisés sur une base de données différente de celles de développement ; il n'y a donc aucun souci de corruption de données lors de leur lancement.

* Il est possible de tester le bon fonctionnement des modèles, mais aussi des vues. Ainsi, nous pouvons vérifier si une vue déclenche bien une redirection, une erreur, ou si l'enregistrement d'un objet a bien lieu.

## Ouverture vers de nouveaux horizons : django.contrib 
En résumé :

* Django est un framework très puissant, il propose de nombreux modules complémentaires et optionnels pour simplifier le développement.

* Ce cours a traité de quelques-uns de ces modules, mais il est impossible de les présenter tous : la documentation présente de façon complète chacun d'entre eux.

* Il existe des centaines de modules non officiels permettant de compléter votre installation et d'intégrer de nouvelles fonctionnalités.

* Nous avons présenté ici humanize, qui rend vos données plus naturelles dans vos templates, et flatpages qui permet de gérer vos pages statiques via l'administration.