# Market Opportunity & Consumer Behavior Analysis: Mexican Dining Sector

**Strategy & Operations | Market Intelligence | Consumer Segmentation**

A data-driven strategic analysis of the Mexican restaurant market, leveraging 10,000+ consumer data points to identify untapped market segments, optimize pricing strategies, and decode the drivers of customer satisfaction.

---

## ⚡ Executive Summary
- **Business Challenge:** New entrants to the Mexican dining market face high failure rates due to a lack of understanding of local consumer demographics and service expectations.
- **Solution:** Conducted a rigorous statistical analysis of consumer profiles, restaurant amenities, and rating interactions. Built an interactive Power BI dashboard ecosystem to visualize supply-demand gaps.
- **Key Finding:** There is a massive underserved market for **"Premium Non-Alcoholic"** dining experiences. While 67% of restaurants don't serve alcohol, the "Social Drinker" demographic is highly correlated with higher spending but unsatisfied with current service levels in budget establishments.

---

## 📊 Strategic Insights

### 1. The "Parking Premium" (Pricing Strategy)
*   **Insight:** A perfect correlation (100%) exists between "High Price" establishments and "dedicated parking/valet" availability.
*   **Recommendation:** For mid-tier restaurants looking to pivot to premium pricing, investing in parking logistics is a non-negotiable prerequisite, not just an add-on.

### 2. The "Sober & Satisfied" Paradox (Consumer Behavior)
*   **Insight:** Non-drinkers provided the highest volume of "Highly Satisfactory" ratings (303 distinct high ratings).
*   **Conclusion:** Alcohol is *not* the primary driver of satisfaction. Food quality and basic service hygiene are the dominant KPIs. A "Dry" restaurant model is statistically viable and potentially higher margin due to lower licensing/compliance costs.

### 3. Geographic Opportunity (Market Entry)
*   **Insight:** **Jiutepec** represents a "Blue Ocean" for health-conscious dining, with a 100% non-smoking consumer base.
*   **Recommendation:** Ideal launchpad for a family-oriented, smoke-free, wellness-focused dining brand.

---

## 🛠️ Methodology & Technical Approach

### Data Modeling (The "Backbone")
*   **Star Schema Design:** Constructed a relational model connecting `Consumers` (Dimension), `Restaurants` (Dimension), and `Ratings` (Fact).
*   **Normalization:** Cleaned redundant location data to ensure accurate geospatial analysis.

### Feature Engineering
*   **Segmentation:** Created dynamic bins for Age ("Young Adults", "Seniors") and Budget ("Low", "Medium", "High") to allow for granular cohort analysis.
*   **Sentiment Quantization:** Mapped 0-2 rating scales to qualitative buckets (Unsatisfactory -> Highly Satisfactory) for executive reporting.

---

## 📉 Dashboards & Deliverables

The project delivers a suite of executive dashboards designed for rapid decision-making:

1.  **The "Market Map" (Overview):** Heatmaps of restaurant density vs. consumer population.
2.  **The "Consumer Persona" (Demographics):** Deep dive into who is eating where (Students vs. Professionals).
3.  **The "Satisfaction Matrix" (Ratings):** Cross-referencing Service Quality with Amenities (WiFi, Parking, Alcohol).

*(See `/assets` folder for high-resolution exports)*

---

## 💻 Tech Stack
- **Analytics Engine:** Power BI (DAX, Power Query)
- **Data Processing:** Python (Pandas for initial cleaning), Excel
- **Data Viz:** Interactive Dashboards, Geo-Spatial Mapping

---
*"Deciphering the 'Why' behind every dining decision."*
