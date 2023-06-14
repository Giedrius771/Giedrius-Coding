# 1 uzduotis##
import numpy as np

vektorius = np.arange(1, 11)
print(vektorius)
##### 2 ####
vektorius2 = np.zeros(10)
print(vektorius2)
#### 3 ###
vektoriusvienetai = np.ones(10)
print(vektoriusvienetai)
#### 4 uzduotis###
vektorius_ketvertai = np.full(10, 4)
print(vektorius_ketvertai)
#### 5 #####
vektoriusNI = np.arange(0, 101, 2)
print(vektoriusNI)
#### 6 #####
matrica = np.arange(1, 26).reshape(5, 5)
print(matrica)
##### 7 #####
matrica = np.arange(1, 26).reshape(5, 5)
print(matrica)

skaičius = matrica[2, 1]
print(skaičius)
## 8 ###
matrica = np.arange(1, 26).reshape(5, 5)
print(matrica)

eilutė = matrica[-1, :]
print(eilutė)
### 9 ####
matrica = np.arange(1, 26).reshape(5, 5)
print(matrica)

submatrica = matrica[:3, :3]
print(submatrica)
#### 10 ###

matrica = np.arange(1, 26).reshape(5, 5)
print(matrica)

submatrica = matrica[1:4, 1:]
print(submatrica)

##### 11 ####

matrica = np.arange(1, 26).reshape(5, 5)
print(matrica)

submatrica = matrica[3:, :]
print(submatrica)
#### 12 #####
np.random.seed(0)
vektorius = np.random.rand(20)
print(vektorius)
#### 13 ####
vektorius = np.random.rand(10)
print(vektorius)

didžiausia_reikšmė = np.max(vektorius)
indeksas_didžiausiai_reikšmei = np.argmax(vektorius)

print("Didžiausia reikšmė:", didžiausia_reikšmė)
print("Indeksas didžiausiai reikšmei:", indeksas_didžiausiai_reikšmei)
##### 14 ####
import numpy as np

vektorius = np.array([18, 87, 3, 2, 41, 23, 11])
mažiausia_reikšmė = np.min(vektorius)
indeksas_mažiausiai_reikšmei = np.argmin(vektorius)

print("Mažiausia reikšmė:", mažiausia_reikšmė)
print("Jos indeksas:", indeksas_mažiausiai_reikšmei)
print(mažiausia_reikšmė)

##### 15 #####
mport
numpy as np

vektorius = np.array([18, 87, 3, 2, 41, 23, 11])
mažiausia_reikšmė = np.min(vektorius)
indeksas_mažiausiai_reikšmei = np.argmin(vektorius)

print("Mažiausia reikšmė:", mažiausia_reikšmė)
print("Jos indeksas:", indeksas_mažiausiai_reikšmei)
print(mažiausia_reikšmė)

print(vektorius.dtype)
#### 16 ####
import numpy as np

vector = np.arange(1, 101)
result = vector[vector > 90]

print(result)
##### 17 ####
import numpy as np

vector = np.arange(1, 101)
result = vector[vector % 7 == 0]

print(result)
###### 18 ####
import numpy as np

matrix = np.linspace(0.025, 1.0, num=40).reshape(5, 8)

print(matrix)
###### 19 ####
import numpy as np

numbers = np.arange(2, 1000)
squared = numbers ** 0.5
matrix = numbers[squared % 1 == 0].reshape(6, 5)
print(matrix)
##### 20 #####
import numpy as np


def pirminis(num):
    if num < 2:
        return False
    for i in range(2, int(np.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


vektorius = np.arange(1, 101)
vectorized_is_prime = np.vectorize(pirminis)
primes = vectorized_is_prime(vektorius)
primes_vector = vektorius[primes]
print(primes_vector)
#########
