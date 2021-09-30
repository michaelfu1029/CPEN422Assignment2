import zlib
import time

curr = 0
seen = {}
t = time.time()
while zlib.crc32(str.encode(str(curr))) not in seen:
    seen[zlib.crc32(str.encode(str(curr)))] = curr
    curr += 1

print("TOOK " + str(time.time() - t))
print(str(curr) + " AND " + str(seen[zlib.crc32(str.encode(str(curr)))]))



x = b'78b847dd0d94cdd72ffcd0a46fab6c6e'
target = zlib.crc32(x)
curr = 0
t = time.time()
while zlib.crc32(str.encode(str(curr))) != target:
    if curr % 10000000 == 0:
        print(curr)
    curr += 1
    
print("TOOK " + str(time.time() - t))
print(curr)