# Testausdokumentti

## Yksikkötestaus

Yksikkötestaus on toteutettu Pythonin Unittest-kirjaston avulla. Ohjelman eri osa-alueille on omat testitiedostonsa, jotka testaavat kyseisen osan toimivuutta. Testit on helppo toistaa ajamalla halutut testit uudelleen. 

Testitiedostot:
- [Trie-tietorakenteeseen liittyvät yksikkötestit](../src/tests/trie_test.py)
- [midin käsittelyyn liittyvät yksikkötestit](../src/tests/midi_test.py)
- [Markovin ketjuun liittyvät yksikkötestit](../src/tests/markovchain_test.py)

### Trie-tietorakenteen yksikkötestaus

Trie-tietorakenne on testattu laajasti.

Testatut funktiot:
- luokka Trie
  - add_list_to_trie
  - search_given_prefix
  - return_choices
- luokka TrieNode
  - add_note

Luokan Trie funktio *size* on apufunktio testaukseen.

### Midin käsittelyyn liittyvien funktioiden yksikkötestaus

Ohjelmassa käytetään *Music21: a toolkit for computer-aided musicology* -nimistä kirjastoa. Kirjasto on *Massachusetts Institute of Technologyn* ylläpitämä. Kirjastoa käytetään funktioissa *midi_to_string* ja *string_to_midi*, joiden avulla midi-tiedosto muutetaan stringiksi ja toisinpäin. String-muotoon muutettuna jokainen nuotti on kuvattu stringinä, joka sisältää tiedon onko kyseessä tauko vai nuotti, nuotin arvo eli sen korkeus ja nuotin/tauon pituus. Yksikkötestien näkökulmasta haasteen tuo se, että ajamalla midi-tiedoston stringiksi ja taas takaisin midiksi aiheuttaa pieniä eroavaisuuksia alkuperäisen ja loppullisen tiedoston välillä. Eroavaisuudet liittyvät nuottien/taukojen pituuksiin. Niitä ei korvakuulolta erota, mutta tiedostojen tarkka vertailu muuttuu mahdottomaksi. Siksi yksikkötestauksessa midi-tiedosto muutetaan ensin stringiksi, sitten takaisin midiksi ja vielä kerran stringiksi. Lopuksi verrataan saatujen stringien nuottien arvoa ja jätetään nuottien pituudet huomiotta. Näin yksikkötestaus menee läpi.

Testatut funktiot:
- midi_to_string
- string_to_midi