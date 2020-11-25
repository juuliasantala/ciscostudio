# Cisco Studio - Ciscolan kauppa

Puheen lopussa Ella ja Minna käyvät Ciscolan kaupassa, joka tarjoaa monsterin metsästyspelin kaupassa vieraileville! Tämä peli mahdollistaa alennuskuponkien keräämisen kaupassa, ja antaa viihdettä lapselle samalla kuin vanhemmat voivat keskittyä ostosten tekoon. Kyseinen peli hyödynsi lokaatioanalytiikkaa, jota pystymme saamaan Merakin tukiasemista.

---

## Mistä elementeistä Ciscolan kaupan fiktiivinen monsteripeli koostuu?

![Sovelluksen elementit](./meraki_location.png)

Päätelaitteen sijainnista saadaan lokaatiotietoa Meraki tukiaseman kautta. Tähän tietoon pääsemme käsiksi Merakin pilven kautta: voimme luoda webhookin ja tilata ajankohtaisen lokaatiotiedon lähetettäväksi sovelluksellemme.

## Miten Merakin lokaatiotieto saadaan omaan sovellukseen?

Merakin lokaatiotieto voidaan tilata helposti omalta Meraki dashboardiltasi. Tarvitset tätä varten julkisen osoitteen, jossa vastaanotat pilvestä lähetettyä tietoa. Testailumuodossa voit käyttää esimerkiksi [ngrok-työkalua](https://ngrok.com/), joka muodostaa tunnelin ja ohjaa liikenteen määrittelemääsi localhost porttiin.

Esimerkkikoodina ohessa on pythonilla toteutettu flask frameworkia hyödyntävä koodi. Se toivottavasti antaa ideaa, miten lokaatiotietoa voidaan ottaa talteen. Tätä voi sitten soveltaa juuri sinun käytössäsi olevaan kieleen ja tarkoitukseen.

Haluatko oppia tarkemmin itse lokaatioanalytiikan käytöstä? Luo itsellesi ilmainen [DevNet-tunnus](https://developer.cisco.com), jonka jälkeen pääset käyttämään DevNetin ilmaisia opiskelumateriaaleja. Meraki lokaatioanalytiikalle löytyy oma [learning lab](https://learninglabs.cisco.com/lab/meraki-03-location-scanning-python/step/1)!

## Mitä muuta voin koodataa Merakin kanssa?

Aivan oikein, lokaatioanalytiikka ei ole ainoa asia mitä voit hyödyntää Merakin avoimien rajapintojen kautta. Meraki tarjoaa laajan skaalan erilaisia rajapintoja, ja paras paikka oppia lisää näistä onkin **[meraki.io](https://meraki.io)**!

Yleisesti, jotta voit käyttää Merakin rajapintoja, tarvitsee sinun
1. enabloida rajapinnat Merakin dashboardilta
2. luoda itsellesi API avain, jolla tunnistaudut rajapintakutsuja tehdessäsi
