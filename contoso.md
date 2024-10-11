## A Snapshot of NYC Dogs

**Executive Summary:** This project taps into my curiosity about all the dogs that call New York City (NYC) home. What kind of dogs are they?  Where do they live?  Where do they play?  

Steps taken with primary tools Power Query and Power BI are summarized below.

Highlights of surprising insights include:
- Despite Manhattan being the densest borough, the most popular licensed known dog breeds are medium-large dogs: Labs and Goldendoodles.
- Manhattan has the most dog runs but the least waste bag dispensers.
- Most dogs live in Northwest Brooklyn.

<iframe title="A Snapshot of NYC Dogs" width="600" height="486" src="https://app.powerbi.com/view?r=eyJrIjoiOTc0YTE3NmYtNDE4ZC00ZWFkLTgwZjctODNmMmY5MzZmNmNjIiwidCI6Ijc5NmIxZGQ2LWQzNmQtNGQwOC05YTMzLWI1MGZkOTUwZTY5ZCIsImMiOjZ9&embedImagePlaceholder=true" frameborder="0" allowFullScreen="true"></iframe>

<br>
<br>
---

### 1. Data collection

Thanks to NYC Open Data's mission to have 'open data for all', it was simple to procure datasets on NYC dog licenses, dog parks, dog waste receptacles and--most surprising of all--squirrels.  During the data exploration phase, I discovered that I also needed a dataset mapping zip codes to neighborhoods/boroughs.  

Ultimately, I used 5 CSV files in this project.

### 2. Data cleansing / transformation

NYC Open Data datasets are largely ready-to-consume; however, I did have to do some minor data cleansing:
- Cleansed the dog license dataset of invalid values in the [AnimalBirthYear] column
- Switched [ZipCode] data type to text in all datasets to prevent aggregation
- Excluded license with birth year in 1912 from Age Distribution and Average Age visuals

### 3. Data exploration / analysis

**Incomplete data -** While exploring the data, it became clear that the datasets were incomplete in some places. 4.5% of people who hold active licenses for their dogs do not know their dog's breed.  The dog run dataset had a significant amount of blanks in some fields.  There's also a mismatch in the dates that the datasets were last updated.  All of this should be considered when reviewing the data analysis.

**Exploration -** I assessed the fields available and chose chart types that would quickly offer users insights.  For instance, bar charts are arguably the easiest chart for everyone to understand and allow for fast comparison of 1 bar versus another.

### 4. Dashboard design with GenAI + Data storytelling

**Design -** I sourced images from Google searches and created a color palette for the data visualizations inspired by the images.  After deciding on the colors, I used [Perplexity AI](https://www.perplexity.ai/) to draft the initial Power BI theme file.

**Storytelling -** With the visuals drafted in the previous phase, I considered what made sense to show next to each other on a dashboard and what would fit on the page.  My process also includes considering which data points are lower priority and could be moved into a less prominent part of the dashboard.  I added slicers that I would expect users to want.

While I would have loved to include a map visual plotting counts of dog licenses or dog runs, the loss of performance on my 5-year-old home computer and cost of calling map APIs for 600k records outweighed the potential benefit.

<img src="images/nycdogsscreenshot.png?raw=true"/>

**Finishing touches -** I layered on small image objects to complete the dashboard design and added info tooltips to provide users with more context into the data.  Finally, I programmed in a date/time stamp that dynamically updates whenever the dashboard is refreshed.

<img src="images/infotooltipscreenshot.png?raw=true"/>

### 5. Iteration

To continue to enhance this dashboard, I propose the following:
- Update all datasets to 2024 data.
- Compile list of desired data points, compare against current dataset fields and make a plan on how to close data gaps (e.g., make fields mandatory in data collection forms).
- Create a drill-through page by borough and/or neighborhood.
- Consider whether to bring in animal bite dataset.

---

### References

[1] Datasets from [Github]([https://opendata.cityofnewyork.us/](https://github.com/sql-bi/Contoso-Data-Generator-V2-Data/releases/tag/ready-to-use-data)
<br>[2] [Cover image](https://graymalin.com/products/picnic-party-central-park)
<br>[3] [Dashboard panorama image](https://www.shutterstock.com/image-vector/people-walk-play-dogs-city-park-2206454515)
<br>[4] [Dashboard bird and sun images](https://designstripe.com/search/assets?style=cheerful)
