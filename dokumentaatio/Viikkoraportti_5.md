# Viikkoraportti 5

- säännöt uuden kappaleen lopettamiseen ja niiden ohjelmointi
- musiikin generoinnin vieminen omaan rekursiivisene fukntioon
  - funktio generoi uusia nuotteja, vaikka alkuperäistä prefixiä ei löytyisi triestä
- musiikin generointi funktion testit
- trie-tietorakenteen testaaminen pitkällä syötteellä

## Tällä viikolla tutustuin 

- algoritmien laaja testaaminen pitkillä syötteillä
- midin toistaminen ja siihen liittyvät ongelmat

## Seuraavaksi

- midi-tiedoston toistamisessa bugeja
  - kun pysäyttää toistamisen kesken, niin ohjelma kaatuu
  - kun yrittää toistaa samaa kappaletta uudelleen tai uutta kappaletta, niin ohjelma kaatuu
- suorituskykytestaus
  - testataan 10 nuotin, 100 nuotin ja 1000 nuotin midillä
  - 100 000 nuotin tallentaminen Triehen eri vaihtoehdoilla
  - 10 000 pituisen kappaleen generoiminen kaikilla eri Trie-vaihtoehdoilla
  - saadaan suorituskyky tallennuksen ja toiston osalta

## Käytetty tuntimäärä

22 tuntia

## Testikattavuus

Käyttöliittymä *ui.py* ja ohjelman käynnistävä *main.py* on jätetty testauksen ulkopuolelle.

!["Testikattavuus 15.2.2023"](./kuvat/testikattavuus_15.2.2023.png)

## Ratkaisua vaativia kysymyksiä:

- mitä musiikin toistamisen kanssa tulisi tehdä? Olen kokeillut useampaa ulkoisat kirjastoa mm. pygame, midi2audio ja pyFluidSynth. Kaikkien kanssa sama ongelma. Jos toiston keskeyttää tai yrittää kuunnella samaa uudelleen tai vaihtaa kappaletta, niin ohjelma kaatuu.Kun toistaa midi-tiedostoja Linuxin omalla playerillä, niin player ei reagoi mihinkään. Midin toistoa ei voi pysäyttää kuin sammuttamalla koko player. Onko parasta jättää koko soitto-ominaisuus pois omasta ohjelmasta ja tyytyä Linuxin playeriin? Ainakin sen voi sammuttaa ja jatkaa musiikin generointia omalla ohjelmalla. 
