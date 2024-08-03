import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
#run this if doesn work in terminal
#pip install pandas numpy matplotlib seaborn scikit-learn

# Load the dataset
data = pd.read_csv('data/raw/global_air_pollution_data.csv')

# Display the first few rows
print(data.head())

# Display basic information about the dataset
print(data.info())

# Check for missing values
print(data.isnull().sum())

# Summary statistics
print(data.describe())

# Handling missing values (example: filling missing values with mean)
data.fillna(data.mean(), inplace=True)

# Remove duplicates
data.drop_duplicates(inplace=True)

# Convert data types if necessary
data['date'] = pd.to_datetime(data['date'])

# Correlation matrix
plt.figure(figsize=(12, 8))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Distribution of a specific pollutant (e.g., PM2.5)
plt.figure(figsize=(10, 6))
sns.histplot(data['pm2.5'], kde=True)
plt.title('Distribution of PM2.5')
plt.show()

# Time series analysis of pollutants
plt.figure(figsize=(14, 8))
data.groupby('date')['pm2.5'].mean().plot()
plt.title('Time Series of PM2.5')
plt.xlabel('Date')
plt.ylabel('PM2.5 Concentration')
plt.show()

# Boxplot to see the distribution of pollutants by country
plt.figure(figsize=(14, 8))
sns.boxplot(x='country', y='pm2.5', data=data)
plt.title('PM2.5 Concentration by Country')
plt.xticks(rotation=90)
plt.show()

# Prepare the data for modeling
features = data[['temperature', 'humidity', 'wind_speed']]  # Example features
target = data['pm2.5']  # Target variable

# Split the data
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Initialize and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
print(f'R^2 Score: {r2}')