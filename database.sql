CREATE TABLE cadastrar_buffet(
	id integer primary key auto_increment,
    nome varchar(200) not null,
    cnpj int not null,
    endereco varchar(300) not null,
    tempo_de_parceria varchar(200) not null,
    tipo_de_parceria varchar(30) not null,
    email varchar(400) not null
);

CREATE TABLE eventos_privados(
	id INT PRIMARY KEY AUTO_INCREMENT,
    id_do_curso INT,
    id_do_representante INT,
    FOREIGN KEY (id_do_curso) REFERENCES marca_evento(id),
    FOREIGN KEY (id_do_representante) REFERENCES representante_de_classe(id)
);

CREATE TABLE `marca_evento` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `nome_da_faculdade` varchar(400) ,
  `nome_do_curso` varchar(150) ,
  `data_disponiveis` date ,
  `enderecos_disponiveis` varchar(300) ,
  `ponto_de_referencia` varchar(100) ,
  `horarios_disponiveis` varchar(300) ,
  `evento_aberto_ou_fechado` char(10) DEFAULT 'FECHADO',
  `limite_de_convidados` int 
);

CREATE TABLE representante_de_classe (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    telefone VARCHAR(20),
    forma_pag VARCHAR(50) default null,
    email VARCHAR(400)
);

CREATE TABLE `dados_empresa` (
  `id_empresa` int NOT NULL AUTO_INCREMENT,
  `cnpj` char(14) NOT NULL, 
  `nome` varchar(100) NOT NULL,
  `endereco` varchar(200) NOT NULL,
  `email` varchar(300) NOT NULL,
  `telefone` varchar(30) NOT NULL,
  PRIMARY KEY (`id_empresa`)
);


select * from representante_de_classe;
select * from marca_evento;
select * from eventos_privados;
drop table representante_de_classe;
drop table marca_evento;
drop table eventos_privados;
