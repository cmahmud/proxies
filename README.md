# SyndProxy private pool

## Current pool

- Alive now: 1078
- Gold now: 356
- HTTP: 378 alive / 68 gold
- HTTPS: 239 alive / 12 gold
- SOCKS4: 213 alive / 129 gold
- SOCKS5: 248 alive / 147 gold

## Historical pool

- Discovered: 129303
- Ever alive: 20363
- Ever gold: 865

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
