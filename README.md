# SyndProxy private pool

## Current pool

- Alive now: 1108
- Gold now: 425
- HTTP: 371 alive / 109 gold
- HTTPS: 304 alive / 26 gold
- SOCKS4: 208 alive / 157 gold
- SOCKS5: 225 alive / 133 gold

## Historical pool

- Discovered: 153184
- Ever alive: 28459
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
