from os import PathLike
from typing import TextIO, TypeAlias, Iterator

LineSource: TypeAlias = str | PathLike[str] | TextIO


def filter_lines(
    source: LineSource,
    search_words: list[str],
    stop_words: list[str],
) -> Iterator[str]:
    searches = set(word.casefold() for word in search_words)
    stops = set(word.casefold() for word in stop_words)

    if isinstance(source, (str, PathLike)):
        with open(source, encoding="utf-8") as stream:
            for line in stream:
                words = set(word.casefold() for word in line.split())
                if (
                    words.isdisjoint(stops)
                    and not words.isdisjoint(searches)
                ):
                    yield line
        return

    for line in source:
        words = set(word.casefold() for word in line.split())
        if words.isdisjoint(stops) and not words.isdisjoint(searches):
            yield line
