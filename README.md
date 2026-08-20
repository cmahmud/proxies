# SyndProxy private pool

## Current pool

- Alive now: 1100
- Gold now: 387
- HTTP: 362 alive / 96 gold
- HTTPS: 234 alive / 24 gold
- SOCKS4: 237 alive / 132 gold
- SOCKS5: 267 alive / 135 gold

## Historical pool

- Discovered: 144740
- Ever alive: 25080
- Ever gold: 1054

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
