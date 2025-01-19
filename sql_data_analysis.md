## SQL Data Analysis

**Project Overview:** Developed a data-driven pricing strategy for a luxury Airbnb apartment in New York City to maximize profitability.

**Key Accomplishments:**
- Leveraged Tableau to create an interactive dashboard using Inside Airbnb data, enabling efficient analysis of market trends and competitor pricing.
- Conducted comparative analysis to determine an optimal initial price point of $500/night for a 2BR/2BA apartment in the Upper West Side, undercutting average competitor prices by $50.
- Proposed a strategic price increase to $550-$600 after establishing a strong rating (4.7+), positioning the property as a premium offering.
- Integrated the Tableau dashboard into a GitHub-hosted website using HTML and JavaScript, demonstrating full-stack capabilities.

**Technical Skills Demonstrated:**
- Data Analysis: Market research, competitive pricing analysis
- Data Visualization: Tableau dashboard creation with custom filters and map integration
- Web Development: HTML, JavaScript for dashboard embedding
- Strategic Thinking: Luxury pricing strategy development

**Future Enhancements:**
- Amenities analysis to identify key differentiators
- Sentiment analysis of reviews to uncover success factors

**Impact:** This project showcases the ability to transform raw data into actionable business strategies, combining analytical skills with market insights to drive profitability in the competitive short-term rental market.

---

### SQL Queries

```
SELECT YEAR(so.ModifiedDate) AS Year, ps.Name AS ProductCategory, SUM(LineTotal) AS SalesTotal
FROM [Sales].SalesOrderDetail AS so
JOIN Production.Product AS p
ON so.ProductID = p.ProductID
JOIN Production.ProductSubcategory AS ps
ON p.ProductSubcategoryID = ps.ProductSubcategoryID
GROUP BY YEAR(so.ModifiedDate), ps.Name
ORDER BY Year DESC, SalesTotal DESC;
```

---

### References

[1] Datasets from [Inside Airbnb](https://insideairbnb.com/new-york-city/), found via Tableau's [blog post](https://www.tableau.com/blog/how-to-find-sources-for-public-data-sets) on public data sets
