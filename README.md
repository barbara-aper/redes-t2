# Trabalho 2 da disciplina de Redes de Computadores
# ABChat
Aline Mendonça Mayerhofer Manhães e Bárbara Alencar de Araujo Pereira

## Descrição
O ABChat é um "Servidor de Chat com Suporte a Múltiplas Salas" simples, que possibilita a diferentes clientes interagirem simultaneamente em diferentes salas de chat em uma aplicação web. Além disso, é possível criar salas de chat com ou sem senha, entrar e sair delas quando quiser, enviar mensagens a uma sala e visualizar todas as salas disponíveis. De imediato, o cliente deve informar seu nome de usuário e "entrar". Depois, a lista de salas ativas no sistema é exibida e o cliente pode entrar em uma sala pré-existente ou criar uma nova sala. Caso a sala escolhida possua senha, o cliente será direcionado a uma tela onde deverá informá-la. Por fim, o cliente é direcionado a sala de chat, na qual pode interagir via mensagens com os usuários que estiverem logados na sala. Todas as salas possuem botão de retorno à sala anterior.

## Tecnologias Utilizadas
Python, SocketIO, Flask, HTML, CSS e JavaScript

## Como Executar 
### Requisitos
Todos os requisitos estão informados no arquivo "requirements.txt".
### Instruções de Execução
1- Clone o repositório:
git clone <URL_DO_REPOSITORIO>

2- Instale as dependências:
pip install -r requirements.txt

3- Execute:
python run.py ou python3 run.py

4- Abra o server no seu navegador com o link para a porta 5000:
http://seu_ip:5000

## Como Testar
Abra o server no seu navegador com o link para a porta 5000: http://seu_ip:5000 . Para testar sozinho, basta abrir diferentes abas em seu navegador com o mesmo link. Para testar com outras pessoas: 
- utilize uma vpn e desative o firewall, caso vocês não estejam em uma mesma rede. Todos poderão acessar ao sistema com o ip da pessoa que executou o arquivo no link http://ip:5000 .
- caso vocês já estejam em uma mesma rede, todos poderão acessar ao sistema com o ip da pessoa que executou o arquivo no link http://ip:5000 . 

## Funcionalidades Implementadas
- login (cliente informa seu nome de usuário)
- criar, listar, entrar e sair de salas de chat
- comunicação via mensagem de texto entre diferentes usuários logados em uma mesma sala de chat
- salas privadas (com senha)

## Possíveis Melhorias Futuras
- Excluir uma sala de chat
- Exibir os usuários logados em uma sala
- Adicionar um botão de envio de mensagem na caixa de texto do chat
