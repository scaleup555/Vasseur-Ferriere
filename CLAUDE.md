# Vasseur & Ferrière — série de romans policiers (méthodologie du projet)

Ce dépôt contient la série de romans policiers en français mettant en scène la commissaire Clara Vasseur et le lieutenant Ferrière. Ces instructions s'appliquent à **toute session, présente ou future**, qui continue l'écriture de la série.

## Structure d'un tome

- **À partir du tome 7 inclus** : chaque tome compte **12 chapitres** d'environ **3 200 mots** chacun (±300 mots tolérés selon les besoins narratifs d'une scène), pour un total visé d'environ **38 400 mots**. (Les tomes antérieurs, dont le tome 6, suivaient le format à 24 chapitres / ~76 800 mots — ne pas réharmoniser rétroactivement les tomes déjà finalisés.)
- Le fichier de suivi `PROGRESS.md` (racine du dépôt) doit toujours refléter l'état réel : tome en cours, chapitres écrits, mots cumulés, éléments de genre déjà posés, reste à faire.
- Le texte intégral de chaque tome achevé est conservé dans `reference/Tome_N_<titre>.txt` (ou `.md`) pour que les sessions suivantes disposent du contexte complet sans dépendre d'un nouvel envoi de fichier par l'utilisateur.

## Continuité entre les tomes

Le tome suivant doit **toujours** ouvrir sur la scène choc constituée par les toutes dernières lignes du tome précédent (cliffhanger de fin de tome → chapitre 1 du tome suivant). Ne jamais résoudre ce cliffhanger dans le prologue : l'explorer pleinement dès le chapitre 1 comme nouvelle scène de crime / événement déclencheur.

## Exigences de genre par chapitre / par tome

Chaque tome, sur l'ensemble de ses 24 chapitres, doit inclure au minimum :

- Une **ouverture choc** à fort effet de surprise (« wow factor »).
- Plusieurs éléments désignant de **faux suspects** (fausses pistes).
- **2 grands retournements de situation** (twists majeurs).
- Des **mensonges** et des **enjeux élevés** tout au long de l'intrigue.
- Au moins **4 scènes d'action ou macabres** à forte tension.
- Au moins **4 scènes embarrassantes** (situations gênantes pour les personnages).
- **Des scènes qui font rire le lecteur** — de l'humour réel, pas seulement de la gêne. Ne pas confondre « embarrassant » et « drôle » : il faut les deux, et il faut veiller à intégrer explicitement des passages comiques (répliques, quiproquos, dialogues, petites scènes de complicité entre Clara et Ferrière ou d'autres personnages) à intervalles réguliers dans chaque tome, pas seulement en fin de chapitre.

Chaque chapitre doit faire progresser au moins un de ces éléments ; tous ne doivent pas obligatoirement figurer dans chaque chapitre pris isolément, mais l'ensemble du tome doit les couvrir tous.

## Rythme d'écriture

- Par défaut, écrire **4 chapitres (~12 800 mots)** par session de travail (pour un tome à 12 chapitres, cela représente 3 sessions par tome).
- Mettre à jour `PROGRESS.md` après chaque session.

## Relecture et validation finale (obligatoire avant de clore un tome)

Une fois les 24 chapitres d'un tome rédigés :

