# exercise1
word = input("Enter a word: ")
characters = list(dict.fromkeys(list(word)))
dict = {}
for key,value in enumerate(word):
    if value in dict:
        dict[value].append(key)
    else:
        dict[value] = [key]
print(dict)


# exercise2
items_purchase = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20"
}
wallet = "$300"
remaining = int(wallet.replace("$","").replace(",",""))
items = list(items_purchase.keys())
items.sort()
items_afford = []

for i in items:
    price = int(items_purchase[i].replace("$","").replace(",",""))
    if remaining >= price:
        items_afford.append(i)
        remaining -= price
print(items_afford)

