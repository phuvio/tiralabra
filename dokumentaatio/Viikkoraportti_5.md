# Viikkoraportti 5

- säännöt uuden kappaleen lopettamiseen ja niiden ohjelmointi
- musiikin generoinnin vieminen omaan rekursiivisene fukntioon
  - funktio generoi uusia nuotteja, vaikka alkuperäistä prefixiä ei löytyisi triestä
- musiikin generointi funktion testit
- trie-tietorakenteen testaaminen pitkällä syötteellä

## Tällä viikolla tutustuin 

- algoritmien laaja testaaminen pitkillä syötteillä

## Seuraavaksi

- midi-tiedoston toistamisessa bugeja
  - toistoa ei nyt pysty keskeyttämään
  - kun yrittää toistaa samaa kappaletta uudelleen tai uutta kappaletta, niin ohjelma kaatuu
- suorituskykytestaus
  - testataan 10 nuotin, 100 nuotin ja 1000 nuotin midillä
  - 100 000 nuotin tallentaminen Triehen eri vaihtoehdoilla
  - 10 000 pituisen kappaleen generoiminen kaikilla eri Trie-vaihtoehdoilla
  - saadaan suorituskyky tallennuksen ja toiston osalta

## Käytetty tuntimäärä

20 tuntia

## Testikattavuus

Käyttöliittymä on jätetty testauksen ulkopuolelle.

!["Testikattavuus 15.2.2023"](./kuvat/testikattavuus_15.2.2023.png)

## Ratkaisua vaativia kysymyksiä:

- musiikin toisto pysäyttää koko muun ohjelman kokonaan. Musiikkin on kuunneltava loppuun asti, ennen kuin ohjelma reagoi mihinkään. Olen kokeillut useampaa ulkoisat kirjastoa mm. pygame, midi2audio ja pyFluidSynth. Kaikkien kanssa sama ongelma. Ongelma on sama myös, kun toistaa midi-tiedostoja Linuxin omalla playerillä. Midin toistoa ei voi pysäyttää kuin sammuttamalla koko player. Onko parasta jättää koko soitto-ominaisuus pois omasta ohjelmasta ja tyytyä Linuxin playeriin. Ainakin sen voi sammuttaa ja jatkaa musiikin generointia omalla ohjelmalla. 