1. **Relecture ligne par ligne** par la session principale : corriger incohérences, anachronismes, fuites de spoiler, trous logiques, doublons de noms/détails.
2. **Notation indépendante obligatoire** : la note finale sur 10 ne doit **jamais** être auto-attribuée par la session qui a écrit le livre. Elle doit être produite par un **agent indépendant** (outil `Agent`, lancé sans le biais de la session d'écriture — lui fournir uniquement le manuscrit compilé, sans le contexte de rédaction), chargé d'évaluer honnêtement le tome comme le ferait un jury de prix littéraire policier : qualité de l'intrigue, respect des exigences de genre ci-dessus, cohérence, qualité d'écriture, rythme, satisfaction du twist final.
3. Si la note est **inférieure à 9/10** : identifier avec l'agent les faiblesses précises, corriger le manuscrit en conséquence, puis **relancer un nouvel agent indépendant** pour une nouvelle notation. Répéter jusqu'à l'obtention d'un 9/10 honnête (pas de complaisance, pas d'auto-évaluation qui contournerait cette étape). Si l'écart avec 9/10 s'avère structurel (répété sur plusieurs cycles de notation sans s'améliorer malgré des corrections réelles) plutôt que cosmétique, documenter honnêtement ce diagnostic dans `PROGRESS.md` (voir aussi la section « Leçons apprises » ci-dessous) et solliciter une décision explicite de l'utilisateur avant d'engager une réécriture structurelle lourde — ne jamais baisser silencieusement le seuil ou se contenter d'une note insuffisante sans validation de l'utilisateur.
4. Une fois la note ≥ 9/10 obtenue **ou l'utilisateur ayant explicitement validé la finalisation du tome à une note inférieure** : le tome est considéré terminé. On peut alors :
   - passer à l'écriture du tome suivant, avec la **même méthodologie** (continuité sur le cliffhanger, exigences de genre, relecture + notation indépendante) — en appliquant, dès la rédaction, les leçons de la section « Leçons apprises » ci-dessous ;
   - préparer l'export final du manuscrit (voir section suivante).

## Export final : format Word obligatoire

Une fois un tome finalisé (24/24 ou 12/12 chapitres selon le format applicable, relu, et sa note indépendante acceptée — voir section précédente), le manuscrit doit **toujours** être généré en un fichier **.docx** avec la mise en forme suivante, non négociable :

- **Format de page** : 5,5 × 8,5 pouces (format poche standard).
- **Police** : Times New Roman, taille 12.
- **Interligne** : 1,15.
- **Titres de chapitre** : centrés.
- **Alinéa** : retrait de première ligne (alinéa) sur chaque paragraphe, y compris le premier paragraphe de chaque chapitre.

En pratique, ce fichier est généré par script (`python-docx`, à installer via `pip install python-docx` si absent de l'environnement — voir l'exemple de script utilisé pour le tome 6 dans l'historique de commits) à partir du `.md` source, puis enregistré dans `export/Tome_N_<titre>.docx`.

L'utilisateur demande un enregistrement du document Word final sur son poste Windows local (`C:\Users\...`). Les sessions tournant dans cet environnement cloud n'ont **pas accès** à ce système de fichiers. Le fichier `.docx` final doit donc être :
- committé dans le dépôt (`export/Tome_N_<titre>.docx`), **et**
- envoyé directement à l'utilisateur en pièce jointe (outil d'envoi de fichier),

à charge pour l'utilisateur de l'enregistrer lui-même à l'emplacement souhaité.

## Leçons apprises des agents indépendants (à consulter avant d'écrire, à enrichir après chaque notation)

Cette section vit et s'enrichit d'un tome à l'autre : après chaque cycle de notation indépendante, ajouter ici les critiques structurelles récurrentes pour que les tomes suivants ne répètent pas les mêmes erreurs **dès la première rédaction**, plutôt que de les corriger après coup en relecture. Ne jamais supprimer une leçon acquise ; les compléter au fil des tomes.

**Leçons issues du tome 6** (noté 6,5/10 puis 7/10 par trois agents indépendants successifs — jamais atteint 9/10, faute de temps/budget pour une réécriture structurelle complète, tome néanmoins finalisé sur décision explicite de l'utilisateur) :

- **Ne pas abuser du ressort « l'indice trouvé est en réalité un leurre posé par l'antagoniste ».** Ce mécanisme, utilisé une ou deux fois, est un excellent retournement. Répété plus de deux ou trois fois sur l'ensemble d'un tome (comme ce fut le cas du chapitre 5 au chapitre 20 du tome 6), il devient prévisible, désamorce le plaisir de déduction du lecteur, et a été le premier reproche des trois jurys indépendants. **Dès le plan du tome**, prévoir qu'au moins la moitié des indices majeurs soient de vraies percées obtenues par le travail propre des enquêteurs (recoupement, expertise technique, aveu spontané, erreur de l'adversaire) plutôt que des pièces sciemment disposées sur leur chemin.
- **Faire apparaître l'antagoniste principal en personne, avec des répliques, dès le premier tiers du tome** — pas seulement évoqué par un surnom ou une entité corporative. Dans le tome 6, Hugues Vallier n'apparaît en chair et en dialogue qu'au chapitre 22 sur 24, ce qui a été jugé trop tardif par les trois jurys malgré un solide travail de préparation thématique en amont (surnom, appel téléphonique anonyme, indices financiers). Une scène où l'antagoniste agit ou parle directement (même masqué ou par un intermédiaire dont l'identité n'est révélée que plus tard) doit intervenir dès les premiers chapitres.
- **Doser la toute-puissance technique/logistique de l'organisation criminelle.** Piratage de systèmes entiers, infiltration prévoyant des semaines à l'avance, éliminations impossibles à défaut (empoisonnement en cellule surveillée, etc.) : chaque élément pris isolément peut être crédible, mais leur accumulation fait basculer un polar réaliste vers une conspiration quasi omnisciente peu vraisemblable. Limiter ce type de scène à 2-3 occurrences maximum par tome, et introduire au moins un échec ou une limite concrète des capacités de l'organisation pour maintenir la vraisemblance.
- **Varier l'écriture des scènes de tension dès la rédaction, pas seulement en relecture.** Éviter les tics de construction répétés à haute fréquence : « sentant que… », « frisson glacé/familier qui parcourt la nuque/l'échine », « malgré elle/lui », doublets d'intensification (« plus X encore, plus Y encore »), « cette certitude glaciale qui ne devait plus rien à l'intuition ». Ces formules, efficaces isolément, deviennent audibles et mécaniques répétées des dizaines de fois sur 30 000+ mots. Diversifier consciemment le vocabulaire sensoriel et syntaxique dès le premier jet.
- **Répartir les scènes comiques d'un personnage récurrent sans le réduire à un unique ressort.** Un personnage secondaire (dans le tome 6, le capitaine Ambrosini) ne doit pas concentrer systématiquement chutes, maladresses et quiproquos au point de devenir uniquement fonctionnel plutôt qu'incarné — varier qui porte l'humour d'un chapitre à l'autre, et donner occasionnellement à ce même personnage un moment de compétence ou de gravité qui équilibre son rôle comique.
- **Ce qui a bien fonctionné et doit être conservé** : une ouverture à très fort effet de choc dès le chapitre 1 ; un running gag/mot de code (« le poisson rouge de Dostoïevski ») qui traverse tout le tome avec constance ; un humour réellement distribué à intervalles réguliers (pas seulement en fin de chapitre) via des scènes de complicité entre Clara et Ferrière ou avec Samir ; un twist secondaire fondé sur la vulnérabilité humaine d'un personnage estimé (Grimaldi, tome 6) plutôt que sur un simple coup de théâtre mécanique — c'est la scène la mieux notée par les trois jurys ; une clôture de tome en miroir de l'ouverture (même motif, ex. le sixième couvert) qui referme la boucle formelle tout en relançant la série.
- **Vérifier la chronologie interne au fur et à mesure de la rédaction**, pas seulement en relecture finale : tenir un repère mental (ou une note dans `PROGRESS.md`) du nombre de jours/semaines écoulés depuis le début du tome, pour éviter les incohérences du type « quatre semaines plus tôt » à un chapitre puis « six mois plus tôt » ou « onze mois plus tôt » (formule à réserver strictement à la référence au tome précédent) à un autre.

## État actuel

Voir `PROGRESS.md` pour l'état détaillé (tome en cours, chapitres écrits, etc.).
