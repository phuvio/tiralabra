# Testausdokumentti

Yksikkötestauksen kattavuusraportti:
![Testikattavuus 25.2.2023](./kuvat/testikattavuus_25.2.2023.png)

## Yksikkötestaus

Yksikkötestaus on toteutettu Pythonin Unittest-kirjaston avulla. Ohjelman eri osa-alueille on omat testitiedostonsa, jotka testaavat kyseisen osan toimivuutta. Testit on helppo toistaa ajamalla halutut testit uudelleen. 

Yksikkötestit voi suorittaa komennolla:

```bash
poetry run invoke test
```

Suorituskykytestit voi ajaa seuraavasti:

Käynnistä poetry:
```bash
poetry shell
```
Siirry hakemistoon src:
```bash
cd src
```
Käynnistä testit:
```bash
python3 performance_test.py
```

Testitiedostot:
- [Trie-tietorakenteeseen liittyvät yksikkötestit](../src/tests/trie_test.py)
- [Musiikin generointiin liittyvät yksikkötestit](../src/tests/generate_music_test.py)
- [Midin käsittelyyn liittyvät yksikkötestit](../src/tests/midi_test.py)
- [Suorituskykytestit](../src/performance_test.py)

### Trie-tietorakenteen yksikkötestaus

Trie-tietorakenne on testattu monipuolisesti ensin lyhyillä syötteillä ja sitten pitkillä syötteillä.

Testatut funktiot:
- luokka Trie
  - add_list_to_trie
  - search_given_prefix
  - return_choices
- luokka TrieNode
  - add_note

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
  - testissä tarkastetaan, että jokaiseen triehen tallennettuun solmuun on tallennettu oikeat alisolmut sekä niiden esiintyvyysmäärät

## Musiikin generointiin liittyvän funktion yksikkötestaus

Musiikin generointi on toteutettu omana funktiona. Funktiolle syötetään trie, johon opetuskappale on tallennettu, aikaisemmin generoitu musiikki sekä prefix, jolla generoidaan seuraava nuotti. Funktio on testattu ensin lyhyillä syötteillä. Sen jälkeen triehen on tallennettu 1000 nuotti pitkä kappale. Testissä kappaleen nuotit sekoitetaan. Sen jälkeen arvotaan prefix ja tarkistetaan, että palautettu arvottu nuotti on mahdollinen.

Testattu funktio:
- generate_music-funktio

Suoritetut testit:
- test_generate_music_from_known_prefix
  - testataan generoiko funktio oikean nuotin, kun prefix löytyy triestä ja sillä on vain yksi vaihtoehto
- test_generate_music_from_unknown_prefix
  - testataan generoiko funktio oikean nuotin, kun ainoastaan prefixin viimeinen nuotti löytyy triestä
  - tämä testi ajetaan varmuuden vuoksi kahteen kertaan samalla trie-tietorakenteella
- test_generate_music_gives_correct_note
  - sekoitetaan tuhat nuottia sisältävä luettelo ja tallennetaan se Trie-tietorakenteeseen
  - arvotaan prefixin pituus ja valitaan siihen arpomalla nuotit edellä mainitusta sekoitetusta nuottiluettelosta
  - tarkistetaan, että edellisessä kohdassa arvotulla prefixillä generoitu nuotti on mahdollinen
  - toistetaan testi 10 000 kertaa 

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
         Aikaa kului: 0.146708 sekuntia
         Keskimääräinen aika per midi-tiedosto 1.46708e-06 sekuntia
         Keskimääräinen aika per nuotti 1.46708e-06 sekuntia
-----------------------------------------------------------------------------
      100 nuotin pituisen midi-tiedoston tallentaminen
         Aikaa kului: 0.129802 sekuntia
         Keskimääräinen aika per midi-tiedosto 1.29802e-05 sekuntia
         Keskimääräinen aika per nuotti 1.29802e-06 sekuntia
-----------------------------------------------------------------------------
      1000 nuotin pituisen midi-tiedoston tallentaminen
         Aikaa kului: 0.125612 sekuntia
         Keskimääräinen aika per midi-tiedosto 0.000125612 sekuntia
         Keskimääräinen aika per nuotti 1.25612e-06 sekuntia
-----------------------------------------------------------------------------

Algoritmin aikavaativuus tallennuksen suhteen on O(n). Tuloksista nähdään, että tiedon tallentaminen triehen riippuu tallennettavan kappaleen pituudesta. Kuitenkin aika per tallennettava nuotti on kaikilla pituuksilla sama eli aikavaativuus on O(n).

Tietojen hakua Trie-tietorakenteesta testattiin hakemalla edellisessä testissä muodostuineista kolmesta Trie-tietorakenteesta 1-, 2-, 3-, 4-, ja 5-nuotin mittaisilla prefixeillä yhteensä 100 000 nuottia. 

