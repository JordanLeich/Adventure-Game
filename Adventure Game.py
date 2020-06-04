# Made by Jordan Leich on 6/3/2020

import time

score = 0


def game():
    global score
    user_age = input('How old are you: ')
    print()
    time.sleep(1)

    if user_age < '18':
        print('Sorry, you are too young for this game... Ending game...')
        print()
        time.sleep(2)
        quit()

    elif user_age >= '18':
        print('This game starts on an empty road with fog everywhere in the distance...')
        print()
        time.sleep(2)
        choice1 = input('You have the choice to either walk down the empty road or walk to a nearby water source ('
                        'road or water): ')
        print()
        time.sleep(1)

        if choice1 == 'road':
            score += 3
            print('You continue to walk down this mysterious empty road and see a blurry image of a person within the '
                  'far distance...')
            print()
            time.sleep(2)
            road_choice = input('Do you wish to avoid the person in the distance or confront the mysterious person ('
                                'avoid or confront): ')
            print()
            time.sleep(2)

            if road_choice == 'avoid':
                score -= 2
                print('From avoiding this mysterious person, you continue your search and eventually find your way '
                      'back home...')
                print()
                time.sleep(2)
                print('But something doesnt seem right... your father is there trying anxiously to find your mother '
                      'who has been lost for hours...')
                print()
                time.sleep(2)
                lost_mother = input('You have the choice to tell your father about the mysterious figure you saw '
                                    'earlier or keep quiet (tell or quiet): ')
                print()
                time.sleep(2)

                if lost_mother == 'tell':
                    score += 2
                    print('You tell your father about what you saw and you both decide to go back out into the '
                          'dangerous fog to search for the figure again...')
                    print()
                    time.sleep(2)
                    print('Upon searching for over 3 hours... it is deemed that your mother is abandoned...')
                    print()
                    time.sleep(2)
                    result()

                elif lost_mother == 'quiet':
                    score -= 6
                    print('You decide to keep quiet about your findings and struggle with the guilt forever knowing '
                          'that the figure from earlier could have been your mother...')
                    print()
                    time.sleep(3)
                    result()

                else:
                    print('Invalid input... Ending game...')
                    print()
                    time.sleep(2)
                    quit()

            elif road_choice == 'confront':
                score += 5
                print('Due to the vast fog in the air, it is difficult to see who this mysterious figure is in the '
                      'distance but nevertheless, you confront the figure after all...')
                print()
                time.sleep(3)
                print('To come to your surprise, it is actually your mother... she explains how she ran off since she '
                      'had got in a argument with your father earlier...')
                print()
                time.sleep(3)
                print('Given that you both are becoming scared and lost at this point, your mother says that enough '
                      'is enough and she knows the way back home to your father...')
                print()
                time.sleep(3)
                print('You both manage to return back home together and reunite as a happy and loving family!')
                print()
                time.sleep(2)
                result()

            else:
                print('Invalid input... Ending game...')
                print()
                time.sleep(2)
                quit()

        elif choice1 == 'water':
            score -= 2
            print('You decide to avoid walking and instead find a nearby water source since your thirst is growing...')
            print()
            time.sleep(2)
            print('After 7 minutes of searching, you come across a swampy area of water that you drink from...')
            print()
            time.sleep(2)
            print('While continuing on your journey, you suddenly faint and die due to poisoned and bacteria filled '
                  'water from the swamp...')
            print()
            time.sleep(3)
            result()

        else:
            print('Invalid input... Ending game...')
            print()
            time.sleep(2)
            quit()

    else:
        print('Invalid input... Restarting question...')
        print()
        time.sleep(2)
        game()


def main():
    global score
    game()


def result():
    global score
    print('You have reached the end of the game... Your final score is: ' + str(score))
    print()
    time.sleep(5)
    play_again = input('Do you wish to play again (yes or no): ')
    print()
    time.sleep(1)
    if play_again == 'yes':
        print('Restarting game...')
        print()
        time.sleep(3)
        game()

    elif play_again == 'no':
        print('Thanks for playing...')
        print()
        time.sleep(2)
        quit()

    else:
        print('Invalid input... Ending game...')
        print()
        time.sleep(2)
        quit()


main()
