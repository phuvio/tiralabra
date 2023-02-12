# Toteutusdokumentti

Markovin ketjun on toteutettu Trie-tietorakenteen avulla. Trie-tietorakenne on ohjelmoitu siten, että Prefix puun jokainen solmu on oma luokan TrieNode objekti. Objektiin on tallennettu kaksi dictionarya. Toiseen dictionaryyn tallentuu kyseiseen solmuun tallennetun nuotin jatkovaihtoehdot siten, että avain on jatkonuotin nimi ja arvo on kyseisen nuotin TrieNode. Toiseen tallennettuun dictionaryyn tallentuu kaikkien jatkovaihtoehtojen nimi sekä kuinka monta kertaa tämä tapaus esiintyi opetusmateriaalissa. TrieNodella on yksi fukntio *add_note*, joka lisää solmuun jatkovaihtoehdon, tai jos jatkovaihtoehto löytyy jo niin lisää yhden esiintyvyysmäärään.

Varsinainen Trie luokka rakentuu TrieNodeista. Trie-luokan funktioita ovat:
- *add_list_to_trie*, joka lisää annetun nuottiluettelon trie-tietorakenteeseen. 
- *search_given_prefix*, joka etsii löytyykö haluttu nuottiluettelo trie-tietorakenteesta
- *return_choices*, joka palauttaa annetun prefixin nuottivaihtoehdot ja niiden esiintyvyysmäärän opetusmateriaalissa
- *size*, joka on apufunktio testaamiseen. Se laskee trie-tietorakenteen solmujen määrän

# Käyttöliittymä

Käyttöliittymä on rakennettu Tkinterin avulla. Siinä käyttäjä voi ladata halutun midi-tiedoston, jota käytetään opetusmateriaalina ja joka syötetään trie-tietorakenteeseen. Käyttäjä antaa prefixin pituuden, jota käytetään musiikin generoimiseen. Pitkällä 5 mittaisella prefixillä generoitu musiikki on hyvin lähellä alkuperäistä. Lyhyellä 1 mittaisella prefixillä generoitu musiikki eroaa suuresti alkuperäisestä. Mielenkiintoisin generoitu musiikki tuntuu tulevan 3 mittaisella prefixillä, jolloin musiikissa on selkeästi alkuperäisen musiikin aineksia, mutta myös jotain aivan muuta.

# Suorituskykyanalyysi

# Työn puutteet ja parannusehdotukset