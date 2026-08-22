# SyndProxy private pool

## Current pool

- Alive now: 1026
- Gold now: 444
- HTTP: 312 alive / 99 gold
- HTTPS: 236 alive / 31 gold
- SOCKS4: 210 alive / 148 gold
- SOCKS5: 268 alive / 166 gold

## Historical pool

- Discovered: 161016
- Ever alive: 31063
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
