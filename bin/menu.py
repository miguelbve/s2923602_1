YorN = ["Y", "N"]
def select_memory():
    another_game = input("Hello, would you like to see the laptop with the most memory (Y/N)?")
    another_game = correct_input(another_game, YorN)
    while another_game == "Y":
        pass


def correct_input(user_input, acceptable_answers):
    while user_input not in acceptable_answers:
        user_input = input("That doesn't sound right, can you repeat? For example: " + acceptable_answers[0])
    return user_input