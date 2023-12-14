# References:
    https://www.oracle.com/br/technical-resources/articles/database-performance/oracle-db19c-com-docker.html
    https://github.com/oracle/docker-images/tree/master/OracleDatabase
    https://container-registry.oracle.com/ords/f?p=113:4:102797434311794:::::

# Para baixar a imagem Oracle é necessário realizar o docker login no registry da Oracle

1. Visit https://container-registry.oracle.com/ and create your new account
2. Select Enterprise.
3. Click “Sign In”
4. Authenticate by entering your registered email ID and password.
5. Accept the License and test if the docker login is working fine or not.
    $ docker login container-registry.oracle.com
6. docker pull container-registry.oracle.com/database/enterprise:latest
7. docker-compose up -d
8. docker ps -a
9. docker logs -f oracle19c

# Para validar o Container Oracle Database

1. Caso seja necessário alterar a senha do usuário "sys"
    $ docker exec oracle19c ./setPassword.sh sys_123
2. Acessando o Oracle com Sql Server
    username: sys
    password: sys_123
    connection_type: Basic
    Role: SYSDBA
    Hostname: localhost
    Port: 1521
    Service name: ORCLPDB1
3. Conectando no banco de dados com SQLPLUS:
    $ sqlplus sys/sys_123@localhost:1521/orclpdb1 as sysdba
4. Conectando no banco de dados utilizando SQLPLUS que está dentro do container Docker:
    $ docker exec -ti oracle19c sqlplus system/sys_123@orclpdb1
5. Acessando o Oracle Enterprise Manager Database Express:
    url: https://localhost:5500/em/shell
    username: sys
    password: sys_123
    container name: <vazio>
    
6. Realizando a parada do banco de dados:
    $ docker stop oracle19c

# Criando a tabela no Oracle para teste
    CREATE TABLE PESSOA 
    (
    ID_ARQUIVO VARCHAR2(255)  
    , CNPJ_CPFUSUFINALRECBDR_TITLAR VARCHAR2(255)  
    , CNPJCREDDRSUB VARCHAR2(255)  
    , CNPJFINCDR VARCHAR2(255) 
    , CODINSTITDRARRAJPGTO VARCHAR2(255)  
    , DTOPTIN VARCHAR2(255)  
    , DTINIOPTIN VARCHAR2(255)  
    );
