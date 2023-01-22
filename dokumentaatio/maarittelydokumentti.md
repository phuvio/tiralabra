# Määrittelydokumentti

Projektin tarkoituksena on toteuttaa Markovin ketjujen avulla algoritmi, joka tuottaa valitun säveltäjän kaltaista musiikkia. 

Tarkoituksena on opettaa algoritmi yhden tai useamman säveltäjän sävellyksillä, jonka jälkeen algoritmi pystyy tuottamaan samantyylistä musiikkia. 

Projekti toteutetaan Pythonilla ja projektin kielenä käytetään suomea. Vertaisarviointi voidaan tehdä myös Javalla tai JavaScriptilla.

Projekti on osa tietojenkäsittelytieteen kandidaatin opintoja.

## Algoritmit ja tietorakenteet

Algoritmina käytetään Markovin ketjuja. Tietorakenteena käytetään trie-tietorakennetta.

Algoritmin aikavaativuus on O(n).

## Lähteet

* https://trepo.tuni.fi/bitstream/handle/10024/119643/SaksaVille;jsessionid=2F436BF031DB6F3D6E229DF18D432FE9?sequence=2
* https://medium.com/hackernoon/generating-music-using-markov-chains-40c3f3f46405
* https://towardsdatascience.com/markov-chain-for-music-generation-932ea8a88305
* https://soe.rutgers.edu/sites/default/files/imce/pdfs/GSET_2020___Generative_Music_Research_Paper_Final_Draft.pdf
* https://medium.com/@vanessaseto1/using-linear-algebra-and-markov-chains-to-algorithmically-generate-music-compositions-7dc88edda642
* https://scholarship.claremont.edu/cgi/viewcontent.cgi?article=1848&context=jhm
* https://en.wikipedia.org/wiki/Trie
* https://albertauyeung.github.io/2020/06/15/python-trie.html/
* https://www.geeksforgeeks.org/trie-insert-and-search/

## Ratkaisua vaativia kysymyksiä:

- kuinka testaus toteutetaan. Yksikkötestauksella on helppo tarkistaa tietorakenteen toiminta, mutta miten algoritmin oikeellisuus testataan?
- käytetäänkö syötteenä yksittäisiä nuotteja, jolloin lopputulos on melodian kaltainen, vai sointuja, jolloin lopputuloksena on sointukulku? Jälkimmäinen tuntuisi tässä vaiheessa mielenkiintoisemmalta.
- mistä löytyy syötteenä käytettää materiaalia?
