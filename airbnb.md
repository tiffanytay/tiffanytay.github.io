## Airbnb Pricing Analysis in NYC

**Executive Summary:** This project identifies a competitive price under a luxury pricing strategy to maximize profitability for an entire Airbnb apartment in New York City (NYC).

Using **Tableau**, I juxtaposed key data points from [Inside Airbnb](https://insideairbnb.com/new-york-city/) onto an NYC map.  Using the dashboard filters I created, I searched for comparable properties to determine that an initial price of around $500 per night would be competitive for a 2 bedroom, 2 bathroom apartment in the Upper West Side neighborhood - about $50 less than the average.   

After establishing a solid rating with many reviews (rated at 4.7 or above to beat the average rating for comparables), I may be able to raise the price to $550-$600, to position my property as an in-demand luxury property with a proven track record.

Finally, I did some light front-end development with **HTML** and **Javascript** to embed the Tableau dashboard on this Github site.

[See embedded dashboard](/airbnbIndex.html)

<img src="images/airbnb_screenshot_UWS.png?raw=true"/>

---

### 1. Key assumptions

[a] Registration was already obtained from the city for short-term stays less than 30 days.

### 2. Data collection

[Inside Airbnb](https://insideairbnb.com) has fairly recent data sets for Airbnb by city.  Ultimately, I used 2 CSV files in this project.

### 3. Data cleansing / transformation

No data cleansing was done at this time.

### 4. Data exploration / analysis

**Exploration -** I weighed the fields available against the data points desired to determine a competitive price.

### 5. Dashboard design + Data storytelling

**Design -** I opted for a dark theme with Airbnb's bright coral pink color as the accent.

**Storytelling -** Location is paramount in real estate. Thus, I decided the dashboard would put maps front and center.  

**Finishing touches -** I embedded the Tableau dashboard on this Github site with some HTML and Javascript code, tweaking the height of the embedded dashboard to optimize viewing.

### 6. Iteration

To continue to enhance this dashboard, I propose the following:
- Parsing the 'Amenities' field to find commonalties amongst comparable properties.
- Running sentiment analysis on reviews to learn what may make one property more successful than others.

---

### References

[1] Datasets from [Inside Airbnb](https://insideairbnb.com/new-york-city/), found via Tableau's [blog post](https://www.tableau.com/blog/how-to-find-sources-for-public-data-sets) on public data sets
<br>[2] 
