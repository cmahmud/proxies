# SyndProxy private pool

## Current pool

- Alive now: 1043
- Gold now: 533
- HTTP: 374 alive / 155 gold
- HTTPS: 240 alive / 87 gold
- SOCKS4: 217 alive / 151 gold
- SOCKS5: 212 alive / 140 gold

## Historical pool

- Discovered: 119812
- Ever alive: 18040
- Ever gold: 713

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
