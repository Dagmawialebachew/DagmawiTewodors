#
# prices = [10, 20, 30]
# total = 0
# for price in prices:
#     total += price
#     print(f'Total: {total}')
# for x in range(4):
#     for y in range(4):
#         print(f'{x}, {y}')

# for x in ['xxxxx', 'xx', 'xxxxx', 'xx', 'xx']:
#     print(x)
# for x_count in [1,1,1,1,5]:
#     output = ''
#     for count in range(x_count):
#          output += 'x'
#     print(output)

largest_number_list = [100, 92 ,200 ,92 , 91]
max = largest_number_list[1]
for identifier in largest_number_list:
    if identifier > max:
        max = identifier
print(max)

#2d lists
# matrix math concept [
#     2 3 3
#     4 5 6
# ]

matrix = [
    [2, 3, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][0])
