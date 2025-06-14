## lseg-platform-assignment
LSEG Platform Assignment

### Summary
We have a nested dictionary/Json, we would like a function that you pass in the object and a key and get back the
value. 

### Example Usage

```
python3 main.py -obj '{"a":{"b":{"c":"d"}}}' -k 'a/b/c'
## RESULT VALUE : d

python3 main.py -obj '{"x":{"y":{"z":"a"}}}' -k 'x/y/z'
## RESULT VALUE : d

python3 main.py -obj '{"f":{"g":{"h":{"i":{"j":"k"}}}}}' -k 'f/g/h/i/j'
## RESULT VALUE : k
```

--- 

## Run Unittest

```
python3 test_main.py -v 

test_five_level (__main__.TestGetNestedValue) ... ok
test_invalid_key (__main__.TestGetNestedValue) ... ok
test_key_not_match (__main__.TestGetNestedValue) ... ok
test_object_invalid_type (__main__.TestGetNestedValue) ... ok
test_success (__main__.TestGetNestedValue) ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
```
