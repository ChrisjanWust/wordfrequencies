from wordfrequencies import get_part_of_speech, get_word_rank

def test_word_frequency():
    assert get_word_rank("the") < get_word_rank("man") < get_word_rank("jumps")
    assert get_part_of_speech("the") == "FUNCTION_WORD"
    assert get_part_of_speech("man") == "NOUN"
    assert get_part_of_speech("jumps") == "VERB"
    assert get_part_of_speech("Chrisjan") is None


if __name__ == "__main__":
    test_word_frequency()