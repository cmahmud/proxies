# SyndProxy private pool

## Current pool

- Alive now: 1306
- Gold now: 426
- HTTP: 455 alive / 91 gold
- HTTPS: 332 alive / 24 gold
- SOCKS4: 224 alive / 150 gold
- SOCKS5: 295 alive / 161 gold

## Historical pool

- Discovered: 136206
- Ever alive: 22386
- Ever gold: 898

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
