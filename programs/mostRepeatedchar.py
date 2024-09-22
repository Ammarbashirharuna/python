words = "i think how this time around am where very lazy about learning"
preq = {}
for i in words:
    if i in preq:
        preq[i] += 1
    else:
        preq[i] = 1
values = sorted(preq.items(), key=lambda kv:kv[1], reverse=True)
print(values[0])