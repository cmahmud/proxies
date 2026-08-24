# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 381
- HTTP: 124 alive / 57 gold
- HTTPS: 44 alive / 9 gold
- SOCKS4: 167 alive / 156 gold
- SOCKS5: 182 alive / 159 gold

## Historical pool

- Discovered: 179370
- Ever alive: 33458
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
