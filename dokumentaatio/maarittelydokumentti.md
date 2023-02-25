# Määrittelydokumentti

Projektin tarkoituksena on toteuttaa Markovin ketjujen avulla algoritmi, joka generoi musiikkia opetusmateriaalina käytetyn kappaleen pohjalta. 

Tarkoituksena on opettaa algoritmi yhdellä kappaleella, jonka jälkeen algoritmi pystyy generoimaan uutta musiikkia imitoimalla kappaletta. 

Projekti toteutetaan Pythonilla ja projektin kielenä käytetään suomea. Vertaisarviointi voidaan tehdä myös Javalla tai JavaScriptilla.

Projekti on osa tietojenkäsittelytieteen kandidaatin opintoja.

## Algoritmit ja tietorakenteet

Algoritmina käytetään Markovin ketjuja. Tietorakenteena käytetään trie-tietorakennetta. Trie soveltuu tähän algoritmiin hyvin. Siihen voidaan helposti tallentaan Markovin ketjuja sekä niiden jälkeiset vaihtoehdot ja tiedon haku tietorakenteesta on nopeaa. Tässä algoritmissa ei tarvita tietojen poistoa.

Algoritmin aikavaativuus on O(n) sekä tiedon tallentamisen että tiedon haun osalta. Tilavaativuus on myös O(n). 

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
