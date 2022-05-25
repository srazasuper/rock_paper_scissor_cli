import random
from utils import win_logic


def game():
    usr = input(" Choose R for  rock, P for paper and S for scissor ! ").upper()
    cmp = random.choice(['R', 'P', 'S'])
    if usr not in ['R', 'P', 'S']:
        return 'Wrong choice'

    if usr == cmp:
        return 'TIE'

    if win_logic(usr, cmp):
        return 'User win'

    return 'Computer win'


if __name__ == "__main__" :
    result = game()
    print(result)
