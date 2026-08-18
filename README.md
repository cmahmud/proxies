# SyndProxy private pool

## Current pool

- Alive now: 845
- Gold now: 284
- HTTP: 270 alive / 35 gold
- HTTPS: 184 alive / 9 gold
- SOCKS4: 220 alive / 140 gold
- SOCKS5: 171 alive / 100 gold

## Historical pool

- Discovered: 102931
- Ever alive: 13961
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
