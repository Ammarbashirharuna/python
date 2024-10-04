class TagCloud:
    #first we define a constructure 
    def __init__(self):
        #then we initialize a tags attrubute to an empty dictionary
        self.tags = {}
    #we can optionaly add a method like add 
    def add(self, tag):
        #here we should check the tag if its there we gonna set it to 1 otherwise we wanna increment it by oone
        #first we use get method to get an item by its key and set a default value if we dont have that  and increment it by one if we already have it
         self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1
    #lets take it to the next level i wanna be able to read the count of a tag using square bracket in this case we need to implement a magic method called get item
    def __getitem__(self, tag):
        return self.tags.get(tags.lower(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    #to be able to count the len of an item in the tagcloud class we have to implement the len method
    def __len__(self):
        return len(self.tags)
    #to iterate over it we should implement iter magic methods 
    def __iter__(self):
        return iter(self.tags)
    


#lets test our program  am gonna called an cloud object
cloud = TagCloud()
cloud.add("Java")
cloud.add("java")
cloud.add("java")
cloud.add("c++")
cloud.add("C++")
cloud.add("C++")

print(cloud.tags)

cloud = TagCloud()
cloud.add("python")
cloud.add("python")
cloud.add("python")
cloud.add("python")
print(cloud["PYTHON"])

