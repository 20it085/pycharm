#list
Downtown = ["Dev", "Vaibhav", "Riken", "Badal", "jinal"]
print(Downtown)
Downtown.remove("jinal")
print(Downtown)
Downtown.append("jinal")
print(Downtown)
a = Downtown.count("Dev")
print(a)

#tapple
downtown = ("Dev", "Vaibhav", "Riken", "Badal", "jinal")
print(downtown)
# downtown[1]="Prince"

a = 1
b = 2
# temp = a
# a = b
# b = temp
a,b = b,a
print(a,b)

#Dictionary
dt = {"Dev":"IT", "Vaibhav":"CS", "Riken":"CS", "Badal":"DCS", "Jinal":"BBA" }
ht = {"Dev":"IT", "Vaibhav":"CS", "Riken":{"CS":"top", "IT":"nop"}, "Badal":"DCS", "Jinal":"BBA" }
print(dt)
print(dt["Dev"])
dt["Prince"] = "IT2"
print(dt)
del dt["Prince"]
print(dt)

print(ht)
print(ht["Riken"])
print((ht["Riken"]["CS"]))
print(ht.get("Riken"))
print(ht.items())
print(ht.keys())
rt = ht.copy()
print(rt)
del rt["Riken"]
print(rt)
print(ht)

#set
l = [1,2,3,4]
s = set(l)
print(s)
s1 = s.union({1,5,6})
print(s1)
s2 = s.intersection(1,3, 5)
print(s,s2)

