# SyndProxy private pool

## Current pool

- Alive now: 875
- Gold now: 278
- HTTP: 294 alive / 39 gold
- HTTPS: 192 alive / 8 gold
- SOCKS4: 223 alive / 139 gold
- SOCKS5: 166 alive / 92 gold

## Historical pool

- Discovered: 102887
- Ever alive: 13778
- Ever gold: 429

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
