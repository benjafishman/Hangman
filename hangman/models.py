from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

# TODO: rename vars to be more intuitive
'''
Hangman object:
stores all relevant guesses, actual word value, session id, and max number of attempts

Also implements checking if guesses were correct either on per letter basis/word itself
'''
class Hangman(models.Model):
    word = models.CharField(max_length=200)
    max_number_guesses = models.IntegerField(default=10)
    current_guess = models.CharField(max_length=200)
    current_guess_num = models.IntegerField(default=0)
    session_id = models.CharField(max_length=200, default='0000000')
    attempts = models.CharField(max_length=200, default='')
    word_attempt = models.CharField(max_length=200, default='')

    def check_letter_guess(self, letter):
        if letter in self.word:
            return True
        return False

    def increment_guesses(self):
        self.current_guess_num += 1

    def get_word(self):

        return self.word

    def check_word_guess(self, guess):
        if guess == self.word:
            self.current_guess = guess
            return True
        else:

            return False
    def update_word_attempts(self, word):
        self.word_attempt += word+' '

    def get_word_attempt(self):
        return self.word_attempt

    def update_attempts(self, letter):
        self.attempts += letter

    def get_attempts(self):
        return self.attempts

    def maxed_out(self):
        return self.current_guess_num >= self.max_number_guesses

    def __str__(self):  # __unicode__ on Python 2
        return self.word

    # boolean funtion to see if guesses are left
    def has_guesses(self):
        if self.current_guess_num < self.max_number_guesses:
            return True

        return False

    def get_current_guess(self):
        return self.current_guess

    def get_current_guess_num(self):
        return self.current_guess_num

    # calculate number of guesses left
    def guesses_left(self):
        return self.max_number_guesses - self.current_guess_num

    def update_guess_result(self, letter):
        # basically build a string of dashes and the result of correct guess
        # if letter matches char put letter, else put dash
        # Remember python strings are immutable so we will have to create a new one each time
        # TODO: can i store python lists in a db?

        # create a list of underscores the length of the word
        results = ['_'] * len(self.word)

        # zip() through the actual word and the current constructed guess
        # and input the newest element
        iter = 0
        for i, p in zip(self.word, self.current_guess):
            # print('1')
            if p == '_':
                #print('2')
                if letter == i:
                    #print('3')
                    results[iter] = i

                    print(results)
            else:
                results[iter] = p
            iter += 1
            print(iter)



        self.current_guess = ''.join(results)


    def did_win(self):
        x = self.current_guess
        y = self.word
        if (len(x) == len(y) and sorted(x) == sorted(y)):
            return True
        else:
            return False




