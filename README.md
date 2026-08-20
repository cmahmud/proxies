# SyndProxy private pool

## Current pool

- Alive now: 768
- Gold now: 375
- HTTP: 242 alive / 71 gold
- HTTPS: 119 alive / 17 gold
- SOCKS4: 225 alive / 149 gold
- SOCKS5: 182 alive / 138 gold

## Historical pool

- Discovered: 145552
- Ever alive: 25449
- Ever gold: 1059

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
