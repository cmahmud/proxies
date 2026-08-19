# SyndProxy private pool

## Current pool

- Alive now: 1033
- Gold now: 395
- HTTP: 320 alive / 71 gold
- HTTPS: 224 alive / 16 gold
- SOCKS4: 255 alive / 148 gold
- SOCKS5: 234 alive / 160 gold

## Historical pool

- Discovered: 129319
- Ever alive: 20465
- Ever gold: 865

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
