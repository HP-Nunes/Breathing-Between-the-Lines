# Breathing Between the Lines: the legacy of red-lining on risk factors of air pollution in Seattle, WA
A collaborative project by Hadrien Picq and Johnathan Padilla

![alt text](readMe_assets/img/banner2.png "Banner")
## Final project for the TechSoup and ParsonsTKO Summer 2020 Data Strategy Mentorship Program.
The project was presented on August 25th, 2020, and can be viewed and accessed: https://parsonstko.com/data-for-social-impact-conference/

### Summary
For decades, the US mortgage industry systematically denied mortgages to people of color through the practice of red-lining, which institutionalized racial segregation. This project team’s analysis focuses on Seattle, linking the city’s history of red-lining with current air pollution levels and health trends. Their data suggests that previously red-lined areas suffer from higher rates of pollution and asthma today than communities zoned as “desirable” in the 1940s. It also finds that people of color are currently underrepresented in air monitoring coverage in Seattle.
***
### Summary of Methodology
#### Multi-Criteria Weighted Overlay Analysis to identify neighborhoods of Seattle suitable for community-level air monitoring strategies, and observe overlaps with the Homeowner Loan Corporation 1936's "Grade of Security" (Redlining) Map.

![alt text](readMe_assets/img/MultiCriteria_GIF.gif "Banner")

<b> Part I: Feature Selection & Weight Assignment </b>

1. Puget Sound Clean Air Agency (PSCAA)’s 2014 Cumulative Risk Assessment: Highly Impacted Communities
Data Source: https://pscleanair.gov/300/Documents

This study from the PSCAA informs its community selection in King's County to implement its [Focus Communities program](https://www.pscleanair.gov/382/Focus-Communities), which involves community-level planning and programming. The composite data was retained solely for the city of Seattle, and assigned weights based on the study's quantile ranking.

![alt text](readMe_assets/img/feat1.jpg "PSCAA data")

2. Office of Planning & Community Development Seattle GeoData’s 2020 Racial and Social Equity Composite Index
Data Source: https://data-seattlecitygis.opendata.arcgis.com/datasets/225a4c2c50e94f2cb548a046217f49f7_0

The Racial and Social Equity Index combines information on race, ethnicity, and related demographics with data on socioeconomic and health disadvantages to identify where priority populations make up relatively large proportions of neighborhood residents. We included specifically the Composite Disadvantage composite index due to its emphasis on socio-economic determinants of healths, many of which are shared concerns as reflected in the PSCAA's [Focus Communities program](https://www.pscleanair.gov/382/Focus-Communities) (highlighted below). Weights were assigned based on the index's quantile ranking.

![alt text](readMe_assets/img/criteria.jpg "2020 Racial and Social Equity Composite Index criteria")

![alt text](readMe_assets/img/feat2.jpg "2020 Racial and Social Equity Composite Index")

3. Zone of coverage of PurpleAir's sensors in Seattle, WA.
Data Source: https://www.purpleair.com/map#15.19/37.781857/-122.489357

![alt text](readMe_assets/img/feat3.jpg "PSCAA data")

4. Community Anchor Institutions 
Data Source (public schools): https://data-seattlecitygis.opendata.arcgis.com/datasets/a2e1128bd7a041358ce455c628ec9834_8
Data Source (public libraries): https://data-seattlecitygis.opendata.arcgis.com/datasets/seattle-public-libraries

![alt text](readMe_assets/img/feat4.jpg "PSCAA data")

5. 2018 Seattle Traffic Count
Data Source: https://data.seattle.gov/Land-Base/2018-Traffic-Flow-Counts/e9vy-mn8x

![alt text](readMe_assets/img/feat5.jpg "PSCAA data")

6. Proximity to Major Traffic Arteries (Interstates I-5 and I-90)
Data Source: https://data.seattle.gov/Land-Base/Street-Network-Database-SND-/nvgs-5agd

![alt text](readMe_assets/img/feat6.jpg "PSCAA data")

***
## Tech Stack

* Jupyter Notebook
* Python 3.8. 3
* QGIS

Packages:
* pandas
* tqdm
* sqlalchemy
* matplotlib
* seaborn
* requests
* os
***
## Group Resources
### Published posts:
[An Introduction to Data Collection: REST APIs with Python & Pizzas](https://medium.com/@geocuriosity/an-introduction-to-data-collection-rest-apis-with-python-pizzas-7b682cef676c) by Hadrien Picq.

[An Introduction to Data Collection: Pulling OpenAQ Data from AWS S3 using AWS Athena](https://medium.com/@johnathan.d.padilla/an-introduction-to-data-collection-pulling-openaq-data-from-s3-using-aws-athena-26863b97c5cb) by Johnathan Padilla

[An Introduction to Data Cleaning: Using Regular Expressions to Clean your Data](https://medium.com/@johnathan.d.padilla/an-introduction-to-data-cleaning-using-regular-expressions-to-clean-your-data-9684ccfac74c) by Johnathan Padilla

### Reference notebooks:

[A Beginners Guide to API | Using Python to Collect Air Quality Data](https://nbviewer.jupyter.org/github/Kidd-Thomas/Air-Quality-Comparison/blob/master/AQS%20API%20GUIDE.ipynb?flush_cache=True) by Thomas Kidd.

[Data Wrangling](https://nbviewer.jupyter.org/github/HP-Nunes/dataStrategyMentorship_airQAproj/blob/master/data_Wrangling.ipynb) by Hadrien Picq.
