# Musiikin tuottaminen Markovin ketjun avulla

- [Määrittelydokumentti](./dokumentaatio/maarittelydokumentti.md)
- [Käyttöohje](./dokumentaatio/kaytto-ohje.md)
- [Testausdokumentti](./dokumentaatio/testausdokumentti.md)
- [Toteutusdokumentti](./dokumentaatio//toteutusdokumentti.md)
- [Viikkoraportti 1](./dokumentaatio/Viikkoraportti_1.md)
- [Viikkoraportti 2](./dokumentaatio/Viikkoraportti_2.md)
- [Viikkoraportti 3](./dokumentaatio/Viikkoraportti_3.md)
- [Viikkoraportti 4](./dokumentaatio/Viikkoraportti_4.md)
- [Viikkoraportti 5](./dokumentaatio/Viikkoraportti_5.md)
- [Viikkoraportti 6](./dokumentaatio/Viikkoraportti_6.md)

# Huomio Python-versiosta

Sovelluksen toiminta on testattu Python-versiolla 3.8. Linux-koneella.

# Komentorivitoiminnot

### Ohjelman asentaminen

Ohjelman voi asentamaan komennolla:

```bash
poetry install
```

### Ohjelman suorittaminen

Ohjelman voi suorittamaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Yksikkötestit suoritetaan komennolla:

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

### Testikattavuus

Yksikkötestien testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu *htmlcov*-hakemistoon.

### Pylint

Tiedoston [.pylintrc](./.pylintrc) määrittelemät tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```

### Autopep

Koodin formatointi automaattisesti PEP 8-tyyliohjeiden mukaisesti onnistuu komennolla:

```bash
poetry run invoke format
```
