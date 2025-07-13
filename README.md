# LangChain Google AI Example

This is a simple Python program that demonstrates how to use LangChain with Google's Generative AI (Gemini) to create a chatbot that explains things in simple terms.

## Prerequisites

- Python 3.8 or higher
- A Google AI Studio API key (get one at https://makersuite.google.com/app/apikey)

## Setup Instructions

### 1. Clone or Download the Project

Make sure you have these files in your project directory:
- `main.py`
- `requirements.txt`
- `.env` (you'll create this)

### 2. Create a Python Virtual Environment

```bash
# Create virtual environment
python3 -m venv langchain_env

# Activate virtual environment
# On Windows:
langchain_env\Scripts\activate

# On macOS/Linux:
source langchain_env/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in your project directory and add your Google API key:

```
GOOGLE_API_KEY=your_google_api_key_here
```

Replace `your_google_api_key_here` with your actual Google AI Studio API key.

### 5. Run the Program

```bash
python main.py
```

## What the Program Does

The program demonstrates two ways to interact with Google's Gemini AI model through LangChain:

1. **Simple Request**: Asks "What is LangChain?" directly
2. **System Prompt Request**: Uses a system message to make the AI explain things like it's talking to a five-year-old

## Expected Output

The program will show two responses:
- A standard explanation of LangChain
- A simplified, child-friendly explanation of LangChain

## Deactivating the Virtual Environment

When you're done, you can deactivate the virtual environment:

```bash
deactivate
```

## Troubleshooting

- **Import errors**: Make sure you're in the activated virtual environment and all dependencies are installed
- **API key errors**: Check that your `.env` file is in the correct location and contains the right API key
- **Model errors**: The program uses the "gemini-pro" model, which should be available with your Google AI Studio API key

## Dependencies

- `langchain`: Core LangChain library
- `langchain-google-genai`: Google Generative AI integration for LangChain
- `langchain-core`: Core LangChain components
- `python-dotenv`: For loading environment variables from .env file