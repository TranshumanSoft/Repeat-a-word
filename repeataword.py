word = str(input("What word do you want to repeat?"))
times = int(input(f"How many times do you want to repeat '{word}'?"))
counter = 0
while counter < times:
    counter = counter + 1
    print(word)