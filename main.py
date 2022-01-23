import random
number_pool = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


# protection from incorrect input


while True:
    length = int(input("How long number will be [1..9]? "))
    if 0 < length < 10:
        break
    else:
        print("Incorrect length, it must be a number between 1 and 9")

hidden_number = [0]
turns = 1
is_win = False


# Computer generates number, that have not to begin with 0 and does not contain similar numerics


def generate_number(length_of_number):
    hidden_number[0] = random.randint(1, 9)
    while len(hidden_number) < length_of_number:
        new_number = random.randint(0, 9)
        if new_number not in hidden_number:
            hidden_number.append(new_number)


# transform list to string, mb will be useful


def transform_to_str(rnd_list):
    hidden_number_str = ""
    for ele in rnd_list:
        hidden_number_str += str(ele)
    return hidden_number_str


try:
    generate_number(length)
    # print(transform_to_str(hidden_number))
except ValueError:
    print("Incorrect length, it must be a number between 1 and 9")


# check, if user's guess is equal to hidden number, or at list how much bulls and cows it contain


def guess_check(rnd_list):
    global is_win

    cows = 0
    bulls = 0
    for i in range(0, length):
        if int(rnd_list[i]) == int(hidden_number[i]):
            cows += 1
        for j in range(0, length):
            if int(rnd_list[i]) == int(hidden_number[j]):
                bulls += 1
    print(f"Bulls: {bulls}, cows: {cows} ")
    if (cows == int(length)) and (bulls == int(length)):
        is_win = True
    return is_win


# check if user input is available


def available_check(rnd_list):
    available = False
    if len(rnd_list) == length:

        for i in range(0, length):
            k = 1
            while k + i < length:
                if rnd_list[i] != rnd_list[k + i]:
                    k += 1
                    available = True
                else:
                    available = False
                    print(available)
                    break

    else:
        available = False
    return available


while not is_win and hidden_number != [0]:
    guess = list(input(f"Turn {turns}: Please, input your {length}-digit guess "))
    if available_check(guess):
        try:
            guess_check(guess)
            turns += 1
        except ValueError:
            print("incorrect input! Try again")
    else:
        print("incorrect input! Try again")
if is_win:
    print(f"Amazing! You beat me in {turns-1} turns!")