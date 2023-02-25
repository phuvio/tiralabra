# Käyttöohje

Ohjelma täytyy ensin asentaa. Asennus tapahtuu komennolla:

```bash
poetry install
```

Sen jälkeen ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

Ohjelman käyttöliittymä avautuu:
![Ohjelman käyttöliittymä](./kuvat/musiikin_generointi_1.png)

Seuraavaksi valitaan haluttu opetuskappale. *Data*-kansioon on tallennettu valmiiksi muutamia erityyppisiä kappaleita, joita voi käyttää opetusmusiikkina.
![Opetuskappaleen valinta](./kuvat/musiikin_generointi_2.png)

Sitten valitaan prefixin pituus.
![Prefixin pituuden valinta](./kuvat/musiikin_generointi_3.png)

Lopuksi klikkaamalla *Generoi musiikkia* -nappia generoitu musiikki tallentuu *data*-kansioon nimellä *generated.midi*.