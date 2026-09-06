# SyndProxy validated proxy pool

## Current pool

- Alive now: 411
- Gold now: 325
- HTTP: 79 alive / 56 gold
- HTTPS: 39 alive / 15 gold
- SOCKS4: 147 alive / 134 gold
- SOCKS5: 146 alive / 120 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48349
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
