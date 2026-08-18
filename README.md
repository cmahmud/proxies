# SyndProxy private pool

## Current pool

- Alive now: 977
- Gold now: 279
- HTTP: 321 alive / 34 gold
- HTTPS: 214 alive / 5 gold
- SOCKS4: 227 alive / 134 gold
- SOCKS5: 215 alive / 106 gold

## Historical pool

- Discovered: 99074
- Ever alive: 11408
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
