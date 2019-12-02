CREATE DATABASE `programa`;


DROP TABLE IF EXISTS `programa`.`categorias`;
CREATE TABLE  `programa`.`categorias` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `descricao` varchar(45) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT;

DROP TABLE IF EXISTS `programa`.`usuario`;
CREATE TABLE  `programa`.`usuario` (
  `id` varchar(8) COLLATE utf8_bin NOT NULL,
  `nome` varchar(20) COLLATE utf8_bin NOT NULL,
  `senha` varchar(8) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT;

DROP TABLE IF EXISTS `programa`.`estabelecimento`;
CREATE TABLE  `programa`.`estabelecimento` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `razaosocial` varchar(250) COLLATE utf8_bin NOT NULL,
  `cnpj` varchar(25) COLLATE utf8_bin NOT NULL,
  `email` varchar(50) COLLATE utf8_bin DEFAULT NULL,
  `endereco` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `cidade` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `estado` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `telefone` varchar(15) COLLATE utf8_bin DEFAULT NULL,
  `dtcadastro` date DEFAULT NULL,
  `categoria` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `status` varchar(11) COLLATE utf8_bin DEFAULT NULL,
  `agencia` varchar(10) COLLATE utf8_bin DEFAULT NULL,
  `conta` varchar(11) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1;


insert into programa.estabelecimento 
values(null,'Marina e Leandro Publicidade e Propaganda Ltda','83235408000170',
'producao@marinaeleandrop.com.br','Rua dos Guarás','São Bernardo do Campo','SP','1135907441','2019-12-01','publicidade','Ativo','2563','022150')