# Java Comment Generator 💬

A small Streamlit app we built for our 3rd semester mini project, that takes Java code and adds meaningful comments to it automatically, using an LLM through the Groq API.

The idea came from a pretty common problem: code without comments is annoying to read later, but writing comments by hand is hard and most will skip. This tool does the boring part for you — you upload or paste a `.java` file, hit generate, and get back the same code with explanations added, plus a quick breakdown of how many classes/methods it found.

## What it does

- Takes Java code as a file upload or pasted text
- Sends it to Llama 3.3 (via Groq) with a prompt that says "add comments only, don't touch the logic"
- Merges the generated comments back into the code
- Shows a simple analysis (line count, number of classes/methods) alongside the result
- Lets you download the commented file or save it locally

It's intentionally narrow in scope — it doesn't try to refactor, optimize, or translate the code, just document it.

## Project structure

app.py # Streamlit app - the UI
core/
comment_generator.py # calls the Groq API to generate comments
inserter.py # merges generated comments back into the original code
analyzer.py # basic structural stats (classes, methods, line count)
utils.py # file load/save helpers
.env # holds GROQ_API_KEY (not committed with a real key)
requirements.txt

## Running it locally

1. Install the dependencies:
   pip install -r requirements.txt
   
2. Grab a free API key from [Groq](https://console.groq.com) and drop it in a `.env` file:
   GROQ_API_KEY=your_api_key_here
   
4. Start the app:
   streamlit run app.py

## Notes / limitations

- Comment quality depends on the model's response, so results aren't perfect every time
- Needs an internet connection since it's calling an external API
- Larger files can be slower or occasionally get truncated by the model

## Why this exists

This was built as an academic project on AI-assisted software documentation — mainly to explore how well an LLM can understand code structure well enough to explain it, and to get hands-on practice wiring a Python backend up to a simple web UI. Sample Java files (`palindrome.java`, `primeOrNot.java`) are included in the repo for testing.

Possible next steps if I keep working on this: support for more languages, an offline/local model option, and maybe a VS Code extension instead of a standalone web app.
