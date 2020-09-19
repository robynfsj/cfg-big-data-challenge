# CFG Big Data Challenge
![challenge header](https://raw.githubusercontent.com/robynfsj/cfg-big-data-challenge/master/images/header.jpg?token=ANPGOVNWGP52LH4EC2QDSYK7NOQV2)
  
The Big Data Challenge was an event run by Code First Girls in association with the Emergent Alliance and Rolls Royce R<sup>2</sup> Data Labs as part of Code Fest 2020.  The theme of the challenge was sustainability moving forwards after COVID-19. We were provided with UK electricity data, data on government policies and measures implemented to combat the pandemic and some economic data. We were asked to pick one question to answer from this [challenge statement](https://github.com/robynfsj/cfg-big-data-challenge/blob/master/challenge%20statements/Has%20Covid-19%20switched%20our%20green%20lights%20off%3F.pdf) so we chose to investigate the impact of COVID-19 on the supply and demand of electricity in the UK. 
  
## Team M
Laura Ramoskaite  
Dimitra Charalampopoulou  
Güzide Sofi  
Robyn Seymour-Jones  
  
## Notebooks
Notebooks used for data exploration as well as the main submission to the challenge can be found in the [notebooks](https://github.com/robynfsj/cfg-big-data-challenge/tree/master/notebooks) directory while those specifically used to model the electricity supply and demand data can be found in the [model](https://github.com/robynfsj/cfg-big-data-challenge/tree/master/model) directory.
  
The main notebook for this project is [submission.ipynb](https://github.com/robynfsj/cfg-big-data-challenge/blob/master/notebooks/submission.ipynb), which has also been uploaded as a [pdf](https://github.com/robynfsj/cfg-big-data-challenge/blob/master/notebooks/submission.pdf).

## Data
[electricity_clean.xlsx](https://github.com/robynfsj/cfg-big-data-challenge/blob/master/data/electricity_clean.xlsx) – Cleaned electricity data from the various tables provided by the UK government (BEIS, 2020). Certain data have been extracted from the different tables. A contents page provides details of what has been extracted, the source table and futher details. Data are mixed in timescale and span. They are mainly quarterly and monthly timescales and mainly span from either 1995 or 1997 to June 2020.

[response_indicies.xlsx](https://github.com/robynfsj/cfg-big-data-challenge/blob/master/data/response_indices.xlsx) – Oxford COVID-19 Government Response Tracker (OxCGRT) data showing the measures put in place by governments in response to COVID-19 (Hale et al. 2020). Only UK data has been extracted. There is one worksheet contained data for all of the UK nations combined as well as separate worksheets for the individual UK nations. Data span 2020-01-01 to 2020-08-23.

[demand.csv](https://github.com/robynfsj/cfg-big-data-challenge/blob/master/data/demand.csv) – Rolling demand data (Elexon, 2020). This provides the current electricity demand in the UK at 5 minute intervals for the period 2020-01-01 to 2020-08-30.

[avg_demand_wk.csv](https://github.com/robynfsj/cfg-big-data-challenge/blob/master/data/avg_demand_wk.csv) – Rolling demand data (Elexon, 2020) averaged (mean) for each week.

[avg_demand_d.csv](https://github.com/robynfsj/cfg-big-data-challenge/blob/master/data/avg_demand_d.csv) – Rolling demand data (Elexon, 2020) averaged (mean) for each day.


## References
BEIS (2020) *Energy Trends: UK electricity*, Department for Business, Energy & Industrial Strategy. Available online: https://www.gov.uk/government/statistics/electricity-section-5-energy-trends [Downloaded 2020-09-12].

Elexon (2020) Rolling Electricity Demand, Elexon Balancing Mechanism Reporting Service (BMRS). Available online: https://www.bmreports.com/bmrs/?q=eds/main [Downloaded 2020-09-14].

Hale, T., Angrist, N., Cameron-Blake, E., Hallas, L., Kira, B., Majumdar, S., Petherick, A., Phillips, T., Tatlow, H & Webster, S. (2020) *Oxford COVID-19 Government Response Tracker*, Blavatnik School of Government. Available online: https://www.bsg.ox.ac.uk/research/research-projects/coronavirus-government-response-tracker [Downloaded 2020-09-12].

