import re
import unicodedata

from stringUtils import *


def findallindices(raw_pattern, text):

    pattern = re.escape(raw_pattern)

    occurrences = 0

    for _ in re.finditer(pattern, text, flags=re.IGNORECASE):

        occurrences += 1

    return occurrences


def iccompute(raw_text):

    text = unicodedata.normalize('NFKD', re.sub('\W+', '', raw_text)).encode('ascii', 'ignore').decode('ascii')

    alphabet_length = len(alphabet)
    text_length = len(text)

    occurrences_count = [findallindices(letter, text) for letter in alphabet]

    sum_of_occurrence_frequency = 0

    for occurrence_count in occurrences_count:

        sum_of_occurrence_frequency += ((occurrence_count / text_length) * ((occurrence_count - 1) / (text_length - 1)))

    ic = sum_of_occurrence_frequency * alphabet_length

    return ic
