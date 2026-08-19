# SyndProxy private pool

## Current pool

- Alive now: 1577
- Gold now: 394
- HTTP: 580 alive / 103 gold
- HTTPS: 414 alive / 21 gold
- SOCKS4: 260 alive / 125 gold
- SOCKS5: 323 alive / 145 gold

## Historical pool

- Discovered: 136221
- Ever alive: 22483
- Ever gold: 907

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
