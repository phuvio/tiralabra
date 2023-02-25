# Toteutusdokumentti

Markovin ketjun on toteutettu Trie-tietorakenteen avulla. Trie-tietorakenne on ohjelmoitu siten, että Prefix puun jokainen solmu on oma luokan TrieNode objekti. Objektiin on tallennettu kaksi dictionarya. Toiseen dictionaryyn tallentuu kyseiseen solmuun tallennetun nuotin jatkovaihtoehdot siten, että avain on jatkonuotin nimi ja arvo on kyseisen nuotin TrieNode. Toiseen tallennettuun dictionaryyn tallentuu kaikkien jatkovaihtoehtojen nimi sekä kuinka monta kertaa tämä tapaus esiintyi opetusmateriaalissa. TrieNodella on yksi fukntio *add_note*, joka lisää solmuun jatkovaihtoehdon, tai jos jatkovaihtoehto löytyy jo TrieNodesta niin lisää yhden esiintyvyysmäärään.

Varsinainen Trie luokka rakentuu TrieNodeista. Trie-luokan funktioita ovat:
- *add_list_to_trie*, joka lisää annetun nuottiluettelon trie-tietorakenteeseen. 
- *search_given_prefix*, joka etsii löytyykö haluttu nuottiluettelo trie-tietorakenteesta
- *return_choices*, joka palauttaa annetun prefixin nuottivaihtoehdot ja niiden esiintyvyysmäärän opetusmateriaalissa
- *size*, joka on apufunktio testaamiseen. Se laskee trie-tietorakenteen solmujen määrän

Musiikin generointi tapahtuu *generate_music*-funktiolla. Funktio on rekursiivinen. Jos haluttu prefix löytyy trie-tietorakenteesta, niin funktio generoi uuden nuotin uuteen kappaleeseen ja palauttaa päivitetyn generoidun musiikin ja päivitetyn prefixin. Mikäli prefixiä ei löydy triestä, niin funktio poistaa prefixistä ensimmäisen nuotin eli nuotin, joka on ollut prefixissä pisimpään. Sen jälkeen se kutsuu itseään uudelleen lyhyemmällä prefixillä. Tätä jatketaan kunnes uusi prefix löytyy triestä. Tällöin funktio generoi uuden nuotin uuteen kappaleeseen ja palauttaa sen jälkeen prefixin pituuden alkuperäiseksi.

Generoidun musiikin lopettaminen on toteutettu siten, että ensin generoidaan musiikkia yhtä pitkä pätkä kuin alkuperäinen kappalekin oli. Sen jälkeen lopetetaan musiikin generointi silloin, kun seuraava generoitu nuotti on sama kuin alkuperäisen kappaleen viimeinen nuotti. Tällöin generoitu musiikki noudattaa musiikin teorian sääntöjä.

## Music21-kirjasto

Ohjelma käyttää ulkoista *Music21: a toolkit for computer-aided musicology* -nimistä kirjastoa, jolla se kääntää midi-tiedostot stringeiksi ja toisinpäin. Kirjasto on *Massachusetts Institute of Technologyn* ylläpitämä. Kirjasto analysoi midi-tiedoston ja muuttaa yksittäiset nuotit tekstiksi. Kirjasto muuttaa myös tauot tekstiksi. Nuottien eteen tulee teksti *n_* ja taukojen *w_*. Nuottien kohdalla seuraavaksi merkitään nuotin numeroarvo esim. *n_48*. Lopuksi merkitään nuotin pituus esim. *n_48_quarter*. Taukojen kohdalla alkumerkin jälkeen merkitään vain tauon pituus esim. *w_1.0*. Trie-tietorakenteeseen tallennetaan sekä nuotit että tauot. Näin musiikin rytmi pysyy vastaavana kuin alkuperäisessä kappaleessa. Kirjasto tunnistaa yhdellä soittimella soitetut kappaleet. Ne voivat olla yksiäänisiä tai polyfonisia. Sen sijaan usealla soittimella tehtyjä midejä kirjasto ei osaa käsitellä.

# Käyttöliittymä

Käyttöliittymä on rakennettu Tkinterin avulla. Siinä käyttäjä voi ladata halutun midi-tiedoston, jota käytetään opetusmateriaalina ja joka syötetään trie-tietorakenteeseen. Käyttäjä valitsee prefixin pituuden, jota käytetään musiikin generoimiseen. Pitkällä 5 mittaisella prefixillä generoitu musiikki on lähellä alkuperäistä. Lyhyellä 1 mittaisella prefixillä generoitu musiikki eroaa suuresti alkuperäisestä. Alkuperäinen kappale vaikuttaa merkittävästi lopputulokseen. Kappaleeksi voi valita yksiäänisen kappaleen tai polyfonisen kappaleen. Yksinkertainen melodia tuottaa mielenkiintoisinta generoitua musiikkia 3-4 mittaisella prefixillä, jolloin musiikissa on selkeästi alkuperäisen musiikin aineksia, mutta myös jotain aivan muuta. Monimutkaisempien kappaleiden kohdalla prefixin pituus 4-5 on paras vaihtoehto. Yksinkertainen Oodi ilolle -kappaleen melodia soitettuna yksiäänisesti tuottaa varsin yllätyksettömiä variaatioita. Sen sijaan monimutkaisemmat kappaleet tuottavat mielenkiintoisempia variaatioita. Generoitu musiikki tallentuu nimellä generated.midi data-kansioon, joka sijaitsee asennetun ohjelman juuressa. Samaan kansioon on tallennettu kappaleita, joita voi käyttää musiikin generointiin.

# Työn puutteet ja parannusehdotukset

- Generoidun musiikin toistaminen puuttuu. Useista yrityksistä huolimatta en saanut musiikin toistoa toimimaan luotettavasti. Musiikin toistamista on kokeiltu *PyGame-*, *midi2audio-* ja *PrettyMidi-*kirjastojen avulla. Kokeilematta jäi *FluidSynth*-kirjasto, joka vaatii *SoundFont*-kirjaston asentamista. Tämä taas vaatisi pääkäyttäjän oikeudet. Vaikka *FluidSynth*:n kautta musiikin toistaminen onnistuisi, niin asennusten hankaluuden takia ei voi taata, että ohjelma sen jälkeen toimisi kaikissa tietokoneissa ongelmitta. Todennäköisesti toisto-ongelma liittyy midi-tiedostojen käsittelyyn. 
- Ohjelmaan voisi lisätä myös mahdollisuuden tallentaa useita kappaleita opetusmateriaaliksi. Tähän liittyy kuitenkin vaara, jos tallennetut kappaleet ovat eri sävelasteikossa. Algoritmi ei osaa ottaa tätä huomioon, jolloin generoitu musiikki voi olla täysin musiikin teorian vastaista.
- Generoidun musiikin lopettamiseen olisi mahdollista kehittää hienostuneempi malli. Nyt musiikki saattaa katketa yllättäen. Tätä varten tulisi laatia musiikin teoriaan pohjautuva oma algoritminsa lopetuksia varten.

# Lähteet

- [music21: a toolkit for computer-aided musicology](http://web.mit.edu/music21/)
- [Algorithmic Music Composition](https://junshern.github.io/algorithmic-music-tutorial/)
- [Markov Chain for music generation](https://towardsdatascience.com/markov-chain-for-music-generation-932ea8a88305)
