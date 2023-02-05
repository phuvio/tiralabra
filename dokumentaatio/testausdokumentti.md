# Testausdokumentti

## Yksikkötestaus

Yksikkötestaus on toteutettu Pythonin Unittest-kirjaston avulla. Ohjelman eri osa-alueille on omat testitiedostonsa, jotka testaavat kyseisen osan toimivuutta. Trie-tietorakennetta ja Markovin ketjua on testattu erilaisilla syötteillä, jotka näkyvät testitiedostoissa. Testit on helppo toistaa ajamalla halutut testit uudelleen. 

Midin käsittelyyn liittyvä testaaminen oli hankalampaa. Ohjelmassa käytetään Music21-nimistä kirjastoa. Kirjasto on laajasti käytetty ja se korvakuulolta toimii hyvin. Yksikkötestien näkökulmasta haasteen tuo se, että ajamalla midi-tiedoston stringiksi ja taas takaisin midiksi aiheuttaa pieniä eroavaisuuksia alkuperäisen ja loppullisen tiedoston välillä. Niitä ei korvakuulolta erota, mutta tiedostojen tarkka vertailu muuttuu mahdottomaksi.

Testitiedostot:
- [Trie-tietorakenteeseen liittyvät yksikkötestit](../src/tests/trie_test.py)
- [midin käsittelyyn liittyvät yksikkötestit](../src/tests/midi_test.py)
- [Markovin ketjuun liittyvät yksikkötestit](../src/tests/markovchain_test.py)

[Yksikkötestien kattavuus](./htmlcov/index.html)