Algoritmin aikavaativuus tiedon haun suhteen on O(n). Alla olevista tuloksista nähdään, että tiedon haku riippuu haettavan prefixin pituudesta, mutta triehen tallennetun kappaleen pituudella ei ole merkitystä eli aikavaativuus on O(n).

-----------------------------------------------------------------------------
Suorituskykytesti: tietojen hakeminen Trie-tietorakenteesta

   Haetaan 100 000 nuottia 1 pituisella prefixillä
-----------------------------------------------------------------------------
      Haku Triestä, johon tallennettu 10 nuotin pituisen midi-tiedosto
         Aikaa kului: 0.0514328 sekuntia
         Keskimääräinen aika 5.14328e-07 sekuntia
-----------------------------------------------------------------------------
      Haku Triestä, johon tallennettu 100 nuotin pituisen midi-tiedosto
         Aikaa kului: 0.0505579 sekuntia
         Keskimääräinen aika 5.05579e-07 sekuntia
-----------------------------------------------------------------------------
      Haku Triestä, johon tallennettu 1000 nuotin pituisen midi-tiedosto
         Aikaa kului: 0.0514541 sekuntia
         Keskimääräinen aika 5.14541e-07 sekuntia
-----------------------------------------------------------------------------
   Haetaan 100 000 nuottia 2 pituisella prefixillä
-----------------------------------------------------------------------------
      Haku Triestä, johon tallennettu 10 nuotin pituisen midi-tiedosto
         Aikaa kului: 0.0906317 sekuntia
         Keskimääräinen aika 9.06317e-07 sekuntia
-----------------------------------------------------------------------------
      Haku Triestä, johon tallennettu 100 nuotin pituisen midi-tiedosto
         Aikaa kului: 0.0903304 sekuntia
         Keskimääräinen aika 9.03304e-07 sekuntia
-----------------------------------------------------------------------------
      Haku Triestä, johon tallennettu 1000 nuotin pituisen midi-tiedosto
         Aikaa kului: 0.0915389 sekuntia
         Keskimääräinen aika 9.15389e-07 sekuntia
-----------------------------------------------------------------------------
   Haetaan 100 000 nuottia 3 pituisella prefixillä
-----------------------------------------------------------------------------
      Haku Triestä, johon tallennettu 10 nuotin pituisen midi-tiedosto
         Aikaa kului: 0.0965574 sekuntia
         Keskimääräinen aika 9.65574e-07 sekuntia
-----------------------------------------------------------------------------
      Haku Triestä, johon tallennettu 100 nuotin pituisen midi-tiedosto
         Aikaa kului: 0.0967405 sekuntia
         Keskimääräinen aika 9.67405e-07 sekuntia
-----------------------------------------------------------------------------
      Haku Triestä, johon tallennettu 1000 nuotin pituisen midi-tiedosto
         Aikaa kului: 0.0963292 sekuntia
         Keskimääräinen aika 9.63292e-07 sekuntia
-----------------------------------------------------------------------------
   Haetaan 100 000 nuottia 4 pituisella prefixillä
-----------------------------------------------------------------------------
      Haku Triestä, johon tallennettu 10 nuotin pituisen midi-tiedosto
         Aikaa kului: 0.101658 sekuntia
         Keskimääräinen aika 1.01658e-06 sekuntia
-----------------------------------------------------------------------------
      Haku Triestä, johon tallennettu 100 nuotin pituisen midi-tiedosto
         Aikaa kului: 0.101578 sekuntia
         Keskimääräinen aika 1.01578e-06 sekuntia
-----------------------------------------------------------------------------
      Haku Triestä, johon tallennettu 1000 nuotin pituisen midi-tiedosto
         Aikaa kului: 0.101564 sekuntia
         Keskimääräinen aika 1.01564e-06 sekuntia
-----------------------------------------------------------------------------
   Haetaan 100 000 nuottia 5 pituisella prefixillä
-----------------------------------------------------------------------------
      Haku Triestä, johon tallennettu 10 nuotin pituisen midi-tiedosto
         Aikaa kului: 0.110796 sekuntia
         Keskimääräinen aika 1.10796e-06 sekuntia
-----------------------------------------------------------------------------
      Haku Triestä, johon tallennettu 100 nuotin pituisen midi-tiedosto
         Aikaa kului: 0.108987 sekuntia
         Keskimääräinen aika 1.08987e-06 sekuntia
-----------------------------------------------------------------------------
      Haku Triestä, johon tallennettu 1000 nuotin pituisen midi-tiedosto
         Aikaa kului: 0.110342 sekuntia
         Keskimääräinen aika 1.10342e-06 sekuntia
