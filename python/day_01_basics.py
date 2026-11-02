def word_count(text):
    """Return a dict of word -> count, case-insensitive."""

    lowered = text.lower().split(' ')
    return [ (word, lowered.count(word)) for word in lowered]




    
