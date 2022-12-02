elf_inventory = []
elf_totals = []

with open('day1_input.txt') as cal_list:
    for line in cal_list:
        line = line.strip()
        try:
            cal_item = int(line)
            elf_inventory.append(cal_item)
            # append that result to elf inventory to be added up
        except ValueError:
            # this happens when we hit an empty line
            elf_tot = sum(elf_inventory)
            # this totals the list, and adds the result to a variable
            elf_totals.append(elf_tot)
            # this adds that result to a second list
            elf_inventory.clear()
            # this clears the first list before starting another loop
            continue

print(max(elf_totals))
# this prints the highest number in the second list: the elf with the most calories

# for Day 1 second half (finding the total sum of the top three elves):

elf_totals.sort()
elf_top_three = elf_totals[-3:]
print(elf_top_three)
print(sum(elf_top_three))
