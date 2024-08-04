# Air Quality Analysis

## Overview
This project aims to analyze air quality by exploring the relationship between PM2.5 (fine particulate matter) levels and the Air Quality Index (AQI). Utilizing statistical models, the project quantifies how changes in PM2.5 concentrations affect AQI values, offering insights into the potential health and environmental impacts.

## Key Findings
- **Strong Correlation**: Our analysis reveals a strong positive correlation (0.990) between PM2.5 and AQI, indicating that as PM2.5 increases, the AQI worsens, highlighting significant health risks.
- **Model Performance**: The regression model achieved a high \( R^2 \) score of 0.926, suggesting that 92.6% of the variance in AQI is predictable from PM2.5 levels.
- **Error Metrics**: The model’s Mean Squared Error (MSE) is 267.578, which means the model predictions are generally close to the actual data points.

## Technologies Used
- **Python**: For all computational and data processing tasks.
- **Jupyter Notebook**: To document and share the project workflow.
- **Libraries**: Pandas for data manipulation, Matplotlib and Seaborn for data visualization.

## Repository Structure
air_quality.ipynb   - Main project notebook containing the analysis.
data/               - Folder containing data files used in the analysis.
images/             - Generated plots and figures used in the analysis.
README.md           - Description and overview of the project.

## Installation
To set up a local development environment and run this notebook, follow these steps:
1. Clone the repository: git clone https://github.com/apkirana/air-quality-analysis.git
2. Install required Python packages: pip install pandas matplotlib seaborn notebook
3. Navigate to the project directory and start Jupyter Notebook:
   cd air-quality-analysis
   jupyter notebook

## Usage
Open the `air_quality.ipynb` notebook in Jupyter to view and run the analysis. Each cell in the notebook includes comments explaining the purpose of the code, making it easy to follow or adapt for related projects.

## Contributing
Contributions to enhance the analysis or improve the predictive models are welcome. Please fork the repository and submit a pull request with your changes.

## License
Distributed under the MIT License. See `LICENSE` for more information.

## Contact
- **Project Link**: [Air Quality Analysis on GitHub](https://github.com/apkirana/air-quality-analysis)
- **LinkedIn:** [Annisa Puspa Kirana](https://id.linkedin.com/in/annisapuspakirana/en)
- **Social Links:** [linktr.ee/puspakirana](http://linktr.ee/puspakirana)
