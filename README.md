# PySubnettingTool

██████╗ ██╗   ██╗███████╗██╗   ██╗██████╗ ███╗   ██╗███████╗████████╗████████╗██╗███╗   ██╗ ██████╗ 
██╔══██╗╚██╗ ██╔╝██╔════╝██║   ██║██╔══██╗████╗  ██║██╔════╝╚══██╔══╝╚══██╔══╝██║████╗  ██║██╔════╝ 
██████╔╝ ╚████╔╝ ███████╗██║   ██║██████╔╝██╔██╗ ██║█████╗     ██║      ██║   ██║██╔██╗ ██║██║  ███╗
██╔═══╝   ╚██╔╝  ╚════██║██║   ██║██╔══██╗██║╚██╗██║██╔══╝     ██║      ██║   ██║██║╚██╗██║██║   ██║
██║        ██║   ███████║╚██████╔╝██████╔╝██║ ╚████║███████╗    ██║      ██║   ██║██║ ╚████║╚██████╔╝
╚═╝        ╚═╝   ╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝    ╚═╝      ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝ 

🎯 **PySubnettingTool** è un piccolo strumento da riga di comando scritto in Python che aiuta a calcolare informazioni fondamentali su una rete IPv4.

## 🔍 Cosa fa

Questo script permette di:

- identificare la *classe* dell'indirizzo IPv4 inserito
- convertire l'indirizzo IPv4 in binario
- calcolare la *subnet mask* in base a:
  - CIDR
  - numero di host richiesti
  - subnet mask già esistente
- calcolare l'*indirizzo di rete*
- calcolare l'*indirizzo di broadcast*
- individuare l'*intervallo di host utilizzabili*
- suggerire l'*indirizzo gateway* consigliato

## 🚀 Come si usa

1. Apri il terminale nella cartella del progetto.
2. Esegui il file `PySubnettingTool.py` con Python:

```bash
python PySubnettingTool.py
```

3. Nel menu principale puoi scegliere:

- `ap` : avvia/reavvia tutti i calcoli in base a un indirizzo IPv4 inserito
- `ch` : calcola la maschera e il CIDR a partire dal numero di host richiesti, senza bisogno di un indirizzo IPv4 iniziale
- `e` : esci dal programma

4. Se scegli `ap`, ti verrà chiesto di inserire un IPv4 valido.
5. Dopo l'indirizzo, potrai decidere se usare una subnet mask esistente (`s`) oppure calcolare la netmask partendo da CIDR o dal numero di host (`n`).

## 🧠 Dettagli tecnici

Lo script utilizza il modulo Python standard `ipaddress` per validare gli indirizzi e calcolare i risultati in modo accurato.

### Calcoli supportati

- **Classe IPv4**: A, B, C, Loopback o D/E
- **Conversione binaria** dell'indirizzo IP
- **Calcolo rete** con operazioni bitwise
- **Calcolo broadcast** con wildcard mask
- **Intervallo host**: primo e ultimo host disponibili
- **Gateway consigliato**: primo host utile
- **Validazione subnet mask**: verifica se la maschera è corretta (1 contigui a sinistra)

## 💡 Esempio d'uso

- Inserisci `ap`
- Digita `192.168.1.10`
- Scegli `n` per calcolare la rete da zero
- Scegli `1` per usare il CIDR (ad esempio `24`)

Il programma mostrerà:

- IP in binario
- classe IP
- netmask calcolata
- rete
- broadcast
- primo e ultimo host utilizzabile
- gateway consigliato

## 🛠️ Possibili modifiche future

Questa versione è già utile, ma può essere migliorata per diventare uno strumento ancora più completo per gli utenti:

- aggiungere il supporto a **IP classless** con tutte le funzioni avanzate
- includere la stampa di **CIDR e mask in formato decimale e binario** insieme
- supportare il calcolo di **sottoreti multiple** a partire da una rete madre
- aggiungere un’interfaccia a menu più moderna con **colori** e output formattato
- salvare i risultati su file `.txt` o `.csv`
- implementare una modalità **batch** per analizzare più indirizzi insieme
- creare un set di funzioni riutilizzabili in un modulo separato per integrarlo in altri progetti
- aggiungere il supporto a **IPv6** per future evoluzioni

## ✅ Perché usarlo

- è facile da usare anche per chi non è esperto
- fornisce risultati completi e leggibili
- è utile per chi studia subnetting o fa piccoli calcoli di rete
- il menu è strutturato e guidato

## 📌 Nota importante

Questo strumento è pensato per reti IPv4. Non gestisce indirizzi IPv6.

## ✨ Suggerimenti per contributori GitHub

- migliorare i messaggi di errore e i suggerimenti per l'utente
- aggiungere controlli più robusti per input errati
- introdurre funzionalità avanzate come il calcolo di **VLSM** e **supernetting**
- creare una versione con output in **HTML** o **formattato con tabella**

Buon lavoro con `PySubnettingTool`! 🖥️🌐
