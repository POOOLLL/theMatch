# Mock
label start_match:
define t = Character(_("Trainer"), color="#c8ffc8")
define m = Character(_("El Bicho"), color="#c8c8ff")
define i = Character("Interviewer")

# This is a variable that is True if you've compared a VN to a book, and False
# otherwise.
default book = False


# The game starts here.
label start:

    scene bg lecturehall
    with fade

    t "Hey what's up? Ready for the match?"

    m "Am I still going to play all the match?"

    menu:
        "yes, play full match":
            jump play_full_match

        "No you will enter after half of the match":
            jump play_last_half

label play_full_match:
    $ play_full_match = True
    m "Ok, I will do my best!"

    t "I love that atitude!"

    t "I have some new strats to show you before the game but lets go to changing rooms to get you prepared."

    m "Perfect I will change while you are explaining."

    t "seems good to me!"

label play_last_half:
    $ play_full_match = False

    m "Ho, you talled me that I was going to play the full match because I did very good trainings during all the week."

    t "Yes I know, I'm sorry, the second trainer propesed to me a better tactick, you going out on the second half."

    m "I dont care you said to me I was going out first!"

    m "Please leave me alone for a while, I need to concentrate and I don't whant to talk to you."

    t "Ok but don't get mad, see you in a while."
    jump match

# parte de victor

define n = Character("Narrator")


# The game starts here.

label match:



    scene stadium

    # shows Santiago Bernabeu

    show El bicho

    # These display lines of dialogue.

    n "It has been a really tie match. Last play of the match, el Bicho raises the ball up."

    n "He sees his team mate "

    menu:
        "Pass it to the teamate":

            jump passit

        "Shoot":

            jump shoot


label passit:
    $ gameWon = False
    n "El bicho passes it tp his teamate"

    n "His teamate tries to drible but he strugles and lose the ball"

    n "The refery blows the whisle and thats the end of the match"

    n "Thats a tie, I don't see too many happy faces in the field"
    jump gameLost1

label shoot:
    $ gameWon = True
    n "El bicho shoots..."

    n "OMG what an incredible goal"

    n "El bicho places the ball at the top right and places his team as the champions"
    jump gameWon1
    # Georgii's part.

    default gameWon = True



    label postMatch:

        if gameWon:
            jump gameWon1
        else:
            jump gameLost1


    label gameWon1:
        "the game was won"
        jump gameWon2

        label gameLost1:
        "the game was lost"
        jump gameLost2

    label gameWon2:
            i "Hello El Bicho, what can you tell us about this game u just had? How was it in your opinion?"

            menu:
             "El Bicho liked the game":
                jump choice_goodGame
             "El bicho didn't like the game":
                jump choice_badGame

    #happy about the game
    label choice_goodGame:
            i "So how do you think this game was in your opinion?"
            m "It was a very good game and im happy we won. The performance of my team was the best."
            i "Okay, now that we know you liked this game, how do you think your teammates liked this game?"
            m "I really hope they liked it as much as me but it's really important for them to know that we have to work even harder in order to win the champions league"
            i "Okay, thank you for this interview, good luck in next games!"
            m "Thank you, bye."
    return

    #not happy about the game
    label choice_badGame:
            i "Hey El Bicho, how did you like this game?"
            m "It´s okay but isn´t good enough in my opinion."
            i "Why do you say so?"
            m "Well, because there were some moments where i made mistakes which i probably wouldn´t make if i would practice more."
            m "But at the end im still happy that we won even though we could do better."
            i "Well we all hope that you will get as good as you want!"
            i "All our viewer wish you luck in the future games, bye El Bicho!"
            m "Thank you everyone who is watching, but i have to go celebrate with my team, so bye everyone!"

            #lost the game
            label gameLost2:
            i "Hello, very sad to see you and your team lose but we still have to ask you some questions"
            i "What do you think was the reason of you losing?"
            m "i think that we got too relaxed at the end thinking that we won."
            i "What would you say about your pesonal performance?"
            m "Well obviously it it want't good enough as we lost so i will do anything to improve myself."
            i "Thanks for your response, we see that you need to leave, so good luck in next games!"
            m "Okay, thanks, bye."


    return
