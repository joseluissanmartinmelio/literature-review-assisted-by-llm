# Literature review with LLMs

## Description

This is an application whose purpose is to facilitate the review of large corpora of literature, especially in the social sciences. The process consists of extracting the text from a pdf, bypassing the text header (can be sensitized in the source code), integrating the text into a context window for some natural language model using the Openai package (openai and deepseek). The consigandos prompts have two functions, the first is to make a general summary of the text, incorporating the main theoretical arguments and the methodology used together with its main results, the second function is to extract the literature review of the text, obtaining a list of the authors cited and the main ideas associated with them.

## Technologies used

LLM: GPT-4o-mini; DeepSeek-V3

Libraries: PyMuPDF; Openai

## Installation

```bash
git clone https://github.com/joseluissanmartinmelio/literature-review-assisted-by-llm.git
cd literature-review-assisted-by-llm
# Recommended to create a virtual environment
pip install -r requirements.txt
```

## How to use

1. Place your PDF file in the desired folder (default: test/).
2. Make sure you have configured your prompt file in prompts/ (there are two prompts by default).
3. Run the main.py script:

```bash
python main.py
```

The script will do the following:

*1. Extract the main text from the PDF, ignoring headers.*

*2. Calculate word statistics (total, unique, most frequent).*

*3. Generate the required task to the LLM.*

*4. Recalculate statistics on the generated text.*

*5. Save the output in an .md file with the name of the author and year of the article.*

You can easily modify the prompt by changing the file in this line of code:

```python
prompt_path = "prompts/summarize_prompt.txt"
```

# TODO

1. Working on a simple interface
2. Establishing some metrics to measure performance with different open source and paid LLM models.
