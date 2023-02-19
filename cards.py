import random
import collections


questions = ["SQL",
"Primärschlüssel",
"Fremdschlüssel",
"(min, max)-Notation",
"Existenzabhängige Entities",
"Generalisierung",
"Aggregation",
"ER -> Relationales Schema",
"Relationales Schema optimieren",
"Relationale Algebra - Operatoren: Selektion σ",
"Relationale Algebra - Operatoren: Projektion Π",
"Relationale Algebra - Operatoren: Umbenennung ρ",
"Relationale Algebra - Operatoren: Kartesisches Produkt ×",
"Relationale Algebra - Operatoren: Join ⋈",
"Relationale Algebra - Operatoren: Theta-Join ⋈_θ",
"Relationale Algebra - Operatoren: Equi-Join ⋈_𝑎=𝑏",
"Relationale Algebra - Operatoren: einseitiger äußerer Join ⟕ / ⟖",
"Relationale Algebra - Operatoren: (vollständiger) äußerer Join ⟗",
"Relationale Algebra - Operatoren: Semi-Join ⋉ / ⋊",
"Relationale Algebra - Operatoren: Anti-(Semi-)Join ⊳/⊲",
"Relationale Algebra - Operatoren: Gruppierung und Aggregation ϒ",
"Mengenoperationen: ∪, ∩, ∖",
"Relationale Division ÷",
"Tupelkalkül",
"Domänenkalkül",
"SQL - Algebra",
"Funktionale Abhängigkeit (Funktional Dependency FD)",
"Armstrong-Axiome",
"Schlüssel",
"Schlüsselbestimmung"
"Attributhülle",
"Kanonische Überdeckung",
"𝐹𝐶 - Berechnung",
"Relationsdekomposition",
"1. Normalform",
"2. Normalform",
"3. Normalform",
"3. Normalform - Synthesealgorithmus",
"Boyce-Codd-Normalform",
"Dekompositionsalgorithmus (Boyce-Codd-Normalform & 4. NF)",
"4. Normalform",
"Speicherhierachie",
"RAID - Types",
"Logische Optimierungen",
"Iteratoren zur physischen Optimierung",
"Transaktionsverwaltung - Operationen",
"ACID"
"Fehlerklassifikation",
"Speicherhierachie - Steal and Force",
"ARIES-Protokoll (Log)",
"WAL",
"Systemabsturz",
"Mehrwertige Abhängigkeiten (multivalued dependencies - MVDs)",
]

