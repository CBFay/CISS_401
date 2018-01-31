# This will create a table in my database called 'gene'

import sqlite3


conn = sqlite3.connect('ebola.db')
c = conn.cursor()

c.execute('''CREATE TABLE gene(locus text, base_pairs text, sequence_type text, definition text, sequence text)''')

"""
Again, I use sqlite.connect() to create a Connection object, and store it in a variable, 'conn'.

Connection objects have an attribute 'cursor()' which returns a 'Cursor' type object.
We can use it to create a Cursor object, and store it in a variable called 'c'.

I like to think of the Cursor object as a person that's typing at the sqlite3 command line,
because Cursor objects (like 'c') can execute SQL commands from Python, without us ever having...
...to use the sqlite3 program manually.

c.execute() is a method, that takes a String as input, that will be executed in sqlite3 as if we had...
...typed it ourselves. I use the triple single-quotes around the String because they let you...
type on multiple lines.

In Python, Strings can be inside double quotes, single quotes, or triples of each.
They each have minor differences, but usually single quotes will work fine.

I really recommend looking at the documentation for sqlite3 here:
https://docs.python.org/3.6/library/sqlite3.html

And also some kind of guide on sqlite3 statements. Here's the one I looked at:
https://www.sitepoint.com/getting-started-sqlite3-basic-commands/

Both of these aren't nearly as scary as they look, and I learned what I needed...
...with under 5 minutes in each of them.

The Python docs specifically are really helpful, and I get here by googling things I don't...
...recognize in Python like 'sqlite3.connect()', or 'conn.cursor()'.
"""
