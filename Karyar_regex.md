# Karyar string processing and regex

### The Many Uses of Regex, i.e. [Situations where Regex can Save the Day](https://www.rexegg.com/regex-uses.html)
Here are some of the thing regular expressions can help you do.

1. Grabbing text in files or validating text input when programming in languages such as `C`, `Java` or `PHP`.
2. Searching (and possibly replacing) text in files when using an advanced text editor such as EditPad Pro and `Notepad++` on Windows (or TextWrangler / BBEdit on OSX), a standalone replace tool such as ABA Replace, or good old grep (the linked page has the best command-line grep for Windows).
3. Searching and replacing across pages of code when using in an IDE such as Visual Studio, Komodo IDE or even Dreamweaver's crippled ECMAScript flavor.
4. For advanced search and replace when using creativity software such as Adobe Indesign.
5. Renaming a hundred files at a time in an advanced file manager such as Directory Opus or a renamer such as PFrank (Win) or A Better Finder Rename (OSX).
6. Searching from the command line using `Perl` one-liners and utilities such as `grep`, `sed` and `awk`.
7. Finding records in a database.
8. Telling `Apache` how to behave with certain `IP addresses`, `urls` or browsers, in htaccess for instance.
9. Helping you while away the tedious afternoon office hours by exchanging regex challenges with your colleagues. 

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


<table "="" border="0" style="table-layout:fixed;">
   <tbody><tr><th class="w100" scope="col"><b>Lookaround</b></th><th class="w180" scope="col"><b>Name</b></th><th class="w320" scope="col"><b>What it Does</b></th></tr><tr class="brown"><td><span class="mono">(?=foo)</span></td><td>Lookahead</td><td>Asserts that what immediately follows the current position in the string is <i>foo</i></td></tr><tr class="beige"><td><span class="mono">(?&lt;=foo)</span></td><td>Lookbehind</td><td>Asserts that what immediately precedes the current position in the string is <i>foo</i></td></tr><tr class="brown"><td><span class="mono">(?!foo)</span></td><td>Negative Lookahead</td><td>Asserts that what immediately follows the current position in the string is not <i>foo</i></td></tr><tr class="beige"><td><span class="mono">(?&lt;!foo)</span></td><td>Negative Lookbehind</td><td>Asserts that what immediately precedes the current position in the string is not <i>foo</i></td></tr>
   </tbody>
</table>
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

