A dashboard for COVID-19 updates in Western Australia.

![[covid19_tracker.png]]

[tracker.zachmanson.com](https://tracker.zachmanson.com) was written in early 2022 to serve as a simple dashboard to visualise the number of COVID-19 infections in Western Australia.

It was borne of mild frustration on how difficult it was to find the number of locally spread cases that had been identified overnight, as opposed to imported cases. During the first few months of WA's this distinction was critical to understanding how quickly the virus was spreading, thought wasn't present in the State Governments own dashboard. They only reported this statistic on their daily(ish) press releases.

My tracker scrapes these press releases, stores them, produces a simple plot of the case numbers and generates a static website based on the data. The script is written in Python using Beautiful Soup to scrape the data, matplotlib to create plots and jinja for the templating. This is run every 20 minutes and served using nginx.

The project has been broken since September 2022, as the government switched to only reporting weekly numbers.

## Links

Source : https://github.com/pavo-etc/wa-covid-tracker
Deployment : https://tracker.zachmanson.com
