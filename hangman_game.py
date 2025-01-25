import random

hangman_art ={0:("   ",
                 "   ",
                 "   "),
              1:(" O ",
                 "   ",
                 "   "),
              2:(" O ",
                 " | ",
                 "   "),
              3:(" O ",
                 "/| ",
                 "   "),
              4:(" O ",
                 "/|\\",
                 "   "),
              5:(" O ",
                 "/|\\",
                 "/  "),
              6:(" O ",
                 "/|\\",
                 "/ \\"),
              }
words = ("aardvark", "alligator", "alpaca", "ant", "anteater", "antelope", "ape", "armadillo", "baboon", "badger", "bat", "bear", "beaver", "bee", "bison", "boar", "buffalo", "butterfly", "camel", "capybara", "caribou", "cat", "caterpillar", "cattle", "chamois", "cheetah", "chicken", "chimpanzee", "chinchilla", "chough", "clam", "cobra", "cockroach", "cod", "coyote", "crab", "crane", "crocodile", "crow", "curlew", "deer", "dinosaur", "dog", "dogfish", "dolphin", "donkey", "dormouse", "dotterel", "dove", "dragonfly", "duck", "dugong", "dunlin", "eagle", "echidna", "eel", "eland", "elephant",  "elk", "emu", "falcon", "ferret", "finch", "fish", "flamingo", "fly", "fox", "frog", "gaur", "gazelle", "gerbil", "giraffe", "gnat", "gnu", "goat", "goldfinch", "goldfish", "goose", "gorilla", "goshawk", "grasshopper", "grouse", "guanaco", "gull", "hamster", "hare", "hawk", "hedgehog", "heron", "herring", "hippopotamus", "hornet", "horse", "human", "hummingbird", "hyena", "ibex", "ibis", "jackal", "jaguar", "jay", "jellyfish", "kangaroo", "kingfisher", "koala", "kookabura", "kouprey", "kudu", "lapwing", "lark", "lemur", "leopard", "lion", "llama", "lobster", "locust", "loris", "louse", "lyrebird", "magpie", "mallard", "manatee", "mandrill", "mantis", "marten", "meerkat", "mink", "mole", "mongoose", "monkey", "moose", "mosquito", "mouse", "mule", "narwhal", "newt", "nightingale", "octopus", "okapi", "opossum", "oryx", "ostrich", "otter", "owl", "ox", "oyster", "panda", "panther", "parrot", "partridge", "peafowl", "pelican", "penguin", "pheasant", "pig", "pigeon", "polar-bear", "pony", "porcupine", "porpoise", "quail", "quelea", "quetzal", "rabbit", "raccoon", "rail", "ram", "rat", "raven", "red-deer", "red-panda", "reindeer", "rhinoceros", "rook", "salamander", "salmon", "sand-dollar", "sandpiper", "sardine", "scorpion", "seahorse", "seal", "shark", "sheep", "shrew", "skunk", "snail", "snake", "sparrow", "spider", "spoonbill", "squid", "squirrel", "starling", "stingray", "stoat", "stork", "swallow", "swan", "tapir", "tarsier", "termite", "tiger", "toad", "trout", "turkey", "turtle", "viper", "vulture", "wallaby", "walrus", "wasp", "weasel", "whale", "wildcat", "wolf", "wolverine", "wombat", "woodcock", "woodpecker", "worm", "wren", "yak", "zebra")

def display_man(wrong_guesses):
    print("---------------------")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("---------------------")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    is_running = True
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()

    print("-----Hangman Game-----")

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)

        guess = input("Enter a letter : ")
        guess = guess.lower()

        if len(guess) !=1 or not guess.isalpha() :
            print("Invalid Entry")
            continue
        if guess in guessed_letters:
            print("You've already guessed this letter")
            continue
        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        
        else:
            wrong_guesses += 1

        if "_" not in hint:
            print("Congratulations! You've guessed the word.")
            display_answer(answer)
            is_running = False
        elif wrong_guesses >= len(hangman_art)-1:
            print(f"You've lost the game")
            is_running = False



if __name__ == "__main__":
    main()