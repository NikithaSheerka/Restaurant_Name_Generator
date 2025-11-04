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

## 📂 Project Structure
```text
Restaurant_Name_Generator/
│
├── app/
│   ├── main.py                # Streamlit entry point (UI)
│   ├── langchain_helper.py    # LangChain + OpenAI logic
│
├── assets/                    # Screenshots for README
│   ├── screenshot_sidebar.png
│   ├── screenshot_home.png
│
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore


⚙️ Setup & Run Instructions

Follow these quick steps to get the app running locally 👇

1️⃣ Clone the repository
git clone https://github.com/NikithaSheerka/Restaurant_Name_Generator.git
cd Restaurant_Name_Generator

2️⃣ Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
# or
source venv/bin/activate   # Mac/Linux

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Add your OpenAI API key

Inside the app/ folder, create a file named Secret_key.py and add:

openapi_key = "sk-your-openai-api-key"

5️⃣ Run the Streamlit app
streamlit run app/main.py


Once it starts, open the local URL:
👉 http://localhost:8501

🎉 That’s it!
Select a cuisine from the sidebar and you’ll see a restaurant name and matching menu appear instantly.

## 🖼️ Output Previews

### Sidebar (Cuisine Selection)
<img src="https://raw.githubusercontent.com/NikithaSheerka/Restaurant_Name_Generator/main/assets/screenshot_sidebar.png" width="400"/>

### Generated Restaurant Name & Menu
<img src="https://raw.githubusercontent.com/NikithaSheerka/Restaurant_Name_Generator/main/assets/screenshot_home.png" width="600"/>




✨ Future Enhancements

Add restaurant logo generation using DALL·E
Categorize menus (Starters, Mains, Desserts)
Export menus as PDF
Let users enter a custom cuisine name

👩‍💻 Author

Sai Nikitha Sheerka
Seattle, WA 🌧️

🪪 License

This project is licensed under the MIT License — see the LICENSE
 file for details.