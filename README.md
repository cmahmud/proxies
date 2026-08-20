# SyndProxy private pool

## Current pool

- Alive now: 720
- Gold now: 378
- HTTP: 208 alive / 71 gold
- HTTPS: 107 alive / 17 gold
- SOCKS4: 224 alive / 152 gold
- SOCKS5: 181 alive / 138 gold

## Historical pool

- Discovered: 145552
- Ever alive: 25449
- Ever gold: 1059

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
