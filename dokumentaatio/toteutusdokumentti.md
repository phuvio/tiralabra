# Toteutusdokumentti

Markovin ketjun on toteutettu Trie-tietorakenteen avulla. Trie-tietorakenne on ohjelmoitu siten, että Prefix puun jokainen solmu on oma luokan TrieNode objekti. Objektiin on tallennettu kaksi dictionarya. Toiseen dictionaryyn tallentuu kyseiseen solmuun tallennetun nuotin jatkovaihtoehdot siten, että avain on jatkonuotin nimi ja arvo on kyseisen nuotin TrieNode. Toiseen tallennettuun dictionaryyn tallentuu kaikkien jatkovaihtoehtojen nimi sekä kuinka monta kertaa tämä tapaus esiintyi opetusmateriaalissa. TrieNodella on yksi fukntio *add_note*, joka lisää solmuun jatkovaihtoehdon, tai jos jatkovaihtoehto löytyy jo niin lisää yhden esiintyvyysmäärään.

Varsinainen Trie luokka rakentuu TrieNodeista. Trie-luokan funktioita ovat:
- *add_list_to_trie*, joka lisää annetun nuottiluettelon trie-tietorakenteeseen. 
- *search_given_prefix*, joka etsii löytyykö haluttu nuottiluettelo trie-tietorakenteesta
- *return_choices*, joka palauttaa annetun prefixin nuottivaihtoehdot ja niiden esiintyvyysmäärän opetusmateriaalissa
- *size*, joka on apufunktio testaamiseen. Se laskee trie-tietorakenteen solmujen määrän

Musiikin generointi tapahtuu *generate_music*-funktiolla. Funktio on rekursiivinen. Jos haluttu prefix löytyy trie-tietorakenteesta, niin funktio generoi uuden nuotin uuteen kappaleeseen ja palauttaa päivitetyn generoidun musiikin ja päivitetyn prefixin. Mikäli prefixiä ei löydy triestä, niin funktio poistaa prefixistä ensimmäisen nuotin eli nuotin, joka on ollut prefixissä pisimpään. Sen jälkeen se kutsuu itseään uudelleen lyhyemmällä prefixillä. Tätä jatketaan kunnes uusi prefix löytyy triestä. Tällöin funktio generoi uuden nuotin uuteen kappaleeseen ja palauttaa sen jälkeen prefixin pituuden alkuperäiseksi.

## Music21-kirjasto

Ohjelma käyttää ulkoista *Music21: a toolkit for computer-aided musicology* -nimistä kirjastoa, jolla se kääntää midi-tiedostot stringeiksi ja toisinpäin. Kirjasto on *Massachusetts Institute of Technologyn* ylläpitämä. Kirjasto analysoi midi-tiedoston ja muuttaa yksittäiset nuotit tekstiksi. Kirjasto muuttaa myös tauot tekstiksi. Nuottien eteen tulee teksti *n_* ja taukojen *w_*. Nuottien kohdalla seuraavaksi merkitään nuotin numeroarvo esim. *n_48". Lopuksi merkitään nuotin pituus esim. *n_48_quarter*. Taukojen kohdalla alkumerkin jälkeen merkitään vain tauon pituus esim. *w_1.0*. Trie-tietorakenteeseen tallennetaan sekä nuotit että tauot. Näin musiikin rytmi pysyy vastaavana kuin alkuperäisessä kappaleessa. Kirjasto tunnistaa pianolla soitetut kappaleet. Ne voivat olla yksiäänisiä tai moniäänisiä. Sen sijaan usealla soittimella tehtyjä midejä kirjasto ei osaa käsitellä.

# Käyttöliittymä

Käyttöliittymä on rakennettu Tkinterin avulla. Siinä käyttäjä voi ladata halutun midi-tiedoston, jota käytetään opetusmateriaalina ja joka syötetään trie-tietorakenteeseen. Käyttäjä antaa prefixin pituuden, jota käytetään musiikin generoimiseen. Pitkällä 5 mittaisella prefixillä generoitu musiikki on hyvin lähellä alkuperäistä. Lyhyellä 1 mittaisella prefixillä generoitu musiikki eroaa suuresti alkuperäisestä. Alkuperäinen kappale vaikuttaa suuresti lopputulokseen. Yksinkertainen melodia tuottaa mielenkiintoisinta generoitua musiikkia 3-4 mittaisella prefixillä, jolloin musiikissa on selkeästi alkuperäisen musiikin aineksia, mutta myös jotain aivan muuta. Monimutkaisempien kappaleiden kohdalla prefixin pituus 4-5 on paras vaihtoehto. Yksinkertainen Oodi ilolle -kappaleen melodia soitettuna yksiäänisesti tuottaa varsin yllätyksettömiä variaatioita. Sen sijaan monimutkaisemmat kappalleet tuottavat mielenkiintoisempia variaatioita.

# Suorituskykyanalyysi

# Työn puutteet ja parannusehdotukset

- generoidun musiikin toistamista ei nyt voi keskeyttää, vaan kappale pitää kuunnella loppuun asti
- kun yrittää toistaa kappaleen uudelleen tai toisen kappaleen, niin ohjelma kaatuu
