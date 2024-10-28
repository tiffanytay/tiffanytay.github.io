## Airbnb Pricing Analysis in NYC

**Executive Summary:** This project contemplates what would be a competitive price to maximize profitability for an entire Airbnb apartment in New York City (NYC), assuming the desired pricing strategy is luxury.

Using **Tableau**, I juxtaposed key data points from [Inside Airbnb](https://insideairbnb.com/new-york-city/) onto an NYC map to condlue that an initial price of around $300 per night would be competitive for Manhattan.   

After establishing a solid rating with many reviews (rated at 91 or above to beat the average rating for Manhattan apartments), I may be able to raise the price to $350-$400, to position my property as an in-demand luxury property with a proven track record.  Furthermore, adding a third bed to the apartment would be more profitable after around 11 nights - assuming that:
[1] a new bed is $1,000;
<br>[2] price is increased by $100 (as justified by the increase in average price from $305 to $390); and 
<br>[3] Airbnb's fee is 3%.

Finally, I did some light front-end development with **HTML** and **Javascript** to embed the Tableau dashboard on this Github site.

[See dashboard](/airbnbIndex.html)

<br>
<br>
---

### 1. Key assumptions

[a] My property is already registered with the city for short-term stays less than 30 days or will only be available for stays 30 days or longer.
<br>[b] The Airbnb host fee is 3%.

### 2. Data collection

[Inside Airbnb](https://insideairbnb.com) has fairly recent data sets for Airbnb by city.

Ultimately, I used 1 XLSX file in this project.

### 3. Data cleansing / transformation

The dataset did not require any cleansing.  

### 3. Data exploration / analysis

**Incomplete data -** While exploring the data, it became clear that the datasets were incomplete in some places. 4.5% of people who hold active licenses for their dogs do not know their dog's breed.  The dog run dataset had a significant amount of blanks in some fields.  There's also a mismatch in the dates that the datasets were last updated.  All of this should be considered when reviewing the data analysis.

**Exploration -** I assessed the fields available and chose chart types that would quickly offer users insights.  For instance, bar charts are arguably the easiest chart for everyone to understand and allow for fast comparison of 1 bar versus another.

### 4. Dashboard design + Data storytelling

**Design -** I sourced images from [Freepik](https://www.freepik.com) and created a color palette based on Airbnb's primary brand color.

**Storytelling -** With the visuals drafted in the previous phase, I considered what made sense to show next to each other on a dashboard and what would fit on the page.  My process also includes considering which data points are lower priority and could be moved into a less prominent part of the dashboard.  I added slicers that I would expect users to want.

<img src="images/nycdogsscreenshot.png?raw=true"/>

**Finishing touches -** I embedded the Tableau dashboard on this Github site with some HTML and Javascript code, tweaking the height of the embedded dashboard to optimize viewing.

### 5. Iteration

To continue to enhance this dashboard, I propose the following:
- Scraping rating review language from Airbnb for NYC properties and running sentiment analysis to learn what may make one property more successful than others.

---

### References

[1] Datasets from [Inside Airbnb](https://insideairbnb.com/new-york-city/), found via Tableau's [blog post](https://www.tableau.com/blog/how-to-find-sources-for-public-data-sets) on public data sets
<br>[2] Filter icon by Adrian Adam from [Noun Project](https://thenounproject.com/browse/icons/term/filter/) (CC BY 3.0)
