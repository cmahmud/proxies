# SyndProxy private pool

## Current pool

- Alive now: 1066
- Gold now: 382
- HTTP: 353 alive / 101 gold
- HTTPS: 263 alive / 25 gold
- SOCKS4: 195 alive / 117 gold
- SOCKS5: 255 alive / 139 gold

## Historical pool

- Discovered: 152755
- Ever alive: 28287
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
