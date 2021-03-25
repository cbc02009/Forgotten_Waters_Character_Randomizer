
import random

name_list = [
]

job_list = [
    'Seeker',
    'All-Seeing',
    'Grifter',
    'Assassin',
    'Survivor',
    'Debater',
    'Orphan',
    'Sea Serpent',
    'Cannonwright',
    'Gold Coat',
    'Duelist',
    'Alchemist',
    'Thespian',
    'Skeleton',
    'Safety',
    'Parent',
    'Trickster',
    'Lovesick',
    'Seasick',
    'Culinary',
    'Doomed'
]

if __name__ == '__main__':

    sysrand = random.SystemRandom()

    result_list = []
    rand_list = []

    num_of_players = len(name_list)

    for index in range(num_of_players):

        #Re-roll if already in list:
        while True:
            # i = random.randint(0, 20)
            rand = sysrand.randint(0, 20)

            print(f"Random: {rand}")

            if rand not in rand_list:
                result_list.append({
                    'index': index,
                    'name': name_list[index],
                    'job': job_list[rand],
                    'p1': 2 * rand + 1,
                    'p2': 2 * rand + 2
                })

                rand_list.append(rand)

                break

            else:
                print("Rerolling")

    for entry in result_list:
        print(f"{entry['name']}, you are The {entry['job']} Pirate. Please print pages {entry['p1']} - {entry['p2']} from playersheets.pdf")
