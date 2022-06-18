from TinyStatistician import TinyStatistician
import numpy as np

print("TEST 1 : a = [1, 42, 300, 10, 59]")
a = [1, 42, 300, 10, 59]
stat = TinyStatistician()
print("mean =", stat.mean(a))
print("median =", stat.median(a))
print("quartile =", stat.quartile(a))
print("percentile 10 =", stat.percentile(a, 10))
print("percentile 28 =", stat.percentile(a, 28))
print("percentile 83 =", stat.percentile(a, 83))
print("var =", stat.var(a))
print("std =", stat.std(a))

print("\nTEST 2 : a = np.array([[1], [2], [3], [4], [5], [6], \
[7], [8], [9], [10], [1], [2], [3], [4], [5]])")
a = np.array([[1], [2], [3], [4], [5], [6], [7],
             [8], [9], [10], [1], [2], [3], [4], [5]])
print("mean =", stat.mean(a))
print("median =", stat.median(a))
print("quartile =", stat.quartile(a))
print("percentile 0 =", stat.percentile(a, 0))
print("percentile 100 =", stat.percentile(a, 100))
print("percentile 25 =", stat.percentile(a, 25))
print("var =", stat.var(a))
print("std =", stat.std(a))

print("\nTEST 3 : Error tests:")
print(stat.mean("Hello"))
print(stat.median(1))
print(stat.quartile((1.0, 2.0)))
print(stat.percentile(a, 110))
print(stat.percentile(a, "bada"))
print(stat.percentile(a, -83))
print(stat.percentile([], 12))
print(stat.var(["Hello", "World"]))
