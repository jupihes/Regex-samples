# Karyar string processing and regex



sample
```python
files = [
'IR_TRUNCATE_POOL1_20240310_DataBuyable.csv',
'IR_TRUNCATE_POOL2_20240416_DataMatrix.csv',
'IR_TRUNCATE_POOL4_20240416_VoiceMatrix.csv',
'IR_TRUNCATE_POOL9_20240420_VoiceMatrix.csv',
'IR_TRUNCATE_POOL5_20240310_DataBuyable.csv',
'IR_TRUNCATE_POOL24_20240406_DataMatrix.csv',
'IR_TRUNCATE_POOL7_20240413_VoiceMatrix.csv',
'  IR_TRUNCATE_POOL 3_20240420_APP .csv',
'  IR_TRUNCATE_POOL1_20240310_DataBuyable.csv  ',
'IR_TRUNCATE_POOL2_20240416_DataMatrix.csv',
'IR_TRUNCATE_POOL4_20240416_VoiceMatrix.txt',
'IR_TRUNCATE_POOL9_20240420_VoiceMatrix..csv',
'IR_TRUNCATE_POOL5_20240310_DataBuyable_.csv',
'IR_TRUNCATE_POOL24_20240406_DataMatrix.csv',
'IR_TRUNCATE_POOL7_20240413_VoiceMatrix.docx',
'IR_TRUNCATE_POOL3_20240420_APP.csv',
'IR_TRUNCATE_POOL1_20240310_DataBuyable.csv',
'IR_TRUNCATE_POOL2_20240416_DataMatrix.csv',
'IR_TRUNCATE_POOL4_20240416_VoiceMatrix.csv',
'IR_TRUNCATE_POOL9_20240420_VoiceMatrix.csv',
'IR_TRUNCATE_POOL5_20240310_DataBuyable$.csv',
'IR_TRUNCATE_POOL24_20240406_DataMatrix&.csv',
'IR_TRUNCATE_POOL7_20240413_VoiceMatrix.csv',
'IR_TRUNCATE_POOL3_20240420_APP.csv']
```

### find `.csv` files

### find `.csv` files with `IR_TRUNCATE` in filename


### Text processing limitation
- Text processing is limited! 
- What to do?
   - regex

### find `.csv` files with `IR_TRUNCATE` at start filename 

### find `.csv` files with `IR_TRUNCATE` at start filename and datetime

```python
pattern = r'.csv'
pattern = r'\S+.csv'
pattern = r'IR_TRUNCATE_POOL\S+.csv'
pattern = r'IR_TRUNCATE_POOL\d_\d{8}_\S+.csv'
pattern = r'IR_TRUNCATE_POOL\d_\d{8}_[a-zA-Z0-9]+.csv'
pattern = r'IR_TRUNCATE_POOL\d_\d{8}_[a-zA-Z0-9_]+.csv'
pattern = r'IR_TRUNCATE_POOL\d_\d{8}_\S+.csv'
pattern = r'IR_TRUNCATE_POOL\d_\d{8}_\S+.csv'

pattern = r'IR_TRUNCATE_POOL\d{1}_\d{8}_\w+(?<![_.\ ]).csv'
pattern = r'IR_TRUNCATE_POOL\d_\d{8}_\w*(?<![._ ]).csv'
```


