# Calculadora

Projeto simples em Python com quatro operações básicas (somar,
subtrair, multiplicar, dividir), testes automatizados e um pipeline
de Integração Contínua (CI) no GitHub Actions.

## Como rodar

```bash
pip install -r requirements.txt
python calculadora.py
```

## Como rodar os testes

```bash
pytest
```

## CI/CD

A cada `push` ou Pull Request na branch `main`, o GitHub Actions
executa automaticamente (veja `.github/workflows/ci.yml`):
1. Instalação das dependências;
2. Verificação de estilo do código (lint);
3. Execução dos testes automatizados.

Se qualquer etapa falhar, o pipeline fica vermelho e o código não
deve ser mesclado à branch principal.
