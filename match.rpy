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
    jump postMatch

label shoot:
    $ gameWon = True
    n "El bicho shoots..."

    n "OMG what an incredible goal"

    n "El bicho places the ball at the top right and places his team as the champions"
    jump postMatch
    # This ends the game.
