# SyndProxy validated proxy pool

## Current pool

- Alive now: 493
- Gold now: 391
- HTTP: 108 alive / 72 gold
- HTTPS: 35 alive / 13 gold
- SOCKS4: 169 alive / 152 gold
- SOCKS5: 181 alive / 154 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48218
- Ever gold: 1525

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
