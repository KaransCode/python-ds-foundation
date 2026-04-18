import numpy as np

rng = np.random.default_rng(seed=1)

ages = rng.integers(1,100,size=(2,10))
print(ages)
child = ages[ages < 13]
teen = ages[(ages > 12) & (ages < 20)]
adult = ages[(ages > 20) & (ages < 45)]
old = ages[(ages > 45) & (ages < 100)]
even = ages[ages % 2 == 0]
odd = ages[ages % 2 != 0]

print(f"Child : {child}")
print(f"Teen : {teen}")
print(f"Adult : {adult}")
print(f"Old : {old}")
print(f"Even : {even}")
print(f"Odd : {odd}")

# where function

adults = np.where(ages >= 18, ages, -1)
print(adults)