questions = [
"Varianten von XSS Angriffen",
"Was sind die 6 Angriffsklassen?",
"Welche 5 Klassen von Schadcode gibt es?",
"Welche 6 Schutzziele gibt es?",
"Was ist ein kryptografisches System?",
"Welche 2 Klassen von kryptografischen Verfahren gibt es?",
"Wie wird ein RSA-Schlüsselpaar berechnet?",
"RSA Verfahren Ver- und Entschlüsselung",
"Beispiele von symmestrischen und asymmetrischen Verfahren",
"Was ist das funktionsprinzip einer Blockchiffre?",
"Warum werden Blockchiffren gepaddet?",
"Was ist der \"Kern\" einer Stromchiffre?",
"Geforderte Eigenschaft bei Stromchiffren",
"Betriebsmodi: ECB + Vor/Nachteile",
"Betriebsmodi: CBC",
"Betriebsmodi: CTR",
"Betriebsmodi: GCM",
"ECC",
"Schutzziele von kryptografische Hashfunktionen und MAC",
"Allgemeine Idee und Vorgehen von kryptografischen Hashfunktionen",
"Anforderungen an eine kryptografische Hashfunktion",
"Wie groß sollte Hashwert h für Kollisions-Resistenz sein?",
"Welche 3 Klassen von Hashfunktionen gibt es?",
"Welche von SHA Hashfunktionen sind (un)sicher?",
"Anforderungen an Passworthashfunktionen",
"Allgemeine Idee und Funktionsweise von MAC",
"Schutzziel(e) von MAC",
"MAC-Probleme: Merkel-Damgård: length extension-Angriffe",
"Sichere MAC-Konstruktion",
"Was ist AEAD?",
"Ziel einer elektronischen (digitalen) Signatur",
"Funktionsprinzip: teilen und nachweisen eine Signatur",
"3 Arten von Schlüsselgenerierung",
"Etablierung gemeinsamer Schlüssel: 2 Klassen von Ansätzen",
"Schlüsselaustausch / KDC",
"Schlüsselaustausch / KEM",
"PFS",
"Schlüsselvereinbarung / DH -> Grundidee",
"Schlüsselvereinbarung / DH -> 3 Phasen",
"Was ist KDF?",
"DH: MitM Angriff (Schema)",
"PFS mit DH-Verfahren",
"Pseudonymsierung vs Anonymisierung",
"Drei Klassen von Basistechniken/Faktoren zur Authentizierung",
"Einmal-Passworte",
"7 Anforderungen an biometrische Merkmale",
"Klassen biometrischer Merkmale",
"Vorgehen bei biometrischer Authentisierung",
"2 Problembereiche biometrischer Authentisierung",
"Challenge-Response (CR) Verfahren",
"Symmetrisches CR-Verfahren (Schema)",
"Asymmetrisches CR-Verfahren (Schema)",
"Zertifikate - What's the point?",
"Standaradzertifikat X.509.v3 - Inhalt",
"Komponenten einer PKI",
"Hierarchie von CAs",
"5 Anforderungen zur Zertifikatvalidierung",
"Zertifikatsrückruf (Revocation)",
"Wie funktioniert OCSP? (+Sketch)",
"SSO - Konzept",
"SSO - Sketch",
"3 Arten von SSO in der Praxis",
"Kerberos - Grundsätze",
"Kerberos - Ticketerstellung",
"Kerberos - Authenticator",
"Definition \"Autorisierung\"",
"Autorisierung - Regelwerk / (4-point-)Access Policy",
"3 Prinzipien zur Rechtekontrolle",
"3 Modelle für Rechtevergabe",
"Zugriffsmatrix-Modell (ZM) - Vor/Nachteile (+Sketch)",
"Role-based Access-Control (RBAC) - Vor/Nachteile",
"Bell-LaPadula-Modell + Vor/Nachteile",
"BLP-MAC-Policy",
"Access Control List (ACL) an Unix/Linux",
"Access Token (AT) bei OAuth - Ablauf",
"Berechtigungskontrolle",
"Zulässigkeitskontrolle",
"Hybride Konzepte von Zugriffskontrolle",
"Wichtige Schutz- und Kontrollaufgaben des Betriebssystems",
"Buffer-Overflow-Angriffe",
"ROP",
"Schutz durch Stack Canries",
"Schutz durch DEP",
"Schutz durch ASLR",
"3 Sicherheitsrelevante Eigenschaften: VMM bzw. Hypervisor",
"Betriebssystem-Level Virtualisierung: Container",
"Container-Konzept: Leichtgewichtige Virtualisierung",
"Firewalls",
"Paketfilter",
"DPI",
"ALG / Proxy-Firewall",
"Transportsicherheit: 5 Punkte zu Sicheren Verbindungen",
"TLS-Protokollablauf 2 Phasen",
"TLS-Handshake",
"VPN",
"Secure Programming - 4 Maßnahmen",
"OWASP Secure Coding Practices",
"Nutzen von 4 Werkzeugen sichere Programmierung",
"Allgemeine Richtlinien",
"ISMS",
"PDCA-Zyklus",
"2 Phasen des BSI-Sicherheitsprozesses",
"6 Schadensszenarien",
"Bedrohungsanalyse STRIDE",
"Bedrohungsbäumen (attack tree)",
"DREAD-Methode: Vorgehen zur Bedrohungs-/Risikobeurteilung & Risikoeinschätzung",
"Penetrationstests Black/Whitebox",
"Reverse Engineering (RE)",
"Programmanalyse",
"Bewertung der IT-Sicherheit",
"Common Criteria, EAL",

"draw ECB",
"draw CBC",
"draw CTR",
"draw GCM",
"draw ECC",
"draw Merkle-Damgard",
"draw AES-CBC",
"draw KDC",
"draw Kerberos-Protokoll",
"definition: Einwegfunktion",
"definition: Kerckhoffs-Prinzip",
"definition: Avalanche Effekt",
"definition: Stormchiffre",
"definition: kryptografische Hashfunktion",
"definition: CA",
"definition: RA",
"definition: Capability-Konzept",
]

