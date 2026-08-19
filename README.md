# SyndProxy private pool

## Current pool

- Alive now: 1204
- Gold now: 417
- HTTP: 371 alive / 89 gold
- HTTPS: 292 alive / 24 gold
- SOCKS4: 248 alive / 140 gold
- SOCKS5: 293 alive / 164 gold

## Historical pool

- Discovered: 136183
- Ever alive: 22283
- Ever gold: 895

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
