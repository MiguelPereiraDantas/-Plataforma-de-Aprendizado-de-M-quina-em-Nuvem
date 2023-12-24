# Plataforma de Aprendizado de Máquina em Nuvem

## Descrição do Projeto

Este projeto é uma plataforma de aprendizado de máquina em nuvem que permite aos usuários treinar modelos de aprendizado de máquina de maneira distribuída. A plataforma utiliza Python e frameworks como TensorFlow ou PyTorch para realizar o treinamento dos modelos.

## Recursos Implementados

- Autenticação de usuários
- Armazenamento de modelos treinados
- Suporte para diferentes frameworks de aprendizado de máquina
- Treinamento distribuído de modelos
- Interface web básica para interação com a plataforma

## Requisitos

Certifique-se de ter o Python instalado em seu ambiente. Você pode instalar as dependências necessárias executando o seguinte comando:

```bash
pip install Flask Flask-WTF Flask-Login
```
## Estrutura do Projeto

A estrutura do projeto é organizada da seguinte maneira:

```bash
/plataforma_ml
   /static
      /css
      /js
   /templates
   /uploads
   /models
   app.py
```

## Como Executar

Clone este repositório:

```bash
git clone https://github.com/MiguelPereiraDantas/-Plataforma-de-Aprendizado-de-M-quina-em-Nuvem.git
cd plataforma_ml
```

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Execute o aplicativo:
```bash
python app.py
```

Acesse a plataforma em http://127.0.0.1:5000/.

## Configurações Adicionais

Configure as opções no arquivo `config.py` conforme necessário.

Certifique-se de ajustar as permissões de pasta para `uploads` e `models` para garantir o correto funcionamento da plataforma.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas (issues) ou enviar pull requests para melhorar este projeto.

## Licença

Este projeto está licenciado sob a MIT License.