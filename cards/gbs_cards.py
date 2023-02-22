# Themengebiete
# C
# Prozesse Thread
# Scheduling
# Interprozesskommunikation
# Speicherverwaltung
# Dateisysteme
# Ein und Ausgabe
# Virtualisierung
# Zusammenfassung



# Fragen Prozesse

questions_prozess_thread = [
    "Implementierung von Prozessen",
    "Erzeugung von Prozessen",
    "Zombies",
    "Waisen",
    "Prozess vs Thread Programm",
    "Prozess vs Thread Pro contra"
]

answers_prozess_thread = [
    "Prozesse werden in der Regel durch den Betriebssystemkernel erzeugt. Der Kernel ist für die Verwaltung der Prozesse zuständig. Er stellt die Prozesse mit ihren Ressourcen bereit und überwacht deren Verhalten. \n" + 
        "Informationen für die Prozessverwaltung\n" +
        "\t- Prozessidentifikator (PID) \n" + "\t- Registern \n" + "\t- Programmzähler \n" + "\t- Stackpointer \n" + "\t- Statusinformationen (wartend & rechnend) \n" + "\t- Priorität \n" + "\t- Zeiger auf den Elternprozess \n"
        "Informationen für die Speicherverwaltung:\n" +
        "\t- Zeiger auf den Speicherbereich des Prozesses \n" + "\t- Zeiger auf den Speicherbereich des Stacks \n" + "\t- Zeiger auf den Speicherbereich des Heap \n" +
        "Informationen für die Dateisystemverwaltung:\n" +
        "\t- Rootverzeichnis \n" + "\t- Zeiger auf die Dateideskriptoren", # Implementierung von Prozessen
    "POSIX-Systemcall: pid_t fork()\n" + 
        "Eltern-Prozess erzeugt extakte Kopie des eigenen Prozesses. \n" +
        "Der neue Prozess wird als Kind-Prozess bezeichnet. \n" +
        "Jeder Prozess hat einen eindeutigen Prozessidentifikator (PID). \n" +
        "Der PID des Kind-Prozesses ist der PID des Eltern-Prozesses + 1.", # Erzeugung von Prozessen
    "Zombies sind Prozesse, die beendet wurden, aber noch nicht von den Eltern-Prozessen abgeholt wurden. \n" + 
        " - Der Prozess ist beendet, aber noch nicht von den Eltern-Prozessen abgeholt worden. \n" +
        " - Wenn ein Kind Porzess so teriniert, dann wird der Speicher des Prozesses de-allokiert und der Exit-Status in den PCB geschrieben. \n" +
        " - Sobald der Exit Status mit wait(PID) abgeholt wurde, wird der Prozess aus dem Prozess-Tabelle entfernt. \n", # Zombies  
    "Waisen entstehen, wenn der Eltern-Prozess vor dem Kind-Prozess beendet wird.", # Waisen
    "\t\t Prozess \t Thread \n" +
        "Erzeugung \t fork() \t pthread_create() \n" +
        "Beendigung \t exit() \t pthread_exit() \n" +
        "Warten \t\t wait() \t pthread_join() \n" +
        "Kommunikation \t Pipes \t\t Shared Memory \n" +
        "Synchronisation  Semaphoren \t Mutex \n" +
        "Speicher \t Heap \t\t Stack \n" +
        "Adressraum \t getpagesize() \t getpagesize()", # Prozess vs Thread Programm
    "\t\t Prozess \t Thread \n" +
        "Erzeugung \t teuer \t billig \n" +
        "Verwaltung \t teuer \t billig \n" +
        "Adressraum \t Eigener \t Gemeinsamer \n" +
        "Kommunikation \t Langsam \t Schneller" # Prozess vs Thread Pro contra
    
]

questions_scheduling = [
    "Ziele für Alle Systeme",
    "Ziele für Batch-Systeme",
    "Ziele für Interaktive Systeme",
    "Ziele für Echtzeit Systeme",
    "Kriteren zur Auswahl von Prozessen",
    "Prozessorverwaltung",
    "Ablauf Dispatching",
    "Wann wird der Dispatcher aktiv?"
    "Scheduling Klassen",
    "Scheduling Strategien in Batch Systemen",
    "Scheduling Strategien in interaktiven Systemen",
    "Scheduling Strategien in Echtzeit Systemen",
    "Multilevel Scheduling",
    "Varianten bei Multicore Scheduling",
    "Globale Warteschlange",
    "Eine Warteschlange pro Prozessor",
    "Hybride Herangehensweise für Wareschlangen",
]

