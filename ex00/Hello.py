ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}
# #your code here
ft_set.remove("tutu!")
ft_set.add("Le Havre!")
ft_set.remove("Hello")
ft_set.add("Hello")
ft_list[1] = "World!"
ft_tuple = ("Hello", "France!")
ft_dict["Hello"] = "42LeHavre!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)