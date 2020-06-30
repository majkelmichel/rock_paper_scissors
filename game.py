import random

default_options = ['paper', 'scissors', 'rock', 'paper', 'scissors', 'rock']


def game(points, possible_inputs, lenght = 3):
    user_option = ''
    while user_option != '!exit':
        user_option = input()
        computer_option = possible_inputs[random.randint(0, len(possible_inputs)-1)]
        # print(possible_inputs)
        if user_option == "!exit":
            break
        if user_option == "!rating":
            print(f"Your rating: {points}")
            continue
        if user_option not in possible_inputs:
            print("Invalid input")
            continue
        ind_user = possible_inputs.index(user_option)
        # print(possible_inputs[ind_user + 1:ind_user + lenght // 2 + 1])
        if computer_option == user_option:
            print(f"There is a draw ({user_option})")
            points += 50
        elif possible_inputs[possible_inputs.index(computer_option)] in possible_inputs[ind_user + 1:ind_user + lenght // 2 + 1]:
            print(f"Sorry but computer chose {computer_option}")
        else:
            print(f"Well done. Computer chose {computer_option} and failed")
            points += 100
    print("Bye!")
    return points


def read_file():
    rf = open('rating.txt')
    rate_list = rf.readlines()
    names = list()
    scores = list()
    for score in rate_list:
        names.append(score.split(' ')[0])
        scores.append(score.split(' ')[1].rstrip('\n'))
    rf.close()
    return names, scores


def write_file(sco, na):
    to_file = list()
    for i in range(len(na)):
        to_file.append(f'{na[i]} {sco[i]} \n')
    file = open('rating.txt', 'w')
    file.writelines(to_file)
    file.close()


def append_file(name, points):
    file = open("rating.txt", 'a')
    file.write(f'{name} {points} \n')
    file.close()


name = input("Enter your name: ")
options = input()
print("Okay, let's start")
names, scores = read_file()

if name in names:
    current_score = int(scores[names.index(name)])
    print(f'Your current score is: {current_score}')
    new_player = False
else:
    current_score = 0
    new_player = True

if len(options) == 0:
    current_score = game(current_score, default_options)
else:
    options = options.split(",")
    len_op = len(options)
    options += options
    current_score = game(current_score, options, len_op)

if new_player:
    append_file(name, current_score)
else:
    scores[names.index(name)] = current_score
    write_file(scores, names)
