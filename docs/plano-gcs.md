# PGC — Plano de Gerenciamento de Configuração: Calculadora

**Enfoque DevOps — Integração e Entrega Contínuas (CI/CD)** · Versão 1.0

| Campo | Descrição |
|---|---|
| Projeto | Calculadora — aplicação Python com as quatro operações básicas (somar, subtrair, multiplicar, dividir) |
| Repositório principal | https://github.com/elisamgomes/calculadora (GitHub, plano gratuito, público) |
| Desenvolvedora Líder / Gerente de Projeto / Responsável por GCS e DevOps | @elisamgomes (acumula as funções, dado o porte da equipe) |
| Desenvolvedor / par de revisão | @otavioroecker (colaborador com permissão de escrita) |
| Equipe | 2 integrantes (1 Líder + 1 Desenvolvedor) |
| Regime de trabalho | Remoto, acadêmico, comunicação assíncrona |

## Histórico de Revisões

| Data | Versão | Descrição | Autora |
|---|---|---|---|
| 28/10/2026 | 1.0 | Elaboração do PGC com enfoque DevOps (CI/CD), adaptado a um projeto acadêmico em Python com equipe de 2 pessoas. | Desenvolvedora Líder |

## 1. Introdução

Este Plano de Gerenciamento de Configuração (PGC) descreve as atividades de Gestão de Configuração de Software (GCS) do projeto **Calculadora**, com ênfase em práticas DevOps: Integração Contínua (CI), Entrega/Implantação Contínua (CD), automação de pipelines e uso de ferramentas gratuitas.

O plano parte de três restrições concretas: (1) equipe de apenas duas pessoas; (2) projeto acadêmico, sem orçamento de infraestrutura; (3) trabalho remoto e assíncrono. Por isso, papéis foram consolidados e a infraestrutura se limita ao GitHub (repositório, Actions, Environments e Rulesets).

### 1.1 Finalidade

Estabelecer um padrão simples, rastreável e verificável para versionamento, revisão, integração e entrega do projeto, de modo que nenhuma mudança chegue à branch `main` sem Pull Request, revisão por outro integrante e pipeline verde.

### 1.2 Escopo

Aplica-se aos dois integrantes da equipe e a todos os itens de configuração do repositório: código-fonte (`calculadora.py`), testes (`tests/`), dependências (`requirements.txt`), pipelines (`.github/workflows/`) e documentação (`README.md`, `docs/`).

### 1.3 Definições, Acrônimos e Abreviações

| Termo | Significado |
|---|---|
| GCS | Gestão de Configuração de Software |
| PGC | Plano de Gerenciamento de Configuração |
| CI | Integração Contínua (Continuous Integration) |
| CD | Entrega/Implantação Contínua (Continuous Delivery / Deployment) |
| Pipeline | Sequência automatizada de etapas de build, teste e implantação |
| Ruleset | Conjunto de regras de proteção de branch do GitHub |
| Environment | Ambiente de implantação do GitHub (staging, production), com regras e revisores próprios |
| Baseline | Conjunto de itens de configuração em estado estável e identificado (tag/release) |
| SemVer | Versionamento Semântico (MAJOR.MINOR.PATCH) |
| GitHub Flow | Estratégia de branching com `main` sempre estável e branches de vida curta |

### 1.4 Referências

