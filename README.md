# Casino Virtual

Este projeto implementa um pequeno casino de consola escrito em Python. O jogador começa com 100€ e pode apostar em dois jogos clássicos:

- **Slot Machine** – gira três símbolos com prémios para pares e jackpots.
- **Roleta Europeia** – permite apostar na cor (vermelho/preto) ou num número específico.

## Requisitos

- Python 3.11+
- (Opcional) `pytest` para executar os testes automatizados.

## Como jogar

1. Instale as dependências opcionais (apenas para correr testes):

   ```bash
   pip install pytest
   ```

2. Inicie o jogo:

   ```bash
   python -m casino.main
   ```

3. Siga as instruções no ecrã para escolher o jogo, definir o valor das apostas e gerir o saldo.

## Testes

Para garantir o comportamento das regras de pagamento das apostas, execute:

```bash
pytest
```
