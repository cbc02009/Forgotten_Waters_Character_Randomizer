
import random

name_list = [
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
    i = sysrand.randint(0, (len(name_list) - 1))

    print(f"You are The {name_list[i]} Pirate. Please print pages {2 * i + 1} - {2 * i  + 2} from playersheets.pdf")
