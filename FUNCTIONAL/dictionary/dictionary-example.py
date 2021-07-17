
def main1():
    month = {'January': 31, 'February': 28, 'March': 31,  'April': 30, 'May': 31, 'June': 30, 
    'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}
    for k, v in month.items():
        print('{} has {} days'.format(k, v))

# def main1()


def getScores():
    return {'Evelyn': 22, 'Helen': 33,'George': 33, 'Alice': 22}

def searchScore(scores, name):
    return scores.get(name, 'Not recorded')

def main():
    scores = getScores() 
    # print(scores)
    while True:
        name = input("Enter name of student or <ENTER> to end: ").capitalize()
        if name == '': break
    print(searchScore(scores, name))

main()