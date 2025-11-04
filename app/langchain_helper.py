import os
import re
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableMap
from app.Secret_key import openapi_key


# 🧹 Text Cleaning Utilities
def clean_text(text: str) -> str:
    """Removes quotes, smart quotes, and extra spaces from restaurant names."""
    cleaned = re.sub(r'^[\'"“”\s]+|[\'"“”\s]+$', '', text.strip())
    return cleaned.replace('"', '').replace('“', '').replace('”', '').strip()


def clean_menu(menu_text: str) -> list[str]:
    """Cleans, splits, and deduplicates menu items into a readable list."""
    raw_items = re.split(r'[\n,]+', menu_text)
    cleaned = []
    for item in raw_items:
        item = item.strip().lstrip("0123456789. ").strip()
        if item and item not in cleaned:
            cleaned.append(item)
    return cleaned



# 🔑 Setup OpenAI Model
os.environ["OPENAI_API_KEY"] = openapi_key
llm = OpenAI(temperature=0.6)


# 🍽️ Chain Logic
def generate_restaurant_name_and_items(cuisine: str) -> dict:
    """Generates a restaurant name and sample menu items for the given cuisine."""

    # Step 1: Define prompts
    name_prompt = PromptTemplate(
        input_variables=["cuisine"],
        template="I want to open a restaurant for {cuisine} food. Suggest a single fancy name for it — only return the name."
    )

    items_prompt = PromptTemplate(
        input_variables=["restaurant_name"],
        template="Suggest 10 menu items for {restaurant_name}. Return them as a comma-separated list."
    )

    # Step 2: Build chains
    name_chain = name_prompt | llm | StrOutputParser()
    menu_chain = (
        name_chain
        | (lambda name: {"restaurant_name": name})
        | items_prompt
        | llm
        | StrOutputParser()
    )

    # Step 3: Combine chains using RunnableMap
    chain = RunnableMap({
        "restaurant_name": name_chain,
        "menu_items": menu_chain
    })

    # Step 4: Invoke chain and clean results
    response = chain.invoke({"cuisine": cuisine})
    return {
        "restaurant_name": clean_text(response["restaurant_name"]),
        "menu_items": clean_menu(response["menu_items"])
    }
