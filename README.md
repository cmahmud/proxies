# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 438
- HTTP: 102 alive / 79 gold
- HTTPS: 85 alive / 24 gold
- SOCKS4: 169 alive / 163 gold
- SOCKS5: 187 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47673
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
