# SyndProxy private pool

## Current pool

- Alive now: 907
- Gold now: 375
- HTTP: 285 alive / 82 gold
- HTTPS: 173 alive / 23 gold
- SOCKS4: 204 alive / 114 gold
- SOCKS5: 245 alive / 156 gold

## Historical pool

- Discovered: 166338
- Ever alive: 32401
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
