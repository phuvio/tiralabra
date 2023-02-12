# Viikkoraportti 4

- trie-tietorakenteen käyttö nuottien tallentamiseen
- käyttöliittymän perustoimintojen ohjelmointi
- musiikin generoinnin ohjelmointi
- trie-tietorakenteen testaamisen suunnittelu pitkillä syötteillä

## Tällä viikolla tutustuin 

- musiikin generointi trie-tietorakenteen avulla

## Seuraavaksi

- käyttöliittymän ohjelmointi
  - syötteiden validointi ja virheilmoitukset
  - algoritmin kehittämän midi-tiedoston soittaminen
- kappaleen lopetus 
  -  mietittävä miten generoitu musiikki saadaan loppumaan hallitusti
- testaaminen pitkillä syötteillä 

## Käytetty tuntimäärä

12 tuntia

## Testikattavuus

Käyttöliittymä on jätetty testauksen ulkopuolelle.

!["Testikattavuus 12.2.2023"](./kuvat/testikattavuus_12.2.2023.png)

## Ratkaisua vaativia kysymyksiä:

- jäin miettimään pitääkö varautua tapauksiin, että generoitu uusi prefix ei löytyisikään trie:stä, mutta onko se turhaa? Voiko niin käydä teoriassakaan?
- mitä pitäisi tehdä midin käsittelyn testaamisen kanssa? Ulkoinen kirjasto, joka kääntää midin stringiksi ja takaisin toimii korvakuulolta hyvin. Kun muutan pidemmän kappaleen midistä stringiksi, takaisin midiksi ja vielä kerran stringiksi, niin matkalla saattaa tapahtua pieniä eroavaisuuksia. Aloin epäilemään, että voisiko johtua Linuxin midi-ajureista, kun ne tuntuvat soittavan joitakin midi-tiedostoja, kuin humalassa. Tempo heiluu. Osa midi-tiedostoista toimii hyvin.
- matriisiratkaisua, jonka tein Markovin ketjun pohjalta, ei varmaankaan tarvita ollenkaan?
