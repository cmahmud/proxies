# SyndProxy private pool

## Current pool

- Alive now: 1078
- Gold now: 553
- HTTP: 396 alive / 188 gold
- HTTPS: 282 alive / 99 gold
- SOCKS4: 187 alive / 120 gold
- SOCKS5: 213 alive / 146 gold

## Historical pool

- Discovered: 124835
- Ever alive: 19240
- Ever gold: 770

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
