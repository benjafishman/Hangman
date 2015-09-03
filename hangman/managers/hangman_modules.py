__author__ = 'benfishman'
from hangman.models import Hangman
from random_words import RandomWords
import datetime


def generate_word():
    # TODO: generate random word
    rw = RandomWords()
    word = rw.random_word()
    return word


# Starts a new hangman game by creating a new hangman model
def start_new_game():
    word = generate_word()

    session_id = get_new_session()

    blank_guess = '_'*len(word)

    hangman = Hangman(word=word, current_guess=blank_guess, session_id=session_id)

    hangman.save()

    return session_id

    # save new Hangman to db
def get_new_session():
    return str(datetime.datetime.now().time()) + "-TEST"

