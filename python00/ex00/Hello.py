# ----------------------- Different type of structures --------------------------- #

# LIST : duplicate elems, different types ok, mutable, ordered
# Utile lorsqu'on a une suite d'elems, l'ordre est important et qu'on doit modifier
ft_list = ["Hello", "tata!"]

# TUPLE : duplicate elems, different types ok, immutable, ordered
# Utile lorsqu'on veut une structure fixe (Coord, RGB) ou que les valeurs ne changent pas
ft_tuple = ("Hello", "toto!")

# SET : no dup, mutable, unordered, math operators
# Utile pour eliminer les doublons, tester l'appartenance, comparaisons
ft_set = {"Hello", "tutu!"}

# DICTIONARY : key-value, no dup, mutable, ordered
# Utile pour associer des donnes, representer un objet, acces rapide par nom
ft_dict = {"Hello" : "titi!"}



# --------- Modifying each data object to display the required greetings ----------#

ft_list.remove("tata!")
ft_list.append("World!")

ft_tuple = ("Hello", "France!")

ft_set.remove ("tutu!")
ft_set.add("Paris!")

ft_dict["Hello"] = "42Paris!"



# ------------------------------ Printing the result ------------------------------#

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
