---
tags:
  - nextjs
---
An alternate frontend for Dan Murphy's

[Alculator](https://alculator.zachmanson.com) was written in the waning days of 2022 to determine the cheapest drinks at Dan Murphy's, per standard drink. The site is build with Next.js and hosted on Vercel.

If you click on the title bar there is a hidden interface used for debugging and finding data anomalies.

## Dan's API

Dan Murphy's website is a bloated Angular project but the public APIs used by the site have little to no security. After some mild poking around I was able to determine the routes needed and the general schema in use. Annoyingly, their APIs seemed designed around serving data that the frontend could display with almost no modification, rather than serving data in a logical format.

For example, for any given product, the site will send a JSON object.  This will contain 3 different prices for the product for the different pack sizes you can purchase them in.  These are labelled `caseprice`, `singleprice`, and `inanysixprice`. Case price, understably, represents the price of a case.  A case of Gage Roads Pipe Dreams Coastal Lager Bottles may have a caseprice of $31.55, but the only way to know how many bottles are in this case are in a field called `caseprice.Message`.  This is actually a string, that *usually* says something like "case (24)", when it should obviously just be an associated int called something like `caseprice.units`.

`singleprice` and `inanysixprice` are even worse, as they are used semi-interchangably. `singleprice` tends to represent the price of a single bottle, and `inanysixprice` tends to represent the price of a single bottle in a pack of 6.  Althought sometimes it's a pack of 4.  Or 8.  When `singleprice` isn't undefined, `singleprice` sometimes refers to the price of a pack of 6.  The only way to know for sure is by checking if `singleprice?.PackType === "Pack"` or `singleprice?.PackType === "Bottle"`.  And of course, when `singleprice` does mean a pack, the number of units is *usually* stored in a string.

This is all in service of avoiding frontend rendering logic as much as possible.  Perhaps this is why their API server is so horrendously slow. It can take minutes to return a list of 500 drinks, and times out easily.  To get all of their products (1000+ beers, 6000+ red winesAn alternate frontend for Dan Murphy's) in my script I needed to sequentially chain queries in batches of 100 drinks.

The data itself is riddled with mistakes an inconsistencies. "Standard Drinks" is inconsistently used in packs, where usually it represents a single unit and [occasionally it represents the sum of all the units](https://www.danmurphys.com.au/product/808932).  Sometimes fields are just completely wrong ([White Bay Brewing Alcohol Volume especially bad](https://www.danmurphys.com.au/product/194571)), or use values for bottles of different sizes ([350mL bottle with 11 standards](https://www.danmurphys.com.au/product/907223)). These products are collected in the [`blacklist.json`](https://github.com/pavo-etc/alculator/blob/main/science/blacklist.json) file and ignored by the script that downloads the catalogue.

[The final script](https://github.com/pavo-etc/alculator/blob/main/science/api.js) is warty and takes about 15 minutes to run, but converts the data to a sane schema.  This script is run daily via GitHub Action, and the new data is directly stored in JSON files and committed to the repo.  This is inefficient, but meant I didn't have to mess around with databases in my deployment.  I do hope to one day set up a proper database for this.

The source code is available on [GitHub](https://github.com/pavo-etc/alculator).