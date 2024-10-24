## Airbnb Competitve Pricing Analysis - NYC

**Executive Summary:** This project contemplates what would be an optimal competitive price for an Airbnb apartment in New York City (NYC).

Using **Tableau** and data from [Inside Airbnb](https://insideairbnb.com/new-york-city/), I analyzed the relevant data points like property zip codes and average prices to conclude that an initial price of around $300 per night is competitive for Manhattan.   

After establishing a solid rating with many reviews (rated at 91 or above to beat the average rating for Manhattan apartments), I may be able to raise the price to $350-$400, to position my property as a luxury property with a proven track record.  Furthermore, adding a third bed to the apartment would be more profitable after around 11 stays - assuming that:
[1] a new bed is $1,000;
<br>[2] price is increased by $100 (as justified by the increase in average price from $305 to $390); and 
<br>[3] Airbnb's fee is 3%.

![](./airbnbHTMLintoMD.svg)

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

[1] Datasets from [Inside Airbnb](https://insideairbnb.com/new-york-city/)
<br>[2] Suitcase image designed by [Freepik](https://github.com/user-attachments/assets/516b6759-d6d8-41e2-a0d6-f87a09904269)
<br>[3] Travel sticker images designed by [Freepik](https://www.freepik.com/free-vector/travel-sticker-set_3731900.htm#fromView=search&page=1&position=4&uuid=906bbde3-dffe-47f5-9a5c-3209741d8b38)
<br>[4] [Dashboard bird and sun images](https://designstripe.com/search/assets?style=cheerful)
