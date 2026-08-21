# SyndProxy private pool

## Current pool

- Alive now: 1016
- Gold now: 394
- HTTP: 319 alive / 89 gold
- HTTPS: 215 alive / 30 gold
- SOCKS4: 246 alive / 148 gold
- SOCKS5: 236 alive / 127 gold

## Historical pool

- Discovered: 160988
- Ever alive: 30879
- Ever gold: 1150

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