answers = [
"Persistent: Angreifer-Script auf Webseite gespeichert, z.B. durch eine nicht gesicherte Kommentarfunktion.\n"
"Non-Persistent: Angreifer-Script wird über die HTTP-Anfrage in Webseite eingebracht, z.B. indem er einem Opfer einen manipulierten Link in einer Phishing-Mail schickt.", #"Varianten von XSS Angriffen",
"1. Ungenügende Eingabevalidierung (z.B. Buffer-Overflow / XSS)\n2. Identitätsdiebstahl (z.B. ARP-Spoofing)\n3.Man-in-the-Middle Attack (z.B. ARP-Cache Poisoning)\n"
"4.Angriffe auf die Verfügbarkeit (z.B. (D)DoS)\n5.Faktor Mensch (z.B. phishing mail)\n6.Web-Application Security (z.B. Broken Access Control)", #"Was sind die 6 Angriffsklassen?",
"1. Virus: nicht selbständiges Programm, das sich selbst in noch nicht infizierte Dateien kopiert. Benötigt Wirtsprogramm, um ausgeführt zu werden.\n"
"2. Emotet: liest Adressbuch von Outlook aus & schickt Mails an gefundene Kontakte. Meist eine Word-Datei mit integrierten Makro angehängt, das beim Öffnen der Datei durch den Empfänger ausgeführt wird.\n"
"3. Schadfunktionalität: Einschleusen von Ransomware oder von Software zur Übernahme des Systems.\n"
"4. Trojaner: Programm, das neben der spezifizierten nützlichen Funktionalität zusätzlich eine versteckte Funktionalität enthält.\n"
"5. Ransomware: verschlüsselt Daten auf Opfer-Rechner", #"Welche 5 Klassen von Schadcode gibt es?",
"1. Confidentiality: Schutz vor unautorisierter Informationsgewinnung\n"
"2. Integrity: Schutz vor unautorisierter und unbemerkter Modifikation\n"
"3. Availability: Schutz vor unbefugter Beeinträchtigung der Funktionalität\n"
"4. Authenticity: Nachweis der Echtheit und Glaubwürdigkeit der Identität einer handelnden Entität (natürliche Person, Maschine, Dienst, …) oder eines zu nutzenden Objekts.\n"
"5. Accountability: Schutz vor unzulässigem Abstreiten durchgeführter Handlungen\n"
"6. Privacy: Die Fähigkeit einer natürlichen Person, die Weitergabe und Nutzung seiner personenbeziehbaren Daten zu kontrollieren (informationelle Selbstbestimmung).", #"Welche 6 Schutzziele gibt es?",
"Mit Mengen der Klartexte m und Kryptotexte c, sowie K Menge der Schlüssel, e, d ∈ K\n E = Verschlüsselungsverfahren, D = Entschlüsselungsverfahren\nSei m ∈ M* mit E_e(m) = c , c ∈ C*, dann gibt es ein d∈K, so dass m = D_d(c)", #"Was ist ein kryptografisches System?",
"1. Symmetrische Verfahren, Secret-Key Verfahren: E, D idR einfach und schnell zu berechnen (e, d sind gleich (symmetrisch) und geheim (Secret Key))\n"
"2. Asymmetrische Verfahren, Public-Key Kryptografie: E, D basieren auf Zahlentheorie & Gruppentheorie. Ein Schlüsselpaar pro Entität, z.B. Bob B: (e_B, d_B) (öffentlicher Schlüssel e z.B. auf Key-Server veröffentlicht / privater Schlüssel d (z.B. d_B ist nur Bob bekannt).\n"
"\tVerschlüsselung: mit öffentlichem Schlüssel e (E_e(m) = c)\n\tEntschlüsselung: mit privatem Schlüssel d (D_d(c) = m)", #"Welche 2 Klassen von kryptografischen Verfahren gibt es?",
"1. wähle 2 große, geheime Primzahlen p, q (> 512 bit)\n"
"2. Berechne RSA-Modul n = pq, n ist öffentlich.\n"
"3. Berechne ϕ(n) = (p -1)(q -1), Eulersche Phi-Funktion effizient zu berechnen, wenn p, q Primzahlen sind.\n"
"4. Wähle e ∈ {1, 2, …, ϕ(n)-1} so, dass gilt ggT(ϕ(n), e) = 1, (e, n) ist der öffentliche Schlüssel.\n"
"5. Berechne den privaten Schlüssel d, so dass gilt: ed = 1 mod ϕ(n). p und q sind Trapdoor-Informationen.\n", #"Wie wird ein RSA-Schlüsselpaar berechnet?",
"Verschlüsselung: RSA_e(x) = xe mod n = y, mit x,y ∈ ℤ_n (Für Klartext x und (e,n))\n"
"Entschlüsselung: x = RSA_d (y) = y^d mod n", #"RSA Verfahren Ver- und Entschlüsselung",
"Symmetrische Verfahren: \n\tAES Standard mit 128, 192, 256 Bit Schlüssel\n\tChaCha20: 256 Bit Schlüssel\n"
"Asymmetrische Verfahren: \n\tRSA, 1024, 2048, 4096, …\n\tECC (Elliptic Curve Cryptography), u.a. 160, 256, 512, …", #"Beispiele von asymmetrische und symmestrische Verfahren",
"Symmetrisches Verfahren: Klartext m zerlegt in Blöcke m_i fester Länge, z.B. 128 bit -> blockweises Verschlüsseln mit Schlüssel k.", #"Was ist das funktionsprinzip einer Blockchiffre?",
"\"Auffüllen\" des Klartextes, so dass dessen Länge ein Vielfaches der Blockgröße ist -> Wird beim Verschlüsseln hinzugefügt, beim Entschlüsseln entfernt.", #"Warum werden Blockchiffren gepaddet?",
"Eine \"gute\" Schlüsselfolge KS: kryptografischer Pseudozufallszahlengenerator (CSPRNG) mit Seed-Wert initialisiert, erzeugt Pseudozufallszahlenfolge KS, \nABER: Deterministisch -> mit Kenntnis von k kann KS rekonstruiert werden", #"Was ist der \"Kern\" einer Stromchiffre?",
"Unterschiedliche Klartexte m_1, m_2 erfordern unterschiedliche Schlüsselfolgen KS_1, KS_2 -> Symmetrischer Schlüssel k muss sich ändern! (s. Betriebsmodi)", #"Geforderte Eigenschaft bei Stromchiffren",
"= \"Electronic Code Book mode\"\nPro:\n\t Parallelisierung der Verschlüsselung & keine Fehlerausbreitung\nCon:\n\tGleiche Klartext-Blöcke ergeben gleiche Chiffre-Blöcke: Muster in langen Nachrichten bleiben im Chiffretext erhalten\nKonsequenz: Statische Analysen, mustern", #"Betriebsmodi: ECB - Vor/Nachteile",
"= \"Cipher Block Chaining\"\nKlartextblock xor mit vorherigem Chiffretextblock. Startwert = Initialisierungsvektor IV, nicht geheim.\n"
"Konsequenz: Gleiche Klartextblöcke & gleicher Schlüssel k ergeben ungleiche Chiffretextblöcke, falls IV unterschiedlich ist (IV sollte zufällig gewählt sein) -> CBC Modus wesentlich sicherer als der ECB Modus.\n"
"Problem: Problem: durch Verkettung ergibt sich eine Fehlerfortpflanzung. Fehlerfortpflanzung ist aber auf nur 2 Blöcke beschränkt", #"Betriebsmodi: CBC",
"= \"Counter mode\"\nInitialisierung eines Zählers ctr mit Zufallszahl Nonce. Zählerstand pro Block m_i : ctr(i) = ctr(i-1) + 1\n"
"Verschlüsselung des i-ten Blockes: ci = mi ⊕ Ek(ctr(i))\nEntschlüsselung des i-ten Blockes: mi = ci ⊕ Ek(ctr(i))", #"Betriebsmodi: CTR",
"= \"Galois/Counter mode\"\nVerschlüsseln von Blöcken m_i durch Blockchiffre im CTR Modus, Blocklänge 128 Bit. Authentisieren der verschlüsselten Daten durch Multiplikation im Galoiskörper GF(2^128)\n"
"Eingaben: Klartext m, Schlüssel k, IV, ggf. assoziierte Daten, zusätzlich auch: Authentizität assoziierter Daten AD (z.B. Header-Daten)\n"
"Implementiert AEAD: Ciphertext-Authentizität (AE) & Daten-Authentizität (AD)", #"Betriebsmodi: GCM",
"= \"Elliptische-Kurven-Kryptografie\" (asymmetrisch)\nElliptische Kurve (Punktmenge die eine Polynomial-Gleichung erfüllt) -> zyklische Gruppe,  in denen das Problem des Diskreten Logarithmus (DLP) schwer zu lösen ist und die mit kürzeren Schlüsseln arbeiten können", #"ECC",
"Integrität und Authenzität", #"Schutzziele von kryptografische Hashfunktionen und MAC",
"Erstellen eines \"digitalen\" Fingerabdrucks h für ein Dokument / Nachricht m, so dass h das Dokument m repräsentiert\n"
"Gegeben Hashfunktion H, n Ganzzahlwert, Nachricht m ∈ M* (Nachrichten mit beliebiger Länge), Hashfunktion H (H: M* → M_n, z.B. n = 128, h der Länge n-Bit), h= H(m) (h nennt man auch Message Digest, feste Länge) -> h(m) ist kein vertraulicher Wert", #"Allgemeine Idee und Vorgehen von kryptografischen Hashfunktionen"
"Ziel: Nutzen von Hashfunktionen für Integritätsüberprüfung\nAnforderungen:\n\tHashwert h charakterisiert Nachricht m eindeutig. \n\tModifikation von m ergibt Nachricht m' mit H(m') = h'. \n\tDamit Modifikation erkannt werden kann, muss gelten: wenn m ≠ m' , dann gilt auch h ≠ h'\n"
"Problem: H ist nicht injektiv, deshalb sind prinzipiell Kollisionen möglich! -> Funktion H so, dass Kollisionen nicht effizient erzeugbar sind:\n"
"1. ∀ m ∈ M* gilt: H(m) = h ist einfach zu berechnen\n"
"2. Einwegeigenschaft (pre image resistance): Gegeben h = H(m) (Bestimmen des Wertes m ∈ M*, mit m = H-1 (h) ist nicht effizient möglich\n"
"3. Schwache Kollisionsresistenz (second pre image resistance): Gegeben sei m ∈ M* -> nicht effizient möglich, ein m' ∈ M* zu finden, so dass gilt: m ≠ m' und H(m) = H(m')\n"
"4. Starke Kollisionsresistenz (collision resistance): Das Finden von Paaren m, m' ∈ M*, mit H(m) = H(m') ist nicht effizient möglich.", #"Anforderungen an eine kryptografische Hashfunktion",
"Antwort liefert Geburtstags-Paradoxon: Gegeben Hashfunktion H, n Bit Hashwerte h, 2^n Werte: \n\tErforderliche Anzahl der Nachrichten, um mit einer Wahrscheinlichkeit > 0.5 eine Kollision zu erzeugen, liegt bei ≈ √2n, also ≈ 2(n/2)\n"
"-> BSI empfiehlt n ≥ 256", #"Wie groß sollte Hashwert h für Kollisions-Resistenz sein?",
"1. Basierend auf Blcokchiffren (z.B. AES-CBC: Letzter 128-Bit-Block als Hashwert)\n2. Dedizierte Hashfunktionen (z.B. SHA (Secure Hash-Algorithm))\n3. Passworthashfunktion (Passworte gehasht abspeichern: Login (Passworteingabe hashen: h'=H(Passwort) -> Abgleich mit gespeichertem Wert: h'= h?))", #"Welche 3 Klassen von Hashfunktionen gibt es?",
"Unsicher: SHA-1, 160-BitUnsicher: SHA-2-Familie (SHA-256 Bit, SHA-512 Bit), basierend auf Merkle-Damgård Konstruktion (vuln to length extension), ABER: SHA-512/256 ist resistent gegen length extension\n"
"Sicher: SHA-3, basierend auf Sponge-Prinzip (Hashlänge: 224 - 512 Bit, Resilient gegen length extension) - SHA512/256: Von den 512 bit von h werden nur 256 bit weiter genutzt", #"Welche von SHA Hashfunktionen sind (un)sicher?",
"Abgleich soll \"langsam\" (Abwehr von Brute Force Angriffen) und viel Speicher / CPU-Zeit benötigen -> parametrisierbare Hashfunktionen, bei Bedarf \"abbremsen\"", #"Anforderungen an Passworthashfunktionen",
"= \"Message-Authentication-Code\"\n Einbringen eines gemeinsamen Geheimnisses in die Berechnung, Authentizität: Nachweis der Kenntnis des Geheimnisses (Geheimnis wird als Schlüssel bezeichnet)\nAchtung: Schlüssel wird hier nicht zum Verschlüsseln genutzt!\n"
"-> MAC = Hashfunktion mit Schlüssel: H: M* × EK → M^n\nGeheimer (Pre-shared) Schlüssel k_AB zwischen Partnern A, B: MAC-Berechnung (mac = H(m'), mit m'= k_(AB)|m, m ist Nachricht) -> Empfänger prüft Authentizität und Integrität von m' mit kAB", #"Allgemeine Idee und Funktionsweise von MAC",
"Authenzität (zusätzlich zu Integrität)", #"Schutzziel(e) von MAC",
"A,B haben gemeinsames Geheimnis k_mac:\nA -> B \t- authentisierte Nachricht: data, h mit h=SHA-1(k_mac ∥ data)\n Angreifer -> B\t - h', data ∥fake mit h' = SHA-1(h ∥ fake), Angreifer kennt aber k_mac nicht!\n"
"B akzeptiert Nachricht data ∥fake als authentisch\n->h geht vollständig in Berechnung ein & Angreifer kann einfach Weiterhashen.", #"MAC-Probleme: Merkel-Damgård: length extension-Angriffe",
"HMAC-Verfahren RFC 2104:\nHMAC Konstruktion kapselt ein existierendes Hash-Verfahren H (H wird damit \"gehärtet\", z.B. HMAC-SHA-1, HMAC-SHA-2, …)\n"
"HMAC(m,k') = H(k'⊕opad | (H(k'⊕ipad | m)))\n 2 Hash-Anwendungen: \n\t1. innerer und äußerer Hash erhöht Kollisionsresistenz\n\t2. Length extension nicht möglich.", #"Sichere MAC-Konstruktion",
"=\"Authenticated Encryption with Associated Data\"\nReihenfolge wichtig!: ENCRYPT-THEN-MAC\nIntegration der Schutzkonzepte in einen Mechanismus: AEAD = Prüfung auch von nicht verschlüsselten Daten (AD) (Assoziierte Daten werden mit Cyphertext verknüpft, z.B. Header Daten unverschlüsselt aber authentisch)\n"
"Beispiele:\n\tChaCha20-Poly1305 (RFC 8439) (Stromchiffte ChaCha20 + MAC-Verfahren Poly1305)\n\t AES-GCM mode", #"Was ist AEAD?",
"Nachweis der nicht-abstreitbaren Urheberschaft eines Dokuments, Nachricht, … (->Schutzziel Accountability)", #"Ziel einer elektronischen (digitalen) Signatur",
"Basis: Public-Key Verfahren:\n\tGegeben sei Alice, besitzt Schlüsselpaar: (k_sig , k_veri)\n\t\tPrivater Signaturschlüssel k_sig bei RSA: k_sig = d\n\t\tÖffentlicher Verifikationsschlüssel k_veri bei RSA: k_veri = e\n"
"Vorgehen: Erstellen einer elektronischen/digitalen Signatur:\n\tSei m das Dokument, das signiert werden soll,\n\tRSA das genutzte Signaturverfahren & \n\tSHA-256 das Hashverfahren für Datenintegrität\n"
"Ablauf:\n\t1. Hashen: SHA-256(m) = h\n\t2. Signieren: RSAd(h) = hd mod n = sig, d ist privater Schlüssel von A\n"
"Prüfen der Korrektheit der Signatur: Prüfer erhält: sig, h\n\t1. Mit dem öffentlichen Schlüssel e von A: Rekonstruktion von h: RSA_e(sig) = sig_e mod n = h'\n\t2. Validieren: h' == h?\n"
"\n\nSignaturverfahren: analog zu Hashfunktionen:\n\tDedizierte Signaturverfahren (z.B. DSA, ECDSA)\n\t(Public Key Verschlüsselung(z.B. RSA)", #"Funktionsprinzip: teilen und nachweisen eine Signatur",
"1. Echte Zufallszahlen TRNG (True Random Number Generator)\n\tDie Entropiequelle basiert auf physikalischen Phänomenen.\n"
"2. Pseudozufallszahlen (PRNG)\n\tAlgorithmus arbeitet deterministisch (Deterministisches Verhalten basiert auf Startwert Seed) -> Kenntnis des Seeds ermöglicht die Berechnung aller Ausgaben der PRNG-Funktion.\n\tWenn ein PRNG zur Generierung von Schlüsselbits genutzt wird, dann muss der Seed-Wert vertraulich sein!\n"
"3. Kryptografisch sichere Zufallszahlengenerator (CSPRNG): \n\1. PRNG dürfen nicht vorhersagbar sein, selbst wenn der Angreifer bereits einen Teil der generierten Zufallsfolge kennt.\n\t2. Sie dürfen keinen Hinweis auf vorhergehende Zufallszahlen liefern, falls der Angreifer eine Zufallszahl errät oder abfängt.\n"
"\t3. Sie sollten Zufallsfolgen erzeugen, die statistisch gleichviele Nullen und Einsen haben und nicht komprimierbar sind.", #"3 Arten von Schlüsselgenerierung",
"1. Schlüsselaustausch,-verteilung (Key Distribution)\n2. Schlüsselvereinbarung (Key Agreement): Diffie-Hellmann (DH)", #"Etablierung gemeinsamer Schlüssel: 2 Klassen von Ansätzen",
"KDC-Server (Key Distribution Center, a.k.a. Trusted Third Party (TTP)):\n\tKDC besitzt Shared Keys kA mit jedem Partner A\n\t\tBei symmetrischer Kryptografie ist k_A ein Secret Key: Master Key\n"
"\t\tBei asymmetrischen Verfahren ist es der öffentliche Schlüssel e_A\n\tShared Keys sind pre-shared ausgetauscht und langlebig (Austauschwege z.B. QR-Code, SMS, PIN-Brief)", #"Schlüsselaustausch / KDC",      Zeichnung aud kap4/s. 8
"KEM (Key Encapsulation Mechanism): Symmetrischer Schlüssel k_AB wird asymmetrisch verschlüsselt.\nBeispiel (Einfacher/naiver Ansatz):\n"
"A kennt e_B, A generiert k_AB B mit RSA-Paar (e_B, d_B)\n"
"   (1)             (2)                     (3)\n"
"c=RSA_eB(k_AB) ----------> B entschlüsselt c: k_AB = RSA_dB(c)", #"Schlüsselaustausch / KEM",
"= \"Perfect Forward Secrecy\":\nWird ein Schlüssel unsicher (z.B. Master Key, privater oder öffentlicher Schlüssel) dürfen andere, zu früheren Zeitpunkten genutzte Schlüssel nicht auch unsicher werden\n"
"-> \"Folgenlosigkeit\": Kompromittierung eines Schlüssels macht eine sichere Kommunikation nicht im Nachhinein unsicher -> neuer Schlüssel darf nicht von einem alten Schlüssel abhängen.", #"PFS",
"Basis: Schwierigkeit des diskreten Logarithmus-Problems (y = g^x mod p ist einfach zu berechnen, Umkehrung log_g y mod p = f^(-1) (y) = x mod p ist sehr schwer zu berechnen.\n"
"Exponentation in ℤ𝑝∗ mit p ist Primzahl, ist eine Einweg-Funktion:\nExponentation ist kommutativ: d.h.:\t 𝑘 = (𝑎𝑦)𝑥 ≡ 𝑎𝑥 𝑦 𝑚𝑜𝑑 𝑝\n"
"Idee des klassischen DH-Verfahrens: \nSowohl A als auch B berechnen den k_AB lokal bei sich -> dafür wird keine vertrauliche Information ausgetauscht", #"Schlüsselvereinbarung / DH -> Grundidee",
"Phase 1: wechselseitiger Austausch öffentlicher Information (Wähle große Primzahl p (allen Teilnehmern bekannt))\n"
"Phase 2: lokale Berechnung eines shared DH-Secrets: DH-kAB (Wähle allen bekannten Wert g ∈ ℤ𝑝∗ , Generator-Element)\n"
"Phase 3: Mit festgelegter Funktion (nicht geheim), erzeugen A und B lokal auf der Basis des DH-k_AB die Schlüsselbits des k_AB:\n"
"\tA und B haben lokal den Shared DH-Key DH-kAB berechnet.\n\tErzeugen eines symmetrischen Shared Keys kAB der Länge n-Bit.\n\tNutzen einer bekannten KDF: mit Parameter DH-kAB und weiteren Parametern, u.a. Länge n & Jeder Partner berechnet unabhängig vom anderen Partner: k_AB = KDF(DH-k_AB , n)", #"Schlüsselvereinbarung / DH -> 3 Phasen",
"= \"Key Derivation Function\": Basis meist Keyed-Hashfunktionen (MAC) (z.B. SHA3):\n\tDer Seed bzw. Key-Teil der KDF-Funktion ist der DH-k_AB Mit KDF werden so viele Schlüsselbits (n) erzeugt, wie erforderlich (z.B. 256 Bits für AES-256)\n\tDie Hashfunktion wird hierfür ggf. mehrfach angewandt, um genügend viele Bits zu generieren.", #"Was ist KDF?",
"           Alice (A)              MitM Joe (J)              Bob (B)\n"
"DH-Keys    (e_A, d_A) ---[e_A]---> (e_J, d_J) ---[e_J]---> (e_B, d_B)\n"
"                   ||                      ||<--------[e_B]--------||\n"
"                   ||<--------[e_J]--------||                      ||\n"
"DH-k_AJ =          ||                      ||         DH-k_BJ =    ||\n"
"(e_J)^a mod p      ||                      ||         (e_J)^b mod p||\n"
"                   ||                      ||                      ||\n"
"Erzeugt k_AJ       ||          Erzeugt k_AJ||         Erzeugt k_BJ ||\n"
"                   ||                      ||                      ||\n"
"k_AJ = KDF(DH-K_AJ)||          Erzeugt k_BJ||     kBJ = KDF(DH-kBJ)||\n"
"                   ||                      ||                      ||\n"
"                    <----------------------><----------------------> \n"
"                       Kommunikation k_AJ      Kommunikation k_BJ    ", #"DH: MitM Angriff (Schema)",
"Basis: jeder Partner X besitzt Signatur-Schlüssel: (veri__x, sig__x)\nFür jede Vereinbarung eines neuen Schlüssels k_AB wird von den Partnern jeweils ein neues DH-Schlüsselpaar (e, d) generiert (= ephemeral keys, sind flüchtig)\n"
"Die öffentlichen Schlüssel werden signiert ausgetauscht: \n\t Sei e_A der DH-Key von A: Signieren des Schlüssels e_A: sig= E_sig__A(e_A) (E ist bspw. RSA)\nEmpfänger verifiziert die Signatur sig mit veri_A: D_veri__A(sig).\n"
"Praxis: \nBei geringer Rechenleistung: 1 Partner (z.B. ein Server), benutzt ein statisches DH-Schlüsselpaar und der Client generiert immer ein neues DH-Paar für jede neue kAB Vereinbarung.", #"PFS mit DH-Verfahren",
"Pseudonymisierung (unterliegt DSGVO): Verarbeitung einer Identität, sodass sie ohne zusätzlichen Daten nicht mehr einer Person zugeordnet werden können\nAnonymisierung (unterliegt DSGVO nicht): Verändern der personenbezogenen Daten, sodass sie unter keinen Unmständen einer Person mehr zugeordnet werden können", #"Pseudonymsierung vs Anonymisierung",
"1. Wissen (z.B. PIN)\n2. Besitz (z.B. SIM-Karte)\n3. Biometire (z.B. Fingerabdruck, Tippverhalten)", #"Drei Klassen von Basistechniken/Faktoren zur Authentizierung",
"Unterscheidung: Hardware/Software-Token & Zeitsynchronisiert/challenge-Response-basiert", #"Einmal-Passworte",
"1. Universalität (Jede Person besitzt das Merkmal)\n2. Eindeutigkeit (Merkmal ist für jede Person verschieden)\n3. Beständigkeit (Merkmal ist unveränderlich)\n4. quantitative Erfassbarkeit mittels Sensoren\n"
"5. Performance: Genauigkeit und Geschwindigkeit\n6. Akzeptanz des Merkmals beim Benutzer\n7. Fälschungssicherheit", #"7 Anforderungen an biometrische Merkmale",
"Statisch (psychologische Merkmale): nur geringe Möglichkeiten zur Auswahl oder Änderung von Referenzdaten\nDynamisch (Verhaltensmerkmale): Merkmal ist nur bei bestimmter Aktion vorhanden", #"Klassen biometrischer Merkmale",
"-----EINMALIG-----\n1. Feature-Extractment: Messdatenerfassung & Digitalisierung durch biometrischen Sensor\n2. Enrollment: Registrierung eines Benutzers: Aufnahme, Auswahl & Speicherung der Referenzdaten (z.B. 5-7 Fingerabdrücke)\n"
"-----BEI JEDER AUTHENTIFIZIERUNG-----\n3. Sensorerfassung: Verfikationsdaten aufnehmen\n4. Datenverabeitung: Verifikationsdaten digitalisieren (und ggf. normalisieren)\n5. Verifikation: Daten mit gespeichertem Template (Referenzwert) (mit Toleranz) vergleichen", #"Vorgehen bei biometrischer Authentisierung",
"Abweichung zwischen Referenz- und Verifikationsdaten:\nFalse-negative: akzeptanzproblem, berechtigter User abgewiesen\nfalse-positive: Sicherheitsproblem, unberechtigter User authentifiziert\n"
"       FAR                         FRR                     ERR     \nFalse-Acceptance-Rate      False-Rejection-Rate    Equal Error Rate", #"2 Problembereiche biometrischer Authentisierung",
"Basisprotokoll zur wissenbasierten Authentizitätsprüfung:\nSzenario: zwei Entitäten A und B mit einseitiger Authentisierung: A authentisiert sich gegenüber B (z.B. beim klassischen Login: Nutzer (A) versus Server (B)\n"
"-> Wechselseitige Authentisierung: A und B authentisieren sich.\n\nAllgemeiner Ablauf: hier A authentisiert sich gegenüber B:\n\tA gibt Identität an (z.B. MAC-Adr.)\n\tB sendet Challenge (z.B. Zufallszahl) an A\n\tA erstellt Response (z.B. mittels Verschlüsselung)\n"
"\tB prüft Response: falls korrekt, hat A geheimes Wissen (z.B. Schlüssel) nachgewiesen.", #"Challenge-Response (CR) Verfahren",
"       A                   Attacker Eve        Prüfende Instanz (B)\n"
"Vorab: k_A, ID_A                                 Vorab: k_A zu ID_A\n"
"Login              ||                      \n"
"                   |--------(1)ID_A------->||                      \n"
"                                           ||      (2)Generate RAND\n"
"                   ||<-------(3)RAND--------|                      \n"
"(4) Create         ||                                              \n"
"E_kA(RAND) = c     ||                                              \n"
"                   |---------(5)c--------->||       (6)Decrypt:    \n"
"                                           ||       D_kA(c) = RAND'\n"
"                                           ||       (7)Check:      \n"
"                                           ||       RAND' = RAND ? \n"
"                   ||<---(8)ok or failed----|                      \n"
"(9)Retry, if failed||                                              \n"
"RAND (=challenge) von B frisch gestellt -> A muss bei jedem Login explizit Kenntnis von k_A nachweisen", #"Symmetrisches CR-Verfahren (Schema)",
"Sei für Alice (A) ein Schlüsselpaar (e_A, d_A) generiert (d_A = private Signaturschlüssel, e_A = öffentliche Validierungsschlüssel), Zertifikat(e_A): enthält eA (bestätigt, dass e_A zu IdA gehört)\n"
"   A(e_A, d_A)                                     Instanz (B)     \n"
"Zert(e_A), ID_A                                 Vorab: k_A zu ID_A \n"
"                   |----------(1)---------->|                      (1) Login-request ID_A, Zertifikat(e_A)\n"
"                                           ||      (2)             (2) Prüft Zertifikat(e_A), generiert RAND Verschlüsselung c = E_(eA)(RAND)\n"
"                   |<---------(3)-----------|                      (3) c\n"
"           (4)     ||                                              (4) Entschlüsselt c, RAND = D_(dA)(c), signierte Response sig= E_(dA)(RAND)\n"
"                   |----------(5)---------->|                      (5) sig\n"
"                                           ||      (6)             (6) Prüft Signatur D_(eA)(sig) = RAND' = RAND ?\n"
"                    <----------(7)----------|                      (7) ok or failed?", #"Symmetrisches CR-Verfahren (Schema)",
"Bescheinigt Bindung von Public Key an die Identität einer Instanz/Subjekt (Person, Server, Gerät…)\nMit digitaler Signatur des Zertifikat-Ausstellers wird die Korrektheit der Daten bestätigt.", #"Zertifikate - What's the point?",
"Ausgestellt durch eine Certificate Authority (CA), Enthält:\n... Angabe zur CA (Issuer)\n... Public Key e_A von A & Verfahren (z.B. RSA)\n... Information zum Ablaufdatum (gültig bis ...)\nDaten im Zertifikat mit dem privaten Key d_(CA) der CA signiert.", #"Standaradzertifikat X.509.v3 - Inhalt",
"PKI = Public Key Infrastructure:\n1. RA   Registration Authority          bürgt für Verbindung öffentlicher Schlüssel-Identitäten/Attributen\n2. CA   Certification Authority         Stellt Zertifikate aus\n"
"3. VA   Validierungsstelle              Überprüfung von Zertifikaten\n4. DIR  Verzeichnisdienst               Verzeichnis mit ausgestellten Zertifikaten\n5. PSE  Personal Security Environment   Sichere Speicherung des privaten Schlüssels", #"Komponenten einer PKI",
"root (besitzt selbstsigniertes root-Zertifikat) -> stellt Zertifikate für untergeordnete CAs aus => Validierung eines Zertifikats via Zertifizierungspfad", #"Hierarchie von CAs",
"Jedes Zertifikat im Pfad muss gültig sein:\n"
"1. Signatur ist gültig.\n2. Keine veralteten Verfahren (z.B. SHA-1)\n3. Zertifikat nicht zurückgerufen\n4. Zertifikat ist (noch) nicht abgelaufen\n5. der Zertifizierungspfad endet bei einer Root-CA, der vertraut wird.", #"5 Anforderungen zur Zertifikatvalidierung",
"Falls privater Key eingeschränkt wurde (z.B. durch Diebstahl oder ungültigkeit)\nLösung mittels OCSP Stapling", #"Zertifikatsrückruf (Revocation)",
"= \"Online Certificate Status Protocol\"\nServer holt regelmässig Bestätigung von CA über Gültigkeit -> Bestätigung ist über mehrere Requests gültig -> Server liefert Bestätigung beim Verbindungsaufbau mit.\n"
"    ___________                     ____________   \n"
"   [           ]----(1)https...--->[            ]  \n"
"   [  BROWSER  ]                   [ Web-Server ]  \n"
"   [___________]<--(2)Zertifikat---[____________]  \n"
"                   gültig? j/n       / \    |      \n"
"                   Zeitstempel        |     |      \n"
"                                      |     |      \n"
"               (2)signiert von        |     | (1) regelmäßige Anfrage:      \n"
"                  OCSP? -> j/n        |     |     Ist Server-Zertifikat noch gültig?\n"
"                                      |    \ /     \n"
"                                  [OCSP-Responder] ", #"Wie funktioniert OCSP? (+Sketch)",
"Idee: Nutzer Alice hinterlegt Credentials bei vertrauenswürdiger Instanz/Service AuC. Für Zugriff auf Service B besorgt sich Alice vom AuC eine Authentizitätsbescheinigung (Ticket/Token/Assertion).\n"
"AuC prüft die Authentizität von Alice und erstellt Ticket für B -> Alice reicht Ticket an B weiter -> B prüft Ticket, führt aber keine eigene Authentisierung durch.\nKonsequenz: Trennung der Authentisierung (durch AuC: Policy Decision-Point, PDP) & Prüfung auf Gültigkeit (durch B: Policy-Enforcement-Point, PEP)", #"SSO - Konzept",
"Alice A            AuC (PDP)       NFS (PEP)       Mail (PEP)  \n"
"k_A                NFS: k_(NFS)    k_(NFS)         k_Mail      \n"
"||                                                             \n"
"||-------(1)------->|                                          (1) Request: Ticket zur Vorlage beim NFS\n"
"||                 ||                                          (2) CR-Protokoll Nachweis k_A\n"
"||<------(2)------>||                                          (3) Erstellung: Ticket für NFS (A kann es wiederholt nutzen)\n"
"||                 ||                                          (4) Ticket für NFS\n"
"                   || (3)                                      (5) Forward: Ticket für NFS\n"
"|<-------(4)--------|                                          (6) Ticket-Prüfung, Autorisierung separat\n"
"||                                                             \n"
"|-----------------(5)------------------>|                      \n"
"                                       || (6)                  ", #"SSO - Sketch",
"1. Unternehmensnetzwerk: Kerberos-Protokol\n2. Web-Anwendungen: OpenID Connect und OAuth\n3. Web-basiert, Akademia: Shibboleth (auch TUM)", #"3 Arten von SSO in der Praxis",
"AuC heißt Key Distribution Server (KDC), ist aufgeteilt in: Ticket-Granting Service (TGS) & Authentication Service\n Verwendet im Standard nur symmetrische Kryptographie\nPre-shared Master Key mit KDC für jeden Nutzer und Dienst: Nutzer A (k_A wird aus Passwort von A abgeleitet) Dienst F (k_F zufällig generiert)\n"
"Der Ticket-Granting Service (TGS) des KDC stellt auf Anfrage (z.B. von A) ein Authentizitäts-Ticket für A zur Vorlage bei einer Instanz/Service S aus (Ticket enthält u.a. die Identitäten A und S und einen symmetrischen Shared Key k_(AS))", #"Kerberos - Grundsätze",
"T^(AS): gültig für A & Server/Service S: T^(AS) = (S, A, addr, timestamp, lifetime, kAS)\nMit(S = Servername, A = anfordernde Instanz, addr = IP-Adresse, lifetime = Key-lifetime, k_(AS) = Schlüssel k_(AS) für S und A\n"
"Ticket wird von TGS mit Master-Key kS von S verschlüsselt (E_(k__s)(T^(AS))) (Bem.: idR wird der AES verwendet) \n-> Ticket T^'(AS) dient der Instanz A zur Vorlage bei S (A muss S berechtigten Besitz des Tickets T^(AS) nachweisen \n-> durch Konzept des Authenticators erreicht", #"Kerberos - Ticketerstellung",
"Authent^A (von Instanz A erzeugt): Authent^A = A, addr, timestamp\nAuthenticator wird mit shared key kAS verschlüsselt: E_(k__AS)(AuthentA) \n-> Nachweis für S, dass A berechtigt ist, TAS vorzulegen, da A Kenntnis des shared Keys k_(AS) nachweist\n"
"(Bem.: Es werden Timestamps in Tickets und Authenticators verwendet: die Partner müssen zeitsynchronisiert sein)", #"Kerberos - Authenticator",
"Vergabe von Zugriffsberechtigungen und Kontrolle: Verhindern von unautorisierter Ressourcennutzung", #"Definition \"Autorisierung\""
"\"Wer darf was, auf welche Weise, unter welchen Bedingungen nutzen (permit) bzw. nicht nutzen (deny)?\"\n1. Wer: Zugreifende Instanz identifizieren (Subjekt: z.B. Nutzer, Prozess, Server, Service)\n2. Auf was: genutzte(s) Objekt/Ressource identifizieren (Objekt/Ressource: z.B. Datei, Datenbankeintrag, Page)\n"
"3. Auf welche Weise: Zugriffsrechte spezifizieren (Zugriffsrecht: z.B. r,w,x, Suchen, Kamera_an, Internet)\n4. Unter welchen Bedingungen: Kontexte spezifizieren (Unter welchen Bedingungen: Kontexte spezifizieren)", #"Autorisierung - Regelwerk / (4-point-)Access Policy",
"1. need-to-know                        minimale Rechte\n2. least priviledge                    nur absolut notwendige Rechte\n3. Complete Mediation / Zero Trust     jeder Zugriff auf eine Ressource ist zu kontrollieren", #"3 Prinzipien zur Rechtekontrolle",
"1. DAC     Discretionary Access Control    benutzerbestimmbare Vergabe/Rücknahme, Ressourcen-Owner bestimmt\n2. RBAC    Role-based Access Control       Aufgaben-orientiert\n3. MAC     Mandatory Access Control        systembestimmte Vergabe/Rücknahme, globale, systemweite Regelungen", #"3 Modelle für Rechtevergabe",
"(Dynamische) Menge von Objekten O_t, (Dynamische) Menge von Subjekten S_t mit: S_t <Teilmenge von> O_t, Menge von Rechten R, Zugriffsmatrix M_t: S_t × O_t → 2^R (Schutz-Zustand zur Zeit t)\n"
"Dynamik: neue Subjekte, neue Objekte, Rechtevergabe, Rechte-Entzug, Löschen\n\n"
"    M_t    |   Datei1   |   Datei2   |   Datei3   |   Prozess1    |    Prozess2   |\n"
"-----------+------------+------------+------------+---------------+---------------+\n"
" Prozess1  |    r/w     |            |    r/w     |               |      s/r      |    r/w = read, write\n"
"-----------+------------+------------+------------+---------------+---------------+    s/r = send, receive\n"
" Prozess2  |            |            |            |      s/r      |               |    o/e = owner, execute\n"
"-----------+------------+------------+------------+---------------+---------------+    s   = signal\n"
" Prozess3  |            |    o/e     |            |       s       |               |\n"
"Pro: Sehr einfach (Sowohl als Modell als auch zur Implementierung)\nCon: Schlecht Skalierbar, Rechtevergabe an Subjekte, nicht Aufgaben, Rechterücknahme aufwändig\nVerbesserung durch Gruppenkonzept", #"Zugriffsmatrix-Modell (ZM) - Vor/Nachteile (+Sketch)",
"Aufgabenorientierte Rechtevergabe durch Rollen-Konzept (Rolle = Aufgabe und die damit verbundenen Verantwortlichkeiten, Pflichten & Berechtigungen)\n"
"Modell: Menge von Subjekten (Nutzer) S_t, Menge von Objekten O_t, Menge von Rollen Role (Rolle r ∈ Role) -> Subjekte sind Rollen zugeordnet: sr : S_t → 2^Role\nMenge von Zugriffsrechten P (permission) für Objekte, Rollen erhalten Rechte: pr : Role → 2^P\n" 
"Nutzer s meldet sich mit einer Rolle an: RL <Teilmenge von> sr(s) (RL ist die Menge der aktiven Rollen des Benutzers s)\n\nRollenhierachie: Vererbung von Zugriffsrechten entlang der Rollenhierarchie\n"
"Basis: Definition einer partielle Ordnung <= auf Role -> Vererbung der Rechte: hierarchisch höhere Rollen erben die Rechte von tieferen Rollen\n"
"Pro: Gute Modellierung unternehmerischer Strukturen & Prozesse (bspw bereits in SAP-Produkte integriert), gut skalierbar in Bezug auf Subjekt-Dynamik, Rollen sind eher statisch,\nRollenmitgliedschaft dynamisch: Rollen-Zuweisung (automatisierte Vergabe der Rechte), Rollen-Entzug (automatisierter Entzug der Rollenrechte)\n"
"Con: Vererbungskonzept verstößt idR gegen need-to-know, Umsetzung (häufig Hunderte von Rollen), keine Kontrolle von Informationsflüssen", #"Role-based Access-Control (RBAC) - Vor/Nachteile",
"Einfach zu prüfende, systemglobale Regeln zur Beschränkung von Inofrmationsflüssen \n-> Multilevel Security (MLS): Klassifizieren von Subj. & Obj. mit Label, Flussrelation die erlaubte FLüsse ziwschen klassifizierten Ob. & Subj. beschreibt\n"
"Pro: Einfach zu implementieren, Formales Modell, potentiell beweisbare Eigenschaften -> Gut geeignet zum Nachbilden hierarchischer Informationsflussbeschränkungen, häufig in Unternehmen, Behörden. \nVarianten der MLS-Policy in der Praxis stark verbreitet -> integriert in Standardsoftware und u.a. in SE-Linux.\n"
"Con: Problem des Blinden Schreibens: s darf o modifizieren, aber anschließend (wegen no-read-up) nicht lesen! \nProblem: Information/Objekte werden sukzessive immer höher eingestuft. Sanitizing-Konzept in der Praxis genutzt -> Zurückstufen.", #"Bell-LaPadula-Modell + Vor/Nachteile",
"no-read-up & no-write-down: Intuitive Interpretation der Regeln (Festlegen partielle Ordnung, Info-flüsse nur entlang der Ordnung zulassen)", #"BLP-MAC-Policy",
"Rechte an Objekten (z.B. Kamera_an, Kamera_aus), Spaltenweise Realisierung der Zugriffsmatrix\n Linux: Rechtevergabe nur an Owner, Group, Rest-of-World", #"Access Control List (ACL) an Unix/Linux",
"1. Client bittet Alice um Rechte an ihren Fotos.\n2. Alice gibt dem Client das Recht.\n3. Client bittet Autorisierungs-Server (AS) um Ausstellung eines Access Token.\n4. AS erstellt Access-Token (Capability) und sendet ihn an Client.\n"
"5. Client weist dem Cloud-Dienst (Ressource Server (RS)) das Token vor.\n6. RS prüft AT und erlaubt Zugriff auf Fotos von Alice.", #"Access Token bei OAuth - Ablauf",
"Aufteilung in: \nBerechtigungskontrolle: PDP (Policy Decision Point)\n\tPrüfung beim erstmaligem Zugriff auf ein Objekt (z.B. open())\n\tAusstellung einer Bescheinigung (z.B. Capability, File-Handle)", #"Berechtigungskontrolle",
"Zulässigkeitskontrolle: PEP (Policy Enforcement Point)\n\tDurch Objektverwalter (z.B. Server) oder OS-Kernel\n\tBei Objektzugriff: Prüfen der Gültigkeit der Bescheinigung\n\tKein Zugriff auf die Rechteinformation (z.B. ACL, notwendig)", #"Zulässigkeitskontrolle",
"Hybride Konzepte: PDP (auf Basis von ACLs, Ausstellen einer Capability), PEP (bei Vorlage von Capabilities)", #"Hybride Konzepte von Zugriffskontrolle",
"Identifikatoren    u.a. Nutzer Prozesse, Dateien und deren sicherer Verwaltung, z.B. inode unter Linux\nZugangskontrolle   Authentisierung, u.a. Passwortverwaltung\n"
"Zugriffs- und Informationsflusskontrolle\n\t\tKonzepte: ACL, Capabilities, Labeling/Klassifizierung\n\t\tKontrollen: idR Bestandteil des Dateisystems (Prüfen der ACLs/Capabilities/Token/Handles, Prüfen der zulässigen Flüsse gemäß z.B. BLP Regeln)\n"
"Speicherschutz     Festplattenverschlüsselung, RAM: Canaries, DEP, ASLR \nVirtualisierung    u.a. Isolierte virtuelle Adressraume pro Prozess", #"Wichtige Schutz- und Kontrollaufgaben des Betriebssystems",
"Angreifer platziert mittels Buffer-Overflow Shellcode in Form von bösartigem Maschinencode auf den Stack -> Rücksprungadresse zeigt nach Überlauf auf Shellcode => Programm führt Code des Angreifers aus", #"Buffer-Overflow-Angriffe",
"= \"Return orientated Programming\"\nRücksprung nicht zu Funktionsanfang, sondern zu beliebiger Instruktionsfolge im Programm, die mit einem Return endet (ROP-Gadget) -> Verknüpfung von ROP-Gadgets zu ROP-Chains mit beliebiger Funktionalität", #"ROP",
"Einfügen eines zufälligen, zur Laufzeit erzeugten Canary-Werts auf dem Stack vor der gespeicherten Rücksprungadresse.\nVor dem Return: Programm vergleicht Canary-Wert mit Referenzwert -> Veränderungen führen zu Programmterminierung.\nErzeugungs- und Prüflogik wird durch Compiler (z.B. GNU CC) ins Programm eingebracht", #"Schutz durch Stack Canries",
"= \"Data Execution Prevention\"\nZiel: Nur .text Segment sollte ausführbar sein\nCPU-Feature NX-bit (No-eXecute) Seiten als nicht ausführbar markiert\nZusätzlich auch: nicht schreibbar: W xor X Policy -> Verhindert, dass Angreifer Shellcode zur Ausführung bringen kann.", #"Schutz durch DEP",
"= \"Address Space Layout Randomization\"\nDEP schützt nicht vor ROP -> ASLR\nAdress-Randomisierung von Stack, Heap und Bibliotheksfunktionen individuell für jeden Programmstart(Linux) bzw pro Systemstart (Windows)\nAber: Text-Segment nicht randomisiert\n\nErweiterung: PIE (Position Inpendent Executable)", #"Schutz durch ASLR",
"VMM= \"Virtual-Machine-Monitor\"\nSoftware, die die virtuelle HW-Schnittstelle zur Verfügung stellt (z.B. VMWare)\n1. Isolation       VMs sind besser von einander und vom VMM abgeschottet\n"
"2. Überwachung     VMM hat jederzeit vollen Zugriff auf die Ressourcen und den Zustand der VMs und der virtuellen Hardware, sieht alles\n3. Kontrolle       VMM kann VMs kontrollieren und verändern, u.a. anhalten, neu starten, Netzwerk-Verkehr filtern", #"3 Sicherheitsrelevante Eigenschaften: VMM bzw. Hypervisor",
"Oft sollen einige wenige Anwendungen auf dem gleichen BS voneinander abgeschirmt in einer Sandbox ablaufen -> Virtuelle Maschine (VM) pro Sandbox sorgt für Isolierung\n"
"Aber: VM umfasst Anwendungsprogramm plus Betriebssystem, BS und Bibliotheken belegen Speicher in RAM und auf Festplatte mehrfach! -> Betriebssystem--Level Virtualisierung (z.B. Container-Lösung)", #"Betriebssystem-Level Virtualisierung: Container",
"Ein Anwendungsprogramm wird zusammen mit seinen Bibliotheken und Abhängigkeiten in einer Einheit gebündelt. Ein Container läuft als isolierter Prozess im User-Space. Mehrere Container können auf einem Rechner nebenläufig laufen -> teilen sich Betriebssystem (z.B. Docker)", #"Container-Konzept: Leichtgewichtige Virtualisierung",
"Perimeter-Schutz, Filtern von Daten-Paketen\nNetzwerk wird in verschiedene Netzsegmente unterteilt ->  An Segmentgrenzen Kontrolle durch Firewall (-Regeln): erlaubte Datenflüsse festlegen. Kontrolle der Einhaltung der Regeln: Ein- und Auslasskontrolle für Datenpakete", #"Firewalls",
" sehr einfache Form einer Firewall: Paketfilter analysieren die Header-des Datenpaktes nach Firewall-Regeln, festgelegt z.B. in iptables (unter Linux) (z.B.: Quelle (src), Ziel (dst) IP Adresse \nAktion pro Datenpaket durchführen: Paket accept, -> drop -> reject", #"Paketfilter",
"= \"Deep Packet Inspection\"\nBetrachtet auch den Payload-Teil eines Pakets. Meistens kein direktes Verständnis des Applikationsprotokolls. Filterung meistens implementiert basiert auf einfachem Signaturmatching\nPrüfung auf Protokollverletzung und Malware möglich\nMissbrauchspotential: Zensur (z.B. um Verbindungsaufbau zum TOR-Netzwerk zu erkennen)", #"DPI",
"= \"Applikation Layer Gateway\"\nZugeschnitten auf bestimmte Applikationen (z.B. HTTP,SMTP, FTP)\nFirewall hat Zugriff auf kompletten Verbindungszustand\nVerbidung wird terminiert und vom ALG selbst erneut aufgebaut (Relay-Konzept)\nDaten werden oft durch Firewall verändert!", #"ALG / Proxy-Firewall",
"1. Authentifikation        nur Gerät oder pro Dienst/Nutzer, einseitig oder wechselseitig\n2. Vertraulichkeit         1 Schlüssel pro Verbindung oder Schlüssel pro Datenpaket\n3. Integrität              Integrität des Verbindungsaufbaus oder pro Datenpaket\n"
"4. Schlüsselaustausch      Pre-shared Key, DH-Verfahren, RSA-Verfahren\n5. Verfahren               Statisch festgelegte Verfahren oder konfigurierbar (z.B. u.a. AES-128 GCM, SHA256, X509-Zertifikate)", #"Transportsicherheit: 5 Punkte zu Sicheren Verbindungen",
"1. Aufbau des sicheren Kanals:     Handshake-Protokoll         Abstimmen des Verschlüsselungsverfahren & der zu nutzenden Cipher-Suite (1 von 5)\n\t\t\t\t\t\t\t\tAuthentisierung (einseitig, beidseitig)\n"
"\t\t\t\t\t\t\t\tErzeugung von zwei Kommunikationsschlüsseln k_(AB), k_(BA) pro Richtung und eines MAC-Schlüssels k_(mac) für den Handshake\n"
"2. Verschlüsselte Kommunikation:   Application Data Protokoll Datenpakete der jeweiligen Anwendung (z.B. HTTP) werden verschlüsselt und versandt -> Empfänger entschlüsselt Paket, Anwendung verarbeitet Daten weiter.", #"TLS-Protokollablauf 2 Phasen",
"        CLIENT                           SERVER    \n"
"           |                               |       \n"
"     (1)   |----------ClientHello--------->|       (A) = {R_C, [S^1, S^2, S^x, . . . ], [(g_C)^1, (g_C)^2, (g_C)^x, . . . ], [A^1, A^2, A^x, . . . ] }\n"
"           |              (A)              |       (B) = {R_S, S^x, (g_S)^x, C_S, Sig_(ks) (H(∇))}, {TEnck_(SC) (HMAC_(k_(mac)) (∇))}\n"
"           |                               |       (C) = {TEnc_(kCS) (HMAC_(kmac) (∇))}\n"
"     (2)   |<----ServerHello, Finished-----|        ∇  = Alle Nachrichten des Handshakes bis zu diesem Punkt\n"
"           |              (B)              |       \n"
"           |                               |       \n"
"     (3)   |-----------Finished----------->|       \n"
"           |              (C)              |       \n"
"           |                               |       \n"
"     (4)   |<------Application Data------->|       \n"
"           |                               |       \n\n\n"
"   Wo      |       Was         |      Stellt ... dar       |          Zweck\n"
"-----------+-------------------+---------------------------+------------------------\n"
"  (A)(B)   |    R_C, R_S       |      Zufallszahlen        | Replay-Verhinderung\n"
"  (A)(B)   |       S^x         |      Cipher Suites        | Vom Server gewünschte Suite\n"
"  (A)(B)   |  [S^1, S^2,..]    |      Cipher Suites        | Liste vom Client unterstützte Cipher-Suites\n"
"  (A)(B)   |    (g_s)^x        |   DH-Params von Ser/Cli.  | DH-Publickey des Servers für das gewählte Verfahren\n"
"  (A)(B)   | [(g_c)^1, (g_c)^2]|   DH-Params von Ser/Cli.  | Öffentliche DH-Parameter des Clients für alle Cipher-Suites\n"
"   (A)     | A^x bzw [A^1, ...]|   Signaturverfahren       | Vom Client unterstützte Signaturverfahren\n"
"   (B)     |       C_S         |Serverzert. mit priv. Key k| Server-Zertifikat zum gewählten Signaturverfahren & öffentlichen Schlüssel mit Identität (d.h. URL) des Servers verknüpft\n"
"   (B)     |     Sig_k(m)      |   Sig über m mittels k    | Sig_(ks)(H(∇)): Nachweis, dass der Server den privaten Schlüssel zum Zertifikat besitzt sowie Authentisierung von (g_s)^x\n"
"   (B)     |   HMAC_k(m)       |  HMAC über m mittels k    | TEnc_(k_SC) (HMAC_kmac(∇)): Nachweis, dass der Server kmac, und damit das DH-Geheimnis, besitzt. D.h. er muss im Besitz\n"
"           |                   |                           | des privaten Keys zu (g_s)^x sein.Außerdem Authentisierung und Integritätssicherung des gesamten bisherigen Handshakes (inkl. (g_s)^x\n"
"   (C)     |   HMAC_k(m)       |  HMAC über m mittels k    | TEnc_(k_CS) (HMAC_kmac(∇)): Nachweis, dass der Client das DH-Geheimnis besitzt und Integritätssicherung des gesamten Handshakes.\n"


"Client (Rechner A) initiiert den Verbindungsaufbau mit ClientHello (ID bezeichnet eine neue Verbindung (sessionID),cs_A ist die Liste von Cipher-Suites, die A unterstützt)\nServer B besitzt einen statischen Signaturschlüssel und ein Serverzertifikat cert(e_B) für den öffentlichen Server-Key e_B\n"
"\t• Server B weist nach, dass er auf die aktuelle Hello-Nachricht antwortet, indem er m1 mit seinem d_B signiert.\n\t• Server B signiert auch seine eigenen Daten in m2.\n\t• Mit DH-e_A und DH-d_B berechnet Server B das DH-Secret s.\n\t• Server B wählt aus cs_A die zu verwendende Suite aus: cs\n"
"\t• Server B weist nach, dass er DH-dB und damit s kennt: er generiert k_AB, k_BA, k_(mac) = KDF(s, R_A, R_B).\nServer B antwortet mit ServerHello und finish\n\t• Sendet seinen DH-e_B, die gewählte Suite cs, seine R_B \n\t• die signierten Daten sowie das Zertifikat cert(e_B), sodass der Rechner A die Signatur prüfen kann.\n"
"\t• Der Server kann bereits verschlüsselte Anwendungsdaten zurücksenden in m5, da er bereits k_(BA) berechnet hat. Die Variante von TLS 1.3 heißt 1RTT (Round Trip Time).\n• A prüft in Schritt 12,13 die Signatur und Integrität von m1, m2, m3\n\t• Signaturvalidierung mit eB aus dem Zertifikat cert(e_B))\n"
"\t• A berechnet mit DH-dA und DH-eB das DH-Secret s und generiert die notwendigen Schlüssel: k_(AB), k_(BA), k_(mac) = KDF(s, R_A, R_B)\n\t• A entschlüsselt D_(kBA)(m4) und prüft Integrität von m1, m3.\n\t• A sendet finish und informiert B damit, dass alles ok ist.", #"TLS-Handshake",
"= \"Virtual Private Networks\"\nNetzinfrastruktur, bei der Komponenten eines privaten Netzes über ein öffentliches Netz kommunizieren und die Illusion besitzen, dieses Netz zur alleinigen Verfügung zu haben\nGängige Implementierungen: OpenVPN (TLS), IPSec, Wireguard\nBspw. Nutzung: End-to-Site-VPN / Remote-Access-VPN", #"VPN",
"1. Secure Coding Guidelines beachten       um häufige Programmierfehler (z.B. fehlende Eingabefilterung, zu vermeiden)\n"
"2. Sicherheitskonzepte beachten            in Programmiersprachen vorhanden (z.B. Memory safe vs. Unsafe Konzepte)\n"
"3. Sicheren Entwicklungszyklus etablieren  Testen, Code-Reviews, Analysen\n"
"4. Toolchain                               Werkzeuge u.a. zur Prüfung, Filterung einsetzen", #"Secure Programming - 4 Maßnahmen",
"z.B.:\nEingabe Filterung   um BO-Probleme, Code-Injection Probleme zu reduzieren, u.a. prepared Statement, Library-Funktionen\nOutput Encoding     Escape Sequenzen, um Return-Werte nicht als ausführbare Befehle zu misinterpretieren\n"
"Memory Safety       sichere Programmiersprachen, Canaries, ASLR\nCrypto Guideline    aktuelle Verfahren und Schlüssellängen Software-Hilfsmittel/Tooling: u.a. automatische Code-Analyse\nLinter              statischen Analysen: out-of-bounds check, Typ-Prüfung, ..", #"OWASP Secure Coding Practices"
"1. Warnings            sollten als Errors angezeigt werden (GCC/clang: -Wall -Wextra -Wpedantic -Werror)\n"
"2. Linter-Tool         Erkennt Programmierfehler und Bad Practices (z.B. invalide Code Pfade mit uninitialisierten Variablen (clang-tidy, eslint, Pylint, …))\n"
"3. Type-Annotation     erkennt frühzeitig Fehler (z.B. Zuweisung an falsch geschriebenes Attribut)\n"
"4. Sanitizer           Erweitern von Code durch den Compiler mit Sanity-Checks, um Speicherverletzung während der Laufzeit zu erkennen", #"Nutzen von 4 Werkzeugen sichere Programmierung",
"Funktionen möglichst nicht selbst implementieren (Stattdessen: Populäre und getestete Bibliotheken sowie implementierte Systeme und Protokolle verwenden, \nz.B. Authentifikation im Web von vielen Webseiten benötigt, aber sichere Implementierung ist schwierig -> Verwendung von OAuth, LDAP (TUM), Firebase)\n"
"Bei Client-Server Architektur niemals sicherheitsrelevante Validierung auf dem Client durchführen (z.B.: Client prüft, ob lokaler Nutzer Admin ist, greift dann auf Admin-Endpoint zu)\n"
"Keinen Code von StackOverflow o.ä. blind kopieren, ohne zu verstehen, was dieser bewirkt. Meist spielt Sicherheit in Codeschnipseln allerdings keine Rolle!", #"Allgemeine Richtlinien",
" = \"Informationssicherheitsmanagementsystem\"\n ISMS durch Standard ISO/IEC 27001 definiert\nFestlegen von Verfahren und Regeln innerhalb einer Organisation, zur Steuerung, Kontrolle und zum Aufrechterhalten sowie fortlaufenden Verbesserung der Informationssicherhei\nt"
"U.a. gesetzliche Auflagen (IT-Sicherheitsgesetz 2.0) für bspw. KRITIS-Betreiber (KRITIS-Sektoren: Grundversorgung (z.B. Wasser), Versorgung(z.B. Transport/Verkher), Dienstleistungen (z.B. IT, Versicherungen))", #"ISMS",
"PDCA =\nPlan:  z.B. Funktionale Anforderungen, Risikoanalyse\nDo:    z.B. Sicherheitsregeln definieren, Umsetzung v. Sicherheitsmaßnahmen\nCheck: z.B. Code-Review, Testing\nAct:   z.B. Patch, Update\n"
"Problemstellung  <===========  \n"
"   ||                       || \n"
"   ||  Plan                 || \n"
"   \/                       || \n"
"Maßnahmen                   || \n"
"   ||                      A|| \n"
"   ||  Do                  c|| \n"
"   \/                      t|| \n"
"Funktionsfähiges System     || \n"
"   ||                       || \n"
"   ||  Check                || \n"
"   \/                       || \n"
"Bewertung ===================  ", #"PDCA-Zyklus",
"1. Strukturanalyse (Beschreibung des (vorhandenen bzw. geplanten) IT-Systems)\n\tBeschreibung der Systemfunktionalität (vorhandener bzw. einzusetzender Systemkomponenten & -dienste), \n\tdes Pflichthefts(Systemanforderungen und Einsatzumgebung des Systems), \n\tErstellung eines Netztopologieplans (grafische Übersicht aller Teilkomponenten + deren Verwendungszweck / technischen Details / Vorhandener Dienste)\n"
"\n2. Schutzbedarfsermittlung (Entscheiden, welchen Schutzbedarf bezüglich CIA haben Objekte, IT-Systeme, Kommunikationsverbindungen, Räume) \n\tSchutzbedarf orientiert sich an möglichen Schäden\n\tSchutzbedarfsfeststellung anhand von Schadensszenarien\n\tSchutzbedarf/Konsequenz nicht quantitativ sondern qualitativ: normaler (begrenzt und überschaubar), hoher (betrachtlich), sehr hoher Bedarf (katastrophales Ausmaß)", #"2 Phasen des BSI-Sicherheitsprozesses",
"1. Verstoß gegen Gesetze und Vorschriften\n2. Datenschutz\n3. Persönliche Unversehrtheit\n4. Beeinträchtigung der Aufgabenerfüllung\n5. negative Innen- oder Außenwirkung\n6. finanzielle Auswirkungen\n"
"Es können mehrere Szenarien zutreffen (z.B. OnlinePortal-Ausfall -> Finanzielle Auswirkungen & Imageschäden)\n"
"Verstöße (z.B. gg. DSGVO): normal (geringfügiger Verstoß: ≤ 10T € oder ≤ 2%' des Umsatzes), sehr hoch (gravierender Verstoß: ≤ 20Mio € oder ≤ 20%' des weltweiten Jahresumsatzes)", #"6 Schadensszenarien",
"   Was     	                Bedrohung (Bsp)                          Abwehr\n"
"---------------------------------------------------------------------------------------------------------\n"
"S poofing                  Phishing, Identity-Theft. etc.      MFA, SSO (Kerberos), PKI, etc.\n"
"T ampering                 Unautorisierte Datenänderung        Hashfunktion, MAC-Verfahren\n"
"R epudiation               Abstreiten von Aktionen             Digitale Signatur, Authentisierung\n"
"I nformation Disclosure    Offene Übertragung, verb. Zugriff   Verschlüsselung (Daten, Kommunikation/TLs)\n"
"D enial of Service         Ransomware, Spam, DDoS Attack       Priorisierung, Quoten, filtern (Firewall)\n"
"E levation of Privelige    Rechteerweiterung, Buffer-O.        Eingabeprüfung(BO), Isolierung, Sandoxing", #"Bedrohungsanalyse STRIDE",
"Graph-basierte Hilfsmittel für Bedrohungs- und Risikoanalyse - Pro Angriffsziel ein Baum: \n• Wurzel beschreibt ein Angriffsziel, z.B. Safe knacken\n• Knoten beschreibt einen einzelnen Angriffsschritt\n• Pfad von Blatt zur Wurzel: Angriff zum Erreichen des Ziels", #"Bedrohungsbäumen (attack tree)",
" Risk-Kategorie     	            Was                                                 0          2.5          5          7.5              10\n"
"-------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"
"D amage                    Schadenspotential der Bedrohung                         |kein Schaden[0]            Informationspreisgabe[5]    keine Verfügbarkeit[10]\n"
"R eproducability           Schwierigkeitsgrad, den Angriff nachzuahmen             |schwierig/unmöglich[0]     komplex[5]      leicht[8]   sehr leicht[10]\n"
"E xploitability            Aufwand, den Angriff durchzuführen                      |               Fortgeschrittene Programmierfähigkeiten[2.5]\n"
"                                                                                   |                           verfügbare Tools[5]\n"
"A ffected                  Anzahl der vom Angriff potentiell betroffenen Nutzer    |keine Nutzer[0] individuelle Nutzer[2.5]               alle Nutzer[10]\n"
"D iscoverability           Schwierigkeit, die Bedrohung zu finden/nutzen           |schwer erkennbar[0]                        bekannte Schwachstelle[8]\n"
"                                                                                   |                                                       Direkt erkennbar[10]\n\n"
"Beurteilung des Risikos:\n01-10  Gering      Geringes Risiko für Infrastruktur oder Daten\n11-24  Medium      Moderates Risiko, behandeln nach: kritisch, hoch\n"
"25-39  Hoch        hohes Risiko duch Schwachstelle, schnell beheben\n40-50  Kritisch    kritische Schwachstelle, sofort beheben", #"Risiko-Beurteilung mit der DREAD-Methode",
"Simulation des Verhaltens eines vorsätzlichen Angreifers -> Schwachstellen und potentielle Schäden ermitteln - Arten:\nBlackbox (keine/geringe System-Kenntnisse vorhanden)\nWhitebox (detaillierte Kenntnisse über interne Strukturen, Anwendungen, Dienste, Source-Code etc)\n"
"Typischerweise: Passwörte raten, dictionary attacks, False Datenpaketeinspielung, etc", #"Penetrationstests Black/Whitebox",
"Ziel: Extrahieren und Verstehen von Softwarebausteinen, die nur in Maschinencode oder kompilierter Form vorliegen (Notwendig in Blackbox Penetrationstests, häufig zeitaufwändige manuelle Arbeit)\nDynamische Analyse: u.a. Programmbeobachtung, Debugger\nStatische Analyse: u.a. Decompiler\n"
"Um RE zu erschweren, wird von Angreifern, aber auch von Software-Entwicklern häufig Obfuskation eingesetzt (Abwandlung des Kontrollflusses, Einfügen von redundantem Code) -> Aber: Obfuskation verhindert kein RE, es verlangsamt nur", #"Reverse Engineering (RE)",
"Ziele: Finden von Programmfehlern, Schwachstellen, Verschiedene Techniken im Einsatz: u.a. Fuzzing (Automatisiertes Finden von Schwachstellen mit zufällig generierten Programmeingaben: testen der Software auf unerwünschtes Verhalten, dynamische Analyse) - idR Blackbox Fuzzing, Quellcode muss nicht vorliegen", #"Programmanalyse",
"Ziele: Einheitliche Bewertungskataloge, Vergleichbarkeit: Wird das Notwendige gemacht; wird es richtig gemacht!\nMaßnahmenkatalog: Menge von Sicherheitsgrundfunktionen\nQualität (der Realisierung): z.B. getestet, ..., formal verifiziert\nGüte (der verwendeten Mechanismen): ungeeignet, ..., unüberwindbar\n"
"Bewertung durch unabhängige Stelle: Evaluation und Zertifizierung, Beispiele für Zertifizierungsinstanzen: TÜV (akkreditiert)\nLeitlinien für Hersteller bzw. Entwickler: Protection Profiles (best practices: worauf ist zu achten?)", #"Bewertung der IT-Sicherheit",
"Common Criteria:\nTOE    Target of Evaluation        IT-Produkt oder -System und die zugehörige Begleitdokumentation, die zu evaluieren sind\nST     Security Target             Menge von Sicherheitsanforderungen, die Grundlage der Evaluation eines TOE sind\n"
"PP     Protection Profile          Implementierungsunabhängige Menge von Sicherheitsanforderungen eines TOE (Risikoanalyse, Schutzziele, Schutzmaßnahmen)\nEAL    Evaluation Assurance Level   7 Evaluationsstufen\n", #"Common Criteria, EAL",

"n/a",
"n/a",
"n/a",
"n/a",
"n/a",
"n/a",
"n/a",
"n/a",
"n/a",
"n/a",
"n/a",
"n/a",
"n/a",
"n/a",
"n/a",
"n/a",
"n/a"
]
