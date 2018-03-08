file = open("aoc2_input.txt") #got this file via curl

sum_arr = 0

for line in file:
    int_line = [int(ele) for ele in line.split('\t') if ele]
    # honestly this bit feels like cheating because python makes it so easy
    sum_arr += max(int_line) - min(int_line)

print(sum_arr)
