import re
import stringUtils
from stringUtils import alphabet


def find_all_indices(raw_pattern, text):

    pattern = re.escape(raw_pattern)

    occurrences = 0

    for _ in re.finditer(pattern, text, flags=re.IGNORECASE):

        occurrences += 1

    return occurrences


def ic_compute(raw_text):

    text = stringUtils.normalize_text(raw_text)

    alphabet_length = len(alphabet)
    text_length = len(text)

    occurrences_count = [find_all_indices(letter, text) for letter in alphabet]

    sum_of_occurrence_frequency = 0

    for occurrence_count in occurrences_count:

        sum_of_occurrence_frequency += ((occurrence_count / text_length) * ((occurrence_count - 1) / (text_length - 1)))

    ic = sum_of_occurrence_frequency * alphabet_length

    return ic
