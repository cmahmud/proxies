# SyndProxy private pool

## Current pool

- Alive now: 1013
- Gold now: 428
- HTTP: 319 alive / 87 gold
- HTTPS: 211 alive / 28 gold
- SOCKS4: 218 alive / 154 gold
- SOCKS5: 265 alive / 159 gold

## Historical pool

- Discovered: 159260
- Ever alive: 30232
- Ever gold: 1143

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
