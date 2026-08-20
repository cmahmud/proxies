# SyndProxy private pool

## Current pool

- Alive now: 1548
- Gold now: 553
- HTTP: 622 alive / 179 gold
- HTTPS: 444 alive / 89 gold
- SOCKS4: 234 alive / 127 gold
- SOCKS5: 248 alive / 158 gold

## Historical pool

- Discovered: 138813
- Ever alive: 23015
- Ever gold: 911

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
