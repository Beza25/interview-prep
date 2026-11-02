import day_01_basics

def test_word_count():
    text = "Python basics. Replace each `pass` with your code. No AI."
    assert day_01_basics.word_count(text) == [
        ("python", 1),
        ("basics.", 1),
        ("replace", 1),
        ("each", 1),
        ("`pass`", 1),
        ("with", 1),
        ("your", 1),
        ("code.", 1),
        ("no", 1),
        ("ai.", 1)
    ]

test_word_count()