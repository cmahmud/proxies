# SyndProxy validated proxy pool

## Current pool

- Alive now: 572
- Gold now: 438
- HTTP: 105 alive / 78 gold
- HTTPS: 89 alive / 23 gold
- SOCKS4: 187 alive / 162 gold
- SOCKS5: 191 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47576
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
