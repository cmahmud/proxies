# SyndProxy private pool

## Current pool

- Alive now: 1067
- Gold now: 494
- HTTP: 393 alive / 120 gold
- HTTPS: 209 alive / 73 gold
- SOCKS4: 213 alive / 148 gold
- SOCKS5: 252 alive / 153 gold

## Historical pool

- Discovered: 114411
- Ever alive: 16939
- Ever gold: 627

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
