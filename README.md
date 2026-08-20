# SyndProxy private pool

## Current pool

- Alive now: 847
- Gold now: 386
- HTTP: 209 alive / 78 gold
- HTTPS: 209 alive / 19 gold
- SOCKS4: 210 alive / 150 gold
- SOCKS5: 219 alive / 139 gold

## Historical pool

- Discovered: 149510
- Ever alive: 26872
- Ever gold: 1088

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
