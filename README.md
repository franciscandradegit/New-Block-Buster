🎬 Can We Predict Movie Success?

A Machine Learning Analysis of Budget, Runtime, and Popularity

⸻

📌 Project Overview

This project explores whether key movie attributes such as runtime, budget, and director influence can predict movie success (e.g. popularity or revenue).

We tested multiple hypotheses using machine learning models to evaluate how well these factors explain movie performance.

⸻

🎯 Hypotheses
	•	H1: Films with larger production budgets generate higher box office revenue
	•	H2: The choice of director significantly influences production budget
	•	H3: Films with longer runtimes tend to have lower popularity

⸻

🧠 Approach

We followed a structured ML workflow:
	1.	Data cleaning and preprocessing
	2.	Feature selection and scaling
	3.	Model training (Linear Regression, KNN, Random Forest)
	4.	Hyperparameter tuning using GridSearchCV
	5.	Model evaluation using R² and MSE

⸻

📊 Key Findings
	•	Overall, models showed low predictive power (low R²)
	•	Runtime and budget alone are weak predictors of success
	•	Hyperparameter tuning improved performance, but only slightly
	•	Simpler models (Linear Regression) often performed as well as or better than complex ones

👉 This suggests that missing features (e.g. genre, cast, marketing) are likely more important drivers of success

⸻

🗂️ Project Structure

New-Block-Buster/
│
├── data/
│   ├── raw/          # Original, unprocessed datasets
│   ├── clean/        # Cleaned and feature-engineered datasets
│   └── notebooks/    # Data cleaning notebooks for each hypothesis
│
├── notebooks/        # Modeling, training, and ML experiments
│
├── figures/          # Visualizations, plots, and charts
│
├── config.yaml       # Project configuration (optional)
├── pyproject.toml    # Project dependencies
├── uv.lock           # Dependency lock file
├── main.py           # Entry point (if used)
└── README.md

⚙️ Models Used
	•	Linear Regression → baseline model
	•	K-Nearest Neighbors (KNN) → non-linear relationships
	•	Random Forest → ensemble model for complex patterns

⸻

🔧 Evaluation
	•	R² Score → explanatory power
	•	MSE (Mean Squared Error) → prediction accuracy

We also used:
	•	Train/Test split
	•	Cross-validation (GridSearchCV) for tuning

⸻

🚀 Future Improvements
	•	Include richer features (genre, cast, marketing, release timing)
	•	Apply more advanced feature engineering
	•	Use larger and more diverse datasets

⸻

🔗 Project Resources

We organized our workflow and tracked progress using Trello, and created a final presentation summarizing our approach and results:
	•	Trello Board (project management): https://trello.com/b/VfQa1se2/new-blockbuster
	•	Presentation Slides: https://canva.link/4711hy9ipa6h2p7

⸻


👥 Team

Project developed collaboratively as part of a Machine Learning project.