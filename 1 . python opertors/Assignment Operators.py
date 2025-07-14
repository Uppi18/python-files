 # Assignment operators are used to assign values to variables.
 # they can also be used to update the variable’s value using arithmetic or bitwise operations.

| Operator | Description             | Example               | Equivalent To
| -------- | ----------------------- | --------------------- | ------------- |
| `+=`     | Add and assign          | `x += 3`              | `x = x + 3`   |
| `-=`     | Subtract and assign     | `x -= 2`              | `x = x - 2`   |
| `*=`     | Multiply and assign     | `x *= 4`              | `x = x * 4`   |
| `/=`     | Divide and assign       | `x /= 2`              | `x = x / 2`   |
| `//=`    | Floor divide and assign | `x //= 2`             | `x = x // 2`  |
| `%=`     | Modulo and assign       | `x %= 3`              | `x = x % 3`   |
| `**=`    | Power and assign        | `x **= 2`             | `x = x ** 2`  |
| `&=`     | Bitwise AND and assign  | `x &= 2`              | `x = x & 2`   |
| \`       | | Bitwise OR and assign | \`x           | = 2\` | \`x = x | 2\` |
| `^=`     | Bitwise XOR and assign  | `x ^= 2`              | `x = x ^ 2`   |
| `>>=`    | Right shift and assign  | `x >>= 1`             | `x = x >> 1`  |
| `<<=`    | Left shift and assign   | `x <<= 1`             | `x = x << 1`  |


x = 10

x += 5   # x = 10 + 5 = 15
print("x += 5:", x)

x *= 2   # x = 15 * 2 = 30
print("x *= 2:", x)

x -= 10  # x = 30 - 10 = 20
print("x -= 10:", x)

x //= 3  # x = 20 // 3 = 6
print("x //= 3:", x)
