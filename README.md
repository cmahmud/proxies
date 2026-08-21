# SyndProxy private pool

## Current pool

- Alive now: 818
- Gold now: 394
- HTTP: 246 alive / 89 gold
- HTTPS: 116 alive / 17 gold
- SOCKS4: 216 alive / 136 gold
- SOCKS5: 240 alive / 152 gold

## Historical pool

- Discovered: 157428
- Ever alive: 29752
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
