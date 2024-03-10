import json
from urllib import request


URL = "http://127.0.0.1"    # URL to connect anki.
PORT = 8765                 # Port to connect anki.


def invoke(cmd_dict: dict):
    """Invoke command through AnkiConnect plugin

    Args:
        cmd_dict (dict): Dictionary contains params and corresponding values.

    Raises:
        TypeError: Response has an unexpected number of fields
        TypeError: Response is missing required error field.
        TypeError: Response is missing required result field.
        ConnectionError: Error raised during anki connection.

    Returns:
        result: Response result from anki.
                See 'https://git.foosoft.net/alex/anki-connect' for details.
    """
    request_json = json.dumps(cmd_dict).encode('utf-8')
    request_url = request.Request(f'{URL}:{PORT}', request_json)
    with request.urlopen(request_url) as session:
        response = json.load(session)
    if len(response) != 2:
        raise TypeError("Response has an unexpected number of fields.")
    if 'error' not in response:
        raise TypeError('Response is missing required error field.')
    if 'result' not in response:
        raise TypeError('Response is missing required result field.')
    if response['error'] is not None:
        raise ConnectionError(response['error'])
    result = response['result']
    return result


def get_deck_template(model_name: str):
    """Get template of specified deck.
    Args:
        model_name (str): Name of the deck.
    Returns:
        result (str): Template string of the deck.
    """
    cmd = {
        "action": "modelTemplates",
        "version": 6,
        "params": {
            "modelName": model_name
        }
    }
    result = invoke(cmd)
    return result


def get_decks():
    """Get deck list string.

    Returns:
        result (str): String of decks names
    """
    result = invoke('deckNames')
    return result


def add_ancient_chinese_card(word: str, explanation: str, extra: str):
    """Add card to ancient Chinese deck.

    Args:
        word (str): word in ancient Chinese
        explanation (str): meaning of the word
        extra (str): extra explanation of comparison of different words

    Returns:
        result: response result of the action
    """
    cmd = {
        "action": "addNote",
        "version": 6,
        "params": {
            "note": {
                "deckName": "古代汉语::常用词",
                "modelName": "古代汉语-常用词",
                "fields": {
                    "Word": f"{word}",
                    "文字": f"{explanation}",
                    "背面额外": f"{extra}"
                },
                "options": {
                    "allowDuplicate": False,
                    "duplicateScope": "deck",
                    "duplicateScopeOptions": {
                        "deckName": "Default",
                        "checkChildren": False,
                        "checkAllModels": False
                    }
                },
                "tags": [
                    "古代漢語",
                    "常用詞",
                ]
            }
        }
    }
    result = invoke(cmd)
    return result

def add_ancient_chinese_cards(words: list[str], explanations: list[str], extras: list[str]):
    """Add card to ancient Chinese deck.

    Args:
        words (list[str]): a list word in ancient Chinese
        explanations (list[str]): a list meaning of the word
        extras (list[str]): a list extra explanation of comparison of different words

    Returns:
        result: response result of the action
    """
    cmd = {
        "action": "addNotes",
        "version": 6,
        "params": {
            "notes": [
                {
                    "deckName": "古代汉语::常用词",
                    "modelName": "古代汉语-常用词",
                    "fields": {
                        "Word": f"{word}",
                        "文字": f"{explanation}",
                        "背面额外": f"{extra}"
                    },
                    "options": {
                        "allowDuplicate": False,
                        "duplicateScope": "deck",
                        "duplicateScopeOptions": {
                            "deckName": "Default",
                            "checkChildren": False,
                            "checkAllModels": False
                        }
                    },
                    "tags": [
                        "古代漢語",
                        "常用詞",
                    ]
                }
                for word, explanation, extra in zip(words, explanations, extras)
            ]
        }
    }
    result = invoke(cmd)
    return result
