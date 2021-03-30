import random
import csv
import turtle

# colours for text
def pryellow(skk):
    print("\033[93m {}\033[00m".format(skk))


def prcyan(skk):
    print("\033[96m {}\033[00m".format(skk))


def prred(skk):
    print("\033[91m {}\033[00m".format(skk))


def prgreen(skk):
    print("\033[92m {}\033[00m".format(skk))


def prpurple(skk):
    print("\033[95m {}\033[00m".format(skk))


def prlightpurple(skk):
    print("\033[94m {}\033[00m".format(skk))


def get_stats_by_name(stat_choice):  # Function to choose stats from csv file
    with open("harrypotter.csv", "r") as csv_file:
        spreadsheet = csv.DictReader(csv_file)
        for row in spreadsheet:
            if row["Name"] == stat_choice:
                return {
                    "Name": row["Name"],
                    "Magic": row["Magic"],
                    "Cunning": row["Cunning"],
                    "Courage": row["Courage"],
                    "Wisdom": row["Wisdom"],
                    "Temper": row["Temper"],
                }
    return {}


def random_harrypotter():  # Function to generate the characters randomly from the csv file
    harrypotter = random.randint(1, 29)  # we have 29 characters to choose from
    with open("harrypotter.csv", "r") as csv_file:
        spreadsheet = csv.DictReader(csv_file)
        counter = 1  # looping through all the rows,
        # as soon as the row number becomes equal
        # to the randomly generated number,
        # I'm returning that row as a dict.
        # The current row number is being stored in
        # the variable called counter
        for row in spreadsheet:
            if counter == harrypotter:
                return {
                    "Name": row["Name"],
                    "Magic": row["Magic"],
                    "Cunning": row["Cunning"],
                    "Courage": row["Courage"],
                    "Wisdom": row["Wisdom"],
                    "Temper": row["Temper"],
                }
            else:
                counter = counter + 1
    return {}


def run(round):  # Function to make choices available for characters and stats to use
    choices = ["Magic", "Cunning", "Courage", "Wisdom", "Temper"]
    opponent_choice = random.choice(choices)
    if random.randint(1, 100) % 2 == 0:  # turn is decided by even or odds if it's divisible by 2.
        # Who begins the round? Player is even. Computer is odd.
        prpurple("\nPlayer:")
        hpCharacters = []
        while len(hpCharacters) < 5:  # it allows the player to choose from 5 randomly generated characters
            my_harrypotter = random_harrypotter()
            if my_harrypotter["Name"] not in hpCharacters:
                hpCharacters.append(my_harrypotter["Name"])
        prpurple("Choose a character: ")
        character_choice = input(hpCharacters)
        my_harrypotter = get_stats_by_name(character_choice)
        prcyan("Your stats are:")
        prcyan(" -" * 10)
        prcyan("  * Magic: {}".format(my_harrypotter["Magic"]))
        prcyan("  * Cunning: {}".format(my_harrypotter["Cunning"]))
        prcyan("  * Courage: {}".format(my_harrypotter["Courage"]))
        prcyan("  * Wisdom: {}".format(my_harrypotter["Wisdom"]))
        prcyan("  * Temper: {}".format(my_harrypotter["Temper"]))
        prcyan(" -" * 10)
        stat_choice = input(
            "Which stat do you want to use? (Magic, Cunning, Courage, Wisdom, Temper)"
        )
        prlightpurple("\nOpponent:")
        opponent_harrypotter = random_harrypotter()
        prlightpurple("The opponent had {}".format(opponent_harrypotter["Name"]))
        prlightpurple("The opponent chose {}".format(opponent_choice))
        my_stat = my_harrypotter[stat_choice]
        opponent_stat = opponent_harrypotter[opponent_choice]
    else:  # The computer starts the game
        prlightpurple("\nOpponent:")
        opponent_harrypotter = random_harrypotter()
        prlightpurple("The opponent was given {}".format(opponent_harrypotter["Name"]))
        prlightpurple("The opponent chose {}".format(opponent_choice))
        opponent_stat = opponent_harrypotter[opponent_choice]
        prpurple("\nPlayer:")
        hpCharacters = []
        while len(hpCharacters) < 5:
            my_harrypotter = random_harrypotter()
            if my_harrypotter["Name"] not in hpCharacters:
                hpCharacters.append(my_harrypotter["Name"])
        prpurple("Choose a character: ")
        character_choice = input(hpCharacters)
        my_harrypotter = get_stats_by_name(character_choice)
        prcyan("Your stats are:")
        prcyan(" -" * 10)
        prcyan("  * Magic: {}".format(my_harrypotter["Magic"]))
        prcyan("  * Cunning: {}".format(my_harrypotter["Cunning"]))
        prcyan("  * Courage: {}".format(my_harrypotter["Courage"]))
        prcyan("  * Wisdom: {}".format(my_harrypotter["Wisdom"]))
        prcyan("  * Temper: {}".format(my_harrypotter["Temper"]))
        prcyan(" -" * 10)
        stat_choice = input(
            "Which stat do you want to use? (Magic, Cunning, Courage, Wisdom, Temper)"
        )
        my_stat = my_harrypotter[stat_choice]

    my_stat = int(my_stat)
    opponent_stat = int(opponent_stat)

    prpurple("My stat: {}".format(my_stat))
    prlightpurple("Computer's stat: {}".format(opponent_stat))

    write_scores_to_file("hpscore.csv", [round, my_stat, opponent_stat])

    return (my_stat, opponent_stat)


