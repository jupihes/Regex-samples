# My Regex notes and samples
My tries on Regex in Python
 

1. Summary cheatsheet 
2. Some notes on for Persian text
3. [Pattern parser creation](https://github.com/jupihes/Regex-samples/blob/main/code.py)

## Cheatsheet
```
Character classes
.	any character except newline
\w\d\s	word, digit, whitespace
\W\D\S	not word, digit, whitespace
[abc]	any of a, b, or c
[^abc]	not a, b, or c
[a-g]	character between a & g
Anchors
^abc$	start / end of the string
\b\B	word, not-word boundary
Escaped characters
\.\*\\	escaped special characters
\t\n\r	tab, linefeed, carriage return
Groups & Lookaround
(abc)	capture group
\1	backreference to group #1
(?:abc)	non-capturing group
(?=abc)	positive lookahead
(?!abc)	negative lookahead
Quantifiers & Alternation
a*a+a?	0 or more, 1 or more, 0 or 1
a{5}a{2,}	exactly five, two or more
a{1,3}	between one & three
a+?a{2,}?	match as few as possible
ab|cd	match ab or cd
```



Regex in Python

```
Character classes
.	any character except newline
\w\d\s	word, digit, whitespace
\W\D\S	not word, digit, whitespace
[abc]	any of a, b, or c
[^abc]	not a, b, or c
[a-g]	character between a & g
Anchors
^abc$	start / end of the string
\b\B	word, not-word boundary
Escaped characters
\.\*\\	escaped special characters
\t\n\r	tab, linefeed, carriage return
Groups & Lookaround
(abc)	capture group
\1	backreference to group #1
(?:abc)	non-capturing group
(?=abc)	positive lookahead
(?!abc)	negative lookahead
Quantifiers & Alternation
a*a+a?	0 or more, 1 or more, 0 or 1
a{5}a{2,}	exactly five, two or more
a{1,3}	between one & three
a+?a{2,}?	match as few as possible
ab|cd	match ab or cd
```



| Regular Expressions | Description                                              |
| ------------------- | -------------------------------------------------------- |
| foo.*               | # Matches any string starting with foo                   |
| \d*                 | # Match any number decimal digits                        |
| [a-zA-Z]+           | # Match a sequence of one or more letters                |
| text                | Match literal text                                       |
| .                   | Match any character except newline                       |
| ^                   | Match the start of a string                              |
| $                   | Match the end of a string                                |
| *                   | Match 0 or more repetitions                              |
| +                   | Match 1 or more repetitions                              |
| ?                   | Match 0 or 1 repetition                                  |
| +?                  | Match 1 or more, as few as possible                      |
| *?                  | Match 0 or more, as few as possible                      |
| {m,n}               | Match m to n repetitions                                 |
| {m,n}?              | Match m to n repetitions, few as possible                |
| [...]               | Match a set of characters                                |
| [^...]              | Match characters, not in a set                           |
| A \| B              | Match A or B (...) Match regex in parenthesis as a group |
| \number             | Matches text matched by the previous group               |
| \A                  | Matches start of the string                              |
| \b                  | Matches empty string at beginning or end of the word     |
| \B                  | Matches empty string not at begin or end of the word     |
| \d                  | Matches any decimal digit                                |
| \D                  | Matches any non-digit                                    |
| \s                  | Matches any whitespace                                   |
| \S                  | Matches any non-whitespace                               |
| \w                  | Matches any alphanumeric character                       |
| \W                  | Matches characters not in                                |
| \w \Z               | Match at end of the string.                              |
| \\                  | Literal backslash                                        |





- Difference between `Search` and `match`

​	   - if pattern not matched in `search` $\to$ result is `None`

``` python
import re
text = 'john.smith@gmail.com'
re.search(r'\S+@\S+\.\S+', text)
d = re.search(r'\S+@\S+\.\S+', text)
d.span()
```



```python
text1 = 'john.smithgmail.com'
d = re.search(r'\S+@\S+\.\S+', text1)
d
d == None
Out[14]: True

```

Note `None` versus `0` in your coding!

```python
text = 'Let’s say that we flipped 100 coins and observed 70 heads. We would like to use these data to test the hypothesis that the true probability is 0.5. First let’s generate our data, simulating 100,000 sets of 100 flips. We use such a large number because it turns out that it’s very rare to get 70 heads, so we need many attempts in order to get a reliable estimate of these probabilties. This will take a couple of minutes to complete.'

re.findall(r'(\d+)',text)
Out[16]: ['100', '70', '0', '5', '100', '000', '100', '70']
```



findall

subs

```
text = 'salam jadi. salam ali. salam hesam. salam sara. salam baba.'

re.sub(r'[sS]alam (\w+)\.','Hi',text)
Out[18]: 'Hi Hi Hi Hi Hi'

re.sub(r'[sS]alam (\w+)\.','Hi \g<1>',text)
Out[19]: 'Hi jadi Hi ali Hi hesam Hi sara Hi baba'

re.sub(r'[sS]alam (\w+)\.','Hi \g<1>.',text)
Out[20]: 'Hi jadi. Hi ali. Hi hesam. Hi sara. Hi baba.'

re.sub(r'[sS]alam (\w+)\.','Hi \g<0>.',text)
Out[21]: 'Hi salam jadi.. Hi salam ali.. Hi salam hesam.. Hi salam sara.. Hi salam baba..'
```



چرا کار نمیکنه؟

```
re.sub(r'[sS]alam (( \w)(\w+)\.)','Hi \g<1>.',text)
Out[29]: 'salam jadi. salam ali. salam hesam. salam sara. salam baba.'
```



str = 'students for passing the exam must have more than 15 grade.'
result = re.findall(r'a*',str)
print(result.count('a') + result.count(''))
60

```
re.compile("^b"))
```



Persian alephba `[آابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی]` or 

Persian \d `[\u06F0-\u06F9]`   or `[۰۱۲۳۴۵۶۷۸۹]` `[۰۱۲۳۴۵۶۷۸۹]` 

\u0645\u062F\u0644 = مدل

[\u060C|\u066C|\u066B]





## pattern match

https://stackoverflow.com/questions/45315753/regex-ignore-part-of-the-string-in-matches 

```python
import re
text = '["warn-error-fatal-failure-exception-ok","parsefailure","anothertag","syslog-warn-error-fatal-failure-exception-ok"]'

regex_pat = '''(?<!warn-error-fatal-)failure(?!-exception-ok),

'''
```

For more detailed, check [detailed example](https://github.com/jupihes/Regex-samples/blob/main/code.py)

