# SyndProxy validated proxy pool

## Current pool

- Alive now: 390
- Gold now: 311
- HTTP: 102 alive / 78 gold
- HTTPS: 55 alive / 24 gold
- SOCKS4: 79 alive / 74 gold
- SOCKS5: 154 alive / 135 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47931
- Ever gold: 1505

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
