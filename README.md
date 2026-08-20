# SyndProxy private pool

## Current pool

- Alive now: 771
- Gold now: 374
- HTTP: 239 alive / 72 gold
- HTTPS: 114 alive / 16 gold
- SOCKS4: 230 alive / 150 gold
- SOCKS5: 188 alive / 136 gold

## Historical pool

- Discovered: 145552
- Ever alive: 25456
- Ever gold: 1060

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
