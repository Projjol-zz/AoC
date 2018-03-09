file = open("aoc2_input.txt") #got this file via curl

sum_arr = 0

for line in file:
    int_line = [int(ele) for ele in line.split('\t') if ele]
    # honestly this bit feels like cheating because python makes it so easy
    sum_arr += max(int_line) - min(int_line)

print(sum_arr)

# part 2 of the problem, input file is the same
file = open("aoc2_input.txt")
sum_arr = 0
for line in file:
    int_line = [int(ele) for ele in line.split('\t') if ele]
    int_line.sort()
    for ele in int_line:
        for comp_val in int_line:
            if ele%comp_val == 0 and ele!= comp_val:
                sum_arr += ele/comp_val

print(sum_arr)