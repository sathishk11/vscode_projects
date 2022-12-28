#dictionary
a={"URL1":"google.com", "URL2":"demoqa.com"}   #{key, value of key}
b={1:"sathish", 2:"rishi", 3:"navayugan"}
print(b[1])
print(a["URL2"])
b[3]="amazon.com" #add method
print(b)
print(b[3])
print(a.get("URL2"))  #get method
print(b.keys()) # it will print how many key is there
print(b.items()) # it will print full details, key and values
print(b.values()) # it will print the values
print(b.pop(3)) # delete particular value
print(b)
print(b.popitem()) # delete last value
b.update({2:"navayugan", 3:"rishi"})  # update key and value
print(b)
b.setdefault(4,"kumar") # update key and value
print(b)