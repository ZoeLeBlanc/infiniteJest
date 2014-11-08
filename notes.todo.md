#Infinite Jest

There are two overarching goals for the project 
1. Learn Python
2. Analyze text patterns in the book Infinite Jest by David Foster Wallace.  

##1. parser.py and parser2.py

Function:

Split by

1. Words &#x2713;
2. Sentences
3. chapters &#x2713;
4. Paragraphs
5. Count occurrences of words (length = one word) &#x2713;
6. Track position of words &#x2713;
7. Count occurrences of phrases (length > one word) &#x2713;
8. Count occurrences of phrases 
9. Attach chronology information to chapters and position of occurrence

###History of how parser.py was created

1.  I first started messing with a small sample file, that I could manage a bit easier. 
2.  I then started looking into how to do simple tasks like splitting into more digestible sections using the  `split()` method.
3.  In order to understand the output of the splitting I was doing I brushed up on understanding Python data structures, using the [best written guide to any programing I had ever seen](http://pymbook.readthedocs.org/en/latest/datastructure.html#matrixmul-py).  
4. I wanted to count something super simple, like words, so I wrote a little program that asks for the word, then prints the number of occurances of that word. This also goes along with one of my long term goals of being able to count all the character/terms and there location relative to book length. 

**Problem**There are several reasons why splitting using ```wordSplit = sampleRead.split()``` doesn't work. Since it is cutting on the space all the symbols are present. 

5.  Do I even need to split into list to get number of occurrences? It might be easier to leave as string, remove symbols, and use the find feature. No.  It is easiest to just remove symbols then make a list. The list will be useful later as I need an index number (position) for each word. 

6. I made the program input the two files from command line, to help with testing. 

7.  Now I need to parse out each chapter. Parsing out each chapter is harder than I imagined.  I think what I need to do is to take advantage of the list of chapters and split by that list and reiterate over that list to split into list. I am going to take the easy way out of this one and add a tag (<ch><1>)to the file, then parse it.

8a. I can go ahead and use my list of word and get counts and understand their index further.  Each word has it's position. The **goal** is to get a tab delimited file for R. 
    
*Theoretical Code*

    position = 
        a.) start of word found when searching through string
    or
        b.) index number in list
            ex.  x from  termSplit

I needed to retrieve the index number of x in termSplit #x = term in terms.txt

