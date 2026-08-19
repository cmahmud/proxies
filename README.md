# SyndProxy private pool

## Current pool

- Alive now: 926
- Gold now: 373
- HTTP: 287 alive / 72 gold
- HTTPS: 182 alive / 17 gold
- SOCKS4: 207 alive / 125 gold
- SOCKS5: 250 alive / 159 gold

## Historical pool

- Discovered: 110856
- Ever alive: 15898
- Ever gold: 506

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
