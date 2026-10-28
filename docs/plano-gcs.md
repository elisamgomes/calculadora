# Plano de Gerenciamento de Configuração (GCS) — Calculadora

Projeto: https://github.com/elisamgomes/calculadora
Responsável (Desenvolvedora Líder): Elisa (@elisamgomes)
Revisor(a) par: @otavioroecker (acesso de escrita)
Versão do plano: 1.0

## 1. Objetivo e escopo

Definir como o código, os testes, os pipelines e a própria documentação da
Calculadora (Python, quatro operações básicas) são versionados, revisados,
integrados e entregues, seguindo o enfoque DevOps (CI/CD) apresentado na
disciplina.

## 2. Itens de configuração

| Item | Local | Observação |
|---|---|---|
| Código-fonte | `calculadora.py` | versionado em Git |
| Testes automatizados | `tests/` | executados com `pytest` |
| Dependências | `requirements.txt` | versões fixadas |
| Pipelines | `.github/workflows/` | `ci.yml` e `cd.yml` |
| Template de PR | `.github/pull_request_template.md` | padroniza revisões |
| **Este plano de GCS** | `docs/plano-gcs.md` | também é item de configuração: só muda por Pull Request |
| README | `README.md` | como rodar, testar e visão do pipeline |

## 3. Estratégia de branches

- `main`: sempre estável e publicável. **Protegida**: não aceita push direto.
- `feature/<n>-<descricao>`: novas funcionalidades.
- `fix/<n>-<descricao>`: correções.
- `docs/<descricao>`: mudanças de documentação (inclusive deste plano).
- Branches criadas a partir da `main` atualizada e removidas após o merge.

## 4. Padrão de commits e versionamento

- Commits e título do PR em **Conventional Commits**: `feat:`, `fix:`, `docs:`,
  `test:`, `chore:`, `ci:`.
- Versionamento semântico (SemVer `MAJOR.MINOR.PATCH`):
  `feat` → MINOR, `fix` → PATCH, mudança incompatível (`!`) → MAJOR.
- Estratégia de merge: **squash merge**, de modo que o título do PR vira o
  commit na `main`.
- Cada versão liberada em produção recebe tag `vX.Y.Z` e Release.

## 4.1 Gerenciamento de mudanças

1. Toda mudança nasce de uma Issue.
2. Desenvolvimento em branch própria, com commits pequenos.
3. Abertura de Pull Request preenchendo o template (Contexto / Decisão /
   Como testar).
4. CI executado automaticamente; o PR só pode ser mesclado com CI verde.
5. Revisão obrigatória de **1 aprovação** do par de revisão (acesso de escrita).
6. Prazo de resposta a PRs: até 3 dias úteis.

## 5. Integração Contínua (CI)

Arquivo: `.github/workflows/ci.yml`. Gatilho: Pull Request para `main`.

1. Instalar dependências.
2. Lint (verificação de estilo).
3. Testes com `pytest`.

O check do CI é **obrigatório** (status check requerido) na regra de proteção
da `main`.

## 6. Entrega Contínua (CD) e ambientes

Arquivo: `.github/workflows/cd.yml`. Gatilho: push na `main` (merge de PR).

| Ambiente | Promoção | Proteção |
|---|---|---|
| `staging` | automática após o merge | sem aprovação |
| `production` | após staging | **revisor obrigatório: Elisa (@elisamgomes)** |

Fluxo: merge na `main` → build e testes → pacote gerado como artefato →
deploy em staging → aprovação no Environment `production` → publicação em
produção, tag e Release.

## 7. Controle de acesso e proteção da `main`

- Repositório público para permitir a avaliação.
- Regra de proteção (Branch protection / Ruleset) na `main`:
  - exigir Pull Request antes do merge;
  - exigir 1 aprovação;
  - exigir o check de CI aprovado;
  - bloquear push direto (inclusive para administradores);
  - bloquear force push e exclusão da branch.
- Colaborador(a) par com permissão **Write**, que atua como revisor(a).
- Evidência da recusa do push direto: print do erro ao tentar
  `git push origin main` (arquivado em `docs/evidencias/`).

## 8. Rollback

Em caso de problema em produção: reverter o commit/PR problemático via
`git revert` em novo Pull Request, ou republicar a tag da versão anterior.

## 9. Auditoria e evidências

| Evidência | Onde |
|---|---|
| Recusa de push direto na `main` | `docs/evidencias/push-recusado.png` |
| Regra de proteção da `main` | `docs/evidencias/regra-main.png` |
| Colaborador(a) com Write | `docs/evidencias/colaboradores.png` |
| Environments `staging` e `production` | `docs/evidencias/environments.png` |
| Execuções do CI/CD | aba **Actions** |

## 10. Histórico do plano

| Versão | Data | Mudança |
|---|---|---|
| 1.0 | 2026-10-28 | Versão inicial |
