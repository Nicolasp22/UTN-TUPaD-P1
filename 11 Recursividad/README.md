# Ejercicios de Recursividad en Python

Este proyecto contiene una serie de **8 ejercicios resueltos** utilizando funciones **recursivas** en Python. Cada uno aborda un problema clásico de programación y está enfocado en comprender y aplicar la recursividad de forma práctica.

---

## 🧮 1. Factorial de números del 1 al N

Calcula el factorial de todos los números desde 1 hasta un número ingresado por el usuario.

- Utiliza una función recursiva `factorial(n)`.
- El factorial de un número `n` se define como `n! = n * (n-1)!`, con `0! = 1`.

📌 **Entrada esperada:** número entero positivo  
📌 **Salida esperada:** lista de factoriales del 1 al N

---

## 🌀 2. Serie de Fibonacci hasta una posición

Muestra la serie de Fibonacci completa hasta una posición indicada por el usuario.

- Se emplea una función recursiva `fibonacci(n)` que sigue la relación `F(n) = F(n-1) + F(n-2)`.

📌 **Entrada esperada:** número entero ≥ 0  
📌 **Salida esperada:** los términos de la serie desde `F(0)` hasta `F(n)`

---

## ⚡ 3. Potencia de un número

Calcula la potencia de una base elevada a un exponente entero no negativo usando recursión.

- Fórmula utilizada: `b^e = b * b^(e-1)`
- Caso base: cualquier número elevado a 0 es 1.

📌 **Entrada esperada:** base y exponente  
📌 **Salida esperada:** resultado de la potenciación

---

## 🔁 4. Conversor decimal a binario

Convierte un número entero positivo a su representación binaria **sin usar funciones de conversión de Python ni cadenas invertidas**.

- Se aplica la lógica `bin(n) = bin(n // 2) + str(n % 2)`

📌 **Entrada esperada:** número entero positivo  
📌 **Salida esperada:** número binario en forma de cadena

---

## 🔍 5. Verificador de palíndromos

Verifica si una palabra ingresada **es un palíndromo**, es decir, se lee igual de izquierda a derecha que de derecha a izquierda.

- Se compara recursivamente la primera y última letra.

📌 **Entrada esperada:** palabra sin espacios ni tildes  
📌 **Salida esperada:** `True` o `False`

---

## ➕ 6. Suma de los dígitos de un número

Suma todos los dígitos de un número entero positivo **sin convertirlo a cadena**.

- Usa operaciones matemáticas: `%` y `//`
- Caso base: si el número es menor que 10, retorna él mismo.

📌 **Entrada esperada:** número entero positivo  
📌 **Salida esperada:** suma de sus dígitos

---

## 🧱 7. Conteo de bloques apilados

Suma la cantidad total de bloques en una estructura de tipo pirámide, donde el nivel 1 tiene 1 bloque, el 2 tiene 2, etc.

- Se basa en la suma recursiva `n + (n-1) + ... + 1`

📌 **Entrada esperada:** cantidad de niveles o bloques base  
📌 **Salida esperada:** total de bloques apilados

---

## 🔢 8. Contador de dígitos

Cuenta cuántas veces aparece un dígito específico dentro de un número **sin convertirlo en string**.

- Divide el número y compara el último dígito con el objetivo.

📌 **Entrada esperada:** número entero y dígito (0 a 9)  
📌 **Salida esperada:** cantidad de veces que aparece ese dígito


## Archivo ejemplos.py
La carpeta contiene un archivo llamado ejemplos.py que sirvió como práctica para entender conceptos de recursividad y realizar ejercicios adicionales.