import sqlite3

file = open("KU182909.txt", "r")
sequence = file.read().replace('\n', '')
definition =    """
                Ebola virus isolate Ebola virus/H.
                sapiens-tc/COD/1995/Kikwit-9510622, complete genome
                """

conn = sqlite3.connect('ebola.db')
c = conn.cursor()

statement = """INSERT INTO gene(locus, base_pairs, sequence_type, definition, sequence)
    VALUES('KU182909', '18959', 'cRNA', ?, ?);"""

c.execute(statement, (definition, sequence))

conn.commit()
conn.close()