answers_scheduling = [
    "Fairness: Jeder Prozess soll gleich viel CPU-Zeit erhalten. \n" +
        "Balance: Alle Teile des Systems (CU, I/O) möglichst effektiv auslasten.", # Ziele für Alle Systeme
    "Durchsatz: So viele Prozesse wie möglich in möglichst kurzer Zeit abarbeiten. \n" +
        "Ausführungszeit: Prozesse so schnell wie möglich beenden. \n" +
        "CPU-Auslastung: So viel wie möglich auslasten.", # Ziele für Batch-Systeme
    "Antwortzeit: Minimiere die Antwortzeit für eingehende Anfragen\n" +
        "Proportionalität: Berücksictige die Erwartungshaltung der Benutzer.", # Ziele für Interaktive Systeme
    "Deadline: Prozesse müssen innerhalb einer bestimmten Zeit fertig sein. \n" +
        "Vorhersagen: Vermeide Qualitätsverluste durch Überlastung.", # Ziele für Echtzeit Systeme
    "Fairnesse vs Priorität: \n" +
        " - Fairness: Jeder Prozess soll gleich viel CPU-Zeit erhalten. \n" +
        " - höher priorisierte Prozesse erhalten mehr CPU-Zeit. \n" +
        "I/O-Bound vs CPU-Bound: \n" +
        " - I/O-Bound: Prozesse, die viel I/O betreiben. \n" +
        " - CPU-Bound: Prozesse, die viel Rechenleistung benötigen. \n" +
        "Wartezeit vs Durchlaufzeit: \n" +
        " - Wartezeit: Zeit, die ein Prozess wartet, bis er an der Reihe ist. \n" +
        " - Durchlaufzeit: Zeit, die ein Prozess benötigt, um zu beenden. \n" +
        "CPU-Auslastung vs Durchsatz: \n" +
        " - CPU-Auslastung: Wie viel CPU-Zeit wird von den Prozessen verbraucht. \n" +
        " - Durchsatz: Wie viele Prozesse werden in einer bestimmten Zeit abgearbeitet. \n", # Kriteren zur Auswahl von Prozessen
    "Aufgaben werden auf Dispatcher und scheduler verteilt. \n" +
        "Dispatcher: \n" +
        "\t Realisiert Prozess-zustandswechsel von rechenwillig nach rechnend. \n" +
        "Scheduler: \n" +
        "\t Wählt den nächsten Prozess aus, der auf den Prozessor zugreifen darf. \n" +
        "\t Wahl des nächsten Prozesses wird duch Scheduling Algorithmen getroffen", # Prozessorverwaltung
    "1. Ändern des Zustnads des rechenden Prozesses auf rechenwillig oder wartend. \n" +
        "2. Sichern des Kontextes des zuvor rechnenden Prozesses. \n" +
        "3. Läd den Kontext des rechenbereiten Prozesses. \n" +
        "4. Ändern des Zustands des rechenbereiten Prozesses auf rechnend. ", # Ablauf Dispatching
    "- Wenn ein neuer Prozess erzeugt wird. \n" +
        "\t - Soll der Eltern- oder Kind-Prozess zuerst ausgeführt werden? \n" +
        "- Wenn ein Prozess terminiert. \n" +
        "\t - Soll der nächste Prozess aus der Ready-Queue oder aus der Waiting-Queue geladen werden? \n" +
        "- Wenn ein Prozess blockiert (aufgrund von IO, semaphoren, etc.) \n" +
        "- Wenn ein Interrupt auftritt. \n" +
        "\t Ein Interrupt ausgehend von einem IO-Gerät, kann einen blockierten Prozess wieder rechenbereit machen. \n" +
        "\t Eine scheduling-Entscheidung kann bei jedem Timer-Interrupt getroffen werden. \n", # Wann wird der Dispatcher aktiv?
    "Preemptive vs Non-Preemptive: \n" +
        "- Preemptive: \n" +
        "\t - Prozesse werden beim Auftreten von bestimmten Ereignissen unterbrochen. \n" +
        "- non-Preemptive: \n" +    
        "\t - Prozesse werden so lange ausgeführt, bis sie blockieren oder freiwillig beenden. \n" +
        "\t - ähnlich wie bei User-Level-Threads in einem Prozess. \n", # Scheduling Klassen
    "First-Come-first-Served: \n" +
        "\t - Prozesse werden in der Reihenfolge ihrer Ankunft behandelt. \n" +
        "Shortest-Job-First: \n" +
        "\t - Prozesse mit der kürzesten Ausführungszeit werden zuerst behandelt. \n" +
        "Shortest-Remaining-Time-First: \n" +
        "\t - Prozesse mit der kürzesten verbleibenden Ausführungszeit werden zuerst behandelt. \n", # Scheduling Strategien in Batch Systemen
    "Round-Robin: \n" +
        "\t - Prozesse werden in einer festen Reihenfolge behandelt. \n" +
        "\t - Jeder Prozess erhält eine bestimmte Zeit (Quantum) auf dem Prozessor. \n" +
        "\t - Nach Ablauf des Quantums wird der Prozess an den Ende der Ready-Queue gesetzt. \n" +
        "Priority Scheduling \n" +
        "\t - Prozesse werden nach ihrer Priorität behandelt. \n", # Scheduling Strategien in interaktiven Systemen
    "Earliest-Deadline-First: \n" +
        "\t - Prozesse mit der nächsten Deadline werden zuerst behandelt. \n" + 
        "Rate-Monotonic-Scheduling" + 
        "\t - Prozesse mit der höchsten Periode werden zuerst behandelt. \n", # Scheduling Strategien in Echtzeit Systemen
    "Short-term-Scheduler: \n" +
        "Preeptive vs Non-Preemptive \n" +
        "Auswahl von geeigneten Prozessen \n" +
        "Dispatcher ist Teil des Short-term-Schedulers \n" +
        "Medium-term-Scheduler: \n" +
        "Entscheidet, ob ein Porzess in denn Speicher geladen werden soll. \n" +
        "Teil des Swapping \n" +
        "Long-term-Scheduler: \n" +
        "Ziel: guten Prozessmix erzielen d.H. Mischung aus I/O intensivenn unnd rechenintensiveen Prozessen" +
        "Der LTS wird aufgerufen wenn ein neuer Prozess erzeugt wird. \n", # Multi-Level-Scheduling
    "Time Sharing: \n" +
        "- Abwechselnde Nutzung von Ressouce \n" +
        "- Langsamer Vorschritt für abhängige Prozesse \n" +
        "Space Sharing: \n" +
        "- Erlaubt abhängige Prozesse auf die gleichen Ressourcen zuzugreifen \n" +
        "- Abhängige Prozesse können gleichzeitig ausgeführt werden \n" +
        "- Vorteil: Keinen Kontextwechsel während deer Laufzeit \n" +
        "- Nachteil: mitunter hohe Wartezeiten" + 
        "Gang Scheduling: \n" +
        "- Kombination von Time- und Space Sharing \n" +
        "- Prozesse werden in Gruppen (Gangs) zusammengefasst \n" +
        "- Prozesse in einer Gang können gleichzeitig ausgeführt werden \n" +
        "- Gangs bekommmen Zeitscheiben zugewiesen \n" # Multi-Programmierung
    "Vorteile: \n" +
        "- Gute CPU-Auslastung \n" +
        "- Fair für Alle Prozesse \n" +
        "Nachteile: \n" +
        "- Schlechte Skalierbarkeit \n" +
        "- Schlechte Cache Lokalität \n", #Globale Warteschlangen
    "Vorteile: \n" +
        "- Gute Skalierbarkeit \n" +
        "- Gute Cache Lokalität \n" +
        "- Einfach zu implementieren \n" +
        "Nachteile: \n" +
        "- Schlechte CPU-Auslastung \n", # Lokale Warteschlangen
    "Vorteile: \n" +
        "- Gute Auslastung \n" +
        "- Prozessoraffinität erlaubt Wiederverwendung von Cache \n" +
        "Nachteile: \n" +
        "- Komplex \n", # Hybrid Warteschlangen
]


questions = questions_prozess_thread + questions_scheduling
answers = answers_prozess_thread + answers_scheduling