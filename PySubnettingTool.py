import ipaddress
import sys

print(r"""
██████╗ ██╗   ██╗███████╗██╗   ██╗██████╗ ███╗   ██╗███████╗████████╗████████╗██╗███╗   ██╗ ██████╗ 
██╔══██╗╚██╗ ██╔╝██╔════╝██║   ██║██╔══██╗████╗  ██║██╔════╝╚══██╔══╝╚══██╔══╝██║████╗  ██║██╔════╝ 
██████╔╝ ╚████╔╝ ███████╗██║   ██║██████╔╝██╔██╗ ██║█████╗     ██║      ██║   ██║██╔██╗ ██║██║  ███╗
██╔═══╝   ╚██╔╝  ╚════██║██║   ██║██╔══██╗██║╚██╗██║██╔══╝     ██║      ██║   ██║██║╚██╗██║██║   ██║
██║        ██║   ███████║╚██████╔╝██████╔╝██║ ╚████║███████╗    ██║      ██║   ██║██║ ╚████║╚██████╔╝
╚═╝        ╚═╝   ╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝    ╚═╝      ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝ 
""")

print("\n---------- AVVIO TUTTI I SISTEMI E MOSTRO L'OBBIETTIVO DEL TOOL... ----------")
print(r"""ℹ️ INFO: Utente benvenuto nel nostro programma quì calcoleremo: 
    • la classe di appartenenza, 
    • la subnet mask, 
    • l'indirizzo di rete, 
    • l'indirizzo di broadcast,
    • l'intervallo di host utilizzabili,
    • l'indirizzo gateway.
(su un'indirizzo ipv4 che inserirai iniizialmente).""")
print("-----------------------------------------------------------------------------")

