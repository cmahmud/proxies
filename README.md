# SyndProxy private pool

## Current pool

- Alive now: 1100
- Gold now: 425
- HTTP: 378 alive / 109 gold
- HTTPS: 286 alive / 26 gold
- SOCKS4: 212 alive / 157 gold
- SOCKS5: 224 alive / 133 gold

## Historical pool

- Discovered: 153184
- Ever alive: 28452
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
