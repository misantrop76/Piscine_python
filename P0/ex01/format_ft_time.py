import time

start = time.time()

standard = f"{start:,.4f}"
scientific = f"{start:.2e}"
date = time.strftime("%b %d %Y", time.localtime())

print(f"Seconds since January 1, 1970: {standard}\
 or {scientific} in scientific notation")
print(date)
