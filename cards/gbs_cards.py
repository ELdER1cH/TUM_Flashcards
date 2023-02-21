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


questions = questions_prozess_thread
answers = answers_prozess_thread