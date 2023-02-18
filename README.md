# Musiikin tuottaminen Markovin ketjun avulla

- [Määrittelydokumentti](./dokumentaatio/maarittelydokumentti.md)
- [Testausdokumentti](./dokumentaatio/testausdokumentti.md)
- [Toteutusdokumentti](./dokumentaatio//toteutusdokumentti.md)
- [Viikkoraportti 1](./dokumentaatio/Viikkoraportti_1.md)
- [Viikkoraportti 2](./dokumentaatio/Viikkoraportti_2.md)
- [Viikkoraportti 3](./dokumentaatio/Viikkoraportti_3.md)
- [Viikkoraportti 4](./dokumentaatio/Viikkoraportti_4.md)
- [Viikkoraportti 5](./dokumentaatio/Viikkoraportti_5.md)

# Huomio Python-versiosta

Sovelluksen toiminta on testattu Python-versiolla 3.8. Linux-koneella.

# Komentorivitoiminnot

### Ohjelman asentaminen

Ohjelman pystyy asentamaan komennolla:

```bash
poetry install
```

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

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
