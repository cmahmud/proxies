# SyndProxy private pool

## Current pool

- Alive now: 1004
- Gold now: 395
- HTTP: 290 alive / 72 gold
- HTTPS: 224 alive / 15 gold
- SOCKS4: 246 alive / 152 gold
- SOCKS5: 244 alive / 156 gold

## Historical pool

- Discovered: 129310
- Ever alive: 20414
- Ever gold: 865

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
