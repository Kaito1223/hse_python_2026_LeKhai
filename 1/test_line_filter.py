from io import StringIO

from line_filter import filter_lines


def test_find_word():
    source = StringIO(
        "hello world\n"
        "I like Python\n"
        "goodbye\n"
    )

    result = list(
        filter_lines(
            source,
            ["python"],
            [],
        )
    )

    assert result == ["I like Python\n"]


def test_ignore_case():
    source = StringIO("Роза красивая\n")

    result = list(
        filter_lines(
            source,
            ["роза"],
            [],
        )
    )

    assert result == ["Роза красивая\n"]


def test_partial_word_not_found():
    source = StringIO("Роза красивая\n")

    result = list(
        filter_lines(
            source,
            ["роз"],
            [],
        )
    )

    assert not result


def test_stop_word():
    source = StringIO("Роза упала на лапу Азора\n")

    result = list(
        filter_lines(
            source,
            ["роза"],
            ["азора"],
        )
    )

    assert not result


def test_file_name(tmp_path):
    file = tmp_path / "test.txt"

    file.write_text(
        "hello\n"
        "python is good\n",
        encoding="utf-8",
    )

    result = list(
        filter_lines(
            file,
            ["python"],
            [],
        )
    )

    assert result == ["python is good\n"]
