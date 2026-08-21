# SyndProxy private pool

## Current pool

- Alive now: 1090
- Gold now: 397
- HTTP: 409 alive / 104 gold
- HTTPS: 218 alive / 25 gold
- SOCKS4: 227 alive / 132 gold
- SOCKS5: 236 alive / 136 gold

## Historical pool

- Discovered: 160027
- Ever alive: 30602
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
