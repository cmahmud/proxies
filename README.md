# SyndProxy validated proxy pool

## Current pool

- Alive now: 431
- Gold now: 325
- HTTP: 104 alive / 76 gold
- HTTPS: 60 alive / 23 gold
- SOCKS4: 101 alive / 86 gold
- SOCKS5: 166 alive / 140 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47949
- Ever gold: 1505

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
