# SyndProxy validated proxy pool

## Current pool

- Alive now: 441
- Gold now: 330
- HTTP: 105 alive / 76 gold
- HTTPS: 58 alive / 25 gold
- SOCKS4: 106 alive / 89 gold
- SOCKS5: 172 alive / 140 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47949
- Ever gold: 1505

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
