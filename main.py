from linkedlists import List


l = List(0)
for i in range(1, 6):
    l.append(i)

l.fullswap()
l.print_list(backwards=True)
