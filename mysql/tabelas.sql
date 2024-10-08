use banco;

CREATE TABLE cliente (
    idcliente INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nomeDoCliente VARCHAR(45) NOT NULL,
    sobrenomeDoCliente VARCHAR(45) NOT NULL,
    dataDeAniversario DATE NOT NULL,
    idade VARCHAR(45) NOT NULL,
    email VARCHAR(100) NOT NULL,
    senha INT(6) NULL
);

CREATE TABLE barsotibank (
    idbarsotiBank INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nomeDoCliente VARCHAR(45) NOT NULL,
    saldo VARCHAR(45) NOT NULL
);

select * from cliente;
select * from barsotibank;