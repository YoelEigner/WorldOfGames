from Utils import SCORES_FILE_NAME


def add_score(difficulty):
    points_of_winning = difficulty
    current_score = open(SCORES_FILE_NAME, 'r')
    new_score = int(current_score.read()) + int(points_of_winning)
    file = open(SCORES_FILE_NAME, 'w')
    file.write(str(new_score))

add_score(5)