words = "i think how this time around am where very lazy about learning"
preq = {}
for i in words:
    if i in preq:
        preq[i] += 1
    else:
        preq[i] = 1
values = sorted(preq.items(), key=lambda kv:kv[1], reverse=True)
print(values[0])

greetig = "hi sir welcome to our place when i wanna do something that i can use it so to delivered your time and date"
prewuency = {}
for i in greetig:
    if i in prewuency:
        prewuency[i] += 1
    else:
        prewuency[i] = 1
values = sorted(prewuency.items(), key=lambda kv:kv[1], reverse=True)
print(values[0])