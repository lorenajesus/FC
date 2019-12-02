
from flaskext.mysql import MySQL
import MySQLdb
print('Conectando...')
conn = MySQLdb.connect(user='root', passwd='root', host='127.0.0.1', port=3306)



# inserindo usuarios
cursor = conn.cursor()


cursor.execute('select * from programa.usuario')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[1])


cursor.execute('select * from programa.estabelecimento')
print(' -------------  Jogos:  -------------')
for estabelecimento in cursor.fetchall():
    print(estabelecimento[1])

# commitando senão nada tem efeito
conn.commit()
cursor.close()