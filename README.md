# performance-evaluation-analysis

![GitHub repo size](https://img.shields.io/github/directory-file-count/brunopascoal/performance-evaluation-analysis?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/top/brunopascoal/performance-evaluation-analysis?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/brunopascoal/performance-evaluation-analysis?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/brunopascoal/performance-evaluation-analysis?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/brunopascoal/performance-evaluation-analysis?style=for-the-badge)
> Este projeto permite a visualização e análise das avaliações de desempenho dos membros da equipe, separando-os entre Assistentes e Seniors. Utiliza-se o Streamlit como interface para a exibição dos dados, permitindo uma interação amigável e intuitiva. O projeto se conecta a um banco de dados para obter as informações das avaliações e processa os dados para serem exibidos corretamente.

# Imagens

![tabela](https://user-images.githubusercontent.com/49947689/235044276-71e0cae2-9d34-4d77-ab0a-c8c9ffafb3b2.png)
![tabela_completa](https://user-images.githubusercontent.com/49947689/235044641-8982c0f7-a3cf-4ef4-8d9f-87951cd30c45.png)
![grafico](https://user-images.githubusercontent.com/49947689/235044310-633e6b22-adc2-4be1-85ea-e8a64b4c3720.png)




### Ajustes e melhorias

O projeto ainda está em desenvolvimento e as próximas atualizações serão voltadas nas seguintes tarefas:

- [ ] Mais opções de visualização de dados;
- [ ] Escolha de escolher periodo das avaliações;
- [ ] Otimização do processo;

## 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

<!---Estes são apenas requisitos de exemplo. Adicionar, duplicar ou remover conforme necessário--->

- Você instalou a versão mais recente de `Python 3.6 ou superior`
- Você tem uma máquina `<Windows / Linux / Mac>`
- Você leu `<guia / link / documentação_relacionada_ao_projeto>`.

## 🚀 Instalando performance-evaluation-analysis

Para instalar performance-evaluation-analysis, siga estas etapas:

### Clone o repositório:

```
git clone https://github.com/brunopascoal/performance-evaluation-analysis.git
```

### Entre no diretório do projeto:

```
cd performance-evaluation-analysis
```

### Crie e ative um ambiente virtual

Linux e macOS:

```
python -m venv venv
source venv/bin/activate
```

Windows:

```
python -m venv venv
venv\Scripts\activate
```

### Instale as bibliotecas necessárias:

```
pip install -r requirements.txt
```

## ☕ Usando performance-evaluation-analysis

Para usar performance-evaluation-analysis, siga estas etapas:

1.Crie uma conexão na pasta do projeto com as informações para conexão ao banco de dados, no seguinte formato:

```
create_connection = {
    'username': 'seu_usuario',
    'password': 'sua_senha',
    'host': 'endereco_do_host',
    'port': 'porta',
    'database_name': 'nome_do_database'
}
```

2.Execute o script principal:

```
streamlit run app.py

```

3.Abra o navegador e acesse o endereço indicado no terminal (geralmente, http://localhost:8501).
4.Utilize o painel lateral para selecionar o tipo de avaliação que deseja visualizar: "Avaliações Assistentes" ou "Avaliações Seniors".
5.Navegue pelas avaliações e gráficos exibidos para cada membro da equipe.

## 📫 Contribuindo para performance-evaluation-analysis

1. Bifurque este repositório.
2. Crie um branch: `git checkout -b <nome_branch>`.
3. Faça suas alterações e confirme-as: `git commit -m '<mensagem_commit>'`
4. Envie para o branch original: `git push origin performance-evaluation-analysis / <local>`
5. Crie a solicitação de pull.

Como alternativa, consulte a documentação do GitHub em [como criar uma solicitação pull](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## 😄 Seja um dos contribuidores<br>

Quer fazer parte desse projeto? Clique [AQUI](CONTRIBUTING.md) e leia como contribuir.

## 📝 Licença

Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE.md) para mais detalhes.

