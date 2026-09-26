from json_processor import process_json


def test_process_json_basic():
    result = []

    process_json(
        '{"key1": "Word1 word2", "key2": "word2 word3"}',
        ["key1", "KEY2"],
        ["WORD1", "word2"],
        lambda key, token: result.append((key, token)),
    )

    assert result == [
        ("key1", "WORD1"),
        ("key1", "word2"),
    ]


def test_process_json_case_sensitive_keys():
    result = []

    process_json(
        '{"key1": "hello", "KEY1": "world"}',
        ["key1"],
        ["hello", "world"],
        lambda key, token: result.append((key, token)),
    )

    assert result == [
        ("key1", "hello"),
    ]


def test_process_json_case_insensitive_tokens():
    result = []

    process_json(
        '{"key1": "HELLO hello HeLLo"}',
        ["key1"],
        ["hello"],
        lambda key, token: result.append((key, token)),
    )

    assert result == [
        ("key1", "hello"),
        ("key1", "hello"),
        ("key1", "hello"),
    ]


def test_process_json_no_required_keys():
    result = []

    process_json(
        '{"key1": "hello"}',
        None,
        ["hello"],
        lambda key, token: result.append((key, token)),
    )

    assert not result


def test_process_json_no_tokens():
    result = []

    process_json(
        '{"key1": "hello"}',
        ["key1"],
        None,
        lambda key, token: result.append((key, token)),
    )

    assert not result
