# SyndProxy private pool

## Current pool

- Alive now: 1064
- Gold now: 419
- HTTP: 363 alive / 87 gold
- HTTPS: 230 alive / 29 gold
- SOCKS4: 233 alive / 146 gold
- SOCKS5: 238 alive / 157 gold

## Historical pool

- Discovered: 159211
- Ever alive: 30203
- Ever gold: 1143

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
