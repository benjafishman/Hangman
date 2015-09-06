__author__ = 'benfishman'

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from hangman.managers import hangman_modules
from .forms import GuessLetterForm
from hangman.models import Hangman


def index(request):
    '''
    :param request: hangman/
    :return: the view
    '''

    # If user presses restart button then we flush the current
    # session and and create a new hangman object with a new
    # session value
    if 'restart-game' in request.POST:
        request.session.flush()
        sid = hangman_modules.start_new_game()
        request.session['hangman_id'] = sid
        return HttpResponseRedirect('')

    # This handles the case a when someone arrives at /hangman
    # from homepage or other link to create a new session and
    # hangman object
    if 'hangman_id' not in request.session:
        sid = hangman_modules.start_new_game()
        request.session['hangman_id'] = sid

    print('hangman_id is %s' % request.session['hangman_id'])

    # Get the hangman object associated with session id
    hangman = Hangman.objects.get(session_id=request.session['hangman_id'])

    # Set the session to expire after 2 minutes of inactivity
    request.session.set_expiry(120)

    # Check if the form was submitted with a POST method
    if request.method == 'POST':
        # Create a Guess Letter form instance and populate it with data from the request:
        form = GuessLetterForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            # grab the cleaned data (the word/letter the user submitted)
            letter = form.cleaned_data['letter']

            print("you submitted: %s." % letter)
            # Set game_over flag to false
            game_over = False

            #####
            # If the user still has guesses left, then we will check their guess and go the hangman workflow
            # If they have no guesses left then they lose
            ###
            if hangman.has_guesses():
                # If they user submitted a letter we check if the letter is in the word
                if len(letter) == 1:
                    if hangman.check_letter_guess(letter):
                        hangman.update_guess_result(letter)
                        print("CORRECT! %s is in the word" % letter)
                        print(hangman.current_guess)
                    else:
                        # They guessed a letter that was not in the word so we will increment their attempts
                        hangman.increment_guesses()
                        # Add their guessed letter to their attempts i.e. junkyard
                        hangman.update_attempts(letter)
                        print("WRONG! %s is not in the word, try again." % letter)

                else:
                    #####
                    # If we got here, the the user submitted a word
                    #
                    # If the user correctly guesses the word then when the did_win function will catch this
                    # and correctly display relay the information to the view
                    #
                    # We will only check if the word they submitted is correct
                    # We will not check for any valid sub-words
                    ###

                    hangman.check_word_guess(letter)
                    hangman.update_word_attempts(letter)
                    hangman.increment_guesses()


                print("you have %i guesses left" % hangman.guesses_left())

                # Save any attempts and guess increments to the database
                hangman.save()

                # Check if the user has won because of their input
                if hangman.did_win():
                    messages.success(request, 'You Won - Good Job!')
                    game_over = True
                # Check if the user has lost because of their input
                elif not hangman.has_guesses():
                    messages.error(request, 'You lost - try again!')
                    game_over = True
                # if neither case is true then the game is still going

            else:
                # probably got here when user refreshed page after losing
                game_over = True
                messages.error(request, 'You lost - try again!')

            # aggregate results of user submission and relay ot the view
            print(hangman.guesses_left())
            guesses_left = hangman.guesses_left()
            # Convert results to a lists to iterate over in the template
            words = str.split(hangman.get_word_attempt())       # any word attempts converted to list
            results = list(hangman.get_current_guess())         # the current correct guesses converted to a list
            pic_num = str(hangman.get_current_guess_num())      # the hangman picture to display converted to a string - i don't remeber why i had to convert to a string - but it worx!!
            junk = list(hangman.get_attempts()) + words         # append the word attempts to the letter attempts so the template just needs one variable


            # show the word in results when a user loses
            if(game_over and not hangman.did_win()):
                results = hangman.get_word()

            # returning the form will remove previous input when page returns
            form = GuessLetterForm()

            return render(request, 'hangman/index.html',
                          {"form": form, "guesses": guesses_left, "results": results, "pic_num": pic_num, "junk": junk,"game_over": game_over})
    # if a GET (or any other method) we'll create a blank form
    else:
        # If we got here, then then the form was not properly submitted
        print("here 3")
        form = GuessLetterForm()

    # aggregate template vars of new hangman object
    guesses_left = hangman.guesses_left()
    words = str.split(hangman.get_word_attempt())                # turn the word attempts into a list
    results = list(hangman.get_current_guess())
    junk = list(hangman.get_attempts())  + words   # append the word attempts to the letter attempts
    pic_num = str(hangman.get_current_guess_num())
    return render(request, 'hangman/index.html', {'form': form, 'guesses': guesses_left, "pic_num": pic_num, 'results': results, "junk": junk} )
    # return render(request, 'hangman/index.html')

