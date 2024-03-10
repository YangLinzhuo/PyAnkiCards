import argparse
from utils import add_ancient_chinese_cards
from markdown import render_text


def main():
    """Main function
    """
    parser = argparse.ArgumentParser('Render markdown file and add to anki.')
    parser.add_argument('--file', type=str, required=True,
                        help="Path to markdown file to be rendered.")
    args = parser.parse_args()
    words, explanations, extras = render_text(args.file)
    print(words)
    print(explanations)
    print(extras)
    # result = add_ancient_chinese_card(words, explanations, extras)
    result = add_ancient_chinese_cards(words, explanations, extras)
    print(result)


if __name__ == "__main__":
    main()
