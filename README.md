# SyndProxy private pool

## Current pool

- Alive now: 1575
- Gold now: 578
- HTTP: 580 alive / 196 gold
- HTTPS: 410 alive / 97 gold
- SOCKS4: 225 alive / 149 gold
- SOCKS5: 360 alive / 136 gold

## Historical pool

- Discovered: 140465
- Ever alive: 23648
- Ever gold: 924

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
