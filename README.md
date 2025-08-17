HEAD
# Student Academic Performance Prediction

End-to-end ML project to predict student academic performance (exam scores) using demographic and academic factors.
Includes EDA, feature engineering, model comparison, hyperparameter tuning, and a Streamlit app for live predictions.

## ✨ Highlights
- Clean EDA with visualizations (Matplotlib)
- Feature engineering (e.g., `average_score`, pass/fail label)
- Models compared: Linear Regression, Random Forest, Gradient Boosting
- Hyperparameter tuning with `RandomizedSearchCV`
- Persisted pipeline (`models/best_model.pkl`)
- **Streamlit app** for interactive predictions (`app/app.py`)

## 🗂️ Repository Structure
```
Student_Academic_Performance_Prediction/
├── app/
│   └── app.py                # Streamlit web app
├── data/
│   ├── .gitkeep              # Place dataset here as StudentsPerformance.csv
├── models/
│   └── .gitkeep              # Trained model artifacts will be saved here
├── notebooks/
│   └── Student_Performance_Analysis.ipynb   # Full end-to-end notebook
├── LICENSE
├── README.md
└── requirements.txt
```

## 📦 Dataset
Use the **StudentsPerformance** dataset (commonly available on Kaggle).  
Place the CSV at:
```
data/StudentsPerformance.csv
```
Expected columns include (typical Kaggle version):
- `gender`, `race/ethnicity`, `parental level of education`, `lunch`, `test preparation course`,
- `math score` (or `math_score` / `math_score` variants), `reading score`, `writing score`.

> ⚠️ Column names vary across sources. The notebook includes a flexible loader that tries common variants and raises a clear message if not found. Update the mapping in the notebook if your column names differ.

## ▶️ Quickstart (Local)
1. Create and activate a virtual environment
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   ```
2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
3. Add the dataset at `data/StudentsPerformance.csv`.
4. Run the notebook (recommended first run)
   ```bash
   jupyter notebook notebooks/Student_Performance_Analysis.ipynb
   ```
5. Train and save the model (the notebook saves to `models/`).
6. Launch the app
   ```bash
   streamlit run app/app.py
   ```

## 🧠 Resume Bullet (Sample)
- Implemented and enhanced a machine learning model to predict student performance using demographic and academic factors; engineered features like `average_score` and tuned Random Forest & Gradient Boosting models to achieve strong **R²** performance. Built an interactive **Streamlit** app for real‑time predictions.

## 📝 Notes
- This project is **inspired by open-source work** and significantly extended with feature engineering, model comparison, tuning, and deployment. Always be transparent in your resume: explain your unique contributions.
- For reproducibility, set the random seed and note versions in `requirements.txt`.

## 📄 License
MIT
# Student_Academic_Performance_Prediction
Predicting student performance using Machine Learning and Streamlit.4ce5c1f67e8f5276da83f908af9c1d91a81773bb
