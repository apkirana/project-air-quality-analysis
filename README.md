# Air Quality Analysis

## Overview
This project aims to analyze air quality by exploring the relationship between PM2.5 (fine particulate matter) levels and the Air Quality Index (AQI). Utilizing statistical models, the project quantifies how changes in PM2.5 concentrations affect AQI values, offering insights into the potential health and environmental impacts.

## Presentation
[Presentation Link](https://docs.google.com/presentation/d/e/2PACX-1vQJCGNjdOgIsuFKvBb-by847hFUxXAchbm2nSbBkQob0Ce5wO24Tqpdp183IQejpzOOOWBa3_uTLk_n/pub?start=true&loop=false&delayms=3000)

## Demo

![Demo Animation](https://github.com/apkirana/project-air-quality-analysis/blob/main/demo-airquality-analysis.gif)

This GIF demonstrates how the application works.


## Key Findings
- **Strong Correlation**: Our analysis reveals a strong positive correlation (0.990) between PM2.5 and AQI, indicating that as PM2.5 increases, the AQI worsens, highlighting significant health risks.
- **Model Performance**: The regression model achieved a high \( R^2 \) score of 0.926, suggesting that 92.6% of the variance in AQI is predictable from PM2.5 levels.
- **Error Metrics**: The model’s Mean Squared Error (MSE) is 267.578, which means the model predictions are generally close to the actual data points.

## Technologies Used
- **Python**: For all computational and data processing tasks.
- **Jupyter Notebook**: To document and share the project workflow.
- **Libraries**: Pandas for data manipulation, Matplotlib and Seaborn for data visualization.

## Repository Structure

```text
air_quality.ipynb   - Main project notebook containing the analysis.
data/               - Folder containing data files used in the analysis.
images/             - Generated plots and figures used in the analysis.
README.md           - Description and overview of the project.
```

## Installation
To set up a local development environment and run this notebook, follow these steps:
```bash
git clone https://github.com/apkirana/project-air-quality-analysis.git
cd project-air-quality-analysis
pip install -r requirements.txt
jupyter notebook
```

## Usage
Open the `air_quality.ipynb` notebook in Jupyter to view and run the analysis. Each cell in the notebook includes comments explaining the purpose of the code, making it easy to follow or adapt for related projects.

## Contributing
Contributions to enhance the analysis or improve the predictive models are welcome. Please fork the repository and submit a pull request with your changes.

## License
Distributed under the MIT License. See `LICENSE` for more information.

---

## Author

**Annisa Puspa Kirana** — PhD researcher, Faculty of Geo-Information Science and Earth Observation (ITC),
University of Twente. Research on agentic AI and LLM-driven workflows for Earth observation.

[Google Scholar](https://scholar.google.com/citations?user=BQl6KOsAAAAJ&hl=en) ·
[ORCID](https://orcid.org/0000-0002-4622-1445) ·
[LinkedIn](https://www.linkedin.com/in/annisapuspakirana) ·
[GitHub](https://github.com/apkirana)
