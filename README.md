# Tabuada Inteligente

Biblioteca para gerar e praticar tabuadas de forma interativa.

## Resumo rápido

- Requisitos: Python 3.8+
- Recomenda-se usar um virtual environment (venv, pipenv, poetry).

## Instalação

Para instalar o pacote, use um dos métodos abaixo:

- **Instalar a partir do PyPI** (se o pacote foi publicado):

    ```bash
    pip install tabuada_inteligente
    # ou, se o nome no PyPI usar hífen:
    pip install tabuada-inteligente
    ```

- **Instalar a partir do repositório GitHub**:

    ```bash
    pip install git+https://github.com/SEU_USUARIO/tabuada_inteligente.git
    # substitua SEU_USUARIO pelo usuário/organização correta
    ```

- **Instalar localmente para desenvolvimento** (na raiz do projeto):

    ```bash
    python -m pip install -e .
    # ou
    python -m pip install .
    ```

### Observações

- Use o mesmo executável Python para instalar e executar (ex.: `python -m pip ...`).
- Se houver `ModuleNotFoundError`, confirme se o ambiente virtual está ativado.

## Uso

Após a instalação, você pode usar o pacote para gerar e praticar tabuadas. Veja alguns exemplos:

```python
import tabuada_inteligente

# Para gerar a tabuada do 5:
tabuada_inteligente.gerar_tabuada(5)

# Para praticar a tabuada do 7:
tabuada_inteligente.praticar_tabuada(7)
```

### Execução como módulo

Se aplicável, você pode executar o pacote como um módulo:

```bash
python -m tabuada_inteligente
# ou, se o projeto define console_scripts, use:
# tabuada-inteligente
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests. Para desenvolvimento local, recomenda-se:

1. Criar um virtualenv.
2. Instalar as dependências com pip antes de desenvolver.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).