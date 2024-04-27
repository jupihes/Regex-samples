
### Course Title: Text Processing and Regular Expressions in Python

 - [x] with Karyar
 
Course Duration: 6 hours

Course Objectives:
- Understand the basics of text processing in Python
- Learn how to use regular expressions to search, match, and manipulate text
- Learn how to develop and check regex pattern for use cases 
- Develop skills in extracting data / information content from webpages / log files / configuration files using text processing and regex in Python

**Target Audience:** Beginner to intermediate Python users who are interested in 
text processing and data extraction.

### Course Schedule:

#### **Session 1: Introduction to String Text Processing in Python (2 hours)**
- Understanding Python strings (immutable sequences of Unicode points)
- Common string operations (concatenation, slicing, common methods `str.find`, `str.replace`, `str.split`, `str.join`, etc.)
- String formatting (`str.format`, f-strings)
- String matching - string operators and built-in methods
   - What is not handy or even possible with lots of string manipulation? 
   - More sophisticated pattern-matching capabilities.
- String limitations for complicated cases: Intro to `regex`
- Hands-on exercise: Manipulating and formatting text data
#### **Session 2: Basic Concepts of Regular Expressions (2 hours)**
- Introduction to Regular Expressions and the `re` module in Python
- Basic patterns and character classes (`[abc]`, `\d`, `\w`, `\s`, `.`)
   - Wildcards and Character Classes
- `re` methods: Using `re.match`, `re.search`, `re.findall`, and `re.split`
- Quantifiers: matching repeating patterns
- Anchors: matching positions in the text
- Using online `regex` tool 
- Hands-on exercise: Creating simple regex patterns to find and extract data

#### **Session 3: Intermediate Regular Expressions (2 hours)**
- regex features 
   - quantifiers `*`, `+`, `?`, `{n}`,
   - greediness vs laziness
- Groups and capturing: extracting specific parts of text
   - Grouping and capturing (`(...)`) 
   - non-capturing groups (`(?:...)`)
   
<!-- - Lookaround assertions (`(?=...)`, `(?!...)`, `(?<=...)`, `(?<!...)`) -->
- Substitution with `re.sub`
- Flags (e.g., `re.IGNORECASE`, `re.MULTILINE`)
- Hands-on exercise: Writing complex regex for pattern matching and substitution


#### Project
- Process and extract clean data from log-file, config file or similar task

