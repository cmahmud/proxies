# SyndProxy private pool

## Current pool

- Alive now: 1392
- Gold now: 448
- HTTP: 505 alive / 106 gold
- HTTPS: 371 alive / 34 gold
- SOCKS4: 234 alive / 141 gold
- SOCKS5: 282 alive / 167 gold

## Historical pool

- Discovered: 159265
- Ever alive: 30357
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
