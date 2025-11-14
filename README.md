# 🍽️ Restaurant Name Generator
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

A fun and interactive Streamlit app that uses **LangChain** and the **OpenAI API** to generate creative restaurant names and custom menus — all with a single click.  
Just pick a cuisine and watch the app do the rest.

---

## 🚀 Features
- Choose from cuisines like **Indian**, **Italian**, **Mexican**, **Arabic**, or **American**
- Generates a **restaurant name** and matching **menu items**
- Clean, minimal UI built with **Streamlit**
- Powered by **LangChain** for LLM chaining and **OpenAI** for text generation

---

## 🧠 Tech Stack
- **Python 3.11+**
- **Streamlit** — front-end framework
- **LangChain** — orchestration layer for LLM logic
- **OpenAI API** — for generating restaurant names and menus

---


## ⚙️ Setup & Run Instructions

Follow these quick steps to get the app running locally 👇

1️⃣ Clone the repository
git clone https://github.com/NikithaSheerka/Restaurant_Name_Generator.git
cd Restaurant_Name_Generator

2️⃣ Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate      # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Add your OpenAI API key

Inside the app/ folder, create a file named Secret_key.py and add:

openapi_key = "sk-your-openai-api-key"

5️⃣ Run the Streamlit app
streamlit run app/main.py


Once it starts, open the local URL:
👉 http://localhost:8501

---

## 🖼️ Output Previews

Sidebar - Cuisine Selection
![Sidebar](https://github.com/NikithaSheerka/Restaurant_Name_Generator/blob/main/assets/screenshot_sidebar.png)

Generated Restaurant Name & Menu
![Home](https://github.com/NikithaSheerka/Restaurant_Name_Generator/blob/main/assets/screenshot_home.png)


## ✨ Future Enhancements

Add restaurant logo generation using DALL·E, Categorize menus (Starters, Mains, Desserts), Let users enter a custom cuisine name


## 🪪 License

This project is licensed under the MIT License