while True:
    print("\n---------- CARICAMENTO MENU PRINCIPALE... ----------")
    print(r"""1. ap  /  ▶️ Avvia/Riavvia tutti i calcoli
2. ch  /  📟 Calcolo degli host (SENZA IPV4 INIZIALE)
3. e   /  ❌ Esci dal programma""")
    print("----------------------------------------------------")
    
    sceltaMenu = input("> Bene utente ora inserisci un'opzione elencata quì sopra: ").lower()

    if sceltaMenu == "ap":
        print("\n---------- AVVIANDO IL SISTEMA (AP) E ATTENDENDO INPUT... ----------")
        ipv4 = input("> Ora utente ti chiediamo subito di inserire un'indirizzo IPV4 (VALIDO) per calcolare il resto: ")
        try:
            oggettoIp = ipaddress.ip_address(ipv4) # Controllo dell'input ipv4
        except ValueError:
            print("❌ ERROR: Ehy utente abbiamo notato che hai inserito un'indirizzo IPV4 non valido (es. di indirizzo: 192.168.1.10) riprova...")
            continue

        primoOttetto = int(oggettoIp.exploded.split('.')[0])
        classe = ""
        if 1 <= primoOttetto <= 126:
            classe = "A"
        elif primoOttetto == 127:
            classe = "Loopback (Riservato)"
        elif 128 <= primoOttetto <= 191:
            classe = "B"
        elif 192 <= primoOttetto <= 223:
            classe = "C"
        else:
            classe = "D (Multicast) o E (Sperimentale)"

        valoreInteroIp = int(oggettoIp)
        numeroInBinario = bin(valoreInteroIp)[2:].zfill(32)
        numeroIpInBinarioPuntato = f"{numeroInBinario[0:8]}.{numeroInBinario[8:16]}.{numeroInBinario[16:24]}.{numeroInBinario[24:32]}"

        print("\n---------- STAMPA DEI RISULTATI INIZIALI... ----------")
        print(f"ℹ️ INFO: IPV4 Inserito inizialmente = {ipv4}")
        print(f"ℹ️ INFO: CLASSE Calcolata in base all'indirizzo = {classe}")
        print(f"ℹ️ INFO: IPV4 Inserito inizialmente trasformato in BINARIO = {numeroIpInBinarioPuntato}")
        print("------------------------------------------------------")

        netmaskEsistente = input("> Utente ora ti domandiamo se hai già una netmask esistente, se si digita (s) altrimenti (n): ").lower()

        if netmaskEsistente == "n":
            while True:
                print("\n---------- CARICANDO IL SISTEMA DI RILEVAMENTO NETMASK... ----------")
                try:
                    sceltaMetodoNetmask = int(input("> Bene utente ora se vuoi calcolare la Netmask inserendo i bit di rete CIDR (digita 1) o in base al numero di host che ti servono (digita 2): "))
                except ValueError:
                    print("❌ ERROR: Ehila utente, devi inserire un numero valido (1 o 2)! Riprova...")
                    continue

                if sceltaMetodoNetmask == 1:
                    print("\n---------- ATTENDO INPUT E CALIBRO IL SISTEMA DI CALCOLO (/CIDR)... ----------")
                    inserimentoCidr = int(input("> Perfetto utente ora ti chiediamo di inserire il CIDR della netmask (senza / solo NUMERO): "))
                    numeroDiHost = 32 - inserimentoCidr
                
                    bitRete = "1" * inserimentoCidr
                    bitHost = "0" * numeroDiHost
                    netmaskBinaria = bitRete + bitHost
                    netmaskPulitaInBinarioPuntata = f"{netmaskBinaria[0:8]}.{netmaskBinaria[8:16]}.{netmaskBinaria[16:24]}.{netmaskBinaria[24:32]}"
                    valoreInteroMask = int(netmaskBinaria, 2)
                    indirizzoDiRete = valoreInteroIp & valoreInteroMask
                    oggettoReteCalcolata = ipaddress.ip_address(indirizzoDiRete)
                    valoreInteroWildcard = valoreInteroMask ^ 4294967295
                    indirizzoDiBroadcast = indirizzoDiRete | valoreInteroWildcard
                    oggettoBroadcastCalcolato = ipaddress.ip_address(indirizzoDiBroadcast)

                    hostDisponibiliCidr = (2 ** numeroDiHost) - 2 if numeroDiHost > 1 else 0

                    primoHostUtile = ipaddress.ip_address(int(oggettoReteCalcolata) + 1) if hostDisponibiliCidr > 0 else oggettoReteCalcolata
                    ultimoHostUtile = ipaddress.ip_address(int(oggettoBroadcastCalcolato) - 1) if hostDisponibiliCidr > 0 else oggettoBroadcastCalcolato
                    indirizzoGateway = primoHostUtile

                    print("\n---------- STAMPA DEI RISULTATI SCELTA /CIDR... ----------")
                    print(f"ℹ️ INFO: CIDR inserito inizialmente = /{inserimentoCidr}")
                    print(f"ℹ️ INFO: NETMASK binaria ricavata = {netmaskPulitaInBinarioPuntata}")
                    print(f"ℹ️ INFO: Indirizzo di RETE ricavato = {oggettoReteCalcolata}")
                    print(f"ℹ️ INFO: Indirizzo di BROADCAST ricavato = {oggettoBroadcastCalcolato}")
                    if hostDisponibiliCidr > 0:
                        print(f"ℹ️ INFO: INTERVALLO DEGLI HOST UTILIZZABILI = {primoHostUtile} - {ultimoHostUtile}")
                        print(f"ℹ️ INFO: INDIRIZZO IP GATEWAY CALCOLATO CONSIGLIATO PER (Router) = {indirizzoGateway} 🌐")
                    else:
                        print(f"ℹ️ INFO: INTERVALLO DEGLI HOST UTILIZZABILI = Nessuno (Rete punto-punto o Host singolo)")
                        print(f"ℹ️ INFO: INDIRIZZO IP GATEWAY CALCOLATO CONSIGLIATO PER (Router) = Non applicabile 🌐")
                    print("------------------------------------------------------")
                    break
                elif sceltaMetodoNetmask == 2:
                    print("\n---------- ATTENDO INPUT E CALIBRO IL SISTEMA DI CALCOLO PER GLI HOST MASSIMI... ----------")
                    hostRischiesti = int(input("> Ok ci siamo, utente ora inserisci il numero di host massimi che ti servono in questa rete: "))

                    bitHost = 1
                    while ((2 ** bitHost) - 2) < hostRischiesti:
                        bitHost += 1

                    calcoloCidr = 32 - bitHost
                    bitPerRete = "1" * calcoloCidr
                    bitPerHost = "0" * bitHost
                    netmaskInBinario = bitPerRete + bitPerHost
                    netmaskInBinarioPuntata = f"{netmaskInBinario[0:8]}.{netmaskInBinario[8:16]}.{netmaskInBinario[16:24]}.{netmaskInBinario[24:32]}"
                    valoreInteroNetmask = int(netmaskInBinario, 2)
                    indirizzoRete = valoreInteroIp & valoreInteroNetmask
                    oggettoDiReteCalcolata = ipaddress.ip_address(indirizzoRete)
                    valoreInteroComplementoA1 = valoreInteroNetmask ^ 4294967295
                    indirizzoBroadcast = indirizzoRete | valoreInteroComplementoA1
                    oggettoDiBroadcastCalcolato = ipaddress.ip_address(indirizzoBroadcast)
                    hostDisponibili = (2 ** bitHost) - 2
                    hostInutilizzati = hostDisponibili - hostRischiesti

                    primoHostUtile = ipaddress.ip_address(int(oggettoDiReteCalcolata) + 1) if hostDisponibili > 0 else oggettoDiReteCalcolata
                    ultimoHostUtile = ipaddress.ip_address(int(oggettoDiBroadcastCalcolato) - 1) if hostDisponibili > 0 else oggettoDiBroadcastCalcolato
                    indirizzoGateway = primoHostUtile

                    print("\n---------- STAMPA DEI RISULTATI HOST... ----------")
                    print(f"ℹ️ INFO: Host richiesti inizialmente = {hostRischiesti}")
                    print(f"ℹ️ INFO: CIDR calcolcato automaticamente = /{calcoloCidr}")
                    print(f"ℹ️ INFO: NETMASK binaria ricavata = {netmaskInBinarioPuntata}")
                    print(f"ℹ️ INFO: Host MASSIMI realmente disponibili = {hostDisponibili}")
                    print(f"ℹ️ INFO: Host inutilizzati trovati = {hostInutilizzati} ⚠️")
                    print(f"ℹ️ INFO: Indirizzo di RETE ricavato = {oggettoDiReteCalcolata}")
                    print(f"ℹ️ INFO: Indirizzo di BROADCAST ricavato = {oggettoDiBroadcastCalcolato}")
                    if hostDisponibili > 0:
                        print(f"ℹ️ INFO: INTERVALLO DEGLI HOST UTILIZZABILI = {primoHostUtile} - {ultimoHostUtile}")
                        print(f"ℹ️ INFO: INDIRIZZO IP GATEWAY CALCOLATO CONSIGLIATO PER (Router) = {indirizzoGateway} 🌐")
                    else:
                        print(f"ℹ️ INFO: INTERVALLO DEGLI HOST UTILIZZABILI = Nessuno (Rete punto-punto o Host singolo)")
                        print(f"ℹ️ INFO: INDIRIZZO IP GATEWAY CALCOLATO CONSIGLIATO PER (Router) = Non applicabile 🌐")
                    print("-----------------------------------------------------")
                    break
        elif netmaskEsistente == "s":
            print("\n---------- CARICANDO IL SISTEMA DI CALCOLO IN BASE ALLA NETMASK CHE VERRÀ DIGITATA... ----------")
            inserimentoNetmask = input("> Ok utente inserisci ora la subnet mask completa per completare i calcoli (es. 255.255.255.0): ")
            try:
                oggettoNetmask = ipaddress.ip_address(inserimentoNetmask) # Controllo dell'input netmask
            except ValueError:
                print("❌ ERROR: Ohh utente abbiamo notato che hai inserito una netmask non valia (es. di netmask: 255.255.255.0) riprova...")
                continue

            valoreInteroDiNetmask = int(oggettoNetmask)
            netmaskInBinario = bin(valoreInteroDiNetmask)[2:].zfill(32)
            calcoloDelCidr = netmaskInBinario.count("1")
            netmaskInBinariaPuntata = f"{netmaskInBinario[0:8]}.{netmaskInBinario[8:16]}.{netmaskInBinario[16:24]}.{netmaskInBinario[24:32]}"

            if "01" in netmaskInBinario:
                print("❌ ERROR: Ehilà utente questa maschera non è valida! Gli 1 di rete devono essere tutti contigui a sinistra.")
                continue
            else:
                indirizzoDiRete = valoreInteroIp & valoreInteroDiNetmask
                oggettoReteCalcolata = ipaddress.ip_address(indirizzoDiRete)
                valoreInteroWildcard = valoreInteroDiNetmask ^ 4294967295
                indirizzoDiBroadcast = indirizzoDiRete | valoreInteroWildcard
                oggettoBroadcastCalcolato = ipaddress.ip_address(indirizzoDiBroadcast)
                bitHost = 32 - calcoloDelCidr
                hostDisponibili = (2 ** bitHost) - 2 if bitHost > 1 else 0 # Nota: il controllo 'if bitHost > 1' serve per evitare numeri negativi con le /31 o /32
                
                primoHostUtile = ipaddress.ip_address(int(oggettoReteCalcolata) + 1) if hostDisponibili > 0 else oggettoReteCalcolata
                ultimoHostUtile = ipaddress.ip_address(int(oggettoBroadcastCalcolato) - 1) if hostDisponibili > 0 else oggettoBroadcastCalcolato
                indirizzoGateway = primoHostUtile

                print("\n---------- STAMPA DEI RISULTATI SUBNET MASK MANUALE... ----------")
                print(f"ℹ️ INFO: Maschera inserita inizialmente = {inserimentoNetmask} ( /{calcoloDelCidr} )")
                print(f"ℹ️ INFO: NETMASK calcolata in binario = {netmaskInBinariaPuntata}")
                print(f"ℹ️ INFO: Indirizzo di RETE ricavato automaticamente = {oggettoReteCalcolata}")
                print(f"ℹ️ INFO: Indirizzo di BROADCAST ricavato automaticamente = {oggettoBroadcastCalcolato}")
                print(f"ℹ️ INFO: Host realmente disponibili in questa rete = {hostDisponibili}")
                if hostDisponibili > 0:
                    print(f"ℹ️ INFO: INTERVALLO DEGLI HOST UTILIZZABILI = {primoHostUtile} - {ultimoHostUtile}")
                    print(f"ℹ️ INFO: INDIRIZZO IP GATEWAY CALCOLATO CONSIGLIATO PER (Router) = {indirizzoGateway} 🌐")
                else:
                    print(f"ℹ️ INFO: INTERVALLO DEGLI HOST UTILIZZABILI = Nessuno (Rete punto-punto o Host singolo)")
                    print(f"ℹ️ INFO: INDIRIZZO IP GATEWAY CALCOLATO CONSIGLIATO PER (Router) = Non applicabile 🌐")
                print("--------------------------------------------------------------------")
    elif sceltaMenu == "ch":
        print("\n---------- AVVIANDO IL SISTEMA (CH) E ATTENDENDO INPUT... ----------")
        try:
            hostMassimiRischiesti = int(input("> Ricevuto utente, ora ti chiediamo di inserire il numero di host massimi che ti servono per questa rete: "))
        except ValueError:
            print("❌ ERROR: Wow utente hai inserito/digitato un testo sconosciuto, riprova...")
            continue

        bitHostMassimi = 1
        while ((2 ** bitHostMassimi) - 2) < hostMassimiRischiesti:
            bitHostMassimi += 1

        calcoloSulCidr = 32 - bitHostMassimi
        bitPerLaRete = "1" * calcoloSulCidr
        bitPerGliHost = "0" * bitHostMassimi
        netmaskInBinaria = bitPerLaRete + bitPerGliHost
        netmaskBinariaPuntata = f"{netmaskInBinaria[0:8]}.{netmaskInBinaria[8:16]}.{netmaskInBinaria[16:24]}.{netmaskInBinaria[24:32]}"
        valoreInteroDellaNetmask = int(netmaskInBinaria, 2)
        oggettoDellaNetmaskCalcolata = ipaddress.ip_address(valoreInteroDellaNetmask)
        hostDisponibiliMassimi = (2 ** bitHostMassimi) - 2
        hostInutilizzatiMassimi = hostDisponibiliMassimi - hostMassimiRischiesti

        print("\n---------- STAMPA DEI RISULTATI PER CALCOLO HOST (CH)... ----------")
        print(f"ℹ️ INFO: Host richiesti inizialmente = {hostMassimiRischiesti}")
        print(f"ℹ️ INFO: CIDR calcolcato automaticamente = /{calcoloSulCidr}")
        print(f"ℹ️ INFO: NETMASK binaria ricavata = {netmaskBinariaPuntata}")
        print(f"ℹ️ INFO: NETMASK decimale trasformata = {oggettoDellaNetmaskCalcolata}")
        print(f"ℹ️ INFO: Host MASSIMI realmente disponibili = {hostDisponibiliMassimi}")
        print(f"ℹ️ INFO: Host inutilizzati trovati = {hostInutilizzatiMassimi} ⚠️")
        print("----------------------------------------------------------------------")
        continue

    elif sceltaMenu == "e":
        print("\n---------- CARICANDO IL SISTEMA DI USCITA... ----------")
        print(f"⚙️ SISTEMA: Spegnimento in corso... Alla prossima.")
        sys.exit()
    else:
        print(f"❌ ERROR: Attento utente ! hai appena inserito un comando non valido. Riprova...")