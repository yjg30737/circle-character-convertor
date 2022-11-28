# circle-character-convertor
Convert circle character into ordinary character

Currently number only.

## Method Overview
* `convert_circle_into_ord(circle_characters) -> None` - If you give the circle character(such as ③) divided by comma or space, this will convert them into ordinary characters and print them as a result.

## Example
```python
convert_circle_into_ord('''
④	①
②	⑤
⑤	④
③	⑤
''')
```

Result
```python
4
1
2
5
5
4
3
5
```
