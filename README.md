# SyndProxy private pool

## Current pool

- Alive now: 1341
- Gold now: 592
- HTTP: 485 alive / 196 gold
- HTTPS: 372 alive / 94 gold
- SOCKS4: 241 alive / 146 gold
- SOCKS5: 243 alive / 156 gold

## Historical pool

- Discovered: 140459
- Ever alive: 23558
- Ever gold: 923

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
