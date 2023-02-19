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
- generate_music-funktio

Luokan Trie funktio *size* on apufunktio testaukseen.

Suoritetut testit:
- test_add_notes_to_trie
  - tarkistaa trien koon, kun siihen on tallennettu 7 nuottia
- test_add_ode_to_joy_to_trie
  - tarkistaa trien koon, kun siihen on tallennettu Oodi ilolle -kappale
- test_add_same_list_to_trie
  - saman nuottiketjun lisääminen ei muuta trien kokoa
- test_add_ode_to_joy_twice_to_trie
  - Oodi ilolle -kappaleen tallentaminen kahteen kertaan triehen ei muuta sen kokoa 
- test_add_two_lists_with_first_same_note
  - kahden erilaisen, mutta samalla nuotilla alkavan, nuottiketjun lisääminen lisää trien kokoa eroavien nuottien määrän verran 
- test_add_two_lists_with_different_notes
  - kahden täysin erilaisen nuottiketjun lisääminen triehen kasvattaa koon nuottiketjujen nuottien määrän verran
- test_find_given_prefix
  - haluttu prefix, joka on tallennettu triehen, löytyy
- test_given_prefix_not_found
  - haluttu prefix, jota ei ole tallennettu triehen, ei löydy
- test_possible_choices_from_given_prefix
  - triestä löytyvä prefix palauttaa luettelon mahdollisista jatkonuoteista
  - testissä verrataan, että löydetyt vaihtoehdot ovat oikein
- test_possible_choices_from_given_prefix_with_more_probabilities
  - triestä löytyvä prefix palauttaa luettelon mahdollisista jatkonuoteista ja niiden esiintyvyydet opetusmateriaalissa
  - testissä verrataan, että löydetyt vaihtoehdot ja niiden todennäköisyydet ovat oikein
- test_no_found_choices_from_given_prefix
  - jos prefixiä ei löydy triestä, niin trie ei palauta jatkovaihtoehtoja
- test_prefix_not_found
  - trie ei palauta jatkovaihtoehtoja, jos prefixiä ei löydy triestä 
- test_find_given_prefixes_from_ode_to_joy
  - tarkistaa koko trien sen jälkeen, kun siihen on tallennettu Oodi ilolle -kappale
- test_generate_music_from_known_prefix
  - testataan generoiko funktio oikean nuotin, kun prefix löytyy triestä ja sillä on vain yksi vaihtoehto
- test_generate_music_from_unknown_prefix
  - testataan generoiko funktio oikean nuotin, kun ainoastaan prefixin viimeinen nuotti löytyy triestä
  - tämä testi ajetaan varmuuden vuoksi kahteen kertaan samalla trie-tietorakenteella

### Midin käsittelyyn liittyvien funktioiden yksikkötestaus

Ohjelmassa käytetään *Music21: a toolkit for computer-aided musicology* -nimistä kirjastoa. Kirjasto on *Massachusetts Institute of Technologyn* ylläpitämä. Kirjastoa käytetään funktioissa *midi_to_string* ja *string_to_midi*, joiden avulla midi-tiedosto muutetaan stringiksi ja toisinpäin. String-muotoon muutettuna jokainen nuotti on kuvattu stringinä, joka sisältää tiedon onko kyseessä tauko vai nuotti, nuotin arvo eli sen korkeus ja nuotin/tauon pituus. Yksikkötestien näkökulmasta haasteen tuo se, että ajamalla midi-tiedoston stringiksi ja taas takaisin midiksi aiheuttaa pieniä eroavaisuuksia alkuperäisen ja loppullisen tiedoston välillä. Eroavaisuudet liittyvät nuottien/taukojen pituuksiin. Niitä ei korvakuulolta erota, mutta tiedostojen tarkka vertailu muuttuu mahdottomaksi. Siksi yksikkötestauksessa midi-tiedosto muutetaan ensin stringiksi, sitten takaisin midiksi ja vielä kerran stringiksi. Lopuksi verrataan saatujen stringien nuottien arvoa ja jätetään nuottien pituudet huomiotta. Näin yksikkötestaus menee läpi.

Testatut funktiot:
- midi_to_string
- string_to_midi

## Suorituskykytestaus

