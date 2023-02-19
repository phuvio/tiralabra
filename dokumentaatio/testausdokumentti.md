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

Algoritmin suorituskykyä on testattu tallentamisen ja tiedon haun osalta. Trie-tietorakenteeseen tallennettiin 10-, 100- ja 1000-nuotin pituiset midi-tiedostot. Kaikkien kolmen tallentamista testattiin tallentamalla jokaisen kohdalla yhteensä 100 000 nuottia Triehen. Tallennus tapahtui siten, että kaikki kahden, kolmen, neljän, viiden ja kuuden nuotin ketjut tallennettiin erikseen. Näin Triestä voi hakea generoitavia nuotteja 1-5-nuotin pituisilla prefixeillä.  

Testien tulos:
-----------------------------------------------------------------------------
Suorituskykytesti: tietojen tallentaminen Trie-tietorakenteeseen
   Tallennetaan 100 000 nuottia
-----------------------------------------------------------------------------
      10 nuotin pituisen midi-tiedoston tallentaminen
         Aikaa kului: 0.198039 sekuntia
         Keskimääräinen aika per midi-tiedosto 0.000002 sekuntia
         Keskimääräinen aika per nuotti 0.000002 sekuntia
-----------------------------------------------------------------------------
      100 nuotin pituisen midi-tiedoston tallentaminen
         Aikaa kului: 0.199934 sekuntia
         Keskimääräinen aika per midi-tiedosto 0.000020 sekuntia
         Keskimääräinen aika per nuotti 0.000002 sekuntia
-----------------------------------------------------------------------------
      1000 nuotin pituisen midi-tiedoston tallentaminen
         Aikaa kului: 0.172730 sekuntia
         Keskimääräinen aika per midi-tiedosto 0.000173 sekuntia
         Keskimääräinen aika per nuotti 0.000002 sekuntia
-----------------------------------------------------------------------------

Tietojen hakua Trie-tietorakenteesta testattiin hakemalla edellisessä testissä muodostuineista kolmesta Trie-tietorakenteesta 1-, 2-, 3-, 4-, ja 5-nuotin mittaisilla prefixeillä yhteensä 100 000 nuottia.

Testin tulos
-----------------------------------------------------------------------------
Suorituskykytesti: tietojen hakeminen Trie-tietorakenteesta
   Haetaan 100 000 nuottia 1 pituisella prefixillä
-----------------------------------------------------------------------------
      Haku Triestä, johon tallennettu 10 nuotin pituisen midi-tiedosto
         Aikaa kului: 0.067806 sekuntia
         Keskimääräinen aika 0.000001 sekuntia
-----------------------------------------------------------------------------
      Haku Triestä, johon tallennettu 100 nuotin pituisen midi-tiedosto
         Aikaa kului: 0.065801 sekuntia
         Keskimääräinen aika 0.000001 sekuntia
-----------------------------------------------------------------------------
      Haku Triestä, johon tallennettu 1000 nuotin pituisen midi-tiedosto
         Aikaa kului: 0.066154 sekuntia
         Keskimääräinen aika 0.000001 sekuntia
   Haetaan 100 000 nuottia 2 pituisella prefixillä
-----------------------------------------------------------------------------
      Haku Triestä, johon tallennettu 10 nuotin pituisen midi-tiedosto
         Aikaa kului: 0.118937 sekuntia
         Keskimääräinen aika 0.000001 sekuntia
-----------------------------------------------------------------------------
      Haku Triestä, johon tallennettu 100 nuotin pituisen midi-tiedosto
         Aikaa kului: 0.120498 sekuntia
         Keskimääräinen aika 0.000001 sekuntia
-----------------------------------------------------------------------------
      Haku Triestä, johon tallennettu 1000 nuotin pituisen midi-tiedosto
         Aikaa kului: 0.119040 sekuntia
         Keskimääräinen aika 0.000001 sekuntia
   Haetaan 100 000 nuottia 3 pituisella prefixillä
-----------------------------------------------------------------------------
      Haku Triestä, johon tallennettu 10 nuotin pituisen midi-tiedosto
         Aikaa kului: 0.129086 sekuntia
         Keskimääräinen aika 0.000001 sekuntia
-----------------------------------------------------------------------------
      Haku Triestä, johon tallennettu 100 nuotin pituisen midi-tiedosto
         Aikaa kului: 0.127506 sekuntia
         Keskimääräinen aika 0.000001 sekuntia
-----------------------------------------------------------------------------
      Haku Triestä, johon tallennettu 1000 nuotin pituisen midi-tiedosto
         Aikaa kului: 0.129165 sekuntia
         Keskimääräinen aika 0.000001 sekuntia
   Haetaan 100 000 nuottia 4 pituisella prefixillä
-----------------------------------------------------------------------------
      Haku Triestä, johon tallennettu 10 nuotin pituisen midi-tiedosto
         Aikaa kului: 0.135731 sekuntia
         Keskimääräinen aika 0.000001 sekuntia
-----------------------------------------------------------------------------
      Haku Triestä, johon tallennettu 100 nuotin pituisen midi-tiedosto
         Aikaa kului: 0.137004 sekuntia
         Keskimääräinen aika 0.000001 sekuntia
-----------------------------------------------------------------------------
      Haku Triestä, johon tallennettu 1000 nuotin pituisen midi-tiedosto
         Aikaa kului: 0.136033 sekuntia
         Keskimääräinen aika 0.000001 sekuntia
   Haetaan 100 000 nuottia 5 pituisella prefixillä
-----------------------------------------------------------------------------
      Haku Triestä, johon tallennettu 10 nuotin pituisen midi-tiedosto
         Aikaa kului: 0.146352 sekuntia
         Keskimääräinen aika 0.000001 sekuntia
-----------------------------------------------------------------------------
      Haku Triestä, johon tallennettu 100 nuotin pituisen midi-tiedosto
         Aikaa kului: 0.145254 sekuntia
         Keskimääräinen aika 0.000001 sekuntia
-----------------------------------------------------------------------------
      Haku Triestä, johon tallennettu 1000 nuotin pituisen midi-tiedosto
         Aikaa kului: 0.147385 sekuntia
         Keskimääräinen aika 0.000001 sekuntia
