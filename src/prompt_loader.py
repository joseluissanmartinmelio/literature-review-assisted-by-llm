def load_prompt(file_path: str, context: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as f:
        template = f.read()
    return template.replace("{context}", context)