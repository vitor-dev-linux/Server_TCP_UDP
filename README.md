# Server Hibrido TCP/UDP

Este é um projeto de servidor híbrido capaz de lidar com conexões TCP e UDP simultaneamente. Ele monitora em tempo real o tipo de conexão (TCP ou UDP), o IP do cliente conectado e a mensagem recebida.

## Pré-requisitos

- Python 3.x
- Ambiente Linux/Windows

## Instruções de Uso

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/server-hibrido.git
cd server-hibrido
```

2. Execute o script de inicialização no Linux:

```bash
./start.sh
```

Para Windows, utilize o script:

```bash
./start.bat
```

Certifique-se de ter as permissões necessárias para executar o script.

## Configuração

Não é necessário configurar nada. O servidor está pronto para ser executado e detectará automaticamente o tipo de conexão (TCP ou UDP) durante o recebimento da mensagem.

## Funcionalidades

- **Detecção Automática de Conexão:** O servidor é capaz de identificar automaticamente se a mensagem está sendo recebida por meio de uma conexão TCP ou UDP.

- **Monitoramento em Tempo Real:** O servidor exibe em tempo real o IP do cliente conectado e a mensagem recebida.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para propor melhorias, corrigir bugs ou adicionar novas funcionalidades.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE). Consulte o arquivo LICENSE para obter mais detalhes.

---

Esperamos que este servidor híbrido seja útil para suas necessidades. Se tiver alguma dúvida ou problema, não hesite em criar uma issue no repositório. Obrigado por usar o Server Hibrido TCP/UDP!
