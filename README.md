# SyndProxy private pool

## Current pool

- Alive now: 990
- Gold now: 342
- HTTP: 377 alive / 58 gold
- HTTPS: 189 alive / 16 gold
- SOCKS4: 213 alive / 132 gold
- SOCKS5: 211 alive / 136 gold

## Historical pool

- Discovered: 129235
- Ever alive: 20044
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
