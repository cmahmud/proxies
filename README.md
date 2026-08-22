# SyndProxy private pool

## Current pool

- Alive now: 970
- Gold now: 391
- HTTP: 294 alive / 86 gold
- HTTPS: 225 alive / 24 gold
- SOCKS4: 227 alive / 149 gold
- SOCKS5: 224 alive / 132 gold

## Historical pool

- Discovered: 165822
- Ever alive: 32336
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
