from markdown_it import MarkdownIt


md = MarkdownIt()   # markdown-it class


"""
<h1>字1</h1>
...
...
<h2>额外</h2>
...
...
<h1>字2</h1>
...
...
<h2>额外</h2>
"""

def _ancient_chinese_render(md_text: str) -> tuple[list[str], list[str], list[str]]:
    contents = md_text.split('<h1>')
    words = []
    explanations = []
    extras = []
    for content in contents:
        if not content:
            continue
        split_contents = content.split('</h1>')
        words.append(split_contents[0].strip())
        remained = split_contents[1]
        split_contents = remained.split('<h2>')
        explanations.append(split_contents[0].strip())
        remained = split_contents[1]
        split_contents = remained.split('</h2>')
        extras.append(split_contents[1].strip())
    return words, explanations, extras


def render_text(file_path: str) -> tuple[list[str], list[str], list[str]]:
    """Render markdown file to html format.

    Args:
        file_path (str): Path to markdown file.

    Returns:
        tuple[list[str], list[str], list[str]]: Rendered result.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        md_text = file.read()

    text_rendered = md.render(md_text)
    words, explanations, extras = _ancient_chinese_render(text_rendered)
    return words, explanations, extras
