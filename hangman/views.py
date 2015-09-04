from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import GuessLetterForm
from django.contrib import messages

from hangman.managers import hangman_modules
from hangman.models import Hangman

from django.views.generic.edit import FormView


def index(request):
    if 'restart-game' in request.POST:
        request.session.flush()
        sid = hangman_modules.start_new_game()
        request.session['session_id'] = sid
        return HttpResponseRedirect('')

    if 'session_id' not in request.session:
        sid = hangman_modules.start_new_game()
        request.session['session_id'] = sid
    # if this is a POST request we need to process the form data
    #guesses_left = 7

    print('session_id is %s' % request.session['session_id'])

    hangman = Hangman.objects.get(session_id=request.session['session_id'])
    if request.method == 'POST':


        print("here 1")
        # create a form instance and populate it with data from the request:
        form = GuessLetterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            letter = form.cleaned_data['letter']
            print("you submitted: %s." % letter)
            #hangman = Hangman.objects.get(session_id=request.session['session_id'])

            game_over = False

            # check if session has guesses left

            if hangman.has_guesses():
                # increment guesses by one
                # check if letter is in word
                # check letter or word
                if len(letter) == 1:
                    if hangman.check_letter_guess(letter):
                        hangman.update_guess_result(letter)
                        print("CORRECT! %s is in the word" % letter)
                        print(hangman.current_guess)
                    else:
                        hangman.increment_guesses()
                        hangman.update_attempts(letter)
                        print("WRONG! %s is not in the word, try again." % letter)
                else:
                    hangman.check_word_guess(letter)
                    hangman.update_word_attempts(letter)
                    hangman.increment_guesses()


                print("you have %i guesses left" % hangman.guesses_left())

                hangman.save()
                if hangman.did_win():
                    messages.success(request, 'You Won - Good Job!')
                    game_over = True

            else:
                game_over = True
                messages.error(request, 'You lost - try again!')


            guesses_left = hangman.guesses_left() + 1

            print(hangman.guesses_left())
            # Convert result to list to iterate over in the template
            words = str.split(hangman.get_word_attempt())       # turn the word attempts into a list
            results = list(hangman.get_current_guess())
            pic_num = str(hangman.get_current_guess_num())
            junk = list(hangman.get_attempts()) + words   # append the word attempts to the letter attempts

            #show the word in results when a user loses
            if(game_over and not hangman.did_win()):
                results = hangman.get_word()
                guesses_left = 0

            form = GuessLetterForm()

            return render(request, 'hangman/index.html',
                          {"form": form, "guesses": guesses_left, "results": results, "pic_num": pic_num, "junk": junk,"game_over": game_over})
    # if a GET (or any other method) we'll create a blank form
    else:
        print("here 3")
        form = GuessLetterForm()

    # request.session.set_test_cookie()
    guesses_left = hangman.guesses_left() + 1
    words = str.split(hangman.get_word_attempt())                # turn the word attempts into a list
    results = list(hangman.get_current_guess())
    junk = list(hangman.get_attempts())  + words   # append the word attempts to the letter attempts
    pic_num = str(hangman.get_current_guess_num())
    return render(request, 'hangman/index.html', {'form': form, 'guesses': guesses_left, "pic_num": pic_num, 'results': results, "junk": junk} )
    # return render(request, 'hangman/index.html')

