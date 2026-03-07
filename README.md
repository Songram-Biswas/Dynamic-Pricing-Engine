This portion is for streamlit Version
💰 Dynamic Pricing Engine - End-to-End MLOps Project
📌 Project Overview
The Dynamic Pricing Engine is a comprehensive Machine Learning solution designed to predict the optimal price of products in an e-commerce ecosystem. By analyzing product features (weight, volume, category) and order context (review scores, delivery delays, seasonality), the engine provides data-driven pricing suggestions to maximize business efficiency while maintaining customer satisfaction.

🚀 Key Features
Real-time Inference: Interactive web interface for instant price prediction.

Modular Architecture: Industry-standard project structure for scalability and maintainability.

Automated Pipelines: Separate pipelines for Data Ingestion, Transformation, and Model Training.

MLOps Integration: Robust logging, exception handling, and model versioning.

Cross-Platform Compatibility: Designed to work seamlessly across Windows and Linux (Cloud) environments.

🛠️ Tech Stack
Language: Python 3.10

Machine Learning: XGBoost, Scikit-learn

Data Handling: Pandas, Numpy

Frontend: Streamlit

Utilities: Dill, PyYAML, from-root

Version Control: Git & Git LFS (Large File Storage)

Deployment: Streamlit Cloud

📁 Project Structure
Plaintext
├── artifact/              # Serialized models and preprocessor pickles
├── notebook/              # Exploratory Data Analysis (EDA) and datasets
├── src/
│   └── pricing_engine/    # Core Modular Source Code
│       ├── components/    # Data Ingestion, Transformation, Model Trainer
│       ├── pipeline/      # Training & Prediction Pipelines
│       ├── utils/         # Common utility functions (IO, Logging)
│       ├── logger/        # Custom logging module
│       └── exception/     # Custom exception handling
├── app.py                 # Streamlit Web Application
├── requirements.txt       # Project dependencies
├── setup.py               # Package configuration for editable install
└── pyproject.toml         # Build system requirements
⚙️ Installation & Setup
Clone the repository:

Bash
git clone https://github.com/Songram-Biswas/Dynamic-Pricing-Engine.git
cd Dynamic-Pricing-Engine
Create a virtual environment:

Bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

Bash
pip install -r requirements.txt
pip install -e .
Run the Streamlit application:

Bash
streamlit run app.py
🧠 Machine Learning Workflow
Data Ingestion: Automatically retrieves raw data from the storage.

Data Transformation: Handles missing values, encodes categorical features, and scales numerical data using a preprocessor pipeline.

Model Training: Utilizes advanced gradient boosting (XGBoost) to train on historical pricing data.

Prediction: Converts user input into a dataframe and passes it through the pre-trained transformation and prediction pipeline.

📊 Business Impact
Setting the right price is critical for e-commerce success. This engine considers Customer Review Scores and Order Status, ensuring that prices are not only competitive but also aligned with the quality of service provided, helping sellers optimize their revenue strategy.

Developed by Songram Biswas Computer Science & Engineering Student | ML & MLOps Enthusiast
