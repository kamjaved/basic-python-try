# 🧠 **1. What is List Comprehension?**

List comprehension is a **shorter and more readable way** to create new lists by looping over an iterable (like a list, range, or string) **in a single line**.

Think of it as similar to `Array.prototype.map()` or `filter()` in JavaScript, but with a cleaner syntax.

---

## ✅ 1. **Very Simple Example (Basic Mapping)**

**Task:** Create a new list of numbers from 0 to 4.

### 🐍 Python:

```python
new_list = [x for x in range(5)]
print(new_list)  # [0, 1, 2, 3, 4]
```

### 🟨 JavaScript Equivalent:

```javascript
const newList = [...Array(5).keys()];
console.log(newList); // [0, 1, 2, 3, 4]
```

You can also compare it to:

```javascript
const newList = Array.from({ length: 5 }, (_, x) => x);
```

---

## ✅ 2. **With Operation (Square each number)**

### 🐍 Python:

```python
squares = [x * x for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]
```

### 🟨 JS:

```javascript
const squares = [...Array(5).keys()].map((x) => x * x);
```

---

## ✅ 3. **With Condition (Filtering)**

**Task:** Get even numbers from 0 to 9

### 🐍 Python:

```python
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]
```

### 🟨 JS:

```javascript
const evens = [...Array(10).keys()].filter((x) => x % 2 === 0);
```

---

## ✅ 4. **If-Else in Comprehension (Ternary Style)**

**Task:** For numbers 0–4, return `'even'` if even else `'odd'`.

### 🐍 Python:

```python
labels = ['even' if x % 2 == 0 else 'odd' for x in range(5)]
print(labels)  # ['even', 'odd', 'even', 'odd', 'even']
```

### 🟨 JS:

```javascript
const labels = [...Array(5).keys()].map((x) => (x % 2 === 0 ? 'even' : 'odd'));
```

---

## ✅ 5. **Nested Loops (Cartesian Product)**

**Task:** Pair letters `['a', 'b']` with numbers `[1, 2]`

### 🐍 Python:

```python
pairs = [(letter, num) for letter in ['a', 'b'] for num in [1, 2]]
print(pairs)
# [('a', 1), ('a', 2), ('b', 1), ('b', 2)]
```

### 🟨 JS:

```javascript
const pairs = ['a', 'b'].flatMap((letter) =>
	[1, 2].map((num) => [letter, num])
);
```

---

## ✅ 6. **Flattening a 2D List**

### 🐍 Python:

```python
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [num for row in matrix for num in row]
print(flattened)  # [1, 2, 3, 4, 5, 6]
```

### 🟨 JS:

```javascript
const matrix = [
	[1, 2],
	[3, 4],
	[5, 6],
];
const flattened = matrix.flat(); // [1, 2, 3, 4, 5, 6]
```

Or if flat isn’t available:

```javascript
const flattened = matrix.reduce((acc, row) => acc.concat(row), []);
```

---

## ✅ 7. **With Function Call / Transformation**

### 🐍 Python:

```python
def double(x):
    return x * 2

doubled = [double(x) for x in range(5)]
print(doubled)  # [0, 2, 4, 6, 8]
```

### 🟨 JS:

```javascript
const double = (x) => x * 2;
const doubled = [...Array(5).keys()].map(double);
```

---

## ✅ 8. **Set/List/Dict Comprehension Variants**

### a) Set Comprehension (Remove duplicates automatically)

```python
unique = {x % 3 for x in range(10)}
print(unique)  # {0, 1, 2}
```

### b) Dictionary Comprehension

