import random
def random_nos():
    randomness: int = random.randint(1,1000)
    random_no: [int]  = list(range(randomness))
    return random_no

if __name__ == "__main__":
    print(f"list of random number from 1 to 1000 is: {random_nos()}")



