# SyndProxy private pool

## Current pool

- Alive now: 994
- Gold now: 381
- HTTP: 323 alive / 85 gold
- HTTPS: 217 alive / 22 gold
- SOCKS4: 227 alive / 143 gold
- SOCKS5: 227 alive / 131 gold

## Historical pool

- Discovered: 165822
- Ever alive: 32335
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