```python
d = {x: x**2 for x in range(5)}
print(d)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

JS analogy:

```javascript
const obj = Object.fromEntries([...Array(5).keys()].map((x) => [x, x * x]));
```

---

## ✍️ Practice Task for You:

**Task:**
Create a list of all numbers between 1 and 20 that are divisible by both 3 and 5, and store `"FizzBuzz"` instead of the number.

Try it using list comprehension.

---

<br/>
<br/>

# 2. Lambda Function

Perfect! Let's dive into **Python's `lambda` functions**, using the same approach as before—from **basic to advanced**, and always with **JavaScript comparisons** so it clicks with your MERN-stack background.

---

## 🧠 What is a `lambda` in Python?

A `lambda` in Python is a **small anonymous (nameless) function**, defined in a single line. It's Python’s way of writing a **function expression**—like an arrow function in JavaScript.

---

## 🔧 Syntax:

```python
lambda arguments: expression
```

This returns the result of the expression **implicitly**.

---

## ✅ 1. **Very Simple Example**

### 🐍 Python:

```python
add = lambda x, y: x + y
print(add(2, 3))  # 5
```

### 🟨 JavaScript Equivalent:

```javascript
const add = (x, y) => x + y;
console.log(add(2, 3)); // 5
```

---

## ✅ 2. **Using lambda inline (without naming it)**

This is where it's often used:

### 🐍 Python:

```python
print((lambda x: x * 2)(4))  # 8
```

### 🟨 JavaScript:

```javascript
console.log(((x) => x * 2)(4)); // 8
```

Just like you can define and immediately call arrow functions in JS.

---

## ✅ 3. **Using lambda with `map()`**

### 🐍 Python:

```python
nums = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, nums))
print(doubled)  # [2, 4, 6, 8]
```

### 🟨 JS Equivalent:

```javascript
const nums = [1, 2, 3, 4];
const doubled = nums.map((x) => x * 2);
console.log(doubled); // [2, 4, 6, 8]
```

---

## ✅ 4. **With `filter()`**

### 🐍 Python:

```python
evens = list(filter(lambda x: x % 2 == 0, range(10)))
print(evens)  # [0, 2, 4, 6, 8]
```

### 🟨 JS:

```javascript
const evens = [...Array(10).keys()].filter((x) => x % 2 === 0);
```

---

## ✅ 5. **With `sorted()` for custom sorting**

### 🐍 Python:

```python
words = ['banana', 'apple', 'cherry']
sorted_words = sorted(words, key=lambda word: len(word))
print(sorted_words)  # ['apple', 'banana', 'cherry']
```

### 🟨 JS:

```javascript
const words = ['banana', 'apple', 'cherry'];
const sortedWords = words.sort((a, b) => a.length - b.length);
```

---

## ✅ 6. **Used with `reduce()` (via `functools`)**

```python
from functools import reduce

nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
print(product)  # 24
```

### 🟨 JS:

```javascript
const nums = [1, 2, 3, 4];
const product = nums.reduce((x, y) => x * y);
```

---

## ✅ 7. **Lambda in Conditional Expressions (Ternary-style)**

### 🐍 Python:

```python
age_category = lambda age: "adult" if age >= 18 else "minor"
print(age_category(20))  # 'adult'
```

### 🟨 JS:

```javascript
const ageCategory = (age) => (age >= 18 ? 'adult' : 'minor');
```

---

## ⚠️ When **NOT** to use `lambda`:

-  If the function is more than **one expression long**, use `def`.
-  For **readability**, especially in complex logic.

---

## ✅ Real-World Use Cases:

| Use Case                                       | Python Lambda Used In              |
| ---------------------------------------------- | ---------------------------------- |
| Inline functions for `map`, `filter`, `reduce` | ✅                                 |
| Custom sort keys                               | ✅                                 |
| Quick conditionals or transforms               | ✅                                 |
| One-off callback-style logic                   | ✅                                 |
| Named utility functions                        | ❌ Better to use `def` for clarity |

---

## 📌 Summary for JS Devs:

| Concept           | JavaScript             | Python Equivalent            |
| ----------------- | ---------------------- | ---------------------------- |
| Arrow function    | `x => x * 2`           | `lambda x: x * 2`            |
| Array.map         | `arr.map(x => ...)`    | `map(lambda x: ..., arr)`    |
| Array.filter      | `arr.filter(x => ...)` | `filter(lambda x: ..., arr)` |
| One-liner ternary | `x => cond ? a : b`    | `lambda x: a if cond else b` |

---

Would you like to try a few mini lambda challenges or refactor regular functions into lambda for practice?
