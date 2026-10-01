# Tabellone della persona facilitatrice de «i Giochi delle Banche»

Tabellone per chi facilita «i Giochi delle Banche», il gioco di educazione critica alla finanza di Fondazione Finanza Etica. È un unico file HTML: si apre con un doppio clic in qualsiasi browser e funziona senza internet.

Il tabellone è pensato per la **versione v2 del gioco**, la seconda edizione del 2024 di edizioni la meridiana, con 20 carte imprevisto. Con edizioni precedenti carte ed effetti potrebbero non corrispondere.

Tabellone versione 0.1, di Fabio Temporiti. Basato sul foglio di calcolo versione 4.0.

## Cosa fa

- **Gioco**: per ogni famiglia e turno si sceglie l'interesse ottenuto in banca; totali e punti qualità della vita si calcolano da soli.
- **Imprevisti**: si sceglie la carta pescata dal suo titolo e dalla sua frase, anche più carte nello stesso turno. Euro e punti vengono applicati a ogni famiglia in base alla banca scelta.
- **Promemoria dei turni**: sopra la tabella ricorda cosa prevede il turno, dalle domande alle banche agli spot fino alla strategia comune.
- **Classifica**: ordine delle famiglie, termometro e andamento della qualità della vita, carte uscite, dove sono andati i soldi banca per banca e domande per la discussione.
- **Salvataggio**: la partita si salva nel browser a ogni scelta, si può scaricare una copia di sicurezza e alla fine i risultati in un file .csv.
- **Proiezione**: si adatta a qualsiasi dimensione della finestra e ha il pulsante «Schermo intero».

## Come scaricarlo

Servono solo due file: il tabellone e, se vuoi stamparlo, il manuale.

1. In questa pagina, nell'elenco dei file in alto, clicca su `i-Giochi-delle-Banche-tabellone-persona-facilitatrice.html`.
2. Nella pagina del file premi il pulsante **Download raw file** (la freccia verso il basso, in alto a destra). Il file si salva nella cartella dei download.
3. Fai lo stesso con `manuale-tabellone-persona-facilitatrice.pdf`, se vuoi il manuale in PDF.

In alternativa: pulsante verde **Code**, poi **Download ZIP**. Scarichi tutto in un file .zip: aprilo e tieni i due file che ti servono.

Mettilo in una cartella dove resterà, per esempio i documenti del computer che userai in aula, prima della partita e non durante.

## Come si usa

1. **Apri il file con un doppio clic.** Si apre nel browser (Firefox, Chrome, Edge o Safari). Non serve internet e non serve installare nulla.
2. **Prepara la partita** in «Famiglie e partita»: di base giocano 5 famiglie e la qualità della vita parte da 100 punti. Puoi attivare altre famiglie e cambiare i nomi.
3. **Proietta** con il pulsante «Schermo intero» in alto, oppure con F11.
4. **A ogni turno**, quando una famiglia torna dalla banca, clicca la sua casella e scegli l'interesse scritto sulla scheda investimento. Sopra la tabella un promemoria ricorda cosa prevede il turno.
5. **Imprevisti**: nella riga «Imprevisto» clicca il riquadro del turno e scegli la carta pescata. Per più carte nello stesso turno clicca di nuovo e scegli «Aggiungi un'altra carta».
6. **Fine partita**: in «Classifica» trovi risultati, grafico, dove sono andati i soldi e le domande per la discussione. «Scarica i risultati e chiudi la partita» salva un file .csv e svuota il tabellone per la volta successiva.

**Se il browser si chiude per sbaglio** la partita non si perde: si salva da sola a ogni scelta. Riapri **lo stesso file con lo stesso browser** e la ritrovi. Non si ritrova se apri il file con un altro browser, se lo sposti o rinomini durante la partita, o se usi una finestra privata. Per sicurezza, a metà partita premi «Scarica copia di sicurezza» in «Famiglie e partita».

Tutto questo è spiegato anche nella sezione «Manuale» del tabellone e nel PDF.

## Chi l'ha fatto

Sono Fabio Temporiti, persona socia di Banca Etica, dove ho ricoperto vari ruoli. Sono attivo nei GIT dal 2012: sono stato persona Comunicatrice del GIT e persona Animatrice di Soci in Rete. Dal 27 Marzo 2013 sono persona Valutatrice Sociale e dal 2014 porto «i Giochi delle Banche» nelle scuole e non solo. Dal 2021 sono coordinatorə del GIT di Padova e dal 22 Novembre 2023 sono iscritto con il numero 18 all'Albo delle persone educatrici critiche alla finanza di Fondazione Finanza Etica. Ho fatto questo tabellone a partire da questa esperienza, per rendere più semplice il lavoro di chi facilita il gioco in aula.

Non è un materiale ufficiale di Fondazione Finanza Etica: i testi delle carte e i nomi delle banche appartengono al gioco originale.

## File

| File | A cosa serve |
|---|---|
| `i-Giochi-delle-Banche-tabellone-persona-facilitatrice.html` | Il tabellone da aprire in aula |
| `manuale-tabellone-persona-facilitatrice.pdf` | Il manuale di una pagina, da stampare |
| `sorgenti/modello.html` | Grafica e logica del tabellone |
| `sorgenti/dati.json` | Le 20 carte imprevisto e le 9 banche, dal file imprevisti.pdf |
| `sorgenti/costruisci.py` | Rigenera il tabellone dal modello e dai dati |

## Per chi vuole modificare il tabellone

Si modificano solo i file in `sorgenti/`, poi:

```
python3 sorgenti/costruisci.py
```

Il manuale è anche dentro il tabellone, nella sezione «Manuale». Per rigenerare il PDF: apri il tabellone, vai in «Manuale», premi «Stampa il manuale» e scegli «Salva come PDF».

## Licenza

Il repository contiene tre parti, con regole diverse:

| Parte | Licenza |
|---|---|
| Codice: il tabellone HTML e i file in `sorgenti/` | [EUPL 1.2](LICENSE) |
| Testi: il manuale (anche in PDF) e questo README | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.it) |
| Testi delle carte imprevisto e nomi delle banche, in `sorgenti/dati.json` | di Fondazione Finanza Etica ed edizioni la meridiana, esclusi dalle due licenze |

Il file `LICENSE` riporta il testo inglese della EUPL 1.2. Tutte le versioni linguistiche hanno lo stesso valore: il testo ufficiale in italiano è sul sito della Commissione europea, [Interoperable Europe](https://interoperable-europe.ec.europa.eu/collection/eupl/eupl-text-eupl-12).

Copyright 2026 Fabio Temporiti.
