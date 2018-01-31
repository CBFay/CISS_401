# running this python script will create a database called 'ebola.db'

import sqlite3

conn = sqlite3.connect('ebola.db')
conn.commit()
conn.close()

"""
Importing the sqlite3 module gives you access to new methods.

One of these methods is 'connect()', which creates a 'connection' type object
that can interact with .db files.

In line 3, I'm making a connection object, and giving it to a variable called 'conn'

'conn' has all the methods that are built into any connection type object.
Almost all types of object types like 'String' and 'Int' also have built in methods.

When something is built into an object by default, it's called an attribute.

My connection object, conn, has an attribute called commit(), which saves the .db file we connected to.
It also has an attribute called close(), which closes the .db file.

Closing files prevents unnecessary resource use, and helps make sure that we don't accidentally
lose data.
"""
