# SyndProxy validated proxy pool

## Current pool

- Alive now: 369
- Gold now: 297
- HTTP: 106 alive / 79 gold
- HTTPS: 32 alive / 19 gold
- SOCKS4: 74 alive / 65 gold
- SOCKS5: 157 alive / 134 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47851
- Ever gold: 1499

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
