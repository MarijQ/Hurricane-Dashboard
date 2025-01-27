# Hurricane Data Analytics and Visualization Dashboard

## Overview

This project leverages data analytics and visualization to gain deeper insights into hurricane and storm patterns over North America from 1975 to 2021. By combining advanced big data processing techniques, interactive dashboards, and statistical analysis, it provides meteorologists and policymakers with tools to better predict storm trajectories, classify storm types, and prepare for potential damages.

### Key Features
1. **High-Performance Data Processing (HPCI)**  
   - Utilized Hadoop and MapReduce to compute storm-related metrics, including relative kinetic energy (RKE).  
   - Processed 20k+ rows of NOAA storm data to assess storm-type damage potentials.  
   - Results revealed hierarchical averages: hurricanes overwhelmingly dominate with the highest energy levels.

2. **Interactive Visualization (DV)**  
   - Created an interactive Tableau & PowerBI dashboard to identify storm patterns over decades.  
   - Visualized trends like storm seasonality, clustering by damage potential, and trajectories of severe hurricanes.  
   - Integrated k-means clustering and multi-chart brushing for intuitive user feedback.

---

## Objectives
1. Analyze seasonal trends, storm trajectory evolution, and classification by damage potential.
2. Compute and validate Relative Kinetic Energy metrics for storm damage estimation.
3. Deliver both high-level dashboards and robust backend infrastructure for storm analytics.

---

## Dataset
NOAA Atlantic Hurricane Dataset (1975–2021):  
- ~20k rows of historical storm data.  
- Key attributes include storm name, year, wind speed, latitude/longitude, and storm diameter.

More details in the [NOAA Dataset](https://www.kaggle.com/datasets/utkarshx27/noaa-atlantic-hurricane-database).

---

## Technical Implementation

### 1. High-Performance Computational Infrastructure
- **Distributed Processing:**  
  Implemented a two-stage MapReduce pipeline:  
  1. Computing RKE for each event (log rows).  
  2. Aggregating storm/year metrics into status-wise categories.  

- **Output Examples:**  
   - Individual storm energies: `AL022006_2006_tropical storm -> 235,800,000.0`  
   - Status KE hierarchy: `hurricane -> 39,615,069,422.7`.

- **Results Visualization:**  
  Post-analytics showcased RKE through boxplots & barplots for storm classifications.

### 2. Data Visualization Dashboard
- **Tools Used:**  
  **Tableau & Power BI** for seamless high-level presentation.  

- **Key Dashboards:**  
  1. **Yearly Storm Frequencies:** Area chart trends from 1975–2021.  
  2. **Seasonality:** Heatmaps covered monthly patterns over decades.  
  3. **Clustering:** Scatter plots by wind/damage metrics using thresholds and k-means.  
  4. **Interactive Paths:** Maps + brushing for storm trajectory & wind trends (multivariate).

- **Technology Highlights**:  
  - Linked brushing for comparative analysis.  
  - Graphed clear axes, clustering metrics, & improved hue for visibility.

---

## Results & Key Insights

### 1. Findings on RKE (HPCI Module)
- Hurricanes exhibit the highest destructive potential.  
- Lower-category storms show predictable consistency.  
- Clustering revealed actionable outliers.

### 2. Storm Visualization (DV Module)
- Frequency trends: 5-decade upward trajectory.  
- Seasonality: Peaks observed in August–October.  
- Map trajectory + brushing: Enabled granular spatial-temporal analysis.

---

## Repository Structure
```plaintext
combined/
├── DV/
│   ├── data.csv
│   ├── PowerBI Project v1.pbix
│   ├── Tableau Project v1.twbx
├── HPCI/
│   ├── storms.csv
│   ├── mapper1.py
│   ├── reducer1.py
│   ├── mapper2.py
│   ├── reducer2.py
│   ├── output1a.txt
│   ├── output1b.txt
│   ├── run_file_2.sh
```

---

## How to Run

1. **Set up Hadoop:**
   - Deploy input files (`storms.csv`) to Hadoop Distributed File System (HDFS).  

2. **Run MapReduce:**
   - Bash script automates mapper/reducer executions.
     ```bash
     chmod +x run_file_2.sh
     ./run_file_2.sh
     ```  

3. **Explore Dashboard:**
   - Open Tableau or PowerBI projects to explore charts.

4. **Visualize and Analyze:**  
   - Python script (`full_analysis_3.py`) for additional data insights.  

---

## Future Improvements
- Leverage Apache Spark for real-time data processing.  
- Incorporate machine learning to enhance storm classification accuracy.  
- Extend the dataset to include global storm coverage.