Finding what exists in parantesis is example :) 
```python
pattern1 = r'\(\S+\)'
```
What is better?
 
   - Lookahead and Lookbehind: (?= … ), (?! … ), (?<= … ), (?<! … )
   - Non-Capturing Groups: (?: … ) and (?is: … )
   - Atomic Groups: (?> … )
   - Named Capture: (?<foo> … ) and (?P<foo> … )
   - Inline Modifiers: (?isx-m)
   - Subroutines: (?1)
   - Recursion: (?R)
   - Conditionals: (?(A)B) and (?(A)B|C)
   - Pre-Defined Subroutines: (?(DEFINE)(<foo> … )(<bar> … )) and (?&foo)
   - Branch Reset: (?| … )
   - Inline Comments: (?# … )
   - Code Capsule: (?{…})
   - PCRE Callouts: (?C…)
   - Version Check: (?(VERSION>=x) … )
   - Ignore ALL Unescaped Whitespace: (?xx)
   - Disable auto-capture: (?n)

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


### Log file

- What is log file?
   - In computing, syslog /ˈsɪslɒɡ/ is a standard for message logging. It allows separation of the software that generates messages, the system that stores them, and the software that reports and analyzes them. Each message is labeled with a facility code, indicating the type of system generating the message, and is assigned a severity level. 
   [Syslog](https://en.wikipedia.org/wiki/Syslog)
   - Why to have such?
      - Know who did what and when
      -      
- sample logs

- [Syslog log sample](https://techdocs.broadcom.com/us/en/symantec-security-software/information-security/symantec-cloudsoc/cloud/audit-home/barracuda-home/log-formats/syslog-log-sample.html)
> `Tue Mar 04 15:57:06 2020: <14>Mar  4 15:53:03 BAR-NG-VF500 BAR-NG-VF500/box_Firewall_Activity:  Info     BAR-NG-VF500 Remove: type=FWD|proto=UDP|srcIF=eth1|srcIP=192.168.70.7|srcPort=35119|srcMAC=08:00:27:da:d7:9c|dstIP=8.8.8.8|dstPort=53|dstService=domain|dstIF=eth0|rule=InternetAccess/<App>:RestrictTim|info=Balanced Session Idle Timeout|srcNAT=192.168.70.7|dstNAT=8.8.8.8|duration=21132|count=1|receivedBytes=130|sentBytes=62|receivedPackets=1|sentPackets=1|user=|protocol=|application=|target=|content=|urlcat`

> `Tue Mar 04 15:57:06 2020: <14>Mar  4 15:53:03 BAR-NG-VF500 BAR-NG-VF500/srv_S1_NGFW:  Info     BAR-NG-VF500 State:          REM(Balanced Session Idle Timeout,20) FWD UDP 192.168.70.7:35119 () -> 8.8.8.8:53`

> `Tue Mar 04 15:57:06 2020: <14>Mar  4 15:53:03 BAR-NG-VF500 BAR-NG-VF500/box_Firewall_audit:  Info     BAR-NG-VF500 1393928583|Remove:|FWD|eth1|UDP|InternetAccess/<App>:RestrictTim|192.168.70.7|35119|8.8.8.8|53|domain|2001|Balanced Session Idle Timeout|192.168.70.7|35119|8.8.8.8|53|eth0|08:00:27:da:d7:9c|62|1|130|1|21132|590`

> `Tue Mar 04 15:57:06 2020: <15>Mar  4 15:53:03 BAR-NG-VF500 BAR-NG-VF500/srv_S1_URL_Cofsd:  Internal BAR-NG-VF500 cofsd: [0000000] 5 DEBUG OF: Generic HTTP Transfer: 6.53%: Download starts in 171 seconds`

> `Tue Mar 04 15:57:06 2020: <14>Mar  4 15:53:04 BAR-NG-VF500 BAR-NG-VF500/box_Firewall_Activity:  Info     BAR-NG-VF500 Remove: type=FWD|proto=UDP|srcIF=eth1|srcIP=192.168.70.7|srcPort=38686|srcMAC=08:00:27:da:d7:9c|dstIP=8.8.8.8|dstPort=53|dstService=domain|dstIF=eth0|rule=InternetAccess/<App>:RestrictTim|info=Session Idle Timeout|srcNAT=192.168.70.7|dstNAT=8.8.8.8|duration=60100|count=1|receivedBytes=0|sentBytes=62|receivedPackets=0|sentPackets=1|user=|protocol=|application=|target=|content=|urlcat=`


![](https://camo.githubusercontent.com/19b839fbb5d21ae486cef3d3a5788aa844ec1453aabdbd728cf40a7a31715a0e/68747470733a2f2f63646e2e6a7364656c6976722e6e65742f67682f6c6f677061692f6c6f67706172736572406d61696e2f646f63732f696d672f6578616d706c652e6a7067)

### Data preprocessing and cleaning with regex
- Logfiles, events, traces, configuration file, dumps
- Webscraping
  
   - log analysis and managment tools
      - Open source
         -  
         - fluentd
            ![fluentd](https://www.fluentd.org/images/fluentd-architecture.png)
      - Propriotry
         - (Splunk)[https://www.splunk.com/]
           ![](/images/Splunk_tool.png)


### Sample online logfiles for investigation
[loghub](https://github.com/logpai/loghub)
- We take [Apache](https://zenodo.org/records/8196385/files/Apache.tar.gz?download=1) 	under 📂 `Server applications` section:

> [Apache](https://zenodo.org/records/8196385/files/Apache.tar.gz?download=1) 	Apache web server error log 		263.9 days 	56,481 	4.90MB 



```text
[Thu Jun 09 06:07:04 2005] [notice] LDAP: Built with OpenLDAP LDAP SDK
[Thu Jun 09 06:07:04 2005] [notice] LDAP: SSL support unavailable
[Thu Jun 09 06:07:04 2005] [notice] suEXEC mechanism enabled (wrapper: /usr/sbin/suexec)
[Thu Jun 09 06:07:05 2005] [notice] Digest: generating secret for digest authentication ...
[Thu Jun 09 06:07:05 2005] [notice] Digest: done
[Thu Jun 09 06:07:05 2005] [notice] LDAP: Built with OpenLDAP LDAP SDK
[Thu Jun 09 06:07:05 2005] [notice] LDAP: SSL support unavailable
[Thu Jun 09 06:07:05 2005] [error] env.createBean2(): Factory error creating channel.jni:jni ( channel.jni, jni)
[Thu Jun 09 06:07:05 2005] [error] config.update(): Can't create channel.jni:jni
[Thu Jun 09 06:07:05 2005] [error] env.createBean2(): Factory error creating vm: ( vm, )
[Thu Jun 09 06:07:05 2005] [error] config.update(): Can't create vm:
[Thu Jun 09 06:07:05 2005] [error] env.createBean2(): Factory error creating worker.jni:onStartup ( worker.jni, onStartup)
[Thu Jun 09 06:07:05 2005] [error] config.update(): Can't create worker.jni:onStartup
[Thu Jun 09 06:07:05 2005] [error] env.createBean2(): Factory error creating worker.jni:onShutdown ( worker.jni, onShutdown)
[Thu Jun 09 06:07:05 2005] [error] config.update(): Can't create worker.jni:onShutdown
[Thu Jun 09 06:07:16 2005] [notice] mod_python: Creating 32 session mutexes based on 150 max processes and 0 max threads.
[Thu Jun 09 06:07:19 2005] [notice] mod_security/1.9dev2 configured
[Thu Jun 09 06:07:19 2005] [notice] Apache/2.0.49 (Fedora) configured -- resuming normal operations
[Thu Jun 09 06:07:19 2005] [notice] jk2_init() Found child 2330 in scoreboard slot 0
[Thu Jun 09 06:07:19 2005] [notice] jk2_init() Found child 2337 in scoreboard slot 7
[Thu Jun 09 06:07:19 2005] [notice] jk2_init() Found child 2332 in scoreboard slot 2
[Thu Jun 09 06:07:19 2005] [notice] jk2_init() Found child 2331 in scoreboard slot 1
[Thu Jun 09 06:07:19 2005] [notice] jk2_init() Found child 2333 in scoreboard slot 3
[Thu Jun 09 06:07:19 2005] [notice] jk2_init() Found child 2335 in scoreboard slot 5
[Thu Jun 09 06:07:19 2005] [notice] jk2_init() Found child 2334 in scoreboard slot 4
[Thu Jun 09 06:07:19 2005] [notice] jk2_init() Found child 2336 in scoreboard slot 6
[Thu Jun 09 06:07:20 2005] [notice] workerEnv.init() ok /etc/httpd/conf/workers2.properties
[Thu Jun 09 06:07:20 2005] [error] mod_jk child init 1 0
[Thu Jun 09 06:07:20 2005] [notice] workerEnv.init() ok /etc/httpd/conf/workers2.properties
[Thu Jun 09 06:07:20 2005] [notice] workerEnv.init() ok /etc/httpd/conf/workers2.properties
[Thu Jun 09 06:07:20 2005] [notice] workerEnv.init() ok /etc/httpd/conf/workers2.properties
[Thu Jun 09 06:07:20 2005] [notice] workerEnv.init() ok /etc/httpd/conf/workers2.properties
[Thu Jun 09 06:07:20 2005] [notice] workerEnv.init() ok /etc/httpd/conf/workers2.properties
[Thu Jun 09 06:07:20 2005] [notice] workerEnv.init() ok /etc/httpd/conf/workers2.properties
[Thu Jun 09 06:07:20 2005] [notice] workerEnv.init() ok /etc/httpd/conf/workers2.properties
[Thu Jun 09 07:11:21 2005] [error] [client 204.100.200.22] Directory index forbidden by rule: /var/www/html/
[Thu Jun 09 12:08:57 2005] [error] [client 207.203.80.15] Directory index forbidden by rule: /var/www/html/
[Thu Jun 09 12:17:49 2005] [error] [client 216.68.171.39] Directory index forbidden by rule: /var/www/html/
[Thu Jun 09 12:48:10 2005] [error] [client 24.158.204.7] Directory index forbidden by rule: /var/www/html/
```

```python
pattern = r'(\w{3} \d{2} \d{2}\:\d{2}:\d{2} \d{4})\] \[([A-Za-z]+)\]'
```
### REGEX in SQL, Pandas, Linux Shell, Perl
#### Pandas
- On series for `str` type column,
  
#### SQL
- Check the specific `SQL` document you are using 
```sql
select 
regexp_extract(regexp_extract(CUS_FILE_NAME, 'part_(.*?\.csv)', 1),'MKT_WHITELIST_POOL_(.*?)_(.*?)_(.*?).csv$',1) as dateKey,
regexp_extract(regexp_extract(CUS_FILE_NAME, 'part_(.*?\.csv)', 1),'MKT_WHITELIST_POOL_(.*?)_(.*?)_(.*?).csv$',2) as campaignName,
regexp_extract(regexp_extract(CUS_FILE_NAME, 'part_(.*?\.csv)', 1),'MKT_WHITELIST_POOL_(.*?)_(.*?)_(.*?).csv$',3) as partnumber
from DATAINGEST.TZ_MKT_FILE_SRC_WHITELIST_POOL
```
#### Linux Shell
- `grep`
#### Perl
[sample available documentation with regex](https://docs.fluentd.org/parser/nginx)
```perl
expression /^(?<remote>[^ ]*) (?<host>[^ ]*) (?<user>[^ ]*) \[(?<time>[^\]]*)\] "(?<method>\S+)(?: +(?<path>[^\"]*?)(?: +\S*)?)?" (?<code>[^ ]*) (?<size>[^ ]*)(?: "(?<referer>[^\"]*)" "(?<agent>[^\"]*)"(?:\s+(?<http_x_forwarded_for>[^ ]+))?)?$/
time_format %d/%b/%Y:%H:%M:%S %z
```

### Regex for Persian language
- utf8 encoding
- [Regex.Persian.Language](https://github.com/mirhmousavi/Regex.Persian.Language)





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


### Project

With help of Python code like [Web link](https://github.com/jupihes/File-size-summarization), get list of whole files and their address of a directory like `D:\`
1. Develop a `regex` to extract all
    - `D:\Folder1`
    - `D:\Folder1\Sub_Folder2`      
2. Clean and remove duplicate and store results as '.xlsx' file     

