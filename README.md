# SyndProxy private pool

## Current pool

- Alive now: 1129
- Gold now: 410
- HTTP: 389 alive / 105 gold
- HTTPS: 281 alive / 28 gold
- SOCKS4: 211 alive / 135 gold
- SOCKS5: 248 alive / 142 gold

## Historical pool

- Discovered: 152753
- Ever alive: 28272
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
