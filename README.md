# SyndProxy private pool

## Current pool

- Alive now: 1303
- Gold now: 432
- HTTP: 468 alive / 94 gold
- HTTPS: 313 alive / 24 gold
- SOCKS4: 220 alive / 148 gold
- SOCKS5: 302 alive / 166 gold

## Historical pool

- Discovered: 136206
- Ever alive: 22402
- Ever gold: 898

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
