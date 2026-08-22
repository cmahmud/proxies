# SyndProxy private pool

## Current pool

- Alive now: 905
- Gold now: 367
- HTTP: 277 alive / 79 gold
- HTTPS: 195 alive / 21 gold
- SOCKS4: 204 alive / 138 gold
- SOCKS5: 229 alive / 129 gold

## Historical pool

- Discovered: 165836
- Ever alive: 32363
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