- Plano de Gerenciamento de Configuração — Enfoque DevOps (CI/CD), modelo do projeto ONGConecta (https://github.com/lzcamargo/ongconecta).
- Documentação do GitHub Actions, Environments e Rulesets.
- Conventional Commits e Versionamento Semântico.

### 1.5 Visão Geral

A GCS é tratada como parte constante do pipeline: cada Pull Request revisado, testado e implantado gera evidências de rastreabilidade (histórico de PRs, execuções do Actions, aprovações e tags). As evidências deste plano estão reunidas em `docs/evidencias/`.

## 2. Cultura DevOps e Papéis

Os papéis do modelo de referência foram consolidados em duas pessoas:

| Papel (modelo) | Quem exerce | Responsabilidades |
|---|---|---|
| Gerente de Projeto / Product Owner | @elisamgomes | Prioriza o backlog (Issues), decide o que entra em cada versão. |
| Engenheiro DevOps / Release Engineer | @elisamgomes | Mantém os workflows de CI/CD, as regras de proteção e os Environments. |
| Desenvolvedor(a) | @elisamgomes e @otavioroecker | Implementam, escrevem testes e revisam os PRs um do outro. |
| QA / Automação de Testes | Ambos | Mantêm a suíte `pytest` executada no pipeline. |
| Segurança | @elisamgomes | Gerencia segredos (GitHub Secrets) e alertas de dependências. |
| Comitê de Controle de Mudanças (CCM) | Ambos | Atua só em mudanças de alto risco; as demais seguem o fluxo de PR. |

**Revisão cruzada obrigatória:** como @elisamgomes é a dona do repositório e a regra de aprovação impede que o autor aprove o próprio PR, a aprovação é dada por @otavioroecker (e vice-versa).

### 2.1 Comunicação assíncrona

- PRs com descrição completa (contexto, decisão, como testar).
- Prazo máximo combinado para revisar um PR: até 3 dias úteis.
- Dúvidas e avisos de deploy registrados nas Issues e nos PRs do próprio repositório.

## 3. Ferramentas, Ambientes e Infraestrutura

### 3.1 Ferramentas

| Categoria | Ferramenta | Finalidade |
|---|---|---|
| Controle de versão | Git + GitHub | Versionamento do código, pipelines e documentação |
| Orquestração CI/CD | GitHub Actions | Build, lint, testes e implantação automatizados |
| Linguagem e testes | Python + `pytest` | Implementação e testes automatizados |
| Dependências | `requirements.txt` | Lista versionada das bibliotecas |
| Proteção de branch | GitHub Rulesets (`proteger-main`) | Impede push direto e exige PR + aprovação |
| Implantação controlada | GitHub Environments | Ambientes `staging` e `production` com revisor obrigatório |
| Rastreamento | GitHub Issues / Pull Requests | Vinculação de mudanças a itens de trabalho |

### 3.2 Ambientes

| Ambiente | Finalidade | Gatilho de promoção |
|---|---|---|
| Revisão (PR) | Validação do PR pelo CI antes do merge | Abertura ou atualização de Pull Request |
| `staging` | Homologação automática da versão integrada | Merge/push na `main` (job `staging` do `cd.yml`) |
| `production` | Versão final | Aprovação manual da revisora obrigatória (@elisamgomes) no Environment `production` |

### 3.3 Estratégia de Branching e Versionamento

Adota-se o **GitHub Flow**:

- `main` — sempre estável, **protegida** pelo ruleset `proteger-main`: não aceita push direto; mudanças entram somente por Pull Request com pelo menos 1 aprovação e CI verde.
- `feature/<issue>-<descrição-curta>` — uma branch por funcionalidade (ex.: `feature/3-operacao-potencia`).
- `fix/<descrição>` — correções.

Versionamento: **SemVer** (`vX.Y.Z`) e **Conventional Commits** (`feat`, `fix`, `docs`, `test`, `chore`, `refactor`), que permitem identificar o tipo da próxima versão (`feat` → MINOR, `fix` → PATCH).

## 4. Identificação da Configuração

### 4.1 Itens de Configuração

São itens de configuração formais, todos versionados no repositório:

- Código-fonte: `calculadora.py`;
- Testes automatizados: pasta `tests/`;
- Dependências: `requirements.txt`;
- Definições de pipeline como código: `.github/workflows/ci.yml` e `.github/workflows/cd.yml`;
- Arquivos de controle: `.gitignore`;
- Documentação: `README.md`, **este plano (`docs/plano-gcs.md`)** e as evidências (`docs/evidencias/`);
- Configurações de proteção (ruleset) e de Environments, registradas por meio de evidências, pois ficam nas configurações do GitHub.

### 4.2 Convenção de Nomenclatura

| Item | Convenção | Exemplo |
|---|---|---|
| Branch de feature | `feature/<issue>-<descrição-curta>` | `feature/3-operacao-potencia` |
| Branch de correção | `fix/<descrição-curta>` | `fix/divisao-por-zero` |
| Commit | `<tipo>(<escopo>): <descrição>` | `feat(calculadora): adiciona potência` |
| Título de PR | Também em Conventional Commits | `fix: corrige divisão por zero` |
| Tag de release | `vX.Y.Z` | `v1.0.0` |

### 4.3 Estrutura do Repositório

```
calculadora/
├── .github/workflows/   # pipelines: ci.yml (PR) e cd.yml (push na main)
├── docs/
│   ├── plano-gcs.md     # este plano
│   └── evidencias/      # prints e registros que comprovam a configuração
├── tests/               # testes automatizados (pytest)
├── .gitignore
├── README.md
├── calculadora.py       # código-fonte
└── requirements.txt     # dependências
```

## 5. Integração Contínua (CI)

Todo Pull Request para a `main` dispara o workflow `ci.yml`. Nenhuma mudança é integrada sem que ele conclua com sucesso.

### 5.1 Etapas do Pipeline de CI

1. Checkout do código;
2. Instalação das dependências (`pip install -r requirements.txt`);
3. Verificação de estilo do código (lint);
4. Execução dos testes automatizados (`pytest`).

Se qualquer etapa falhar, o pipeline fica vermelho e o PR não pode ser integrado.

### 5.2 Política de Pull Request e Revisão de Código

- Push direto na `main` é **recusado** pelo ruleset `proteger-main` (evidência em `docs/evidencias/`);
- Todo PR exige **no mínimo 1 aprovação** de outro integrante (@otavioroecker ou @elisamgomes, conforme o autor);
- O par de revisão tem **acesso de escrita** ao repositório (Settings → Collaborators);
- Merge somente com CI verde;
- PRs pequenos e descritivos, para permitir revisão assíncrona.

### 5.3 Critérios de Qualidade (Quality Gate)

- Zero erros de lint;
- 100% dos testes automatizados passando;
- Cobertura de testes: meta de ≥ 60%, a ser medida e exigida de forma progressiva à medida que a suíte evoluir;
- Cada nova operação ou correção deve vir acompanhada de ao menos um teste.

## 6. Entrega e Implantação Contínua (CD)

O workflow `cd.yml` é disparado por **push na `main`** (isto é, após o merge de um PR) e executa três jobs encadeados:

| Job | Descrição | Condição |
|---|---|---|
| `build` | Prepara o projeto e gera o artefato da versão | Automático |
| `staging` | Implanta no Environment `staging` | Automático, após o `build` |
| `production` | Implanta no Environment `production` | **Pausa até a aprovação manual** de @elisamgomes (revisora obrigatória) |

### 6.1 Ambientes protegidos (GitHub Environments)

- `staging`: sem revisores, promoção automática;
- `production`: **Required reviewers = @elisamgomes**. O pipeline fica em "Waiting" até que a revisora clique em *Review deployments* e aprove (evidência em `docs/evidencias/`).

### 6.2 Estratégia de Implantação

Promoção progressiva: o mesmo artefato é validado em `staging` e, mediante aprovação humana, segue para `production`.

### 6.3 Rollback e Recuperação

Em caso de problema, a reversão é feita com `git revert` do commit problemático, por meio de um novo PR (com revisão e CI), o que dispara um novo ciclo de CD com a versão corrigida. Versões estáveis anteriores permanecem acessíveis pelas tags e releases.

## 7. Infraestrutura como Código (IaC)

Não há infraestrutura própria: o projeto usa somente recursos do GitHub. Ainda assim, vale o princípio de "tudo versionado": os pipelines são definidos como código em `.github/workflows/`, e qualquer mudança neles passa por PR, revisão e CI. As configurações feitas pela interface do GitHub (ruleset e Environments) são documentadas neste plano e comprovadas em `docs/evidencias/`.

## 8. Controle de Configuração e Mudança

### 8.1 Processo de Solicitação de Mudança

Fluxo padrão: **Issue → branch → commits → Pull Request → revisão por outro integrante → CI verde → merge (squash) → CD (staging → aprovação → production)**. Esse fluxo já é o registro formal e rastreável de cada mudança.

### 8.2 Comitê de Controle de Mudança (CCM)

Composto pelos dois integrantes. É acionado apenas em mudanças de alto impacto, como alterar as regras de proteção da `main`, mudar os Environments ou abrir exceção ao fluxo padrão. Mudanças de rotina dispensam o comitê: a revisão do PR o substitui.

## 9. Baselines e Releases

### 9.1 Geração de Baseline

Cada versão estável aprovada para `production` recebe uma **tag SemVer** (`vX.Y.Z`) associada ao commit correspondente, formando uma baseline identificável e reproduzível.

### 9.2 Notas de Versão

As notas de versão são redigidas a partir dos Conventional Commits desde a última tag e publicadas na aba *Releases* do repositório.

## 10. Estimativa do Status de Configuração

### 10.1 Monitoramento

A aba **Actions** mostra o resultado de cada execução de CI e CD; a aba **Pull Requests** guarda o histórico de revisões e aprovações.

### 10.2 Métricas acompanhadas

| Métrica | Descrição |
|---|---|
| Deployment Frequency | Frequência de implantações em `production` |
| Change Failure Rate | Percentual de implantações que exigiram correção |

### 10.3 Relatórios e Auditorias

O histórico do GitHub Actions, os PRs aprovados e o histórico de commits da `main` constituem a auditoria de GCS. As evidências de configuração ficam em `docs/evidencias/`.

## 11. Marcos

1. Repositório criado e público;
2. Proteção da `main` (ruleset `proteger-main`) e par de revisão com acesso de escrita;
3. Pipeline de CI (`ci.yml`) funcionando em PRs;
4. Pipeline de CD (`cd.yml`) com Environments `staging` e `production`;
5. Plano de GCS e evidências publicados na `main`, via PR aprovado pelo par de revisão;
6. Primeira release com tag `v1.0.0`.

## 12. Treinamento e Recursos

- O `README.md` documenta como executar a aplicação, os testes e o pipeline;
- Este plano e o `docs/evidencias/` servem de guia para novos integrantes;
- As revisões de PR são usadas como oportunidade de aprendizado mútuo, com comentários explicativos.

## 13. Controle de Dependências de Terceiros

O projeto não tem subcontratados. As bibliotecas de terceiros são listadas e versionadas em `requirements.txt`, tratadas como itens de configuração. Atualizações de dependências seguem o mesmo fluxo de PR, revisão e CI das demais mudanças. Segredos, quando necessários, ficam apenas no GitHub Secrets ou Environments, nunca no código.

## 14. Quadro-Resumo do Pipeline CI/CD

| Etapa | Descrição | Gatilho |
|---|---|---|
| CI | Instala dependências, executa lint e testes (`pytest`) | Abertura/atualização de Pull Request |
| Revisão | 1 aprovação do par de revisão + CI verde | PR pronto para merge |
| Merge | Integração na `main` (push direto é recusado) | Aprovação + CI verde |
| CD — build | Gera o artefato da versão | Push na `main` |
| CD — staging | Implantação automática em `staging` | Sucesso do build |
| Gate de release | Aprovação manual da revisora obrigatória | Sucesso em staging |
| CD — production | Implantação em `production` e tag de release | Aprovação do gate |

## Anexo — Evidências (`docs/evidencias/`)

| # | Evidência | O que comprova |
|---|---|---|
| 1 | Tela "You can't commit to `main` because it is a protected branch" | Recusa do push direto na `main` |
| 2 | Ruleset `proteger-main` (Settings → Rules) | Regras de proteção ativas na `main` |
| 3 | Settings → Collaborators, com a permissão do colega | Par de revisão com acesso de escrita |
| 4 | PR aprovado pelo colega | Revisão cruzada funcionando |
| 5 | Settings → Environments (`staging` e `production`, com revisor obrigatório) | Environments configurados |
| 6 | Execução do CD aguardando aprovação em `production` | Gate de aprovação funcionando |
