## A Snapshot of NYC Dogs

**Project description:** This project taps into my curiosity about all the dogs that call New York City (NYC) home. What kind of dogs are they?  Where do they live?  Where do they play?  Data cleansing was done in Power Query and data visualization in Power BI.

### 1. Data collection

Thanks to NYC Open Data's mission to have 'open data for all', it was simple to procure datasets on NYC dog licenses, dog parks, dog waste receptacles and--most surprising of all--squirrels.  I sourced images from Google searches and created a color palette for the data visualizations inspired by the images.

Find dataset on zip codes and neighborhoods/boroughs

### 2. Data cleansing / transformation

NYC Open Data's datasets are largely ready-to-consume; however, I did have to cleanse the dog license dataset of invalid values in the [AnimalBirthYear] column and switch [ZipCode] data type to text to prevent aggregation. 

Missing data in dog license dataset - unknown names/breeds
Missing data in dog runs dataset - surface

### 3. Data exploration / analysis to form hypotheses

```javascript
if (isAwesome){
  return true
}
```

### 4. Data storytelling with visualizations

<img src="images/dummy_thumbnail.jpg?raw=true"/>

### 5. Provide a basis for further data collection

Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. 

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

---

### References

[1] Datasets from [NYC Open Data](https://opendata.cityofnewyork.us/)
<br>[2] Images: cover (https://graymalin.com/products/picnic-party-central-park), winter oil painting (https://www.etsy.com/listing/1669834351/dogs-central-park-play-oil-painting), Bethesda Fountain (https://www.etsy.com/listing/257851858/central-park-bethesda-terrace-with-dog), fall (https://www.pinterest.com/pin/me-and-my-dog-in-central-park-nyc-illustration-by-iamlaurael--791226228295682665/), cartoon (https://www.shutterstock.com/image-vector/morning-city-park-happy-family-having-1566026362)