answers = [
"Structured\nQuery\nLanguage", #"SQL"
"Minimale Menge an Attributen, die ein Tupel eindeutig identifizieren", #"Primärschlüssel"
"Verweisen auf Primärschlüssel einer anderen Relation („Tabelle“)", #"Fremdschlüssel"
"Bsp:\n(min, max): Angenommen, Polyeder ist fixiert, dann gibt es (4, *) Tupel, die dieses Polyeder enthalten", #"(min, max)-Notation"
"„schwache“ Entity -> existiert nur in Kombination mit „starker“ Entity -> Beziehung immer 1:N oder 1:1 (eher selten)", #"Existenzabhängige Entities"
"„is-a“-Beziehung Attribute werden von Ober- an Untertyp weitergegeben -> Wie Vererbung bei objektorientierter Programmierung", #"Generalisierung"
"Ist-Teil-von“-Beziehung", #"Aggregation"
"Entities:\n\t◦ Jede Entity wird zur Relation\n\t◦ Entity-Attribute -> Attribute der Relation\n\t◦ Schlüssel bleibt erhalten\n"
"Beziehunhgen\n\t◦ Jede Beziehung wird Relation (Vorsicht: Oft Möglichkeit, zu optimieren)\n\t◦ Attribute werden übernommen\n\t◦ Schlüssel setzt sich abhängig von den Funktionalitäten aus denen der beteiligten Entities zusammen\n" #"ER -> Relationales Schema"
"1:N-Beziehungen\n\t◦ Beziehungsrelation weglassen\n\t◦ In „N-Entity” Attribute der Beziehung, Fremdschlüssel von „1-Entity“ einfügen\n"
"1:1-Beziehungen\n\t◦ Beziehungsrelation und eine der Entities weglassen\n\t◦ Attribute der Entity und der Beziehung alle in verbleibende Entity übernehmen", #"Relationales Schema optimieren"
"Filtert Einträge einer Relation anhand einer bestimmten Eigenschaft (Eigenschaften sind vergleichend: <, >, =, …)", #"Relationale Algebra - Operatoren: Selektion σ"
"Gibt nur die angegebenen Attribute aller Tupel in der Relation zurück (relationales Modell ist mengenorientiert. Entstehende doppelte Einträge kommen nur einmal vor)", #"Relationale Algebra - Operatoren: Projektion Π"
"Es können ganze Relationen oder einzelne Attribute umbenannt werden (Wenn zum Beispiel mit zwei Relationen gearbeitet wird, die viele gleiche Attribute haben hilft das bei der Unterscheidung)", #"Relationale Algebra - Operatoren: Umbenennung ρ"
"Erzeugt neue Relation, in der alle Einträge der beiden gegebenen miteinander kombiniert werden", #"Relationale Algebra - Operatoren: Kartesisches Produkt ×"
"Ähnlich wie kartesisches Produkt, aber:\n\t◦ Kombiniert nur die Einträge, in denen alle Attribute mit gleichem Namen den gleichen Wert haben\n\t◦ Doppelte Spalten werden wegprojiziert", #"Relationale Algebra - Operatoren: Join ⋈"
"Ähnlich wie normaler Join, aber:\n\t◦ Bei normalen Join: Paare in denen alle Attribute mit gleichem Namen übereinstimmen werden kombiniert\n\t◦ Hier: Paare, die die Bedingung 𝜃 erfüllen werden kombiniert\n\t◦ Redundante Spalten werden nicht wegprojiziert", #"Relationale Algebra - Operatoren: Theta-Join ⋈_θ"
"Sonderfall des Theta-Joins, in dem die Join-Bedingung 𝜃 die Form 𝑎 = 𝑏 hat...\n\t◦ Anders als der „normale“ Join vergleicht der Equi-Join nicht Spalten mit gleichem Namen sondern nur die gegebenen\n\t◦ Achtung: Wie beim Theta-Join werden doppelte Spalten hier nicht wegprojiziert", #"Relationale Algebra - Operatoren: Equi-Join ⋈_𝑎=𝑏"
"Grundsätzlich wie natürlicher Join 𝐴 ⋈ 𝐵, aber:\n\t◦ Tupel, die einen Joinpartner finden werden kombiniert und behalten (gleich)\n\t◦ Tupel aus der „äußeren“ Relation, die keinen Joinpartner finden werden behalten und mit Null-Einträgen kombiniert", #"Relationale Algebra - Operatoren: einseitiger äußerer Join ⟕ / ⟖"
"„Kombination“ aus linkem und rechtem äußeren Join:\n\t◦ Tupel, die einen Joinpartner finden werden kombiniert und behalten (gleich)\n\t◦ Tupel aus beiden Relationen, die keinen Joinpartner finden werden behalten und mit Null-Einträgen kombiniert", #"Relationale Algebra - Operatoren: (vollständiger) äußerer Join ⟗"
"Ähnlich wie natürlicher Join 𝐴 ⋈ 𝐵, aber:\n\t◦ Tupel, die keinen Joinpartner finden, werden verworfen (gleich)\n\t◦ Tupel, die einen Joinpartner finden, werden behalten aber nicht kombiniert", #"Relationale Algebra - Operatoren: Semi-Join ⋉ / ⋊"
"„Gegenteil vom Semi-Join“:\n\t◦ Tupel, die keinen Joinpartner finden, werden behalten und nicht kombiniert\n\t◦ Tupel, die einen Joinpartner finden, werden verworfen", #"Relationale Algebra - Operatoren: Anti-(Semi-)Join ⊳/⊲"
"Nicht Teil der klassischen Algebra sondern Erweiterung\n\t◦ Fasst alle Einträge in der gegebenen Spalte zusammen und wendet gegeben Funktion(en) an\n\t◦ Beispiele: count(*), sum(Einwohner), min(Einwohner),…", #"Relationale Algebra - Operatoren: Gruppierung und Aggregation ϒ"
"Voraussetzung: Gleiches Schema\n\t◦ Attribute, die nur in einer Relation vorkommen müssen wegprojiziert werden\n\t◦ Attribute, die mit unterschiedlichen Namen vorkommen, müssen gleich umbenannt werden\n\t◦ Domänen der Attribute müssen gleich sein\n\n"
"∪ (Vereinigung): Alle Einträge, die in mindestens einer Relationen vorkommen, ohne Duplikate\n\t∩ (Schnitt): Alle Einträge, die in beiden Relationen vorkommen\n\t∖ (Differenz): Alle Einträge, die nur in der ersten Relation vorkommen", #"Mengenoperationen: ∪, ∩, ∖"
"Zweck: Finde Einträge in 𝐴, die mit allen Einträgen in 𝐵 zusammen vorkommen\nVoraussetzung: Für 𝐴 ÷ 𝐵 muss 𝐵 ⊆ 𝐴 sein\nBeispiel: MatrNr der Studenten, die alle Vorlesungen mit vier SWS hören ( ℎ𝑜𝑒𝑟𝑒𝑛 ÷ 𝜌𝑉𝐿 (Π𝑉𝑜𝑟𝑙𝑁𝑟 (𝜎𝑆𝑊𝑆=4 (𝑉𝑜𝑟𝑙𝑒𝑠𝑢𝑛𝑔𝑒𝑛))) )", #"Relationale Division ÷"
"{𝑠 | 𝑃(𝑠)}, wobei 𝑃 eine Bedingung ist (Bsp.: Finde Studenten, die in jeder ihrer Prüfungen 1.0 geschrieben haben: {𝑠 𝑠 ∈ 𝑆𝑡𝑢𝑑𝑒𝑛𝑡𝑒𝑛 ∧ ∀𝑝 ∈ 𝑝𝑟𝑢𝑒𝑓𝑒𝑛(𝑠. 𝑚𝑎𝑡𝑟𝑛𝑟 = 𝑝. 𝑚𝑎𝑡𝑟𝑛𝑟 ⇒ 𝑝. 𝑛𝑜𝑡𝑒 = 1.0)})\n"
"Quantoren:\n\tAllquantor ∀𝑥 ∈ 𝑋 𝑃 𝑥:      Die Bedingung 𝑃 muss für alle 𝑥 gelten\n\tExistenzquantor ∃𝑥 ∈ 𝑋 𝑃 𝑥: Die Bedingung 𝑃 muss für mindestens ein 𝑥 gelten", #"Tupelkalkül"
"{[𝑣1, 𝑣2, … , 𝑣𝑛] 𝑃(𝑣1, … , 𝑣𝑛)}, wobei 𝑃 eine Bedingung ist (Bsp.: : Finde Studenten, die in jeder ihrer Prüfungen 1.0 geschrieben haben ( {[𝑚, 𝑛, 𝑠] 𝑚, 𝑛, 𝑠 ∈ 𝑆𝑡𝑢𝑑𝑒𝑛𝑡𝑒𝑛 ∧ ∀𝑣, 𝑝, 𝑛𝑜 ( 𝑚, 𝑣, 𝑝, 𝑛𝑜 ∈ 𝑝𝑟𝑢𝑒𝑓𝑒𝑛 ⇒ 𝑛𝑜 = 1.0)} )\n"
"Drei Bedingungen:\n\t◦ Konstante im Ergebnistupel ⇒ muss in Domäne von 𝑃 liegen\n\t◦ ∃𝑥 𝑃 𝑥 ⇒ darf nur für 𝑥 ∈ Domäne von 𝑃 erfüllbar sein\n\t◦ ∀𝑥 𝑃 𝑥 ⇒ muss für alle 𝑥 ∉ Domäne von 𝑃 erfüllt sein", #"Domänenkalkül"
"""SELECT attribut1, attribut2,…       Π_(𝑎𝑡𝑡𝑟𝑖𝑏𝑢𝑡1,𝑎𝑡𝑡𝑟𝑖𝑏𝑢𝑡2,…)\nFROM rel1, rel2,…                   𝑟𝑒𝑙1 × 𝑟𝑒𝑙2 × ⋯\nWHERE Bedingung;                    𝜎_(𝐵𝑒𝑑𝑖𝑛𝑔𝑢𝑛𝑔)\n\n
SELECT attribut FROM relation R     𝜌_𝑅(𝑟𝑒𝑙𝑎𝑡𝑖𝑜𝑛)\nSELECT attribut AS a FROM relation  𝜌_(𝑎←𝑎𝑡𝑡𝑟𝑖𝑏𝑢𝑡)(𝑟𝑒𝑙𝑎𝑡𝑖𝑜𝑛)""", #"SQL - Algebra"
"""Ein Attribut B ist funktional abhängig von A, wenn folgendes gilt: Zwei Tupel mit dem gleichen Wert in A haben auch den gleichen Wert in B \n\n{ 𝐴} → { 𝐵} oder kurz: 𝐴 → 𝐵 \n\n
ℛ = {𝐴1, 𝐴2, … } das Schema einer Relation, 𝑅 ihre Ausprägung -> Dann gilt für 𝛼 ⊆ ℛ, 𝛽 ⊆ ℛ: 𝛼 → 𝛽 genau dann, wenn ∀𝑟, 𝑠 ∈ 𝑅 gilt: 𝑟. 𝛼 = 𝑠. 𝛼 ⇒ 𝑟. 𝛽 = 𝑠. 𝛽 \n
𝛽 ist voll funktional von 𝛼 abhängig, wenn:\n\t◦ 𝛼 → 𝛽, und \n\t◦ 𝛼 kann nicht mehr verkleinert (d.h. keines der Attribute in 𝛼 weggelassen) werden, sodass die Abhängigkeit danach immer noch gilt. \n\nSchreibweise: 𝛼 →° 𝛽""", #"Funktionale Abhängigkeit (Funktional Dependency FD)"
"""Herleitung von FDs. Hier gilt: 𝛼, 𝛽, 𝛾, 𝛿 ⊆ ℛ\n\t◦ Reflexivität:                 Für 𝛽 ⊆ 𝛼 gilt: 𝛼 → 𝛽\n\t◦ Verstärkung:                  Wenn 𝛼 → 𝛽 gilt, dann auch 𝛼𝛾 → 𝛽𝛾\n\t◦ Transitivität:                Wenn 𝛼 → 𝛽 und 𝛽 → 𝛾 gelten, dann gilt auch 𝛼 → 𝛾
\n\t◦ Vereinigungsregel:            Wenn 𝛼 → 𝛽 und 𝛼 → 𝛾 gelten, dann auch 𝛼 → 𝛽𝛾\n\t◦ Dekompositionsregel:          Wenn 𝛼 → 𝛽𝛾 gilt, dann auch 𝛼 → 𝛽 und 𝛼 → 𝛾\n\t◦ Pseudotransitivitätsregel:    Wenn 𝛼 → 𝛽 und 𝛽𝛾 → 𝛿, dann gilt auch 𝛼𝛾 → 𝛿""", #"Armstrong-Axiome"
"{S1, S2, … } → ℛ\nSchlüsselypen:\n\n\tSuperschlüssel:\n\t\t◦ Bedingung: 𝛼 → ℛ\n\t\t◦ „ allgemeine“ Schlüsseldefinition\n\n\tKandidatenschlüssel/Schlüsselkandidaten:\n\t\t◦ Bedingung: 𝛼 →° ℛ, d.h. 𝛼 ist minimal\n\t\t◦ Eine Relation kann mehrere haben", #"Schlüssel"
"""Wenn alle funktionalen Abhängigkeiten bekannt sind, kann man relativ unkompliziert einen möglichen Schlüssel finden:\n\t1. Attribute, die nur links auftauchen müssen Teil des Schlüssels sein\n\t
2. Attributhülle der Menge bestimmen\n\t3. Entspricht die Attributhülle der gesamten Relation?\n    ◦ Ja → fertig, Schlüssel gefunden\n    ◦ Nein → ein Attribut hinzufügen, weiter mit 2.""", #"Schlüsselbestimmung"
"Alle Attribute, die mithilfe der geltenden FDs aus den gegebenen Attributen bestimmt werden können.\n\nDiese beinhaltet auch Attribute, die erst in 2, 3,… Schritten bestimmt werden können", #"Attributhülle"
"""Kleinstmögliche Menge an FDs, die folgende Eigenschaften erfüllt:\n\t◦ 𝐹𝐶 bestimmt die gleichen Attribute, die die ursprüngliche Menge\n\t◦ Keine der FDs enthält überflüssige Attribute\n\t
◦ Jede linke Seite kommt nur ein einziges Mal vor\n\nDas bedeutet z.B.:\n\t◦ Wenn 𝛼 → 𝛾 gilt, dann ist 𝛼𝛽 → 𝛾 ∉ 𝐹𝐶\n\t◦ Statt 𝛼 → 𝛽 und 𝛼 → 𝛾 ist nur 𝛼 → 𝛽𝛾 ∈ 𝐹𝐶""", #"Kanonische Überdeckung"
"""1. Linksreduktion auf allen FDs 𝛼 → 𝛽 ∈ 𝐹 durchführen\n\tWenn es auf der linken Seite ein Attribut gibt, das man weglassen kann (d.h. auch ohne das Attribut kann ganz 𝛽) erzeugt werden, wird es entfernt\n\n
2. Rechtsreduktion auf allen FDs 𝛼 → 𝛽 ∈ 𝐹 durchführen\n\tAttribute auf der rechten Seite, die schon durch andere FDs erzeugt werden können weggelassen werden\n\n
3. Falls FDs der Form 𝛼 → ∅ entstanden sind: Weglassen\n\n4. FDs mit gleicher linker Seite zusammenfassen""", #"𝐹𝐶 - Berechnung"
"""Relationen können aufgeteilt werden, wenn folgende Bedingungen erfüllt sind:\n\n\tVerlustlosigkeit:\n\t\t◦ Alle Informationen aus der ursprünglichen Relation sind in den neuen wiederzufinden\n\t\t
◦ Eine Zerlegung ist verlustlos, wenn für alle möglichen Ausprägungen 𝑅 = 𝑅1 ⋈ 𝑅2 gilt. Das ist automatisch der Fall, wenn 𝑅1 ∩ 𝑅2 → 𝑅1 oder 𝑅1 ∩ 𝑅2 → 𝑅2\n\n\t
Abhängigkeitserhaltung:\n\t\t◦ Alle FDs aus der Ursprungsrelation sind auf neue Relationen übertragbar""", #"Relationsdekomposition"
"Schema ist in 1NF, wenn alle Attribute atomar sind", #"1. Normalform",
"""Schema ist in 2NF, wenn es in 1NF ist und für jedes Attribut b auf der rechten Seite gilt:\n\tb ist Teil eines Kandidatenschlüssels oder\n\tb ist nicht von einer echten Teilmenge eines Kandidatenschlüssels abhängig\n\n
-> Jedes Nichtschlüsselattribut ist voll funktional von jedem Schlüsselkandidaten abhängig (Bsp.: Ein Schlüsselkandidat ist hier (TitelNr, Album), für Band und Herkunft reicht aber Album -> nicht voll funkt. abh.)""",  #"2. Normalform"
"""Schema ist in 3NF, wenn jede FD α->β mindestens eine der folgenden Bedingungen erfüllt:\n\tα->β ist trivial (β⊆α)\n\tα ist Superschlüssel\n\tJedes Attribut in β ist in einem Kandidatenschlüssel enthalten\n\n
-->Kein Nichtschlüsselattribut hängt transitiv von einem Schlüsselkandidaten ab, d.h. Für jede funkt. Abh. 𝛼 → 𝛽 muss gelten:\n\t
• 𝛽 ⊆ 𝛼 (die FD ist trivial, z.B. Band → Band), oder\n\t• Alle Attribute von 𝛽 sind in einem Kandidatenschlüssel enthalten (z.B. Titel → TitelNr), oder\n\t• 𝛼 ist Superschlüssel (z.B. Album → Band)""", #"3. Normalform"
"""◦ Verlustlos (d.h. alle Informationen bleiben erhalten)\n◦ Abhängigkeitserhaltend ist (d.h. alle FDs gelten immer noch)\n◦ Relationen im Ergebnis sind alle in dritter Normalform\n\n
1. Finde Kanonische Überdeckung der FDs (siehe letzte Woche)\n2. Für jede FD 𝛼 → 𝛽 wird eine Relation 𝑅𝛼 = 𝛼 ∪ 𝛽 erstellt, alle passenden FDs werden 𝑅𝛼 zugeordnet
3. Falls kein Kandidatenschlüssel in einer der Relationen aus 2. auftaucht, wird eine neue Relation erstellt, die nur den Kandidatenschlüssel enthält\n4. Redundante Relationen (die Teilmengen anderer Relationen sind) werden entfernt""", #"3. Normalform - Synthesealgorithmus"
"""Schema ist in BCNF, wenn jede FD α->β mindestens eine der folgenden Bedingungen erfüllt:\n\tα->β ist trivial (β⊆α)\n\tα ist Superschlüssel\n\n
Wie 3. Normalform, aber kein Teil eines Kandidatenschlüssels ist funktional von einem Teil eines anderen Kandidatenschlüssels abhängig \n-> Wenn es nur einen einzigen Kandidatenschlüssel gibt, ist die Relation automatisch in BCNF""", #"Boyce-Codd-Normalform"
"""
1. Starte mit 𝑍 = ℛ\n2. Solange es ein Relationenschema ℛ𝑖 ∈ 𝑍 gibt, das nicht in BCNF ist:\n    1. Finde eine FD 𝛼 → 𝛽 sodass\n        ◦ 𝛼 ∩ 𝛽 = ∅ → nicht trivial\n        ◦ ¬ 𝛼 → ℛ𝑖 → kein Superschlüssel\n    2. Zerlege ℛ𝑖 in ℛ𝑖1 ≔ 𝛼 ∪ 𝛽 und ℛ𝑖2 ≔ ℛ𝑖 ∖ 𝛽
3. Entferne 𝑅𝑖 aus 𝑍 und füge 𝑅𝑖1 und 𝑅𝑖2 ein, also 𝑍𝑛𝑒𝑢 = 𝑍𝑎𝑙𝑡 ∖ ℛ𝑖 ∪ 𝑅𝑖1 ∪ 𝑅𝑖2\n4. go to 1""", #"Dekompositionsalgorithmus (Boyce-Codd-Normalform & 4. NF)"
"""Schema ist in 4NF, wenn jede MVD α->>β mindestens eine der folgenden Bedingungen erfüllt:\n    α->>β ist trivial (β⊆α oder α∪β = R)\n    α ist Superschlüssel
--> Alle MVDs 𝛼 → 𝛽 müssen entweder trivial sein oder 𝛼 ein Superschlüssel""", #"4. Normalform"
"CPU-Register < Cache < Hauptspeicher < Plattenspeicher < Archivspeicher", #"Speicherhierachie"
"""RAID 0      Striping                            Datenblöcke in Reiehe gespeichert\n
RAID 1      Mirroring                           Daten gespiegelt/kopiert\n
RAID 2      Hamming-Code (Fehlererkennung)      Datenbytes + HC verteilt auf angehängten Platten\n
RAID 3      Platte speichert Parität            Datenbytes + Gesamtparity pro Reihe auf einer Platte\n
RAID 4      Platte speichert Parität            Datenblöcke + Gesamtparity pro Reihe auf einer Platte\n
RAID 5      Parität verteilt gespeichert        Datenblöcke, parity aller Plattenreihen auf Platten aufgeteilt\n\n
RAID 01     RAID 1, dann RAID 0""", # "RAID - Types"
"""1. Aufbrechen von Selektionen\n2. Verschieben von Selektionen „nach unten“\n3. Selektionen und Kreuzprodukte zu Joins zusammenfassen
4. Joinreihenfolge bestimmen\n5. Einfügen von Projektionen\n6. Verschieben von Projektionen „nach unten“""", #"Logische Optimierungen"
"""Ermöglichen, verschiedene Implementierungen gegeneinander auszutauschen, und Zwischenergebnisse zu verwenden ohne sie komplett speichern zu müssen\n\t
◦ open: Initialisierung (Eingabe öffnen, etc.)\n\t◦ next: Berechnet das nächste Tupel des Ergebnisses und gibt es zurück\n\t
◦ close: Schließt Eingabe, gibt Ressourcen frei\n\t◦ cost/size: Gibt (geschätzte) Berechnungskosten bzw. Ergebnisgröße zurück""", #"Iteratoren zur physischen Optimierung"
"""begin of transaction (BOT)\n\t◦ Markiert Beginn der Transaktion\n\ncommit\n\t◦ Erfolgreiches beenden der Transaktion\n\t◦ Änderungen werden dauerhaft in die DB geschrieben\n\n
abort/rollback\n\t◦ Erfolgloses beenden der Transaktion\n\t◦ Änderungen werden rückgängig gemacht\n\ndefine savepoint\n\t◦ Sicherungspunkt, auf den sich eine Transaktion zurücksetzen lässt\n\n
backup transaction\n\◦ Transaktion wird auf den letzten Sicherungspunkt zurückgesetzt""", #"Transaktionsverwaltung - Operationen"
"""A tomicity       „ganz oder gar nicht“\nC onsistency     DB vorher in konsistentem Zustand → danach auch\n
I solation       parallel ausgeführte Transaktionen beeinflussen sich nicht gegenseitig\nD urability      Änderungen erfolgreicher Transaktionen bleiben erhalten""", #"ACID"
"""Lokale Fehler in einer noch festgeschriebenen Transaktion (= vor commit):\n\t◦ R1-Recovery: Änderungen zurücksetzen\n\n
Fehler mit Hauptspeicherverlust:\n\t◦ R2-Recovery: Abgeschlossene Transaktionen müssen erhalten bleiben\n\t◦ R3-Recovery: Nicht abgeschlossene TA müssen zurückgesetzt werden\n\n
Fehler mit Hintergrundspeicherverlust:\n\t◦ R4-Recovery: Durch Backups etc. Datenverlust verhindern""", #"Fehlerklassifikation"
"""Grundsätzlich:\nSteal -> welche Seiten dürfen im Puffer ersertzt werden?\nForce -> Wann von abgeschlossenen Transaktionen eingebrachte Änderungen eingebracht werden?\n\n
◦ ¬𝑠𝑡𝑒𝑎𝑙: Ersetzen von Seiten, die von einer noch aktiven Transaktion modifiziert wurden ist ausgeschlossen\n
◦ 𝑠𝑡𝑒𝑎𝑙: Jede nicht fixierte Seite kann ersetzt werden\n\n𝑓𝑜𝑟𝑐𝑒: Änderungen werden zum Transaktionsende auf den Hintergrundspeicher geschrieben\n
◦ ¬𝑓𝑜𝑟𝑐𝑒: geänderte Seiten können im Puffer bleiben und erst später zurückgeschrieben werden\n\n
        |    force      |       ¬force      |\n--------+---------------+-------------------+\n
¬steal  |    ¬Redo      |       Redo        |\n        |    ¬Undo      |      ¬Undo        |\n
--------+-----------------------------------+\nsteal   |    ¬Redo      |       Redo        |\n
        |     Undo      |       Undo        |\n""", #"Speicherhierachie - Steal and Force"
"""
[LSN, TA, PageID, Redo, Undo, PrevLSN], wobei:\n\nWhat                        |                   Why                     |               Syntax\n
----------------------------+-------------------------------------------+-----------------------------------------\nLSN (Log Sequence Number)   | Eindeutige Kennung des Log-Eintrags       |   #3\n
TA                          | Transaktionskennung des Durchführers      |   T_1\nPageID                      | Seitenkennung der veränderten Seite       |   P_A\n
Redo                        | Wie kann die Änderung nachvollzogen werden|   A += 50 (logisch), A = 50 (physisch)\nUndo                        | Wie kann die Änderung revidiert werden    |   A -= 50 (logisch), A = 0 (physisch)\n
PrevLSN                     | Zeigt vorigen Transaktions-Log-Eintrag    |   #1\n""", #"ARIES-Protokoll (Log)"
"""=\"Write Ahead Log\"\n\n\t◦ Bevor eine TA commited wird, müssen alle ihre Log-Einträge ausgeschrieben werden (notwendig für Redo)\n\t
◦ Bevor eine modifizierte Seite ausgelagert werden darf, müssen alle ihre Log-Einträge in Log-Datei und Log-Archiv ausgeschrieben werden (notwendig für Undo)
--> Log-Einträge werden typischerweise doppelt gespeichert:\n\t◦ In eine Log-Datei für „schnellen“ Zugriff (z.B. auf Plattenspeicher) für R1, R2 und R3-Recovery\n\t
◦ In ein Log-Archiv für sicheren Zugriff (getrennt, z.B. auf Magnetband) für R4-Recovery""", #"WAL"
"""1. Die Winner- (erfolgreicher commit) und Loser-Transaktionen (noch kein commit) werden bestimmt\n2. Alle Änderungen (winner und loser) werden wiederhergestellt (Redo)\n
3. Änderungen der loser-TA werden mit Compensation Log Record (CLG) rückgängig gemacht (Undo)\n\nHaben folgende Form: \n<LSN‘, TA, PageID, Redo, PrevLSN, UndoNextLSN>,\n
bsp. zu Log-Eintrag [#3, T_1, P_A, A += 50, A -= 50, #1] -> <#3', T_1, P_A, A -= 50, #3, #1>""", #"Systemabsturz"
"""
Für ein relationales Schema ℛ, mit 𝛼 ⊆ ℛ, 𝛽 ⊆ ℛ und 𝛾 = 𝑅 ∖ (𝛼 ∪ 𝛽) bedeutet 𝛼 ↠ 𝛽:\n
Wenn die Tupel (𝛼1, 𝛽1, 𝛾1) und 𝛼1, 𝛽2, 𝛾2 in der Relation 𝑅 enthalten sind, dann müssen auch die Tupel (𝛼1, 𝛽2, 𝛾1) und 𝛼1, 𝛽1, 𝛾2 existieren.\n
-->Bei identischen Werten für 𝛼 können die Werte von 𝛽 vertauscht werden. Die so entstehenden Tupel sind ebenfalls in 𝑅.\n\nWenn 𝛼 → 𝛽, dann gilt auch 𝛼 ↠ 𝛽\n\t
◦ Wenn nur ein einziger 𝛽-Wert zu jedem 𝛼 vorkommt, gibt es nichts zu tauschen ⟹ die Bedingung ist automatisch erfüllt\nWenn 𝛼 ↠ 𝛽 gilt, dann auch immer 𝛼 ↠ ℛ ∖ (𝛼 ∪ 𝛽)\n\t
◦ Wenn die 𝛽-Werte sich beliebig mit den 𝛾-Werten kombinieren lassen, dann auch andersherum\nEine MVD ist trivial wenn eine der folgenden beiden Bedingungen erfüllt ist:\n\t
◦ 𝛽 ⊆ 𝛼 (dann gilt automatisch auch 𝛼 → 𝛽 und damit 𝛼 ↠ 𝛽)\n\t◦ 𝛽 = 𝑅 − 𝛼 (In diesem Fall wäre 𝛾 = ∅, damit auch 𝛾1 = 𝛾2 = ∅, was die Bedingung der MVDs \n""", #"Mehrwertige Abhängigkeiten (multivalued dependencies - MVDs)"
]



index = 0
counter = 0
used_indices = collections.deque()
print("Press \"q\" to exit at any time\n\n")
print(len(questions))
while 1:

    index = random.randrange(len(questions))
    
    if not used_indices.__contains__(index):
        used_indices.insert(index, index)
    elif len(used_indices) == len(questions):
        inp = input("All questions have been asked. Would you like to start again? If not, press 'n' \n")
        if inp == "n":
            break
        else:
            used_indices.clear()
            counter = 0
            continue
    else:
        continue
    
    inp = input("Press ENTER for a question or q to exit: \n")
    if(inp == "q"):
        break
    counter += 1
    print(f"Question # {counter} of {len(questions)}:\n")
    print(questions[index])
    print("\n")
    
    inp = input("Press ENTER for the answer: \n")
    if(inp == "q"):
        break
    print(answers[index])
    print("\n")