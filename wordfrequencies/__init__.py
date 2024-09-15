from pathlib import Path
from collections import namedtuple
from lazy_object_proxy import Proxy
import csv

WordData = namedtuple("WordData", ["rank", "part_of_speech"])


def load_word_map():
    part_of_speech_map = {
        "fw": "FUNCTION_WORD",
        "v": "VERB",
        "n": "NOUN",
        "r": "ADVERB",
        "j": "ADJECTIVE",
        "u": "INTERJECTION",
        "m": "NUMERALS",
        "K": "PROPER_NOUN",
        "abbr": "ABBREVIATION",
    }

    csv_path = Path(__file__).parent / "word_frequency_data.tsv"
    word_map = {}

    with open(csv_path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter='\t')
        for i, row in enumerate(reader, start=1):
            value = WordData(i, part_of_speech_map[row['POS']])
            for inflection in row['INFLECTIONS'].split(","):
                inflection = inflection.strip()
                word_map[inflection] = value

    return word_map


word_map = Proxy(load_word_map)


def get_word_rank(word) -> int:
    """
    Lower rank = higher frequency, 1 = high frequency word

    Note this will often fail because the data we're working on is only the top 5000 words
    In that case, a number 50% larger than the max will be returned
    """
    word = word.strip().lower()
    try:
        return word_map[word].rank
    except KeyError:
        return int(len(word_map) * 1.5)


def get_part_of_speech(word):
    """
    Note this will often fail because the data we're working on is only the top 5000 words
    In that case, None will be returned
    """
    word = word.strip().lower()
    try:
        return word_map[word].part_of_speech
    except KeyError:
        return None


