# SyndProxy private pool

## Current pool

- Alive now: 1006
- Gold now: 441
- HTTP: 309 alive / 101 gold
- HTTPS: 213 alive / 30 gold
- SOCKS4: 212 alive / 148 gold
- SOCKS5: 272 alive / 162 gold

## Historical pool

- Discovered: 161016
- Ever alive: 31066
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