<table "="" border="0" style="table-layout:fixed;"><tbody><tr><th class="w100" scope="col"><b>Lookaround</b></th><th class="w180" scope="col"><b>Name</b></th><th class="w320" scope="col"><b>What it Does</b></th></tr><tr class="brown"><td><span class="mono">(?=foo)</span></td><td>Lookahead</td><td>Asserts that what immediately follows the current position in the string is <i>foo</i></td></tr><tr class="beige"><td><span class="mono">(?&lt;=foo)</span></td><td>Lookbehind</td><td>Asserts that what immediately precedes the current position in the string is <i>foo</i></td></tr><tr class="brown"><td><span class="mono">(?!foo)</span></td><td>Negative Lookahead</td><td>Asserts that what immediately follows the current position in the string is not <i>foo</i></td></tr><tr class="beige"><td><span class="mono">(?&lt;!foo)</span></td><td>Negative Lookbehind</td><td>Asserts that what immediately precedes the current position in the string is not <i>foo</i></td></tr></tbody></table>
[regex-lookarounds](https://www.rexegg.com/regex-lookarounds.html)

#### Negative Lookbehind  (?<!...)
Ensures that the given pattern would not match and end at the current position in the expression. The pattern must have a fixed width. Does not consume characters.

```python
pattern = r'IR_TRUNCATE_POOL\d{1}_\d{8}_\w+(?<![_.\ ]).csv'
pattern = r'IR_TRUNCATE_POOL\d_\d{8}_\w*(?<![._ ]).csv'
```

#### Negative Lookahead

(?!...)
Starting at the current position in the expression, ensures that the given pattern will not match. Does not consume characters.

```python
pattern = r'(?:[0-9]{1,3}\.){3}[0-9]{1,3}(?![a-zA-Z0-9_.])'

http://94.182.130.251
http://94.182.130.238
http://94.182.130.248
http://94.182.130.246
http://195.213.236.87.mail.iranianwebman.ir
http://14.214.236.87.mail.iranianwebman.ir
http://129.214.236.87.mail.iranianwebman.ir
http://185.141.107.200
http://185.120.221.156
http://185.120.221.154
http://185.67.101.14
http://5.160.219.190
http://195.181.39.125
```

### Password sample
 - We need a password that must meet four below conditions:
   
   1. The password must have between six - 6 and ten 10 word characters 
   2. It must include at least one lowercase character
   3. It must include at least three uppercase characters
   4. It must include at least one digit

[regex-lookarounds](https://www.rexegg.com/regex-lookarounds.html)

[regex-disambiguation](https://www.rexegg.com/regex-disambiguation.html)

finding what exists in parantesis is example :) 
   - Lookahead and Lookbehind: `(?= … )`, `(?! … )`, `(?<= … ), (?<! … )`
   - Non-Capturing Groups: `(?: … )` and `(?is: … )`
   - Atomic Groups: `(?> … )`
   - Named Capture: `(?<foo> … )` and `(?P<foo> … )`
   - Inline Modifiers: `(?isx-m)`
   - Subroutines: `(?1)`
   - Recursion: `(?R)`
   - Conditionals: `(?(A)B)` and `(?(A)B|C)`
   - Pre-Defined Subroutines: `(?(DEFINE)(<foo> … )(<bar> … ))` and `(?&foo)`
   - Branch Reset: `(?| … )`
   - Inline Comments: `(?# … )`
   - Code Capsule: `(?{…})`
   - PCRE Callouts: `(?C…)`
   - Version Check: `(?(VERSION>=x) … )`
   - Ignore ALL Unescaped Whitespace: `(?xx)`
   - Disable auto-capture: `(?n)`


### what if `date` part contains `time` as well

```
files = [
'IR_TRUNCATE_POOL2_202404161220_DataMatrix.csv',
'IR_TRUNCATE_POOL4_202404161700_VoiceMatrix.txt',
'IR_TRUNCATE_POOL9_2024042010_VoiceMatrix..csv',
'IR_TRUNCATE_POOL5_202403103500_DataBuyable_.csv',
'IR_TRUNCATE_POOL24_202404062715_DataMatrix.csv',
'IR_TRUNCATE_POOL7_20240413_VoiceMatrix.docx',
'IR_TRUNCATE_POOL3_20240420_APP.csv']
```



### REGEX in SQL, Pandas, Linux Shell, Perl

#### SQL
- Check the specific `SQL` document you are using 
```sql
select 
regexp_extract(regexp_extract(CUS_FILE_NAME, 'part_(.*?\.csv)', 1),'MKT_WHITELIST_POOL_(.*?)_(.*?)_(.*?).csv$',1) as dateKey,
regexp_extract(regexp_extract(CUS_FILE_NAME, 'part_(.*?\.csv)', 1),'MKT_WHITELIST_POOL_(.*?)_(.*?)_(.*?).csv$',2) as campaignName,
regexp_extract(regexp_extract(CUS_FILE_NAME, 'part_(.*?\.csv)', 1),'MKT_WHITELIST_POOL_(.*?)_(.*?)_(.*?).csv$',3) as partnumber
from DATAINGEST.TZ_MKT_FILE_SRC_WHITELIST_POOL
```






### Question

I need a 9 hour course plan covering `text processing` and `regex` in python aiming to teach students to learn
- string text processing
- using simple `regex`
- using advanced `regex` 
- extracting content from `log` file or `configuration` file

### Course Title: Text Processing and Regular Expressions in Python

Course Duration: 6 hours

Course Objectives:
- Understand the basics of text processing in Python
- Learn how to use regular expressions to search, match, and manipulate text
- Learn how to develop and check regex pattern for usecases 
- Develop skills in extracting content from log files and configuration files using text processing and regex in Python

---------------------------------

Course Outline:

Day 1: Introduction to Text Processing (1 hour)

- Introduction to text processing in Python
- Understanding strings and common string operations
- Basic text manipulation techniques
- Examples and hands-on exercises
- String limitations for complicated cases: Intro to `regex`

Day 2: Introduction to Regular Expressions (1 hour)

- What are regular expressions and their importance in text processing
- Basic regex syntax: literals, metacharacters, and character classes
- Matching and searching patterns in Python using the `re` module
- Examples and hands-on exercises

Day 3: Advanced Regular Expressions (1.5 hours)

- Quantifiers: matching repeating patterns
- Anchors: matching positions in the text
- Groups and capturing: extracting specific parts of text
- Lookahead and lookbehind assertions
- Examples and hands-on exercises

Day 4: Text Extraction from Log Files (2 hours)

- Parsing log files using text processing and regex
- Identifying patterns in log files
- Extracting relevant information from log files
- Processing log files using Python
- Examples and hands-on exercises

Day 5: Text Extraction from Configuration Files (2 hours)

- Overview of configuration files and their structure
- Parsing configuration files using text processing and regex
- Extracting configuration settings using regular expressions
- Writing Python scripts to process configuration files
- Examples and hands-on exercises

Day 6: Final Project (1.5 hours)

- Applying the acquired knowledge and skills to complete a final project
- Working on a text processing and regex task
- Solving a real-world problem by extracting content from either a log file or a configuration file
- Reviewing and discussing the solutions

---------------------------------

This course plan covers a comprehensive introduction to text processing, regular expressions, and their practical applications in Python. It allows students to understand and practice different techniques for working with text data and extracting specific information from log files and configuration files.


### Answer GPT 4 

Certainly! In order to cover the specified topics in a 9-hour course, each section will have corresponding hands-on exercises to reinforce the learning points covered in the lectures. It's crucial that each topic includes practical examples to ensure students are able to apply the concepts in real-world situations.

**Course Title:** Mastering Text Processing and Regular Expressions in Python

**Total Course Duration:** 6 Hours

### Course Title: Text Processing and Regular Expressions in Python

Course Duration: 6 hours

Course Objectives:
- Understand the basics of text processing in Python
- Learn how to use regular expressions to search, match, and manipulate text
- Learn how to develop and check regex pattern for usecases 
- Develop skills in extracting data / infomation content from webpages / log files / configuration files using text processing and regex in Python

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

- Hands-on exercise: Manipulating and formatting text data
- String limitations for complicated cases: Intro to `regex`

#### **Session 2: Basic Concepts of Regular Expressions (2 hours)**
- Introduction to Regular Expressions and the `re` module in Python
- Basic patterns and character classes (`[abc]`, `\d`, `\w`, `\s`, `.`)
   - Wildcards and Character Classes
- `re` methods: Using `re.match`, `re.search`, `re.findall`, and `re.split`
- Quantifiers: matching repeating patterns
- Anchors: matching positions in the text
- Hands-on exercise: Creating simple regex patterns to find and extract data

#### **Session 3: Inermediate Regular Expressions (2 hours)**
- Advanced regex features 
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







#### **Session 4: Practical Text Processing - Extracting Data from Logs (2 hours)**
- Log file structure and common patterns
- Strategies for parsing log files using regex
- Capturing data from logs (timestamps, log levels, messages)
- Handling multi-line log entries
- Hands-on exercise: Extracting error reports and statistics from a sample log file

#### **Session 5: Practical Text Processing - Working with Configuration Files (2 hours)**
- Overview of configuration file formats (INI, YAML, JSON, etc.)
- Reading and writing configuration files using respective modules and regex
- Extracting settings: key-value pairs, sections, and structure
- Modifying configuration files with text processing
- Hands-on exercise: Updating a configuration file to set up a simple application

#### **Session 6: Capstone Project and Course Wrap-up (0.5 hours)**
- Overview of a practical text processing task, perhaps combining elements from earlier sessions
- Break into small groups for the capstone project: Extract specific information from provided log and configuration files.
- End-of-course Q&A, discussion of projects, and wrap-up

**Materials and Resources:**
- Reference sheets for Python string methods and regex
- Sample log and configuration files for exercises
- Python scripts as a starting point for hands-on exercises

**Course Delivery:**
- The course will be a mix of lectures, live coding demonstrations, and hands-on exercises.
- The instructor will provide support during exercises and review the solutions to ensure understanding.
- Participants will be encouraged to share their screen during exercises for real-time feedback.

By the end of the course, students will have a strong foundation in processing text in Python and using regular expressions for a wide range of applications, including but not limited to extracting information from logs and configuration files.




### Answer claude

Here is a 9 hour course plan to teach students text processing and regex in Python:
Day 1
Morning (3 hours)

    - Introduction to Python strings (30 mins)
        - String basics: creating, indexing, slicing
    - Basic string methods (1 hour)
        - `lower()`, `upper()`, `strip()`, `split()`, `join()` etc.
    - Formatted strings (30 mins)
        - `f-strings`, `str.format()`

Afternoon (3 hours)

    - Regular expressions basics (2 hours)
        - Intro to regex and regex syntax
        - Searching, matching, finding with re module
        - `re.search()`, `re.match()`, `re.findall()`
    - Regex quantifiers and groups (1 hour)
        - `*, +, ?, {n,m}` quantifiers
        - `()` groups, `|` alternation

Day 2
Morning (3 hours)

    - More advanced regex (2 hours)
        - Character classes, anchors
        - re.sub() for find and replace
        - re.compile()
    - Regex exercises (1 hour)
        - Practice with regex on sample text

Afternoon (3 hours)

    File I/O basics (30 mins)
    Reading text files (1 hour)
        Open, read, close text files
    Extracting text from files (1.5 hours)
        Regex to find patterns/data in text files
        Extract log data, config file data
    Writing text files (30 mins)

Day 3
Morning (3 hours)

    Recap and review of materials (1 hour)
    Text processing exercises (2 hours)
        Practice string methods and regex on sample text

Afternoon (3 hours)

    Project work (3 hours)
        Use skills to extract data from real log/config files
        Analyze and process extracted text
        Output cleaned data to new files



https://python-course.eu/advanced-python/advanced-regular-expressions.php
