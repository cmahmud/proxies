# SyndProxy private pool

## Current pool

- Alive now: 1090
- Gold now: 532
- HTTP: 388 alive / 159 gold
- HTTPS: 258 alive / 84 gold
- SOCKS4: 235 alive / 150 gold
- SOCKS5: 209 alive / 139 gold

## Historical pool

- Discovered: 119814
- Ever alive: 18049
- Ever gold: 713

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
