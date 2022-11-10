## Pipe

[![Maintainability](https://api.codeclimate.com/v1/badges/159a73ad4b24d66bf0ed/maintainability)](https://codeclimate.com/github/mnogom/pipe/maintainability)
[![python-ci](https://github.com/mnogom/pipe/actions/workflows/python-ci.yaml/badge.svg)](https://github.com/mnogom/pipe/actions/workflows/python-ci.yaml)
[![Test Coverage](https://api.codeclimate.com/v1/badges/159a73ad4b24d66bf0ed/test_coverage)](https://codeclimate.com/github/mnogom/pipe/test_coverage)

### Import
```python
from pipe.pipe import Pipe
from pipe import utils as u
```

---
### Utils
* Real utils
  * `revargs` - replace first argument and second 
    ```python
    x = 2
    u.divide(x)(10)  # 0.2
    u.revargs(u.divide)(x)(10)()  # 5.0

    u.revargs(u.map)([1, 2, 3])(u.add(1))()  # [2, 3, 4]
    ```

  * `casc` - make any function cascade callable
    ```python
    #  1. With lambda functions
    u.casc(lambda x, y, z: x + y + z)(1)(2)(3)()  # 6

    #  2. With functions:
    @u.casc
    def fn(x, y, z):
        return x + y + z

    fn(1)(2)(3)()  # 6
    ```
  
  * `stt` - set argument last argument to any position
    ```python
    @u.casc
    def fn(a, b, c):
        return (a + b) * c
  
    x = 1
    
    # Default calls 'fn'
    fn(x)(2)(3)()  # 9
    fn(2)(3)(x)()  # 5

    # Place last argument to first position
    u.stt(0)(fn)(2)(3)(x)()  # 9
    ```
* Predicates:
```python
u.is_even(10)()  # True
u.is_gt(5)(4)()  # True
u.is_lt(5)(4)()  # False
u.is_eq(100)(100)()  # True
```
* Basic math
```python
u.add(1)(2)(3)(4)(5)()  # 15
u.sub(10)(2)(1)()  # 7
u.power(2)(10)() == 1024
u.multiply(1)(2)(3)(4)(5)()  # 120
u.divide(2048)(4)(4)(4)(4)(4)()  # 2

#  Complex maths
#    Let's try to calculate:
#      10 + (8 - 2 * 3) * (12 - 4) / 2 + 6 = 26

# Formatted
u.add(10)(
  u.divide(
      u.multiply(
          u.multiply(
              u.sub(8)(
                  u.multiply(2)(3)()
              )()
          )(
              u.sub(12)(4)()
          )()
      )()
  )(2)()
)(6)()

#  Same but one-line
u.add(10)(u.divide(u.multiply(u.multiply(u.sub(8)(u.multiply(2)(3)())())(u.sub(12)(4)())())())(2)())(6)()
```
* Basic array operations
```python
a = [1, 2, 3]
b = u.concat(a)([4, 5])([6])()  # [1, 2, 3, 4, 5, 6]
a == b  # False
```
```python
a = [1, 2, 3]
u.push(a)(4)(5)(6)()
a  # [1, 2, 3, 4, 5, 6]
```
* Conditions
```python
# Main functionality
a = u.iff(True)(1)(2)  # 1

# Complex examples:

#  1. execute in 'iff'
x = 5
b = u.iff(u.is_gt(x)(2)())(u.multiply(x)(10)())(u.divide(x)(10)())  # 50

#  2. execute after 'iff'
x = 5
b = u.iff(u.is_gt(x)(2)())(u.multiply(x)(10))(u.divide(x)(10))()  # 50

#  3. set output function and send arguments after 'iff':
x = 5
b = u.iff(u.is_gt(x)(2)())(u.multiply)(u.divide)(x)(10)()  # 50

```
* Higher-order functions
```python
u.map(u.multiply(10))([1, 2, 3])()  # [10, 20, 30]
u.filter(u.is_even)([1, 2, 3, 4])()  # [2, 4]
```
---

### Using pipe (in development)
```python
pipe = Pipe()
# ((1 + 1) * 2 - 1) / 3 + 3
pipe >> 1 >> u.add(1) >> u.multiply(2) >> u.revargs(u.sub)(1) >> u.revargs(u.divide)(3) >> u.add(3)

pipe = Pipe()
pipe >> [1, 2, 3] >> u.map(u.add(1)) >> u.filter(u.is_even) >> u.filter(u.casc(lambda x: x > 3))
pipe.result  # [4]
pipe.steps  # '[1, 2, 3] >> [2, 3, 4] >> [2, 4] >> [4]'

pipe = Pipe()
pipe >> 2 >> u.iff(u.is_even(pipe.result)())('even')('odd')
pipe.result  # even
```
