# 🦴 KOA Detector — Gen-AI Multimodal Prediction and Prescriptive Care for Knee Osteoarthritis Progression

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-3.0.3-lightgrey)
![EfficientNet](https://img.shields.io/badge/Model-EfficientNet--B0-orange)
![IEEE](https://img.shields.io/badge/Published-IEEE%20ICOIICS%202025-green)
![CVR](https://img.shields.io/badge/Accepted-CVR%202026-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

> An AI-powered web application for detecting and predicting Knee Osteoarthritis (KOA) progression using multimodal data — X-ray imaging and clinical patient data — with personalized prescriptive care recommendations.

---

## 🌐 Live Demo
🔗 **[Click here to view the live prototype](https://koa-detector-2.onrender.com/)**

---

## 📌 Table of Contents
- [About the Project](#about-the-project)
- [Key Features](#key-features)
- [System Architecture](#system-architecture)
- [Tech Stack](#tech-stack)
- [Modules](#modules)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Publication Status](#publication-status)
- [Team](#team)

---

## 📖 About the Project

Knee Osteoarthritis (KOA) is one of the leading causes of chronic pain,
disability, and reduced quality of life in aging populations. Current
diagnostic and treatment approaches remain **reactive and symptom-focused**,
while existing machine learning solutions struggle to:

- Integrate multimodal data (images + clinical records)
- Capture temporal disease progression
- Provide personalized recommendations

### Our Solution:
A **Generative AI-based multimodal framework** that:
- Detects KOA grade from X-ray images using **EfficientNet-B0**
- Predicts disease progression using **Neural Network Regression**
- Provides **"What-If" lifestyle simulation** to show patients how
  lifestyle changes delay disease progression

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🩻 X-ray Analysis | KOA grade detection (Grade 0-4) using EfficientNet-B0 |
| 📊 Progression Prediction | Estimates months to next KOA stage |
| ⚙️ Lifestyle Simulator | Shows impact of exercise and BMI on progression |
| 📈 Analytics Dashboard | Dataset distribution and model performance charts |
| 🎯 Risk Classification | Low / Moderate / High / Very High risk levels |
| 💊 Prescriptive Care | Personalized actionable recommendations |

---

## 🏗️ System Architecture
```
INPUT LAYER          DATA PROCESSING        MULTIMODAL FUSION      OUTPUT LAYER
─────────────        ───────────────        ─────────────────      ────────────
X-ray Image    →     Image Preprocessing →                    →    Risk Level
                     EfficientNet-B0     →  Combined Feature  →    KOA Grade
                     KOA Grade Pred.     →  Vector            →    Progression
Clinical Data  →     Data Preprocessing →                    →    Time
                     Normalization       →                    →    Lifestyle
                                                                   Simulation
```

---

## 🛠️ Tech Stack

### Prototype (This Repository)
| Layer | Technology |
|---|---|
| Frontend | HTML5, CSS3, JavaScript |
| Backend | Python, Flask |
| Deployment | Render.com |
| Version Control | GitHub |

### Actual Research Project
| Layer | Technology |
|---|---|
| Deep Learning | PyTorch, EfficientNet-B0 |
| Image Processing | OpenCV, PIL |
| Data Processing | Pandas, NumPy, Scikit-learn |
| Visualization | Matplotlib, Seaborn |
| Augmentation | MixUp, Random Erasing, Color Jitter |

---

## 📦 Modules

### 1. Offline Data Augmentation
- Applied to Grade-4 class to fix class imbalance
- Techniques: Rotation (±10°), Horizontal Flip,
  Brightness Adjustment, Zoom Scaling (0.9–1.1)
- Increased Grade-4 samples to 800 images

### 2. Data Preprocessing (X-ray)
- Grayscale to 3-channel conversion
- ImageNet normalization
- Random Erasing, Affine Transformation
- PyTorch DataLoader (80% train / 20% test)

### 3. EfficientNet-B0 Training
- Pretrained on ImageNet
- Custom classifier: Dropout(0.6) + FC(5 outputs)
- AdamW optimizer + ReduceLROnPlateau scheduler
- CrossEntropy Loss with Label Smoothing
- Early Stopping + Model Checkpointing
- MixUp Augmentation during training

### 4. Data Preprocessing (Clinical Dataset)
- Removed non-informative identifiers
- StandardScaler normalization
- 80/20 train-test split
- Converted to PyTorch tensors

### 5. Progression Prediction & Analysis
- Neural Network Regression (Input→64→32→Output)
- Predicts progression score (0–1)
- Converts score to estimated months
- Lifestyle Impact Analysis (Exercise, BMI, Walking)

---

## ⚙️ Installation

### Prerequisites
- Python 3.11+
- pip

### Steps

**1. Clone the repository**
```bash
git clone https://github.com/yourusername/koa-detector.git
cd koa-detector
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the application**
```bash
python app.py
```

**4. Open in browser**
```
http://localhost:5000
```

---

## 🚀 Usage

### Demo Flow:
```
1. Home Page      → Click "Start Analysis"
2. Input Page     → Enter patient details + upload X-ray
3. Click          → "Run AI Analysis"
4. Diagnosis Page → View KOA Grade, Risk, Health Score
5. Analytics Page → View dataset charts and model comparison
6. Simulator Page → Adjust lifestyle sliders → See improvement
```

### Sample Test Values:

| Grade | Age | BMI | Pain | Stiffness | Expected Result |
|---|---|---|---|---|---|
| Grade 0 | 25 | 20 | 1 | 1 | Normal, Low Risk |
| Grade 1 | 35 | 22 | 3 | 3 | Doubtful OA, Low Risk |
| Grade 2 | 45 | 26 | 5 | 5 | Mild OA, Moderate Risk |
| Grade 3 | 55 | 28 | 7 | 6 | Moderate OA, High Risk |
| Grade 4 | 65 | 32 | 9 | 8 | Severe OA, Very High Risk |

---

## 📊 Results

| Metric | ResNet-18 | EfficientNet-B0 |
|---|---|---|
| Validation Accuracy | ~61% | ~73% |
| Parameters | 11.7M | 5.3M |
| Training Speed | Faster | Slightly Slower |
| Medical Imaging | Good Baseline | Better ✅ |

### Why EfficientNet-B0?
EfficientNet uses **compound scaling** to balance network depth,
width, and resolution — making it ideal for detecting subtle
structural changes in knee X-rays.

---



## 👥 Team

| Name | Role | College |
|---|---|---|
| **Harshida KS** |Frontend Developer | Saveetha Engineering College |
| **Tharshini M** | Backend Developer |Saveetha Engineering College |
| **Rubasri R** | AI/ML Engineer | Saveetha Engineering College |



---

## 🌱 SDG Alignment

- **SDG 3** — Good Health and Well-being
- **SDG 9** — Industry, Innovation and Infrastructure
- **SDG 10** — Reduced Inequalities

---

## 📚 References

1. T. Tariq et al., "Knee osteoarthritis detection and classification
   using X-rays," IEEE Access, vol. 11, 2023.
2. A. Hussain et al., "Automated chest X-ray analysis using deep
   ensemble strategy," IEEE Access, vol. 11, 2023.
3. M. Zargoush et al., "ML-driven diabetes care using
   predictive-prescriptive analytics," Scientific Reports, vol. 15, 2025.

---



---

<p align="center">
  Made  by Team TrioTech <br/>
  Saveetha Engineering College
</p>
