# SyndProxy private pool

## Current pool

- Alive now: 1029
- Gold now: 448
- HTTP: 313 alive / 100 gold
- HTTPS: 214 alive / 31 gold
- SOCKS4: 234 alive / 149 gold
- SOCKS5: 268 alive / 168 gold

## Historical pool

- Discovered: 161016
- Ever alive: 31034
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
