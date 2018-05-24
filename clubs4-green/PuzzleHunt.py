import random

random_nums = [39, 28, 485, 230, 103, 23, 103, 4, 20, 342, 934, 3490, 42, 90, 40, 394, 2827, 10, 6, 5, 1, 1, 5, 4, 1, 2, 6, 5, 30, 3234, 34, 765, 674, 458]
rand_index = 0
testing = True

def puzzle_randint(min_num, max_num):
    global testing
    if testing:
        diff = max_num - min_num + 1
        global rand_nums 
        global rand_index
        rand_num = (random_nums[rand_index] % diff) + min_num
        rand_index = (rand_index + 1) % len(random_nums)
        return rand_num
    else:
        return random.randint(1,6)