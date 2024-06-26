"""Functions for creating, transforming, and adding prefixes to strings."""

import re

def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """

    return "un"+word


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """
    connector = " :: "+vocab_words[0]
    print(connector.join(vocab_words))
    return connector.join(vocab_words)


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """

    if word[-5:-4]=="i":
        return word[0:-5]+"y"
    return word[0:-4]


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """

    return re.sub(r"[,]|[.]","",sentence.split()[index])+"en"

def decode(message_file):
  with open(message_file, "r") as f:
    # print(len(f.read().splitlines()))
    message_dict = {int(line.split()[0]): line.split()[1] for line in f}

  step = 1
  decoded_message = []
  current_index = 1
  while current_index in message_dict:
    decoded_message.append(message_dict[current_index])
    step += 1
    current_index += step
  return ' '.join(decoded_message)

print(decode("message.txt"))