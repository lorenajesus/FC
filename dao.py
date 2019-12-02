from models import Estabelecimento, Usuario

SQL_DELETA_ESTABELECIMENTO = 'delete from programa.estabelecimento where id = %s'
SQL_ESTABELECIMENTO_POR_ID = 'SELECT  id,razaosocial,cnpj,email,endereco,cidade,estado,telefone,dtcadastro,categoria,status,agencia,conta from programa.estabelecimento where id = %s'
SQL_USUARIO_POR_ID = 'SELECT id, nome, senha from usuario where id = %s'
SQL_ATUALIZA_ESTABELECIMENTO = 'UPDATE programa.estabelecimento SET razaosocial=%s, cnpj=%s, email=%s, endereco=%s, cidade=%s, estado=%s, telefone=%s, dtcadastro=%s,categoria=%s, status=%s, agencia=%s, conta=%s where id = %s'

SQL_BUSCA_ESTABELECIMENTOS = 'SELECT id,razaosocial,cnpj,email,endereco,cidade,estado,telefone,dtcadastro,categoria,status,agencia,conta from programa.estabelecimento'

SQL_CRIA_ESTABELECIMENTO = 'INSERT into programa.estabelecimento values (null,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)'



class EstabelecimentoDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, estab):
        print('ID', estab.id)
        print('tentando ')
        cursor = self.__db.connection.cursor()

        if (estab.id):
            print('ID',estab.id)
            cursor.execute(SQL_ATUALIZA_ESTABELECIMENTO, (estab.id,estab.rz_social, estab.cnpj,estab.email, estab.endereco, estab.cidade, estab.estado,estab.dtcadastro, estab.telefone,  estab.categoria,estab.status, estab.agencia, estab.conta))
        else:
            cursor.execute(SQL_CRIA_ESTABELECIMENTO, (estab.rz_social, estab.cnpj, estab.email, estab.endereco, estab.cidade, estab.estado, estab.telefone, estab.dtcadastro, estab.categoria,estab.status, estab.agencia, estab.conta))
            #cursor.execute(SQL_CRIA_ESTABELECIMENTO, ('Marina e Leandro Publicidade e Propaganda Ltda','83235408000170','producao@marinaeleandrop.com.br','Rua dos Guarás','São Bernardo do Campo','SP','1135907441','2019-12-01','publicidade',1,'2563','022150'))
            estab.id = cursor.lastrowid
        self.__db.connection.commit()
        return estab

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_ESTABELECIMENTOS)
        estab = traduz_estabelecimento(cursor.fetchall())
        return estab

    def busca_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_ESTABELECIMENTO_POR_ID, (id,))
        tupla = cursor.fetchone()
        return Estabelecimento(tupla[0],tupla[1], tupla[2], tupla[3],tupla[4],tupla[5],tupla[6],tupla[7],tupla[8],tupla[9],tupla[10],tupla[11],tupla[12])


    def deletar(self, id):
        self.__db.connection.cursor().execute(SQL_DELETA_ESTABELECIMENTO, (id, ))
        self.__db.connection.commit()


class UsuarioDao:
    def __init__(self, db):
        self.__db = db

    def buscar_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_USUARIO_POR_ID, (id,))
        dados = cursor.fetchone()
        usuario = traduz_usuario(dados) if dados else None
        return usuario


def traduz_estabelecimento(estab):
    def cria_estabelecimento_com_tupla(tupla):
        return Estabelecimento(tupla[1],tupla[2], tupla[3],tupla[4],tupla[5],tupla[6],tupla[7],tupla[8],tupla[9],tupla[10],tupla[11],tupla[12],id=tupla[0])
    return list(map(cria_estabelecimento_com_tupla, estab))


def traduz_usuario(tupla):
    return Usuario(tupla[0], tupla[1], tupla[2])
