# 🧠 HealthAI: Intelligent Healthcare Assistant Using IBM Granite

HealthAI is an AI-powered healthcare assistant designed to provide users with accurate, empathetic, and data-driven medical insights. Built using Python, Streamlit, and IBM Watson Machine Learning (Granite 13B), HealthAI enables users to chat about symptoms, predict diseases, generate treatment plans, and view health analytics.

---

## 🚀 Features

- 💬 Patient Chat
- 🔍 Disease Prediction
- 💊 Treatment Plans
- 📊 Health Analytics

---

## 🏗 Project Architecture


Streamlit UI  →  Python Backend  →  IBM Granite AI (via API)


---

## 📁 Folder Structure


HealthAI/
├── app.py
├── utils.py
├── .env
├── requirements.txt
├── data/
└── venv/


---

## ⚙ Setup Instructions

### Prerequisites

- Python 3.8 or higher
- IBM Cloud account with Watson ML service
- Git
- Virtual environment (recommended)

### Installation

bash
git clone https://github.com/yourusername/HealthAI.git
cd HealthAI
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
pip install -r requirements.txt


---

### .env File

Create a file named .env in the root directory and add the following:

env
IBM_WATSON_ML_API_KEY="your_api_key"
IBM_WATSON_ML_URL="your_service_url"


---

## ▶ Running the App

bash
streamlit run app.py


---

## 🧪 Testing Strategy

- Unit Testing
- Integration Testing
- User Testing

---

## 🔮 Future Enhancements

- User authentication
- Real patient data
- Voice input
- Alerts for health metrics
- Mobile responsiveness

---

## 📜 License

MIT

---

## 🤝 Contributors

- Moparthi Charitha  
- Maram Navya  
- Manne Abhishek  
- Matta Prastuthi

---

## 🌐 Acknowledgements

- IBM Watson Machine Learning  
- Streamlit