*Theoretical Code*

    print "%i (tab) %s (tab) %" %(termCount, x, (index#) )

8b.  I scraped a really great characters list from the html of [A Character Guide to Infinite Jest](http://web.archive.org/web/20040811014451/http://www.ilstu.edu/~tffeene/ij/characterguide.html)that also give a group category to the characters. The problem is that the way in which I find the characters in 8a, will not work, because many of the character's names are more than one word.  I will try to use the counter[] method. The counter method words with terms, so at least I can get the number of occurrences, just not the position.

9. Chronology. 

Each Chapter has the chronology attached. 

Do later.

10.  Split chapters. I put tags by hand in the line right before the chapter heading.  

For example 

    <ch><*> #* being the chapter number

What would be some ways in which I could accomplish this?  a. There has to be a way to find the total in every chapter while going through the book once.  b. Or are we going to have to split the book into chapters and then count the instances?  The only way I know how at this point is to split into chapters.  

I am splitting by chapter tags, but unsure how to name tags, I am sure what I have to do is make a dictionary. Key being the chapter # and value being the text in the chapter. 

Wait a second....This seems to be a little complex, but I do totally need to learn this at some point.  I can get the positions of each chapter from parser1.py of the chapters.  Then I can sort occurrences by the range of the chapters.  This would make things a lot easier I believe. 

Come back.

11. So it appears as though I have two scripts. One to count the number of occurrences of any phrase in the whole book (parser2.py).  The other script has the ability to get a single word instance in a list along with position. 

The problem is I would like to combine functionality of both of the scripts into one awesome script.  I want to be able to use phrases, but then I won't have word position.   Is there another way to find position?  Character, as in letter? That could work.  At this point I need to figure out what I need exactly. 

What do I want to visualize? How do I need to structure that data?

1. Bubble chart for how many times a character is mentioned.  Maybe work on a list of characters that is one word. 

2. Position chart, where I map the occurrence across the book, with the chapter deliniated.  I could easily just find the chapter positions.  No.  Just add a new column in R.  

    dataset$chapter <- 1200-3000 = "chapter 2"

This can be visualized in R using ggplot. 

###TODOD NEXT



##Programing concepts learned

This is just a list of programming concepts and tricks I learned that I find useful.

Here you are reading one line at a time. Could come in handy if you specify when to stop.  

    fh.readline()
    'YEAR OF THE DEPEND ADULT UNDERGARMENT \n'
    \>>> fh.readline(2)
    'Th'
    \>>> fh.readline(5)
    'ough '
    fh.readline(405)
    \>>> 'only one-half ethnic Arab and a Canadian by birth and residence, the medical attache is nevertheless once again under Saudi diplomatic immunity, this time as special ear-nose-throat consultant to the personal physician of Prince Q---------, the Saudi Minister of Home Entertainment, here on northeastern U.S.A. soil with his legation to cut another mammoth deal with 

Is what returns one variable that can be added to string?  What type of data is it.  How do you ask again?

    />>> isinstance(nextthirty,int);
    False
    />>> isinstance(nextthirty,basestring);
    True

You can assign it to a variable 

    />>> nextthirty = fh.readline(30)
    />>> nextthirty
    'l attache turns thirty-seven t'

If I continue reading line?  Does nextthirirty stay the same?  Should.

    \>>> nextForty = fh.readline(40)
    \>>> nextthirty
    'l attache turns thirty-seven t'
    \>>> nextForty

So we know it is part of the string. That means I can connect them together. If I can figure out how to cut them at every sentence (minus the acrynyms), Make a string of sentences in every paragraph. The key will be the paragraph and the value will be the string of sentences which belong to that paragraph. 

Many times it happens that we want to add more data to a value in a dictionary and if the key does not exists then we add some default value. You can do this efficiently using dict.setdefault(key, default). via [pymbook.readthedocs.org](http://pymbook.readthedocs.org/en/latest/datastructure.html#dictionaries)

    />>> data = {}
    />>> data.setdefault('names', []).append('Ruby')
    />>> data
    {'names': ['Ruby']}
    />>> data.setdefault('names', []).append('Python')
    />>> data
    {'names': ['Ruby', 'Python']}
    />>> data.setdefault('names', []).append('C')
    />>> data
    {'names': ['Ruby', 'Python', 'C']}
        'American lunar Y.D.A.U. The legation fin'

**You can lists within lists.** via [pymbook.readthedocs.org](http://pymbook.readthedocs.org/en/latest/datastructure.html#dictionaries)

    />>> a
    [45, 43624356, -3434, 1, 45, 23, 1, 111, [45, 56, 90]]
    />>> a[-1]
    [45, 56, 90]


**```find()``` method for a string**

If it matches to more than one, it will reply ```0```

    />>> a
    'for for fight for but there'
    />>> a.find("for")
    0
    />>> a.find("fight")
    8

**help**

    \>>> help(["foo", "bar", "baz"])
    Help on list object:

    class list(object)
    ...


    |
    |  index(...)
    |      L.index(value, [start, [stop]]) -> integer -- return first index of value
    |

**```enumerate()``` to get indexes of multiple if duplicates are in the list.

    for i, j in enumerate(['foo', 'bar', 'baz']):
        if j == 'bar':
            print i

list.index(x)
Return the index in the list of the first item whose value is x. It is an error if there is no such item.

##Old parts of parser.py

    #manually enter the word to split
    word = str(raw_input("Please enter a word to count:")) 

    #this counts the number of occurrences of the word.  
    print 'There are %d occurrences of the word %s ' % (wordNum, searchWord)

    #counts all the occurrences of each word in term file from the text file.

    for x in termSplit:
    print x
    termCount = sampleSplit.count(x)
    print "There are %i occurrences of the character %s in this section." %(termCount, x)
    #counts all the occurrences of each word in term file from the text file.
    for x in termSplit:
    print x
    termCount = sampleSplit.count(x)
    print "There are %i occurrences of the character %s in this section." %(termCount, x)

##```counter[]```
from collections import Counter
str = "Mary had a little lamb"
counter = Counter(str)
print counter['a']

##Data Mining the internet with Python

**Resource*** [How to Mine the Web](http://www.whosbacon.com/how-to-mine-the-web)

You will need three main things

1. HTTP client.  The first step is to gather all of the content and make it in a readible form.

good option [Requests: HTTP for Humans](http://docs.python-requests.org/en/latest/index.html)

2. Content Parsing.  Once you have the content, you can now parse the data. You can parse the text(HTML) by using a structual tranverser like [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/) or pattern matching with Regex.  Pattern matching might be the easiest option for me.  I will have to look at the html. 

I just looked at the source.  And it should be pretty easy to just copy the source page for each page and use pattern matching for content between ```<b></b>``` tags.

##Resources:

[Interview](http://kottke.org/07/12/infinite-jest)
[Joe Hansen little write up](http://www.itsokaytobesmart.com/post/36749070169/infinite-jest-literary-fractal)
[Pym Book](http://pymbook.readthedocs.org/en/latest/index.html): Excellent introduction to Python.

###JSON
[w3 schools introduction](http://www.w3schools.com/json/json_syntax.asp)

##D3 ideas

[Interactive Data Visualization for the Web Book](http://chimera.labs.oreilly.com/books/1230000000345/index.html)

[Sunburst](http://bl.ocks.org/kerryrodden/7090426)
[Hierarchical Edge Bundling](http://bl.ocks.org/mbostock/1044242)
[Co-occurrencee](http://bost.ocks.org/mike/miserables/): This is just an[Adjacency Matrix](http://en.wikipedia.org/wiki/Adjacency_matrix)
[Arc Diagram](http://mbostock.github.io/protovis/ex/arc.html)
[Bubble Diagram](http://bl.ocks.org/mbostock/4063269)
[Donut Chart](http://bl.ocks.org/mbostock/3887193)