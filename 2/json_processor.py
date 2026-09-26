from typing import Any, Callable
import json


def process_json(
    json_str: str,
    processed_key: list[str] | None = None,
    found_tokens: list[str] | None = None,
    callback: Callable[[str, str],  Any] | None = None
):
    data = json.loads(json_str)
    if processed_key is None or found_tokens is None or callback is None:
        return

    set_processed_key = set(processed_key)
    token_map = {token.lower(): token for token in found_tokens}

    for key, value in data.items():

        if key not in set_processed_key:
            continue

        for word in value.split():
            token = token_map.get(word.lower())

            if token is not None:
                callback(key, token)
