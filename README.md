

# 🎓 Student Academic Performance Prediction

This project predicts **student academic performance (average exam score)** based on demographic and academic attributes such as gender, parental education, lunch type, and test preparation course.

It includes:

* 📊 **Data Analysis** of student performance dataset
* 🧠 **Machine Learning model** (scikit-learn pipeline) for prediction
* 🌐 **Interactive Web App** built with Streamlit

---

## 🚀 Features

✅ Predicts student’s average score out of 100
✅ Clean ML pipeline with preprocessing + model
✅ Streamlit app for user-friendly interaction
✅ Ready to deploy and showcase on resume/GitHub

---

## 📂 Project Structure

```
Student_Academic_Performance_Prediction/
│
├── app/
│   └── app.py                # Streamlit web application
│
├── models/
│   └── best_model.pkl        # Trained ML model
│
├── data/
│   └── StudentsPerformance.csv   # Dataset
│
├── notebooks/
│   └── Student_Performance_Analysis.ipynb  # Jupyter analysis
│
├── requirements.txt          # Project dependencies
├── train_model.ipynb         # Model training notebook
├── README.md                 # Project documentation
└── LICENSE
```

---

## ⚙️ Tech Stack

* **Python 3.12+**
* **Pandas, NumPy** – Data handling
* **scikit-learn** – Machine Learning
* **Joblib** – Model saving/loading
* **Streamlit** – Web application

---

## 📊 Dataset

The dataset `StudentsPerformance.csv` contains student details and scores in three subjects:

* Math
* Reading
* Writing

Target variable: **Average Score** (mean of three subject scores).

---

## ▶️ How to Run

### 1️⃣ Clone the repository

```bash
git clone https://github.com/safia-alam/Student_Academic_Performance_Prediction.git
cd Student_Academic_Performance_Prediction
```

### 2️⃣ Create & activate environment (recommended)

```bash
conda create -n student_pred python=3.12 -y
conda activate student_pred
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Streamlit app

```bash
streamlit run app/app.py
```

---

## 📸 Screenshots

🔹 **Input Form Example**
![App Screenshot](https://1drv.ms/i/c/46ea1d2de37f5e6f/Ef1pobELAMpGl2TmOJH0_e8Bj-RpHA1IAnw7N5K7kFpbTA?e=Ia9uZe)

---

## 🌟 Why This Project is Different?

Unlike basic ML projects that stop at a Jupyter Notebook, this project goes further by:

* ✅ Providing an **end-to-end solution** (data → model → web app)
* ✅ Packaging the ML model (`best_model.pkl`) for reuse
* ✅ Offering a professional **Streamlit UI** for real-time predictions
* ✅ Being **resume-ready** and deployment-ready

---

## 📌 Future Enhancements

* 🔮 Deploy on **Streamlit Cloud / Heroku**
* 📱 Add **visualizations** for better insights
* 🧑‍🎓 Include more features (attendance, study hours, etc.)

---

## 📝 Author

👩‍💻 **Safia Alam H B**

* 📧 Email: [shaiksafia24@outlook.com](mailto:shaiksafia24@outlook.com)
* 🌐 GitHub: [safia-alam](https://github.com/safia-alam)

---


