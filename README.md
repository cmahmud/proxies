# SyndProxy private pool

## Current pool

- Alive now: 966
- Gold now: 280
- HTTP: 366 alive / 28 gold
- HTTPS: 139 alive / 5 gold
- SOCKS4: 243 alive / 134 gold
- SOCKS5: 218 alive / 113 gold

## Historical pool

- Discovered: 100094
- Ever alive: 12603
- Ever gold: 398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
