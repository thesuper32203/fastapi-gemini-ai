# FastAPI Gemini AI

A simple FastAPI project to demonstrate how to build an API server for an AI application using Gemini.

## Setting Up

**Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate
```

**Install dependencies**

```bash
pip install -r requirements.txt
```

**Set up API Key**

Create a `.env` file in the root of the project and add your Gemini API key:

```
GEMINI_API_KEY="your_gemini_api_key"
```

You can get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey).

The application will load this key from the `.env` file automatically.

## How To Run

To run the application, use the following command:

```bash
uvicorn src.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

### Via `curl`

You can send a request to the chat API using `curl`:

```bash
curl -X POST "http://127.0.0.1:8000/chat" \
     -H "Content-Type: application/json" \
     -d '{"prompt": "Why is the sky blue?"}'
```

### Via FastAPI Docs

You can also use the auto-generated FastAPI documentation to interact with the API.

Once the server is running, go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your browser.

## Configuration

You can configure the system prompt by editing the `src/prompts/system_prompt.md` file.

## Architecture

The project is structured to be modular, allowing for different AI platforms to be used.

- `src/main.py`: The main FastAPI application file.
- `src/ai/base.py`: Defines the `AIPlatform` interface.
- `src/ai/gemini.py`: The implementation of the `AIPlatform` interface for Gemini.
- `src/prompts/system_prompt.md`: The system prompt for the AI.

To use a different AI, you would create a new class that inherits from `AIPlatform` and implement the `chat` method. Then, you would update `src/main.py` to use your new AI class.
