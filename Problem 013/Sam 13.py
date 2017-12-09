data = open("data.csv", "r+")

list_of_numbers = [int(x.strip()) for x in  data.readlines()]
print(str(sum(list_of_numbers))[:10])