def write_scores_to_file(file, scores):  # Function to write scores to file
    with open("hpscore.csv", "a") as f:
        writer = csv.writer(f)
        # write the scores
        writer.writerow(scores)

# the game
def play():
    pryellow(" $$   $$    $$      $$$$$$$   $$$$$$$  $$    $$    $$$$$$   $$$$$$  $$$$$$$$ $$$$$$$$  $$$$$$$  $$$$$$$")
    pryellow(" $$   $$  $$  $$    $$    $$  $$    $$  $$  $$     $$   $$ $$    $$    $$       $$     $$       $$    $$")
    pryellow(" $$$$$$$  $$$$$$$   $$$$$$$   $$$$$$$     $$       $$$$$$  $$    $$    $$       $$     $$$$$$$  $$$$$$$")
    pryellow(" $$   $$  $$   $$   $$    $$  $$    $$    $$       $$      $$    $$    $$       $$     $$       $$    $$")
    pryellow(" $$   $$  $$   $$   $$     $$ $$     $$   $$       $$        $$$$      $$       $$     $$$$$$$  $$     $$")
    print("\n")
    pryellow("                                  Welcome to Harry Potter Top Trumps!")
    rnd = 1
    user_input = int(input("How many rounds do you want to play?"))
    rounds = user_input
    try:
        rounds = int(user_input)
    except ValueError:
        print("Not a number")

    my_total_wins = 0
    opponent_total_wins = 0
    my_total_score = 0
    opponent_total_score = 0

    header = ["Round", "Me", "Computer"]
    with open("hpscore.csv", "w+") as f:
        writer = csv.writer(f)
        # write the header
        writer.writerow(header)

    for i in range(rounds):
        print("\n")
        prred("*" * 10)
        print("  Round:", rnd)
        prred("*" * 10)

        my_score, opponent_score = run(rnd)
        my_total_score = my_total_score + my_score  # cumulative score for player from cumulative stats
        opponent_total_score = opponent_total_score + opponent_score

        if my_score > opponent_score:
            prgreen("You Win!")
            my_total_wins = my_total_wins + 1

        elif my_score < opponent_score:
            prred("You Lose!")
            opponent_total_wins = opponent_total_wins + 1
        else:
            pryellow("Draw!")

        rnd = rnd + 1

    prcyan(
        "Final total scores are\n Your score: {} \n Opponent's score: {}".format(
            my_total_score, opponent_total_score
        )
    )

    write_scores_to_file("hpscore.csv", ["Total", my_total_score, opponent_total_score])

    prpurple(
        "You won {} rounds, the opponent won {} rounds so...".format(
            my_total_wins, opponent_total_wins
        )
    )
    if my_total_wins > opponent_total_wins:
        prgreen("   You win the game!")
        # turtle:
        turtle.bgcolor("green")
        # write text
        # styling font
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(5, 150)
        turtle.write("Congratulations! You have won! Your prize: The Deathly Hallows!",
                     align="center", font=("Verdana", 15, "normal"))
        # deathly hallow symbol
        bob = turtle.Turtle()
        bob.hideturtle()
        bob.speed(1000)
        bob.pensize(10)
        bob.penup()
        bob.goto(-80, -35)
        bob.pendown()
        for i in range(3):
            bob.forward(200)
            bob.left(120)
        bob.forward(95)
        for i in range(36):
            bob.forward(10)
            bob.left(10)
        bob.forward(6)
        bob.left(90)
        bob.forward(172)
        turtle.done()
    elif my_total_wins < opponent_total_wins:
        prred("   You lose the game")
        # turtle:
        turtle.bgcolor("red")
        # write text
        # styling font
        turtle.speed(1000)
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(5, 150)
        turtle.write("Too bad! Maybe some glasses could help?",
                     align="center", font=("Verdana", 15, "normal"))
        # glasses
        # object tr for turtle
        tr = turtle.Turtle()

        # set thickness for each ring
        tr.pensize(5)

        tr.color("black")
        tr.penup()
        tr.goto(-100, -25)
        tr.pendown()
        tr.circle(45)

        # line
        tr.penup()
        tr.goto(-50, 20)
        tr.pendown()
        tr.fd(105)

        tr.color("black")
        tr.penup()
        tr.goto(100, -25)
        tr.pendown()
        tr.circle(45)
        tr.hideturtle()

        # scar
        turtle.penup()
        turtle.goto(-5, 50)
        turtle.pendown()
        turtle.color("yellow")
        turtle.pensize(10)
        length = 25
        angle = 90
        turtle.left(angle)
        turtle.forward(length)
        turtle.left(angle)
        turtle.backward(length)
        turtle.left(angle)
        turtle.backward(length)

        turtle.done()
    else:
        pryellow("   It's an overall draw")

play()

