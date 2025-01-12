# Sistema de Gerenciamento de Estoque

Este é um projeto simples de gerenciamento de estoque desenvolvido em Python. Ele permite adicionar produtos ao estoque, atualizar quantidades, consultar o estoque e remover produtos indisponíveis. O objetivo do projeto é ajudar a praticar conceitos básicos de programação, manipulação de dados, e persistência utilizando arquivos JSON.

---

## **Funcionalidades**

- **Adicionar ou atualizar o estoque**:
  - Adicione novos produtos ao estoque.
  - Atualize a quantidade de produtos já existentes.

- **Remover produtos do estoque**:
  - Remova produtos que não são mais necessários ou estão indisponíveis.

- **Consultar o estoque**:
  - Exiba todos os produtos cadastrados com suas respectivas quantidades.
  - Consulte informações sobre um produto específico.

- **Salvar e carregar estoque**:
  - Salva automaticamente o estoque em um arquivo JSON para persistência de dados.
  - Carrega os dados do estoque salvos ao iniciar o programa.

---

## **Como executar o projeto**

1. Certifique-se de ter o Python instalado na sua máquina (versão 3.6 ou superior).
2. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/sistema-gerenciamento-estoque.git
   ```
3. Acesse o diretório do projeto:
   ```bash
   cd sistema-gerenciamento-estoque
   ```
4. Execute o programa:
   ```bash
   python main.py
   ```

---

## **Estrutura do Projeto**

- **`main.py`**: Arquivo principal do código com todas as funcionalidades.
- **`estoque.json`**: Arquivo onde o estoque é salvo e carregado automaticamente.
- **`README.md`**: Documentação do projeto.

---

## **Tecnologias Utilizadas**

- **Linguagem**: Python
- **Biblioteca**: JSON (para persistência de dados)

---

## **Ideias para Melhorias Futuras**

1. **Interface Gráfica**:
   - Criar uma interface visual para facilitar o uso do sistema.

2. **Filtros e Relatórios**:
   - Adicionar filtros para exibir produtos com estoque baixo.
   - Gerar relatórios em formatos como PDF ou Excel.

3. **Autenticação de Usuários**:
   - Implementar um sistema de login para diferentes usuários (administradores e colaboradores).

4. **Controle de Preços**:
   - Adicionar preços aos produtos e calcular o valor total do estoque.

5. **Histórico de Movimentações**:
   - Manter um log de entradas, saídas e alterações no estoque.

6. **Validação Avançada**:
   - Melhorar as validações de entrada, como limites máximos para quantidades ou nomes duplicados.

---

## **Licença**

Este projeto é livre para uso e modificação. Sinta-se à vontade para contribuir ou utilizá-lo como inspiração para seus próprios projetos.

---

Desenvolvido por [Arilson Filadelfo](https://github.com/arilsonfiladelfo).
