"""Generate sales report showing total melons each salesperson sold."""


# My way is under this


salespeople_and_melons_sold = {}

# Opens up the file 
sales_file = open('sales-report.txt')

# Iterates through each line of the text file
for line in sales_file:
    # Strips white space on the right of the text file
    line = line.rstrip()
    # Splits each line by the pipe (so into 3 parts)
    entries = line.split('|')

    # Sets salesperson equal to entries[0]
    salesperson = entries[0]
    # Sets melons to an int of entries[2]
    melons = int(entries[2])

    salespeople_and_melons_sold[salesperson] = salespeople_and_melons_sold.get(salesperson,0) + melons

# Iterates through both lists to print how much they sold
for salespeople, sales in salespeople_and_melons_sold.items():
    print(f"{salespeople} sold {sales} melons")



# There original way is down below

# salespeople = []
# melons_sold = []

# # Opens up the file 
# # Could have named the file better
# f = open('sales-report.txt')

# # Iterates through each line of the text file
# for line in f:
#     # Strips white space on the right of the text file
#     line = line.rstrip()
#     # Splits each line by the pipe (so into 3 parts)
#     entries = line.split('|')
#     # Sets salesperson equal to entries[0]
#     salesperson = entries[0]

#     # Sets melons to an int of entries[2]
#     melons = int(entries[2])

#     # Checks is salesperson is in the folder with all of the salespeople above, 
#     # if so, just adds to the melons they sold
#     # Would be better if data was arranged in a dictionary so position doesn't 
#     # need to be found
#     if salesperson in salespeople:
#         position = salespeople.index(salesperson)
#         melons_sold[position] += melons
        
#     # adds salesperson and melons sold to two diff folders if not in their already
#     # could have just .get and not had an if and else statement
#     else:
#         salespeople.append(salesperson)
#         melons_sold.append(melons)

# # Iterates through both lists to print how much they sold
# for i in range(len(salespeople)):
#     print(f'{salespeople[i]} sold {melons_sold[i]} melons')