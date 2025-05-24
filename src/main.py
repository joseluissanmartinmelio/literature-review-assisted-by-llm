from pdf_reader import extract_text_without_footer_header
from word_stats import count_words
from ai_module import ai_assistant
from utils import save_to_file
from prompt_loader import load_prompt
import os

if __name__ == "__main__":
    pdf_path = ""
    author_year = ""
    output_path = f"{author_year}.md"
    prompt_path = "prompts/summarize_prompt.txt"

    text = extract_text_without_footer_header(pdf_path)
    print("\nExtracted Text\n")
    print(text)

    stats = count_words(text)
    print("\nText Statistics")
    print(f"Total words: {stats['total']}")
    print(f"Unique words: {stats['unique']}")
    print("Most common words:")
    for word, count in stats['most_common']:
        print(f"  {word}: {count}")

    prompt = load_prompt(prompt_path, text)

    response = ai_assistant(prompt)
    print("\nAI Response\n")
    print(response)

    stats_response = count_words(response)
    print("\nResponse Statistics")
    print(f"Total words: {stats_response['total']}")
    print(f"Unique words: {stats_response['unique']}")
    print("Most common words:")
    for word, count in stats_response['most_common']:
        print(f"  {word}: {count}")

    save_to_file(response, output_path)

