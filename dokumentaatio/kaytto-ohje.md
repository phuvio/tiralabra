# Käyttöohje

Lataa [ohjelma](https://github.com/phuvio/tiralabra/releases) viimeisin julkaisu.

Asenna ohjelma. Asennus tapahtuu komennolla:

```bash
poetry install
```

Ohjelman voi suorittamaan komennolla:

```bash
poetry run invoke start
```

Ohjelman käyttöliittymä avautuu:

![Ohjelman käyttöliittymä](./kuvat/musiikin_generointi_1.png)

Seuraavaksi valitaan haluttu opetuskappale. Opetuskappaleina voi käyttää yhdellä soittimella soitettuja midi-tiedostoja. *Data*-kansioon on tallennettu valmiiksi muutamia erityyppisiä kappaleita, joita voi käyttää opetusmusiikkina.

![Opetuskappaleen valinta](./kuvat/musiikin_generointi_2.png)

Sitten valitaan prefixin pituus.

![Prefixin pituuden valinta](./kuvat/musiikin_generointi_3.png)

Lopuksi klikkaamalla *Generoi musiikkia* -nappia generoitu musiikki tallentuu *data*-kansioon midi-tiedostona nimellä *generated.midi*.
