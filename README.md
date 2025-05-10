

# 🍳 AI recipe generator using OpenAI API

This tutorial walks you through creating a simple AI-powered recipe generator using Python and the OpenAI API. You'll input the name of a dish, and the app will return a detailed recipe including ingredients and preparation steps.


## Features

- Uses OpenAI GPT models (GPT-4o or GPT-3.5-Turbo)
- Returns organized, chef-quality recipes


##  Prerequisites

Before getting started, make sure you have:

- A code editor like [VS Code](https://code.visualstudio.com/)
- [Python](https://www.python.org) version 3.8 or higher
- `pip` (Python package manager)
- An [OpenAI account](https://platform.openai.com/signup) with an API key
- Internet connection


## Installation

### 1. Clone the repository

Download the files from GitHub or use this command:

`
git clone https://github.com/yourusername/recipe-generator.git
cd recipe-generator`


### 2. Install dependencies

Open up your terminal and run the following commands:

- `pip install openai` to install the OpenAI Python library
- `pip install python-dotenv` to install the python-dotenv package

**Note**: If using Python 3, use pip3 instead, for example, `pip3 install openai python-dotenv`.

### 3. Set up your API key:

- Open the file and type: OPENAI_API_KEY=your_api_key_here
- Replace "your_api_key_here" with your actual OpenAI API key
- Save the file

### 4. Creating recipe generator

- In the terminal run `python recipe.py` to generate the recipe. 

## File Overview

`recipe.py` — Main Python script to generate recipes.

`.env` — Stores your OpenAI API key (not tracked by Git).

## Example Prompt

`“Show me the ingredients, recipe, and preparation method of this dish: Chakalaka. Organize your answer in clear and concise bullet points.”`















